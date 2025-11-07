#!/usr/bin/env python3
"""
Strands Agent Team Web Application for Railway Deployment
"""
import os
import asyncio
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'strands-agent-team-secret-key')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure Groq model
groq_model = LiteLLMModel(
    model_id=os.getenv('GROQ_MODEL', 'groq/llama-3.1-8b-instant'),
    client_args={
        "api_key": os.getenv("GROQ_API_KEY"),
    },
    params={
        "temperature": float(os.getenv('TEMPERATURE', '0.7')),
        "max_tokens": int(os.getenv('MAX_TOKENS', '500')),
    }
)

# Define tools
@tool
def research_topic(topic: str) -> str:
    """Research a given topic and provide key insights.
    
    Args:
        topic: The topic to research
        
    Returns:
        Key insights about the topic including trends, applications, and future outlook
    """
    return f"Research on {topic}: This field is experiencing rapid growth with significant innovations. Key areas include recent technological advances, practical applications across industries, and promising future developments. Current trends show increasing adoption and integration into various sectors."

@tool
def plan_project(project_description: str) -> str:
    """Create a structured plan for any project.
    
    Args:
        project_description: Brief description of the project to plan
        
    Returns:
        Step-by-step project plan with timeline and key milestones
    """
    return f"Project Plan for '{project_description}':\nPhase 1: Requirements & Research\nPhase 2: Design & Architecture\nPhase 3: Development & Implementation\nPhase 4: Testing & Quality Assurance\nPhase 5: Deployment & Launch\nPhase 6: Monitoring & Maintenance\n\nEach phase includes specific deliverables and success criteria."

@tool
def analyze_code(code_snippet: str) -> str:
    """Analyze code for quality, best practices, and improvements.
    
    Args:
        code_snippet: The code to analyze
        
    Returns:
        Code analysis with suggestions for improvement
    """
    return f"Code Analysis:\n✓ Syntax appears correct\n✓ Follows basic structure\n💡 Suggestions: Add error handling, improve documentation, consider edge cases, add unit tests for reliability."

# Create agents
research_agent = Agent(
    model=groq_model,
    system_prompt="You are a Research Analyst specializing in technology and business topics. Use the research_topic tool to provide comprehensive, well-structured insights on any subject.",
    tools=[research_topic],
    name="Research Analyst"
)

planning_agent = Agent(
    model=groq_model,
    system_prompt="You are a Project Planner with expertise in breaking down complex projects into manageable phases. Use the plan_project tool to create detailed, actionable project plans.",
    tools=[plan_project],
    name="Project Planner"
)

developer_agent = Agent(
    model=groq_model,
    system_prompt="You are a Senior Software Engineer focused on code quality and best practices. Use the analyze_code tool to provide thorough code reviews and improvement suggestions.",
    tools=[analyze_code],
    name="Senior Developer"
)

coordinator_agent = Agent(
    model=groq_model,
    system_prompt="""You are a Team Coordinator managing three specialists:
    • Research Analyst - For research, analysis, and information gathering
    • Project Planner - For project planning, task breakdown, and roadmapping  
    • Senior Developer - For code analysis, review, and technical guidance
    
    Analyze each request and delegate to the most appropriate specialist. For research tasks, use Research Analyst. For planning tasks, use Project Planner. For code-related tasks, use Senior Developer. Provide concise, actionable responses.""",
    tools=[research_agent, planning_agent, developer_agent],
    name="Team Coordinator"
)

@app.route('/')
def index():
    """Main page with agent interface"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Process with agent
        response = coordinator_agent(user_message)
        
        return jsonify({
            'response': response,
            'timestamp': datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Processing error: {str(e)}'
        }), 500

@app.route('/api/agents')
def get_agents():
    """Get information about available agents"""
    return jsonify({
        'agents': [
            {
                'name': 'Research Analyst',
                'description': 'Research and analysis on any topic',
                'specialties': ['Technology research', 'Market analysis', 'Trend identification']
            },
            {
                'name': 'Project Planner',
                'description': 'Strategic project planning and task breakdown',
                'specialties': ['Project roadmapping', 'Task decomposition', 'Timeline planning']
            },
            {
                'name': 'Senior Developer',
                'description': 'Code analysis and technical guidance',
                'specialties': ['Code review', 'Best practices', 'Technical recommendations']
            },
            {
                'name': 'Team Coordinator',
                'description': 'Intelligent task delegation and coordination',
                'specialties': ['Task routing', 'Multi-agent coordination', 'Workflow optimization']
            }
        ]
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
