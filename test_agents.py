import os
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel

# Load environment variables
load_dotenv()

# Test Groq connection
def test_groq_connection():
    """Test basic connection to Groq API"""
    try:
        groq_model = LiteLLMModel(
            model_id="groq/llama-3.1-8b-instant",
            client_args={
                "api_key": os.getenv("GROQ_API_KEY"),
            },
            params={
                "temperature": 0.5,
                "max_tokens": 100,
            }
        )
        
        test_agent = Agent(
            model=groq_model,
            system_prompt="You are a helpful assistant. Respond briefly."
        )
        
        response = test_agent("Hello! Can you respond with 'Groq is working!'?")
        print(f"✅ Groq Connection Test: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Groq Connection Test Failed: {e}")
        return False

def test_individual_agents():
    """Test each agent individually"""
    from agent_team import research_agent, planning_agent, developer_agent
    
    print("\n🔍 Testing Research Agent...")
    try:
        response = research_agent("Briefly research artificial intelligence")
        print(f"✅ Research Agent: {response[:100]}...")
    except Exception as e:
        print(f"❌ Research Agent Error: {e}")
    
    print("\n📋 Testing Planning Agent...")
    try:
        response = planning_agent("Plan a simple website project")
        print(f"✅ Planning Agent: {response[:100]}...")
    except Exception as e:
        print(f"❌ Planning Agent Error: {e}")
    
    print("\n💻 Testing Developer Agent...")
    try:
        response = developer_agent("Review this Python code: print('hello')")
        print(f"✅ Developer Agent: {response[:100]}...")
    except Exception as e:
        print(f"❌ Developer Agent Error: {e}")

if __name__ == "__main__":
    print("🧪 Testing Strands Agent Team with Groq")
    print("=" * 50)
    
    # Test basic connection
    if test_groq_connection():
        print("\n🎯 Testing individual agents...")
        test_individual_agents()
    else:
        print("\n❌ Basic connection failed. Please check your GROQ_API_KEY.")
