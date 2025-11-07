import os
from dotenv import load_dotenv
import litellm

load_dotenv()

# Test direct LiteLLM call
try:
    response = litellm.completion(
        model="groq/llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Hello"}],
        api_key=os.getenv("GROQ_API_KEY")
    )
    print("✅ Direct LiteLLM test passed")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ Direct LiteLLM test failed: {e}")
    print(f"API Key: {os.getenv('GROQ_API_KEY')[:10]}...")
