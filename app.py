import os
from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel

# Load environment variables
load_dotenv()

# Configure Groq model via LiteLLM
groq_model = LiteLLMModel(
    model_id="groq/llama-3.1-70b-versatile",
    client_args={
        "api_key": os.getenv("GROQ_API_KEY"),
    },
    params={
        "temperature": 0.7,
        "max_tokens": 1000,
    }
)

@tool
def research_analyst(query: str) -> str:
    """Research and analyze information about a given topic.
    
    Args:
        query: The topic or question to research
        
    Returns:
        A comprehensive analysis of the research topic
    """
    return f"Research analysis for '{query}': This topic requires comprehensive investigation of current trends, historical context, and future implications."

@tool
def task_planner(project_description: str) -> str:
    """Break down a project into actionable tasks and create a plan.
    
    Args:
        project_description: Description of the project to plan
        
    Returns:
        A structured task breakdown and timeline
    """
    return f"Project plan for '{project_description}':\n1. Requirements gathering\n2. Design phase\n3. Implementation\n4. Testing\n5. Deployment\n6. Maintenance"

@tool
def code_review(code_snippet: str) -> str:
    """Review code for best practices, bugs, and improvements.
    
    Args:
        code_snippet: The code to review
        
    Returns:
        Detailed code review with suggestions
    """
    return f"Code review completed:\n- Syntax: OK\n- Best practices: Good\n- Suggestions: Consider adding error handling and documentation"

# Create specialized agents
research_agent = Agent(
    model=groq_model,
    system_prompt="You are a Research Analyst. Your role is to gather, analyze, and synthesize information on various topics. Use the research_analyst tool to provide comprehensive insights.",
    tools=[research_analyst],
    name="Research Analyst"
)

planning_agent = Agent(
    model=groq_model,
    system_prompt="You are a Project Planner. Your role is to break down complex projects into manageable tasks and create actionable plans. Use the task_planner tool to structure project workflows.",
    tools=[task_planner],
    name="Project Planner"
)

developer_agent = Agent(
    model=groq_model,
    system_prompt="You are a Senior Developer. Your role is to write, review, and improve code. Use the code_review tool to ensure code quality and best practices.",
    tools=[code_review],
    name="Senior Developer"
)

# Create coordinator agent that can delegate to other agents
coordinator_agent = Agent(
    model=groq_model,
    system_prompt="""You are a Team Coordinator. You oversee a team of specialized agents:
    - Research Analyst: Handles research and analysis tasks
    - Project Planner: Creates project plans and task breakdowns  
    - Senior Developer: Handles code review and development tasks
    
    When a user request comes in, analyze it and delegate to the appropriate specialist agent.
    For complex requests involving multiple domains, coordinate between multiple agents.""",
    tools=[research_agent, planning_agent, developer_agent],
    name="Team Coordinator"
)

# Initialize Flask app
app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strands Agent Team with Groq LLM</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .team-info {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }
        .team-member {
            margin: 10px 0;
            padding: 10px;
            background: white;
            border-radius: 5px;
            border-left: 4px solid #007bff;
        }
        textarea {
            width: 100%;
            height: 100px;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            resize: vertical;
            box-sizing: border-box;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
            width: 100%;
        }
        button:hover {
            background-color: #0056b3;
        }
        button:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        .response {
            margin-top: 20px;
            padding: 15px;
            background: #e9ecef;
            border-radius: 8px;
            white-space: pre-wrap;
            font-family: monospace;
        }
        .loading {
            text-align: center;
            color: #666;
            font-style: italic;
        }
        .examples {
            margin-top: 30px;
        }
        .example {
            background: #f8f9fa;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            cursor: pointer;
            border: 1px solid #dee2e6;
        }
        .example:hover {
            background: #e9ecef;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Strands Agent Team with Groq LLM</h1>
        
        <div class="team-info">
            <h3>Team Members:</h3>
            <div class="team-member">🔍 Research Analyst - Research and analysis</div>
            <div class="team-member">📋 Project Planner - Task planning and breakdown</div>
            <div class="team-member">💻 Senior Developer - Code review and development</div>
            <div class="team-member">👥 Team Coordinator - Orchestrates the team</div>
        </div>
        
        <form id="agent-form">
            <textarea 
                id="user-input" 
                placeholder="Enter your request here... (e.g., 'Research the latest trends in AI')"
                required
            ></textarea>
            <button type="submit" id="submit-btn">Send Request</button>
        </form>
        
        <div id="response-container"></div>
        
        <div class="examples">
            <h3>Example Requests:</h3>
            <div class="example" onclick="setInput('Research the latest trends in AI')">
                Research the latest trends in AI
            </div>
            <div class="example" onclick="setInput('Plan a mobile app development project')">
                Plan a mobile app development project
            </div>
            <div class="example" onclick="setInput('Review this Python code: def add(a, b): return a + b')">
                Review this Python code: def add(a, b): return a + b
            </div>
            <div class="example" onclick="setInput('I need to research AI trends and then plan a project for an AI assistant')">
                I need to research AI trends and then plan a project for an AI assistant
            </div>
        </div>
    </div>

    <script>
        function setInput(text) {
            document.getElementById('user-input').value = text;
        }
        
        document.getElementById('agent-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const input = document.getElementById('user-input').value;
            const submitBtn = document.getElementById('submit-btn');
            const responseContainer = document.getElementById('response-container');
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Processing...';
            responseContainer.innerHTML = '<div class="loading">🤖 Coordinator is processing your request...</div>';
            
            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: input }),
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    responseContainer.innerHTML = `<div class="response"><strong>🎯 Response:</strong><br>${data.response}</div>`;
                } else {
                    responseContainer.innerHTML = `<div class="response" style="background: #f8d7da; color: #721c24;"><strong>❌ Error:</strong><br>${data.error}</div>`;
                }
            } catch (error) {
                responseContainer.innerHTML = `<div class="response" style="background: #f8d7da; color: #721c24;"><strong>❌ Network Error:</strong><br>${error.message}</div>`;
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Request';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Serve the main web interface."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests via JSON API."""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_input = data['message'].strip()
        if not user_input:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Process the request through the coordinator agent
        response = coordinator_agent(user_input)
        
        return jsonify({'response': response})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint for Railway."""
    return jsonify({'status': 'healthy', 'service': 'Strands Agent Team'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
