#!/usr/bin/env python3
"""
Intelligent Lead Scoring Engine
An AI-powered lead scoring and prioritization tool
"""

import pandas as pd
from typing import Dict, List
import warnings

warnings.filterwarnings('ignore')


class LeadScorer:
    """
    Main class for scoring and ranking leads based on multiple factors
    """
    
    def __init__(self):
        pass
        
    def calculate_firmographic_score(self, lead: Dict) -> float:
        """
        Calculate score based on company firmographics
        
        Args:
            lead: Dictionary containing lead information
            
        Returns:
            Firmographic score (0-100)
        """
        score = 0
        max_score = 100
        
        # Revenue range matching (0-30 points)
        revenue = lead.get('revenue', 0)
        if revenue >= 10000000:  # $10M+
            score += 30
        elif revenue >= 1000000:  # $1M+
            score += 20
        elif revenue >= 100000:  # $100K+
            score += 10
            
        # Employee count optimization (0-25 points)
        employees = lead.get('employees', 0)
        if 50 <= employees <= 500:  # Sweet spot
            score += 25
        elif 10 <= employees <= 1000:
            score += 15
        elif employees > 0:
            score += 5
            
        # Industry alignment (0-25 points)
        target_industries = ['Technology', 'SaaS', 'Software', 'IT Services']
        if lead.get('industry') in target_industries:
            score += 25
            
        # Growth indicators (0-20 points)
        if lead.get('recent_funding', False):
            score += 10
        if lead.get('hiring_active', False):
            score += 10
            
        return min(score, max_score)
    
    def calculate_digital_footprint_score(self, lead: Dict) -> float:
        """
        Calculate score based on digital footprint
        
        Args:
            lead: Dictionary containing lead information
            
        Returns:
            Digital footprint score (0-100)
        """
        score = 0
        max_score = 100
        
        # Website technology stack (0-30 points)
        tech_stack = lead.get('tech_stack', [])
        modern_tech = ['React', 'Vue', 'Angular', 'AWS', 'Azure', 'GCP', 'Kubernetes']
        tech_matches = sum(1 for tech in tech_stack if tech in modern_tech)
        score += min(tech_matches * 5, 30)
        
        # Social media presence (0-30 points)
        linkedin_followers = lead.get('linkedin_followers', 0)
        if linkedin_followers >= 10000:
            score += 20
        elif linkedin_followers >= 1000:
            score += 15
        elif linkedin_followers >= 100:
            score += 10
            
        twitter_followers = lead.get('twitter_followers', 0)
        if twitter_followers >= 5000:
            score += 10
        elif twitter_followers >= 500:
            score += 5
            
        # Content engagement levels (0-20 points)
        engagement_rate = lead.get('engagement_rate', 0)
        score += min(engagement_rate * 100, 20)
        
        # Recent news/activity (0-20 points)
        if lead.get('recent_news', False):
            score += 20
            
        return min(score, max_score)
    
    def calculate_contact_quality_score(self, lead: Dict) -> float:
        """
        Calculate score based on contact quality
        
        Args:
            lead: Dictionary containing lead information
            
        Returns:
            Contact quality score (0-100)
        """
        score = 0
        max_score = 100
        
        # Decision-maker identification (0-40 points)
        title = lead.get('contact_title', '').lower()
        executive_titles = ['ceo', 'cto', 'cfo', 'vp', 'director', 'head', 'chief']
        if any(exec_title in title for exec_title in executive_titles):
            score += 40
        elif 'manager' in title:
            score += 20
            
        # Contact information completeness (0-40 points)
        if lead.get('email'):
            score += 15
        if lead.get('phone'):
            score += 15
        if lead.get('linkedin_url'):
            score += 10
            
        # Engagement probability (0-20 points)
        if lead.get('email_verified', False):
            score += 10
        if lead.get('responded_before', False):
            score += 10
            
        return min(score, max_score)
    
    def score_lead(self, lead: Dict) -> Dict:
        """
        Calculate overall lead score
        
        Args:
            lead: Dictionary containing lead information
            
        Returns:
            Dictionary with scores and overall score
        """
        firmographic_score = self.calculate_firmographic_score(lead)
        digital_score = self.calculate_digital_footprint_score(lead)
        contact_score = self.calculate_contact_quality_score(lead)
        
        # Weighted average (can be adjusted based on business priorities)
        overall_score = (
            firmographic_score * 0.35 +
            digital_score * 0.30 +
            contact_score * 0.35
        )
        
        return {
            'lead_id': lead.get('id', 'Unknown'),
            'company_name': lead.get('company_name', 'Unknown'),
            'firmographic_score': round(firmographic_score, 2),
            'digital_footprint_score': round(digital_score, 2),
            'contact_quality_score': round(contact_score, 2),
            'overall_score': round(overall_score, 2),
            'priority': self._get_priority(overall_score)
        }
    
    def _get_priority(self, score: float) -> str:
        """Determine priority level based on score"""
        if score >= 80:
            return 'High'
        elif score >= 60:
            return 'Medium'
        elif score >= 40:
            return 'Low'
        else:
            return 'Very Low'
    
    def score_leads(self, leads: List[Dict]) -> pd.DataFrame:
        """
        Score multiple leads and return sorted DataFrame
        
        Args:
            leads: List of lead dictionaries
            
        Returns:
            DataFrame with scored and ranked leads
        """
        scored_leads = [self.score_lead(lead) for lead in leads]
        df = pd.DataFrame(scored_leads)
        df = df.sort_values('overall_score', ascending=False)
        df['rank'] = range(1, len(df) + 1)
        
        return df
    
    def export_results(self, df: pd.DataFrame, filename: str = 'scored_leads.csv'):
        """
        Export scored leads to CSV
        
        Args:
            df: DataFrame with scored leads
            filename: Output filename
        """
        df.to_csv(filename, index=False)
        print(f"Results exported to {filename}")


def main():
    """Example usage of the LeadScorer"""
    print("🎯 Intelligent Lead Scoring Engine\n")
    
    # Example leads data
    sample_leads = [
        {
            'id': 'L001',
            'company_name': 'TechCorp Inc',
            'revenue': 15000000,
            'employees': 150,
            'industry': 'Technology',
            'recent_funding': True,
            'hiring_active': True,
            'tech_stack': ['React', 'AWS', 'Kubernetes'],
            'linkedin_followers': 5000,
            'twitter_followers': 2000,
            'engagement_rate': 0.15,
            'recent_news': True,
            'contact_title': 'CTO',
            'email': 'cto@techcorp.com',
            'phone': '+1-555-0100',
            'linkedin_url': 'linkedin.com/in/techcorp-cto',
            'email_verified': True,
            'responded_before': False
        },
        {
            'id': 'L002',
            'company_name': 'StartupXYZ',
            'revenue': 500000,
            'employees': 25,
            'industry': 'SaaS',
            'recent_funding': True,
            'hiring_active': True,
            'tech_stack': ['Vue', 'GCP'],
            'linkedin_followers': 500,
            'twitter_followers': 300,
            'engagement_rate': 0.08,
            'recent_news': False,
            'contact_title': 'CEO',
            'email': 'ceo@startupxyz.com',
            'phone': None,
            'linkedin_url': 'linkedin.com/in/startupxyz-ceo',
            'email_verified': True,
            'responded_before': True
        },
        {
            'id': 'L003',
            'company_name': 'MegaCorp Global',
            'revenue': 50000000,
            'employees': 5000,
            'industry': 'Manufacturing',
            'recent_funding': False,
            'hiring_active': False,
            'tech_stack': [],
            'linkedin_followers': 50000,
            'twitter_followers': 10000,
            'engagement_rate': 0.05,
            'recent_news': False,
            'contact_title': 'Sales Manager',
            'email': 'manager@megacorp.com',
            'phone': '+1-555-0200',
            'linkedin_url': None,
            'email_verified': False,
            'responded_before': False
        }
    ]
    
    # Initialize scorer
    scorer = LeadScorer()
    
    # Score leads
    print("Scoring leads...")
    results = scorer.score_leads(sample_leads)
    
    # Display results
    print("\n📊 Lead Scoring Results:\n")
    print(results.to_string(index=False))
    
    # Export results
    scorer.export_results(results)
    print("\n✅ Lead scoring complete!")


if __name__ == '__main__':
    main()
