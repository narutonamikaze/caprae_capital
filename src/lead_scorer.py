"""
Lead Scorer Module

This module implements an AI-powered lead scoring system that evaluates leads based on:
- Company firmographics (revenue, industry, employee count)
- Digital footprint analysis
- Contact quality assessment
"""

from typing import Dict, Any


class LeadScorer:
    """
    Intelligent Lead Scoring Engine
    
    Scores leads based on multiple factors including company firmographics,
    digital footprint, and contact quality.
    """
    
    def __init__(self):
        """Initialize the Lead Scorer with default weights"""
        self.weights = {
            'firmographics': 0.4,
            'digital_footprint': 0.3,
            'contact_quality': 0.3
        }
        
        # Revenue range scoring (in millions)
        self.revenue_scores = {
            '0-1M': 20,
            '1M-10M': 40,
            '10M-50M': 70,
            '50M-100M': 85,
            '100M+': 95
        }
        
        # Industry alignment scores
        self.industry_scores = {
            'Technology': 90,
            'SaaS': 95,
            'Finance': 80,
            'Healthcare': 75,
            'Manufacturing': 60,
            'Retail': 55,
            'Other': 40
        }
        
        # Employee count scoring
        self.employee_ranges = [
            (1, 10, 30),
            (11, 50, 50),
            (51, 200, 70),
            (201, 500, 85),
            (501, float('inf'), 95)
        ]
    
    def score_firmographics(self, lead_data: Dict[str, Any]) -> float:
        """
        Score based on company firmographics
        
        Args:
            lead_data: Dictionary containing company information
            
        Returns:
            Firmographics score (0-100)
        """
        score = 0
        count = 0
        
        # Revenue scoring
        if 'revenue_range' in lead_data:
            revenue = lead_data['revenue_range']
            score += self.revenue_scores.get(revenue, 40)
            count += 1
        
        # Industry scoring
        if 'industry' in lead_data:
            industry = lead_data['industry']
            score += self.industry_scores.get(industry, 40)
            count += 1
        
        # Employee count scoring
        if 'employee_count' in lead_data:
            emp_count = lead_data['employee_count']
            emp_score = self._score_employee_count(emp_count)
            score += emp_score
            count += 1
        
        # Growth indicators
        if 'growth_rate' in lead_data:
            growth = lead_data.get('growth_rate', 0)
            if growth > 0.3:  # 30% growth
                score += 90
            elif growth > 0.15:  # 15% growth
                score += 70
            else:
                score += 50
            count += 1
        
        return score / count if count > 0 else 50
    
    def score_digital_footprint(self, lead_data: Dict[str, Any]) -> float:
        """
        Score based on digital presence and footprint
        
        Args:
            lead_data: Dictionary containing digital presence information
            
        Returns:
            Digital footprint score (0-100)
        """
        score = 0
        count = 0
        
        # Website presence
        if 'website' in lead_data and lead_data['website']:
            score += 80
            count += 1
        
        # Technology stack (modern tech = higher score)
        if 'tech_stack' in lead_data:
            tech = lead_data['tech_stack']
            if isinstance(tech, list):
                # Modern frameworks indicate tech-savvy company
                modern_tech = ['React', 'Vue', 'Angular', 'Python', 'Node.js', 'AWS', 'Azure']
                tech_score = min(100, 50 + len([t for t in tech if t in modern_tech]) * 10)
                score += tech_score
                count += 1
        
        # Social media presence
        if 'social_media' in lead_data:
            social = lead_data['social_media']
            if isinstance(social, dict):
                platforms = len([k for k, v in social.items() if v])
                score += min(100, 40 + platforms * 15)
                count += 1
        
        # Recent news/funding
        if 'recent_news' in lead_data and lead_data['recent_news']:
            score += 85
            count += 1
        
        if 'funding_status' in lead_data:
            funding = lead_data['funding_status']
            if funding == 'Series A+':
                score += 90
            elif funding == 'Seed':
                score += 70
            else:
                score += 50
            count += 1
        
        return score / count if count > 0 else 50
    
    def score_contact_quality(self, lead_data: Dict[str, Any]) -> float:
        """
        Score based on contact information quality
        
        Args:
            lead_data: Dictionary containing contact information
            
        Returns:
            Contact quality score (0-100)
        """
        score = 0
        count = 0
        
        # Email presence and quality
        if 'contact_email' in lead_data:
            email = lead_data['contact_email']
            if email and '@' in email:
                # Decision maker emails (ceo, cto, founder, etc.)
                if any(role in email.lower() for role in ['ceo', 'cto', 'founder', 'vp', 'director']):
                    score += 95
                else:
                    score += 70
                count += 1
        
        # Phone number
        if 'contact_phone' in lead_data and lead_data['contact_phone']:
            score += 75
            count += 1
        
        # LinkedIn profile
        if 'linkedin_url' in lead_data and lead_data['linkedin_url']:
            score += 80
            count += 1
        
        # Decision maker identification
        if 'job_title' in lead_data:
            title = lead_data['job_title'].lower()
            if any(role in title for role in ['ceo', 'chief', 'president', 'founder', 'owner']):
                score += 95
            elif any(role in title for role in ['vp', 'vice president', 'director', 'head']):
                score += 85
            elif any(role in title for role in ['manager', 'lead']):
                score += 65
            else:
                score += 40
            count += 1
        
        # Completeness bonus
        if 'data_completeness' in lead_data:
            completeness = lead_data['data_completeness']
            score += completeness * 100
            count += 1
        
        return score / count if count > 0 else 50
    
    def score_lead(self, lead_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate overall lead score
        
        Args:
            lead_data: Dictionary containing all lead information
            
        Returns:
            Dictionary with overall score and component scores
        """
        firmographics_score = self.score_firmographics(lead_data)
        digital_score = self.score_digital_footprint(lead_data)
        contact_score = self.score_contact_quality(lead_data)
        
        # Weighted overall score
        overall_score = (
            firmographics_score * self.weights['firmographics'] +
            digital_score * self.weights['digital_footprint'] +
            contact_score * self.weights['contact_quality']
        )
        
        return {
            'overall_score': round(overall_score, 2),
            'firmographics_score': round(firmographics_score, 2),
            'digital_footprint_score': round(digital_score, 2),
            'contact_quality_score': round(contact_score, 2),
            'grade': self._get_grade(overall_score)
        }
    
    def _score_employee_count(self, count: int) -> float:
        """Score based on employee count"""
        for min_emp, max_emp, score in self.employee_ranges:
            if min_emp <= count <= max_emp:
                return score
        return 30
    
    def _get_grade(self, score: float) -> str:
        """Convert numerical score to letter grade"""
        if score >= 90:
            return 'A+'
        elif score >= 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'F'
    
    def rank_leads(self, leads: list) -> list:
        """
        Rank multiple leads by their scores
        
        Args:
            leads: List of lead data dictionaries
            
        Returns:
            List of leads sorted by score (highest first)
        """
        scored_leads = []
        for lead in leads:
            score_data = self.score_lead(lead)
            scored_leads.append({
                **lead,
                'scores': score_data
            })
        
        # Sort by overall score (descending)
        return sorted(scored_leads, key=lambda x: x['scores']['overall_score'], reverse=True)
