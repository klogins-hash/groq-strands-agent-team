import os
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel

# Load environment variables
load_dotenv()

# Configure Groq model via LiteLLM (non-streaming)
groq_model = LiteLLMModel(
    model_id="groq/llama-3.1-70b-versatile",
    client_args={
        "api_key": os.getenv("GROQ_API_KEY"),
    },
    params={
        "temperature": 0.7,
        "max_tokens": 1000,
        "stream": False,  # Disable streaming to avoid the error
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

def main():
    print("🚀 Strands Agent Team with Groq LLM")
    print("=" * 50)
    print("Team Members:")
    print("🔍 Research Analyst - Research and analysis")
    print("📋 Project Planner - Task planning and breakdown")
    print("💻 Senior Developer - Code review and development")
    print("👥 Team Coordinator - Orchestrates the team")
    print("=" * 50)
    print("\nType your requests or 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not user_input:
                continue
                
            print(f"\n🤖 Coordinator is processing: {user_input}")
            response = coordinator_agent(user_input)
            print(f"\n🎯 Response: {response}\n")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
