#!/usr/bin/env python3
"""
Working Strands Agent Team with Groq LLM
"""
import os
from dotenv import load_dotenv
from strands import Agent, tool

load_dotenv()

# Import the correct model class
from strands.models.litellm import LiteLLMModel

# Configure Groq model via LiteLLM
groq_model = LiteLLMModel(
    model_id="groq/llama-3.1-8b-instant",
    client_args={
        "api_key": os.getenv("GROQ_API_KEY"),
    },
    params={
        "temperature": 0.7,
        "max_tokens": 500,
    }
)

# Simple test agent
test_agent = Agent(
    model=groq_model,
    system_prompt="You are a helpful AI assistant. Respond clearly and concisely."
)

# Research agent with tool
@tool
def get_research_info(topic: str) -> str:
    """Get research information about a topic.
    
    Args:
        topic: The topic to research
        
    Returns:
        Research findings and insights
    """
    return f"Research on {topic}: This is a rapidly evolving field with significant implications for technology and society. Key areas include recent developments, current challenges, and future opportunities."

research_agent = Agent(
    model=groq_model,
    system_prompt="You are a research analyst. Use the get_research_info tool to provide comprehensive insights on topics.",
    tools=[get_research_info],
    name="Research Analyst"
)

# Planning agent with tool
@tool
def create_project_plan(project: str) -> str:
    """Create a structured project plan.
    
    Args:
        project: Description of the project
        
    Returns:
        Step-by-step project plan
    """
    return f"Project Plan for {project}:\n1. Define requirements and objectives\n2. Design architecture and approach\n3. Implement core functionality\n4. Test and validate\n5. Deploy and monitor\n6. Maintain and iterate"

planning_agent = Agent(
    model=groq_model,
    system_prompt="You are a project planner. Use the create_project_plan tool to break down projects into actionable steps.",
    tools=[create_project_plan],
    name="Project Planner"
)

# Coordinator agent
coordinator_agent = Agent(
    model=groq_model,
    system_prompt="""You are a team coordinator with access to:
    - Research Analyst: For research and analysis tasks
    - Project Planner: For project planning and task breakdown
    
    Analyze user requests and delegate to the appropriate agent. For research tasks, use the Research Analyst. For planning tasks, use the Project Planner.""",
    tools=[research_agent, planning_agent],
    name="Team Coordinator"
)

def test_basic_functionality():
    """Test basic agent functionality"""
    print("🧪 Testing Basic Agent Functionality")
    print("=" * 50)
    
    try:
        response = test_agent("Hello! Please confirm that Groq is working correctly.")
        print(f"✅ Basic Agent: {response}")
        return True
    except Exception as e:
        print(f"❌ Basic Agent Error: {e}")
        return False

def test_research_functionality():
    """Test research agent"""
    print("\n🔍 Testing Research Agent")
    print("=" * 50)
    
    try:
        response = research_agent("Research artificial intelligence trends")
        print(f"✅ Research Agent: {response}")
        return True
    except Exception as e:
        print(f"❌ Research Agent Error: {e}")
        return False

def test_planning_functionality():
    """Test planning agent"""
    print("\n📋 Testing Planning Agent")
    print("=" * 50)
    
    try:
        response = planning_agent("Plan a simple website development project")
        print(f"✅ Planning Agent: {response}")
        return True
    except Exception as e:
        print(f"❌ Planning Agent Error: {e}")
        return False

def test_coordinator():
    """Test coordinator agent"""
    print("\n👥 Testing Team Coordinator")
    print("=" * 50)
    
    try:
        response = coordinator_agent("I need to research machine learning")
        print(f"✅ Coordinator: {response}")
        return True
    except Exception as e:
        print(f"❌ Coordinator Error: {e}")
        return False

def interactive_mode():
    """Run interactive agent team"""
    print("\n🚀 Interactive Agent Team Mode")
    print("=" * 50)
    print("Available agents:")
    print("• Research Analyst - Research and analysis")
    print("• Project Planner - Project planning")
    print("• Team Coordinator - Delegates to specialists")
    print("\nType your requests or 'exit' to quit")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not user_input:
                continue
                
            print(f"\n🤖 Processing: {user_input}")
            response = coordinator_agent(user_input)
            print(f"\n🎯 Response: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 Strands Agent Team with Groq LLM")
    print("=" * 60)
    
    # Run tests
    success = True
    success &= test_basic_functionality()
    success &= test_research_functionality()
    success &= test_planning_functionality()
    success &= test_coordinator()
    
    if success:
        print("\n🎉 All tests passed!")
        print("\n💡 Starting interactive mode...")
        interactive_mode()
    else:
        print("\n❌ Some tests failed. Check the errors above.")
