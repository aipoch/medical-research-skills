#!/usr/bin/env python3
"""
Patent Claim Mapper - Patent Infringement Risk Analysis Tool

Features:
1. Parse patent claim text
2. Extract technical features
3. Compare with product features
4. Generate infringement risk assessment report

Author: OpenClaw Skills Team
Version: 1.0.0
"""

import re
import json
import argparse
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime


@dataclass
class ClaimElement:
    """Technical element in patent claim"""
    text: str
    element_type: str  # 'apparatus', 'method', 'feature', 'limitation'
    keywords: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)


@dataclass
class ClaimMapping:
    """Mapping between patent claim and product"""
    claim_element: str
    product_feature: Optional[str]
    mapping_status: str  # 'mapped', 'not_mapped', 'partial'
    similarity_score: float
    analysis_notes: str


@dataclass
class InfringementReport:
    """Patent infringement analysis report"""
    patent_number: str
    product_name: str
    overall_risk: str  # 'high', 'medium', 'low', 'clear'
    risk_score: float
    claim_mappings: List[ClaimMapping] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


class PatentClaimMapper:
    """Main class for patent claim mapping and analysis"""
    
    def __init__(self):
        self.claim_parser = ClaimParser()
        self.feature_extractor = FeatureExtractor()
        self.comparison_engine = ComparisonEngine()
    
    def analyze_infringement(self, patent_claims: str, product_description: str,
                            patent_number: str = "", product_name: str = "") -> InfringementReport:
        """Analyze potential patent infringement"""
        # Parse patent claims
        parsed_claims = self.claim_parser.parse(patent_claims)
        
        # Extract product features
        product_features = self.feature_extractor.extract(product_description)
        
        # Compare claims to features
        mappings = self.comparison_engine.compare(parsed_claims, product_features)
        
        # Calculate overall risk
        risk_score = self._calculate_risk_score(mappings)
        overall_risk = self._risk_level(risk_score)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(mappings, overall_risk)
        
        return InfringementReport(
            patent_number=patent_number,
            product_name=product_name,
            overall_risk=overall_risk,
            risk_score=risk_score,
            claim_mappings=mappings,
            recommendations=recommendations
        )
    
    def _calculate_risk_score(self, mappings: List[ClaimMapping]) -> float:
        """Calculate infringement risk score"""
        if not mappings:
            return 0.0
        
        mapped_count = sum(1 for m in mappings if m.mapping_status == 'mapped')
        partial_count = sum(1 for m in mappings if m.mapping_status == 'partial')
        
        score = (mapped_count + 0.5 * partial_count) / len(mappings)
        return min(score, 1.0)
    
    def _risk_level(self, score: float) -> str:
        """Convert score to risk level"""
        if score >= 0.8:
            return "high"
        elif score >= 0.5:
            return "medium"
        elif score >= 0.2:
            return "low"
        else:
            return "clear"
    
    def _generate_recommendations(self, mappings: List[ClaimMapping], 
                                  risk_level: str) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if risk_level == "high":
            recommendations.append("Consider design-around options for mapped elements")
            recommendations.append("Consult patent attorney for invalidity analysis")
        elif risk_level == "medium":
            recommendations.append("Investigate alternative implementations")
            recommendations.append("Monitor patent family for related claims")
        
        unmapped = [m for m in mappings if m.mapping_status == 'not_mapped']
        if unmapped:
            recommendations.append(f"Review {len(unmapped)} unmapped claim elements")
        
        return recommendations


class ClaimParser:
    """Parse patent claim text into structured elements"""
    
    def parse(self, claims_text: str) -> List[ClaimElement]:
        """Parse claim text into elements"""
        elements = []
        
        # Split into individual claims
        claims = re.split(r'\n\s*\d+\.', claims_text)
        
        for claim_text in claims:
            if not claim_text.strip():
                continue
            
            # Extract claim elements
            element = ClaimElement(
                text=claim_text.strip(),
                element_type=self._classify_type(claim_text),
                keywords=self._extract_keywords(claim_text)
            )
            elements.append(element)
        
        return elements
    
    def _classify_type(self, text: str) -> str:
        """Classify claim type"""
        text_lower = text.lower()
        if 'method' in text_lower or 'process' in text_lower:
            return 'method'
        elif 'apparatus' in text_lower or 'system' in text_lower:
            return 'apparatus'
        elif 'composition' in text_lower:
            return 'composition'
        return 'feature'
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract key technical terms"""
        # Simple keyword extraction
        words = re.findall(r'\b[A-Z][a-z]+\b', text)
        return list(set(words))[:10]  # Return unique keywords


class FeatureExtractor:
    """Extract features from product description"""
    
    def extract(self, description: str) -> List[Dict]:
        """Extract product features"""
        features = []
        
        # Split into sentences
        sentences = re.split(r'[.!?]+', description)
        
        for sent in sentences:
            if not sent.strip():
                continue
            
            feature = {
                'text': sent.strip(),
                'keywords': self._extract_keywords(sent),
                'technical_terms': self._extract_technical_terms(sent)
            }
            features.append(feature)
        
        return features
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text"""
        words = re.findall(r'\b[A-Z][a-z]+\b', text)
        return list(set(words))[:10]
    
    def _extract_technical_terms(self, text: str) -> List[str]:
        """Extract technical terminology"""
        # Look for compound technical terms
        terms = re.findall(r'\b[A-Z][a-z]+(?:\s+[a-z]+){1,3}\b', text)
        return list(set(terms))[:5]


class ComparisonEngine:
    """Compare patent claims to product features"""
    
    def compare(self, claims: List[ClaimElement], 
                features: List[Dict]) -> List[ClaimMapping]:
        """Compare claims to features"""
        mappings = []
        
        for claim in claims:
            best_match = self._find_best_match(claim, features)
            
            mapping = ClaimMapping(
                claim_element=claim.text[:100],  # Truncate for readability
                product_feature=best_match['text'] if best_match else None,
                mapping_status=best_match['status'] if best_match else 'not_mapped',
                similarity_score=best_match['score'] if best_match else 0.0,
                analysis_notes=best_match.get('notes', '')
            )
            mappings.append(mapping)
        
        return mappings
    
    def _find_best_match(self, claim: ClaimElement, 
                         features: List[Dict]) -> Optional[Dict]:
        """Find best matching feature for claim element"""
        best_match = None
        best_score = 0.0
        
        for feature in features:
            score = self._calculate_similarity(claim, feature)
            
            if score > best_score:
                best_score = score
                best_match = feature
                best_match['score'] = score
                
                # Determine mapping status
                if score >= 0.7:
                    best_match['status'] = 'mapped'
                elif score >= 0.4:
                    best_match['status'] = 'partial'
                else:
                    best_match['status'] = 'not_mapped'
        
        return best_match
    
    def _calculate_similarity(self, claim: ClaimElement, 
                             feature: Dict) -> float:
        """Calculate similarity between claim and feature"""
        claim_keywords = set(claim.keywords)
        feature_keywords = set(feature.get('keywords', []))
        
        if not claim_keywords or not feature_keywords:
            return 0.0
        
        # Jaccard similarity
        intersection = claim_keywords & feature_keywords
        union = claim_keywords | feature_keywords
        
        return len(intersection) / len(union) if union else 0.0


def main():
    parser = argparse.ArgumentParser(description="Patent Claim Mapper")
    parser.add_argument("--patent-claims", required=True, help="Patent claims text file")
    parser.add_argument("--product-description", required=True, help="Product description file")
    parser.add_argument("--patent-number", help="Patent number for reference")
    parser.add_argument("--product-name", help="Product name")
    parser.add_argument("--output", default="infringement_report.json", help="Output file")
    
    args = parser.parse_args()
    
    # Load files
    with open(args.patent_claims, 'r') as f:
        claims_text = f.read()
    
    with open(args.product_description, 'r') as f:
        product_text = f.read()
    
    # Analyze
    mapper = PatentClaimMapper()
    report = mapper.analyze_infringement(
        claims_text, 
        product_text,
        patent_number=args.patent_number or "",
        product_name=args.product_name or ""
    )
    
    # Save report
    with open(args.output, 'w') as f:
        json.dump(asdict(report), f, indent=2)
    
    print(f"Infringement Analysis Complete")
    print(f"Overall Risk: {report.overall_risk.upper()}")
    print(f"Risk Score: {report.risk_score:.1%}")
    print(f"Report saved: {args.output}")


if __name__ == "__main__":
    main()
