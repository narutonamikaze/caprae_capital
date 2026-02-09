"""
Unit tests for the Lead Scorer module
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lead_scorer import LeadScorer


class TestLeadScorer(unittest.TestCase):
    """Test cases for the LeadScorer class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.scorer = LeadScorer()
    
    def test_initialization(self):
        """Test that scorer initializes with correct weights"""
        self.assertEqual(self.scorer.weights['firmographics'], 0.4)
        self.assertEqual(self.scorer.weights['digital_footprint'], 0.3)
        self.assertEqual(self.scorer.weights['contact_quality'], 0.3)
    
    def test_score_firmographics_revenue(self):
        """Test firmographics scoring with revenue data"""
        lead_data = {'revenue_range': '10M-50M'}
        score = self.scorer.score_firmographics(lead_data)
        self.assertEqual(score, 70)
    
    def test_score_firmographics_industry(self):
        """Test firmographics scoring with industry data"""
        lead_data = {'industry': 'SaaS'}
        score = self.scorer.score_firmographics(lead_data)
        self.assertEqual(score, 95)
    
    def test_score_firmographics_employee_count(self):
        """Test firmographics scoring with employee count"""
        lead_data = {'employee_count': 150}
        score = self.scorer.score_firmographics(lead_data)
        self.assertEqual(score, 70)
    
    def test_score_firmographics_combined(self):
        """Test combined firmographics scoring"""
        lead_data = {
            'revenue_range': '50M-100M',
            'industry': 'Technology',
            'employee_count': 300
        }
        score = self.scorer.score_firmographics(lead_data)
        # (85 + 90 + 85) / 3 = 86.67
        self.assertAlmostEqual(score, 86.67, places=1)
    
    def test_score_digital_footprint_website(self):
        """Test digital footprint scoring with website"""
        lead_data = {'website': 'https://example.com'}
        score = self.scorer.score_digital_footprint(lead_data)
        self.assertEqual(score, 80)
    
    def test_score_digital_footprint_tech_stack(self):
        """Test digital footprint scoring with tech stack"""
        lead_data = {'tech_stack': ['React', 'Python', 'AWS']}
        score = self.scorer.score_digital_footprint(lead_data)
        # 50 + 3 * 10 = 80
        self.assertEqual(score, 80)
    
    def test_score_contact_quality_email(self):
        """Test contact quality scoring with email"""
        lead_data = {'contact_email': 'john@example.com'}
        score = self.scorer.score_contact_quality(lead_data)
        self.assertEqual(score, 70)
    
    def test_score_contact_quality_decision_maker_email(self):
        """Test contact quality scoring with decision maker email"""
        lead_data = {'contact_email': 'ceo@example.com'}
        score = self.scorer.score_contact_quality(lead_data)
        self.assertEqual(score, 95)
    
    def test_score_contact_quality_job_title(self):
        """Test contact quality scoring with job title"""
        lead_data = {'job_title': 'CEO'}
        score = self.scorer.score_contact_quality(lead_data)
        self.assertEqual(score, 95)
    
    def test_score_lead_complete(self):
        """Test complete lead scoring"""
        lead_data = {
            'revenue_range': '10M-50M',
            'industry': 'SaaS',
            'employee_count': 150,
            'website': 'https://example.com',
            'contact_email': 'ceo@example.com'
        }
        result = self.scorer.score_lead(lead_data)
        
        self.assertIn('overall_score', result)
        self.assertIn('firmographics_score', result)
        self.assertIn('digital_footprint_score', result)
        self.assertIn('contact_quality_score', result)
        self.assertIn('grade', result)
        
        # Verify score is within valid range
        self.assertGreaterEqual(result['overall_score'], 0)
        self.assertLessEqual(result['overall_score'], 100)
    
    def test_get_grade(self):
        """Test grade assignment"""
        self.assertEqual(self.scorer._get_grade(95), 'A+')
        self.assertEqual(self.scorer._get_grade(85), 'A')
        self.assertEqual(self.scorer._get_grade(75), 'B')
        self.assertEqual(self.scorer._get_grade(65), 'C')
        self.assertEqual(self.scorer._get_grade(55), 'D')
        self.assertEqual(self.scorer._get_grade(45), 'F')
    
    def test_rank_leads(self):
        """Test ranking multiple leads"""
        leads = [
            {'company_name': 'Low Score', 'revenue_range': '0-1M'},
            {'company_name': 'High Score', 'revenue_range': '100M+', 'industry': 'SaaS'},
            {'company_name': 'Medium Score', 'revenue_range': '10M-50M'}
        ]
        
        ranked = self.scorer.rank_leads(leads)
        
        # Verify they are sorted by score (descending)
        self.assertEqual(ranked[0]['company_name'], 'High Score')
        self.assertEqual(ranked[2]['company_name'], 'Low Score')
    
    def test_empty_lead_data(self):
        """Test scoring with empty lead data"""
        lead_data = {}
        result = self.scorer.score_lead(lead_data)
        
        # Should return default score of 50
        self.assertEqual(result['firmographics_score'], 50)
        self.assertEqual(result['digital_footprint_score'], 50)
        self.assertEqual(result['contact_quality_score'], 50)
        self.assertEqual(result['overall_score'], 50)
        self.assertEqual(result['grade'], 'D')


if __name__ == '__main__':
    unittest.main()
