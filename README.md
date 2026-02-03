# 🎯 Caprae Capital - Intelligent Lead Scoring Engine

An AI-powered lead scoring and prioritization tool that addresses the critical challenge of lead quality over quantity. This tool automatically scores and ranks prospects based on multiple conversion factors, helping sales teams focus on the most promising leads.

## 🌟 Features

### Core Capabilities

**Company Firmographics Analysis**
- Revenue range matching
- Industry alignment
- Employee count optimization
- Growth indicators (funding, hiring activity)

**Digital Footprint Analysis**
- Website technology stack evaluation
- Social media presence assessment
- Content engagement level tracking
- Recent funding or news monitoring

**Contact Quality Assessment**
- Decision-maker identification
- Contact information completeness validation
- Engagement probability scoring

## 💼 Value Proposition & Business Impact

**Why This Approach Maximizes Business Value:**

✅ **Solves the Volume Problem**: Sales teams get overwhelmed with unqualified leads. This tool prioritizes the most promising prospects.

✅ **Increases Conversion Rates**: By focusing on high-scoring leads first, sales teams can achieve better ROI on their outreach efforts.

✅ **Reduces Manual Qualification Time**: Automated scoring eliminates hours of manual lead research and qualification.

✅ **Scalable Intelligence**: The AI model improves over time as it learns from successful conversions.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation on Your Personal PC

1. **Clone the repository**
```bash
git clone https://github.com/narutonamikaze/caprae_capital.git
cd caprae_capital
```

2. **Create a virtual environment (recommended)**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

Run the example script to see the lead scorer in action:

```bash
python example_usage.py
```

This will:
- Load sample leads from `leads.json`
- Score and rank them based on multiple factors
- Display detailed results
- Export results to `scored_leads.csv`

### Using the Lead Scorer in Your Code

```python
from lead_scorer import LeadScorer

# Initialize the scorer
scorer = LeadScorer()

# Define your leads
leads = [
    {
        'id': 'L001',
        'company_name': 'TechCorp Inc',
        'revenue': 15000000,
        'employees': 150,
        'industry': 'Technology',
        'recent_funding': True,
        'tech_stack': ['React', 'AWS'],
        'contact_title': 'CTO',
        'email': 'cto@techcorp.com',
        # ... more fields
    }
]

# Score the leads
results = scorer.score_leads(leads)

# Export results
scorer.export_results(results, 'my_scored_leads.csv')
```

### Working with Your Own Data

1. Create a `leads.json` file with your lead data following the example format
2. Run `python example_usage.py`
3. Check the generated `scored_leads.csv` for results

### Lead Data Format

Each lead should include the following fields (optional fields can be omitted):

```json
{
  "id": "unique_id",
  "company_name": "Company Name",
  "revenue": 1000000,
  "employees": 50,
  "industry": "Technology",
  "recent_funding": true,
  "hiring_active": true,
  "tech_stack": ["React", "AWS"],
  "linkedin_followers": 1000,
  "twitter_followers": 500,
  "engagement_rate": 0.10,
  "recent_news": false,
  "contact_title": "CEO",
  "email": "contact@company.com",
  "phone": "+1-555-0100",
  "linkedin_url": "linkedin.com/in/contact",
  "email_verified": true,
  "responded_before": false
}
```

## 📊 Scoring Methodology

The lead scoring engine evaluates three main dimensions:

1. **Firmographic Score (35% weight)**: Company size, revenue, industry alignment, growth signals
2. **Digital Footprint Score (30% weight)**: Technology stack, social media presence, engagement
3. **Contact Quality Score (35% weight)**: Decision-maker level, contact completeness, verification

Final scores range from 0-100 with priority levels:
- **High Priority**: 80-100
- **Medium Priority**: 60-79
- **Low Priority**: 40-59
- **Very Low Priority**: 0-39

## 📁 Project Structure

```
caprae_capital/
├── lead_scorer.py      # Main lead scoring engine
├── example_usage.py    # Example usage script
├── leads.json          # Sample lead data
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🔧 Customization

You can customize the scoring weights in the `lead_scorer.py` file:

```python
# Adjust weights in the score_lead method
overall_score = (
    firmographic_score * 0.35 +    # Adjust this weight
    digital_score * 0.30 +          # Adjust this weight
    contact_score * 0.35            # Adjust this weight
)
```

## 📝 License

This project is open source and available for personal and commercial use.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📧 Contact

For questions or support, please open an issue on GitHub.
