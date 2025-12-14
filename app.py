from flask import Flask, render_template, request, jsonify
import os
from textwrap import dedent
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize API keys
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
AGNO_API_KEY = os.environ.get('AGNO_API_KEY')

# Fail fast if GROQ_API_KEY is missing when app starts (optional)
if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set. The /generate endpoint will return an error until it is configured.")

# Initialize the research agent
def create_research_agent():
    """Create and return a configured research agent"""
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[
            DuckDuckGoTools(),
            Newspaper4kTools()
        ],
        description=dedent("""
        You are an elite research analyst in the financial services domain.
        Your expertise encompasses:

        -Deep investigative financial research and analysis
        -Fact-checking and source verification
        -Data-driven reporting and visualization
        -Expert interview synthesis
        -Trend analysis and future predictions
        -Complex topic simplification
        -Ethical practices
        -Balanced perspective presentation
        -Global context integration
        """),
        instructions=dedent("""
        1. Research Phase
          -Search for 5 authoritative sources on the topic
          -Prioritize recent publications and expert opinions
          -Identify key stakeholders and perspectives

        2. Analysis Phase
          -Extract and verify critical information
          -Cross-reference across multiple sources
          -Identify emerging patterns and trends
          -Evaluate conflicting viewpoints
        3. Writing Phase
         -Craft an attention-grabbing headline
         -Structure content in Financial Report style
         -Include relevant quotes and statistics
         -Maintain objectivity and balance
         -Explain complex concepts clearly

        4. Quality Phase
          -Verify all facts and attributions
          -Ensure narrative flow and readability
          -Add context where necessary
          -Include future implications
        """),
        expected_output=dedent("""
         #{Compelling Headline}
         ## Executive Summary
         {Concise overview of key findings and significance}

         ## Background & Context
         {Historical context and importance}
         {Current landscape overview}

         ## Key Findings
         {Main discoveries and analysis}
         {Expert insights and quotes}

         ## Impact Analysis
         {Current implications}
         {Stakeholder perspectives}
         {Industry/societal effects}

         ## Future Outlook
         {Emerging trends}
         {Expert predictions}
         {Potential challenges and opportunities}

         ## Expert Insights
         {Notable quotes and analysis from industry leaders}
         {Contrasting viewpoints}

         ## Sources and Methodology
         {List of primary sources with key contributions}
         {Provide https:// links of all the primary sources}
         {Research methodology overview}


         ---
         Research conducted by Financial Agent
         Credit Rating Style Report
         Published:{current date}
         Last Updated:{current date}
        """),
        markdown=True,
    )

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_report():
    """Generate a financial research report based on user query"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Please provide a research query'
            }), 400
        
        # Check API keys
        if not GROQ_API_KEY:
            return jsonify({
                'success': False,
                'error': 'GROQ_API_KEY not configured. Please set the environment variable.'
            }), 500
        
        # Create agent and generate report
        research_agent = create_research_agent()
        # Generate the report
        response = research_agent.run(query)
        
        return jsonify({
            'success': True,
            'report': response.content
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'groq_api_key_set': bool(GROQ_API_KEY),
        'agno_api_key_set': bool(AGNO_API_KEY)
    })

if __name__ == '__main__':
    # Allows `flask run` or `python app.py`
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
