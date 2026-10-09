import os
import argparse
import sys
import json
import base64
import subprocess
import re
import requests
from datetime import datetime

# Configuration
DEFAULT_GENERATOR = "google/gemini-3.6-flash"
DEFAULT_REVIEWER = "google/gemini-3.6-flash"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_RETRIES = 3
QUALITY_THRESHOLD = 8.5

# Global variables (will be set by args)
GENERATOR_MODEL = DEFAULT_GENERATOR
REVIEWER_MODEL = DEFAULT_REVIEWER

def get_api_key():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        print("\nTo fix this:")
        print("1. Get a key from https://openrouter.ai/")
        print("2. Set the environment variable:")
        print("   - Windows (PowerShell): $env:OPENROUTER_API_KEY=\"your_key_here\"")
        print("   - Linux/macOS: export OPENROUTER_API_KEY=\"your_key_here\"")
        sys.exit(1)
    return api_key

def call_openrouter_api(messages, model, response_format=None):
    """
    Calls the OpenRouter API using standard requests.
    """
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/scientific-schematics", # Optional
        "X-Title": "Scientific Schematics Skill" # Optional
    }
    
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }
    
    if response_format:
        payload["response_format"] = response_format

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Call Error: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response: {e.response.text}")
        return None

def extract_python_code(content):
    """
    Extracts Python code block from markdown.
    """
    match = re.search(r'```python(.*?)```', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return content.strip() # Fallback if no markdown blocks

def generate_diagram_code(description, feedback=None):
    """
    Generates Python code to create the diagram using Matplotlib.
    """
    print(f"Generating diagram code with {GENERATOR_MODEL}...")
    
    system_prompt = """
    You are an expert scientific illustrator and Python programmer.
    Your task is to write a Python script using 'matplotlib' to generate a high-quality scientific schematic based on the user's description.
    
    Requirements:
    1. Use 'matplotlib.pyplot' and 'matplotlib.patches' or 'networkx'.
    2. The script MUST save the figure to 'output_schematic.png' in the current directory.
    3. Ensure high resolution (dpi=300).
    4. Use professional color schemes (e.g., 'viridis', 'plasma', or muted scientific colors).
    5. Label all components clearly.
    6. Return ONLY the Python code, wrapped in ```python ... ``` blocks.
    """
    
    user_content = f"Create a scientific schematic for: {description}"
    if feedback:
        user_content += f"\n\nPrevious attempt feedback (please fix these issues): {feedback}"
        
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]
    
    response = call_openrouter_api(messages, GENERATOR_MODEL)
    if response and 'choices' in response:
        return extract_python_code(response['choices'][0]['message']['content'])
    return None

def execute_diagram_code(code, output_path):
    """
    Executes the generated Python code to create the image.
    """
    print("Executing diagram generation code...")
    
    # Write code to a temporary file
    temp_script = "temp_generate.py"
    with open(temp_script, "w") as f:
        f.write(code)
        # Ensure the script saves to the correct path if it doesn't already
        # We append a safeguard just in case, or rely on the prompt.
        # Let's rely on the prompt but check for file existence later.
    
    try:
        # Run the script
        result = subprocess.run([sys.executable, temp_script], capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"Execution Error:\n{result.stderr}")
            return False
        
        # Check if output file was created (assuming prompt compliance: output_schematic.png)
        # We rename it to the desired output path
        if os.path.exists("output_schematic.png"):
            if os.path.exists(output_path):
                os.remove(output_path)
            os.rename("output_schematic.png", output_path)
            return True
        else:
            print("Error: Script did not generate 'output_schematic.png'.")
            return False
            
    except Exception as e:
        print(f"Execution Exception: {e}")
        return False
    finally:
        if os.path.exists(temp_script):
            os.remove(temp_script)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def review_diagram(image_path, description, doc_type):
    """
    Reviews the generated diagram using a Vision model.
    """
    print(f"Reviewing diagram with {REVIEWER_MODEL}...")
    
    base64_image = encode_image(image_path)
    
    system_prompt = f"""
    You are a senior scientific editor for a top-tier {doc_type}.
    Review the attached schematic image based on the user's description: "{description}".
    
    Evaluate based on:
    1. Clarity and Readability
    2. Scientific Accuracy (based on visual structure)
    3. Aesthetics (professionalism, alignment, color usage)
    4. Accessibility (colorblind safety, font size)
    
    Return a JSON object with:
    - "score": number (0-10)
    - "feedback": string (concise actionable improvements)
    - "pass": boolean (true if score >= {QUALITY_THRESHOLD})
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": [
            {"type": "text", "text": "Please review this scientific schematic."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
        ]}
    ]
    
    # Request JSON response format if supported by the model/provider
    # For now, we'll try standard prompt engineering or provider specific param
    response = call_openrouter_api(messages, REVIEWER_MODEL)
    
    if response and 'choices' in response:
        content = response['choices'][0]['message']['content']
        # Extract JSON from content
        try:
            # Look for JSON block
            match = re.search(r'\{.*\}', content, re.DOTALL)
            if match:
                return json.loads(match.group(0))
            return json.loads(content)
        except json.JSONDecodeError:
            print("Warning: Could not parse review JSON. Returning raw feedback.")
            return {"score": 5.0, "feedback": content, "pass": False}
    return None

def generate_schematic(description, doc_type="journal", generator=DEFAULT_GENERATOR, reviewer=DEFAULT_REVIEWER):
    """
    Main entry point for schematic generation.
    """
    global GENERATOR_MODEL, REVIEWER_MODEL
    GENERATOR_MODEL = generator
    REVIEWER_MODEL = reviewer
    
    get_api_key() # Ensure key exists
    
    print(f"Starting schematic generation for: '{description}'")
    print(f"Target document type: {doc_type}")
    print(f"Using Generator: {GENERATOR_MODEL}")
    print(f"Using Reviewer: {REVIEWER_MODEL}")
    
    output_dir = "figures"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"schematic_{timestamp}.png")
    
    feedback = None
    
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n--- Attempt {attempt}/{MAX_RETRIES} ---")
        
        # Step 1: Generate Code
        code = generate_diagram_code(description, feedback)
        if not code:
            print("Failed to generate code.")
            continue
            
        # Step 2: Execute Code
        success = execute_diagram_code(code, output_path)
        if not success:
            feedback = "The Python code failed to execute or did not save 'output_schematic.png'. Please check syntax and library usage."
            print("Generation failed. Retrying...")
            continue
            
        # Step 3: Review
        review = review_diagram(output_path, description, doc_type)
        if not review:
            print("Review failed (API error). Assuming success for now.")
            break
            
        print(f"Review Score: {review.get('score')}/10")
        print(f"Feedback: {review.get('feedback')}")
        
        if review.get('pass', False) or review.get('score', 0) >= QUALITY_THRESHOLD:
            print(f"Success! Quality threshold met.")
            break
        else:
            feedback = review.get('feedback')
            
    print(f"\nFinal schematic saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate publication-quality schematics.")
    parser.add_argument("description", type=str, help="Description of the diagram to generate")
    parser.add_argument("--doc-type", type=str, choices=["journal", "poster"], default="journal", help="Target document type")
    parser.add_argument("--generator", type=str, default=DEFAULT_GENERATOR, help=f"Generator model ID (default: {DEFAULT_GENERATOR})")
    parser.add_argument("--reviewer", type=str, default=DEFAULT_REVIEWER, help=f"Reviewer model ID (default: {DEFAULT_REVIEWER})")
    
    args = parser.parse_args()
    generate_schematic(args.description, args.doc_type, args.generator, args.reviewer)
