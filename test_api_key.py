#!/usr/bin/env python3
"""
Test script to verify Groq API key functionality
"""
import os
from dotenv import load_dotenv
import litellm

# Load environment variables
load_dotenv()

def test_api_key():
    """Test the Groq API key with a simple request"""
    
    api_key = os.getenv("GROQ_API_KEY")
    
    print("🔑 Testing Groq API Key")
    print("=" * 40)
    
    if not api_key:
        print("❌ No API key found in environment variables")
        print("Please ensure GROQ_API_KEY is set in your .env file")
        return False
    
    print(f"📋 API Key found: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    # Test with different Groq models
    models_to_test = [
        "groq/llama-3.1-8b-instant",
        "groq/llama-3.1-70b-versatile",
        "groq/mixtral-8x7b-32768"
    ]
    
    for model in models_to_test:
        print(f"🧪 Testing model: {model}")
        try:
            response = litellm.completion(
                model=model,
                messages=[{"role": "user", "content": "Hello! Respond with 'API key is working'"}],
                api_key=api_key,
                max_tokens=50,
                temperature=0.1
            )
            
            result = response.choices[0].message.content
            print(f"✅ Success: {result}")
            print()
            
            # If first model works, we can stop
            break
            
        except Exception as e:
            print(f"❌ Failed: {e}")
            print()
    
    # Test with verbose logging for debugging
    print("🔍 Testing with debug logging...")
    litellm.set_verbose=True
    
    try:
        response = litellm.completion(
            model="groq/llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Test"}],
            api_key=api_key
        )
        print("✅ Debug test passed")
        
    except Exception as e:
        print(f"❌ Debug test failed: {e}")
        return False
    
    return True

def test_alternative_method():
    """Test using direct Groq client if available"""
    try:
        import groq
        from groq import Groq
        
        api_key = os.getenv("GROQ_API_KEY")
        client = Groq(api_key=api_key)
        
        print("🔧 Testing with direct Groq client...")
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Hello!"}],
            max_tokens=50
        )
        
        print(f"✅ Direct client test: {response.choices[0].message.content}")
        return True
        
    except ImportError:
        print("📦 Groq client not installed, installing...")
        os.system("pip install groq")
        return test_alternative_method()
        
    except Exception as e:
        print(f"❌ Direct client test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Groq API Key Verification Tool")
    print("=" * 50)
    
    # Test with LiteLLM
    success = test_api_key()
    
    if not success:
        print("\n" + "=" * 50)
        print("🔧 Trying alternative method...")
        test_alternative_method()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 API key is working correctly!")
    else:
        print("⚠️  API key test failed. Please check:")
        print("   1. API key is valid and active")
        print("   2. Account has sufficient credits")
        print("   3. Network connection is stable")
        print("   4. API key is properly set in .env file")
