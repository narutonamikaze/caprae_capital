#!/usr/bin/env python3
"""
Example script demonstrating how to use the Lead Scoring Engine
"""

from lead_scorer import LeadScorer
import json


def load_leads_from_json(filename: str):
    """Load leads from a JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found. Using sample data.")
        return None


def main():
    # Initialize the lead scorer
    scorer = LeadScorer()
    
    # Try to load leads from file, or use sample data
    leads = load_leads_from_json('leads.json')
    
    if not leads:
        # Sample leads for demonstration
        leads = [
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
                'linkedin_url': 'linkedin.com/in/startupxyz-ceo',
                'email_verified': True,
                'responded_before': True
            }
        ]
    
    # Score all leads
    print("🎯 Intelligent Lead Scoring Engine")
    print("=" * 50)
    print(f"\nScoring {len(leads)} leads...\n")
    
    results = scorer.score_leads(leads)
    
    # Display results
    print("📊 Scored Leads (Ranked by Overall Score):")
    print("=" * 50)
    print(results[['rank', 'company_name', 'overall_score', 'priority']].to_string(index=False))
    
    print("\n📈 Detailed Breakdown:")
    print("=" * 50)
    for _, lead in results.head(3).iterrows():
        print(f"\n{lead['rank']}. {lead['company_name']}")
        print(f"   Overall Score: {lead['overall_score']}/100 ({lead['priority']} Priority)")
        print(f"   - Firmographic Score: {lead['firmographic_score']}/100")
        print(f"   - Digital Footprint: {lead['digital_footprint_score']}/100")
        print(f"   - Contact Quality: {lead['contact_quality_score']}/100")
    
    # Export results
    output_file = 'scored_leads.csv'
    scorer.export_results(results, output_file)
    print(f"\n✅ Results exported to {output_file}")
    
    # Print summary statistics
    print("\n📊 Summary Statistics:")
    print("=" * 50)
    print(f"Total Leads Scored: {len(results)}")
    print(f"High Priority Leads: {len(results[results['priority'] == 'High'])}")
    print(f"Medium Priority Leads: {len(results[results['priority'] == 'Medium'])}")
    print(f"Low Priority Leads: {len(results[results['priority'] == 'Low'])}")
    print(f"Very Low Priority Leads: {len(results[results['priority'] == 'Very Low'])}")
    print(f"\nAverage Score: {results['overall_score'].mean():.2f}")
    print(f"Highest Score: {results['overall_score'].max():.2f}")
    print(f"Lowest Score: {results['overall_score'].min():.2f}")


if __name__ == '__main__':
    main()
