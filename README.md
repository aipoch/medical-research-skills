<div align="center">

# AIPOCH Medical Research Skills

Add Skills. Run Your Research.

<br>

[![License](https://img.shields.io/badge/License-MIT-ff6b6b?style=for-the-badge)](./LICENSE)
![Skills Count](https://img.shields.io/badge/Skills-420%2B-4dabf7?style=for-the-badge)
![Work%20with](https://img.shields.io/badge/Work%20with-OpenClaw%20%7C%20Opencode%20%7C%20Claude-9775fa?style=for-the-badge)
[![Follow on X](https://img.shields.io/badge/Follow%20on%20X-%40aipoch__ai-212529?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aipoch_ai)
[![YouTube](https://img.shields.io/badge/YouTube-%40AIPOCH__AI-ff0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AIPOCH_AI)

<br>

<p align="center">
  <a href="https://www.aipoch.com/">
    <img src="https://github.com/user-attachments/assets/1a6a7005-d9fc-49d5-8dba-3cb822d7e71d" alt="AIPOCH Demo GIF" width="800"/>
  </a>
</p>

<br>

*420+ medical research skills · Evidence Insights · Protocol Design · Data Analysis · Academic Writing*

⭐ If you find this repository useful, consider giving it a star! It helps more researchers discover Medical Research Agent Skills and supports the continued development of this library.

</div>

---

## 🤔 What it is?

AIPOCH is a curated library of 420+ Medical Research Agent Skills, built to work with**​ OpenClaw** and other AI agent platforms, including​**​ OpenCode and Claude**​.

It supports the research workflow across four core areas: Evidence Insights, Protocol Design, Data Analysis, and Academic Writing.

Equip your AI agent with Medical Research Skills, and turn it into a capable medical research assistant.

AIPOCH also introduces **Medical ​Skill Auditor​**​— a structured evaluation framework designed to assess the quality of Medical Research Agent Skills. Its core function is to perform a comprehensive quality check on a Skill before it is officially deployed to users. You can view [evaluation results for selected AIPOCH skills here](https://www.aipoch.com/agent-skills/medical-research-literature-reader-pro/eval-result).

---

## 🗂️ Skills Overview

All skills in AIPOCH are ​**originally designed and developed in-house**​, built to reflect medical research workflows and standards.

The library is primarily organized into five categories: ​**Evidence Insights, Protocol Design, ​Data Analysis,  Academic Writing**​, and Others.

| 📚**Category** | **Highlights**                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
|🔍 **Evidence Insight**   | e.g., search strategy design, database selection, evidence-level prioritization, critical appraisal, literature synthesis and gap identification.|
| 🧪 **Protocol Design**    |e.g., experimental design generation, study type selection, causal inference planning, statistical power calculation, validation strategy.        |
|📊 **Data Analysis**      | e.g., R/Python bioinformatics code generation, statistical modeling, data cleaning pipelines, machine learning workflows, result visualization.  |
|✍️ **Academic Writing**   |  e.g., SCI manuscript drafting, methods/results/discussion writing, meta-analysis narrative, cover letters, abstract generation.|
| 🌍 **Other (General / Non-Research)**          | all general skills that do not fall into categories 1–4.                                                                                   |

**📌 Total Skills in Library: 420 and growing**

## Complementary External Literature Source

While AIPOCH skills are developed in-house, **[Paperzilla](https://github.com/paperzilla-ai/paperzilla-skills)** is a useful external complement for biology and medical literature monitoring. It currently supports project-based bioRxiv and medRxiv feeds, lets agents fetch paper markdown for summarization and relevance assessment, and has PubMed support planned. The OpenClaw distribution is also available on [ClawHub](https://clawhub.ai/pors/paperzilla).

## 🎬 AIPOCH Medical Research Skills — Demo

<p align="center">
  <a href="https://www.youtube.com/watch?v=Pq4E9mCO1t8" target="_blank">
<img width="4480" height="2516" alt="medical research literature reader pro" src="https://github.com/user-attachments/assets/c3de83ec-43d8-4c37-8079-6354c138b0fa" />
  </a>
</p>

<p align="center">
A brief showcase of AIPOCH Medical Research Skills in action across research workflows.
</p>

## 🚀 How to Start?

### ⚙️ Requirements

​**Host Platform**​: **OpenClaw (installed and running)** or any compatible AI Agent framework that supports Skill integration.

If you don't have OpenClaw,[ please follow the official OpenClaw setup guide.](https://github.com/openclaw/openclaw)

​**Git**​: Required for cloning the repository. [Git LFS](https://git-lfs.com/)

### 🦞 Connect with OpenClaw

#### **Method 1:**

**I'm a human**

```markdown
curl -sL https://aipoch.com/skill.md > ./skills/aipoch.md
```

1. Run the command to initialize setup
2. Select 'OpenClaw' as your target agent
3. Follow the prompts to link your library

**I'm an agent**

```markdown
Read https://aipoch.com/skill.md and follow the instructions to join Aipoch
```

1. Download the integration guide
2. Manually configure your agent's skill path
3. Verify the connection in your dashboard

---

#### **Method 2:**

**🦞 Install into OpenClaw Plug-in**

[OpenClaw](https://openclaw.ai) is a self-hosted AI agent gateway. You can install all AIPOCH skills into OpenClaw with a single command.

**macOS / Linux / WSL:**

```bash
bash <(curl -s https://raw.githubusercontent.com/aipoch/medical-research-skills/main/scientific-skills/scripts/openclaw-install.sh)
```

**Windows (Git Bash):**

```bash
curl -s https://raw.githubusercontent.com/aipoch/medical-research-skills/main/scientific-skills/scripts/openclaw-install.sh -o /tmp/install.sh
bash /tmp/install.sh
```

The script will:

1. Clone this repository into a temporary directory
2. Copy all `SKILL.md` skill folders into `~/.openclaw/skills/`
3. Skip any skills that are already installed

After installation, restart your gateway to pick up the new skills:

```bash
openclaw gateway restart
```

> **Tip:** Run with `--dry-run` first to preview what will be installed without making any changes.
> 
> ```bash
> bash <(curl -s https://raw.githubusercontent.com/aipoch/medical-research-skills/main/scientific-skills/scripts/openclaw-install.sh) --dry-run
> ```

> **Note:** Skills are installed to `~/.openclaw/skills/` by default (visible to all agents). To install into a specific workspace instead, set the environment variable before running:
> 
> ```bash
> OPENCLAW_SKILLS_DIR=~/.openclaw/workspace/skills bash <(curl -s https://raw.githubusercontent.com/aipoch/medical-research-skills/main/scientific-skills/scripts/openclaw-install.sh)
> ```

---

## 🧠 AIPOCH Medical Skill Auditor

<p align="center">
  <a href="https://youtu.be/soH-l1DTRtw?si=71npBdTxOLBGT_IL">
    <img src="https://github.com/user-attachments/assets/16d5801e-8a4b-4f2f-a102-42836ca69a69" width="700">
  </a>
</p>

### 🧩What is Medical Skill Auditor?

Skill Evaluator is a standardized tool designed to assess the quality of Agent Skills. Its core function is to perform a comprehensive quality check on a Skill before it is officially deployed to users.

### ⚙️How does Medical Skill Auditor Work?

#### 🚫Veto Gates

To enforce strict quality control, Skill Auditor is designed with two layers of veto mechanisms. Any failure in these checks may lead to immediate rejection of a skill.

##### **Skill ​Veto**

* Operational Stability
* Structural Consistency
* Result Determinism
* System Security

##### **Research ​Veto**

* Scientific Integrity
* Practice Boundaries
* Methodological Ground
* Code Usability

#### 🧰 **Core Capability**

Evaluates a skill’s design and contract against key dimensions such as **Functional Suitability, Reliability, Performance & Context, Agent Usability, Human Usability, Security, Agent-Specific and Maintainability.**

#### 📊 Medical Task

Assesses actual outputs of a skill with layered criteria.

For skill testing, the AI automatically generates inputs. The number of inputs in specific categories will increase or decrease depending on the complexity of the skill. The following 7 inputs represent the most comprehensive version.

* Canonical
* Variant A
* Edge
* Variant B
* Stress
* Scope Boundary
* Adversarial

**Skill Complexity Classification**

| Label    | Code/Rank | Definition                                |
| ---------- | ----------- | ------------------------------------------- |
| Simple   | S         | Narrow task scope                         |
| Moderate |M         | Moderate branching or multiple task types |
| Complex  | C         | Broad or multi-step specialized skill     |

**Simple (S):** 3 inputs

**Moderate (M):** 5 inputs

**Complex (C):** 7 inputs

### Final Score

The Skill Evaluator uses a two-stage scoring system: static evaluation (design quality, accounting for 40%) and dynamic evaluation (runtime performance, accounting for 60%). The final overall score is derived by combining both.

* Static (40%)
* Dynamic (60%)

Final Score = Static Score × 40% + Dynamic Score × 60%

You can view [evaluation results for selected AIPOCH skills here](https://www.aipoch.com/agent-skills/medical-research-literature-reader-pro/eval-result).

## Star History

<a href="https://www.star-history.com/?repos=aipoch%2Fmedical-research-skills&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=aipoch/medical-research-skills&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=aipoch/medical-research-skills&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=aipoch/medical-research-skills&type=date&legend=top-left" />
 </picture>
</a>
