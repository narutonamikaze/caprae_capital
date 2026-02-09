"""
Example usage of the Intelligent Lead Scoring Engine

This script demonstrates how to use the LeadScorer to score and rank leads.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lead_scorer import LeadScorer


def main():
    """Demonstrate lead scoring functionality"""
    
    # Initialize the scorer
    scorer = LeadScorer()
    
    print("=" * 80)
    print("Intelligent Lead Scoring Engine - Demo")
    print("=" * 80)
    print()
    
    # Sample leads
    leads = [
        {
            'company_name': 'TechCorp Inc',
            'revenue_range': '10M-50M',
            'industry': 'SaaS',
            'employee_count': 150,
            'website': 'https://techcorp.com',
            'contact_email': 'ceo@techcorp.com',
            'job_title': 'CEO',
            'tech_stack': ['React', 'Python', 'AWS'],
            'social_media': {'linkedin': True, 'twitter': True},
            'funding_status': 'Series A+',
            'growth_rate': 0.35
        },
        {
            'company_name': 'Small Startup LLC',
            'revenue_range': '1M-10M',
            'industry': 'Technology',
            'employee_count': 25,
            'website': 'https://smallstartup.com',
            'contact_email': 'founder@smallstartup.com',
            'job_title': 'Founder',
            'tech_stack': ['Vue', 'Node.js'],
            'funding_status': 'Seed'
        },
        {
            'company_name': 'Manufacturing Co',
            'revenue_range': '50M-100M',
            'industry': 'Manufacturing',
            'employee_count': 500,
            'website': 'https://mfgco.com',
            'contact_email': 'sales@mfgco.com',
            'job_title': 'Sales Manager'
        },
        {
            'company_name': 'Retail Store',
            'revenue_range': '0-1M',
            'industry': 'Retail',
            'employee_count': 8,
            'contact_email': 'owner@retailstore.com',
            'job_title': 'Owner'
        }
    ]
    
    # Score individual lead
    print("INDIVIDUAL LEAD SCORING")
    print("-" * 80)
    lead = leads[0]
    score_data = scorer.score_lead(lead)
    
    print(f"Company: {lead['company_name']}")
    print(f"Overall Score: {score_data['overall_score']} (Grade: {score_data['grade']})")
    print(f"  - Firmographics: {score_data['firmographics_score']}")
    print(f"  - Digital Footprint: {score_data['digital_footprint_score']}")
    print(f"  - Contact Quality: {score_data['contact_quality_score']}")
    print()
    
    # Rank all leads
    print("RANKED LEADS")
    print("-" * 80)
    ranked_leads = scorer.rank_leads(leads)
    
    for i, lead in enumerate(ranked_leads, 1):
        scores = lead['scores']
        print(f"{i}. {lead['company_name']}")
        print(f"   Score: {scores['overall_score']} | Grade: {scores['grade']}")
        print(f"   Industry: {lead.get('industry', 'N/A')} | "
              f"Revenue: {lead.get('revenue_range', 'N/A')} | "
              f"Employees: {lead.get('employee_count', 'N/A')}")
        print()
    
    # Score breakdown explanation
    print("SCORING METHODOLOGY")
    print("-" * 80)
    print("The Lead Scorer uses weighted scoring across three dimensions:")
    print(f"  1. Firmographics (40%): Revenue, industry, employee count, growth")
    print(f"  2. Digital Footprint (30%): Website, tech stack, social media, funding")
    print(f"  3. Contact Quality (30%): Email, phone, LinkedIn, decision-maker level")
    print()
    print("Grade Scale:")
    print("  A+ (90-100): Highest priority - immediate outreach")
    print("  A  (80-89):  High priority - outreach within 24h")
    print("  B  (70-79):  Medium priority - outreach within week")
    print("  C  (60-69):  Low priority - nurture campaign")
    print("  D  (50-59):  Very low priority - automated nurture")
    print("  F  (<50):    Not recommended for outreach")
    print()
    print("=" * 80)


if __name__ == '__main__':
    main()
