#!/usr/bin/env python3
"""
Simple test of the agent team with Groq
"""
import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.litellm import LiteLLMModel

load_dotenv()

# Configure Groq model
groq_model = LiteLLMModel(
    model_id="groq/llama-3.1-8b-instant",
    client_args={
        "api_key": os.getenv("GROQ_API_KEY"),
    },
    params={
        "temperature": 0.7,
        "max_tokens": 200,
    }
)

def test_basic_agent():
    """Test a basic agent"""
    print("🤖 Testing Basic Agent with Groq")
    print("=" * 40)
    
    agent = Agent(
        model=groq_model,
        system_prompt="You are a helpful assistant. Respond briefly and clearly."
    )
    
    try:
        response = agent("Hello! Tell me in one sentence why Groq is fast.")
        print(f"✅ Agent Response: {response}")
        return True
    except Exception as e:
        print(f"❌ Agent Error: {e}")
        return False

def test_research_agent():
    """Test the research agent"""
    from agent_team_final import research_agent
    
    print("\n🔍 Testing Research Agent")
    print("=" * 40)
    
    try:
        response = research_agent("Briefly research what makes AI agents useful")
        print(f"✅ Research Response: {response}")
        return True
    except Exception as e:
        print(f"❌ Research Agent Error: {e}")
        return False

def test_coordinator():
    """Test the coordinator agent"""
    from agent_team_final import coordinator_agent
    
    print("\n👥 Testing Team Coordinator")
    print("=" * 40)
    
    try:
        response = coordinator_agent("I need to research AI trends")
        print(f"✅ Coordinator Response: {response}")
        return True
    except Exception as e:
        print(f"❌ Coordinator Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Strands Agent Team Test")
    print("=" * 50)
    
    # Test basic functionality
    if test_basic_agent():
        test_research_agent()
        test_coordinator()
        
        print("\n🎉 All tests completed!")
        print("\n💡 To run the interactive agent team:")
        print("   python agent_team_final.py")
    else:
        print("\n❌ Basic test failed")
