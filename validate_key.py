#!/usr/bin/env python3
"""
Validate Groq API key format and test with curl
"""
import os
import subprocess
import json
from dotenv import load_dotenv

load_dotenv()

def validate_key_format():
    """Check if the API key has the correct format"""
    api_key = os.getenv("GROQ_API_KEY")
    
    print("🔍 Validating API Key Format")
    print("=" * 40)
    
    if not api_key:
        print("❌ No API key found")
        return False
    
    print(f"📋 API Key: {api_key[:10]}...{api_key[-4:]}")
    print(f"📏 Length: {len(api_key)} characters")
    
    # Groq API keys should start with 'gsk_' and be 56 characters long
    if not api_key.startswith('gsk_'):
        print("❌ API key should start with 'gsk_'")
        return False
    
    if len(api_key) != 56:
        print(f"❌ API key should be 56 characters, got {len(api_key)}")
        return False
    
    print("✅ API key format is correct")
    return True

def test_with_curl():
    """Test API key using curl command"""
    api_key = os.getenv("GROQ_API_KEY")
    
    print("\n🌐 Testing with curl")
    print("=" * 40)
    
    # Prepare curl command
    curl_cmd = [
        'curl', '-X', 'POST',
        'https://api.groq.com/openai/v1/chat/completions',
        '-H', 'Content-Type: application/json',
        '-H', f'Authorization: Bearer {api_key}',
        '-d', json.dumps({
            'model': 'llama-3.1-8b-instant',
            'messages': [{'role': 'user', 'content': 'Hello'}],
            'max_tokens': 10
        })
    ]
    
    try:
        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            response = json.loads(result.stdout)
            if 'choices' in response:
                print("✅ curl test successful!")
                print(f"Response: {response['choices'][0]['message']['content']}")
                return True
            else:
                print(f"❌ Unexpected response: {response}")
                return False
        else:
            print(f"❌ curl failed with return code {result.returncode}")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ curl request timed out")
        return False
    except Exception as e:
        print(f"❌ curl test failed: {e}")
        return False

def check_account_status():
    """Provide guidance on checking account status"""
    print("\n💡 Account Status Checklist")
    print("=" * 40)
    print("1. Visit https://console.groq.com/")
    print("2. Check if your account is active")
    print("3. Verify you have API credits available")
    print("4. Generate a new API key if needed")
    print("5. Ensure the key is copied correctly (no extra spaces)")

if __name__ == "__main__":
    print("🔑 Groq API Key Validation Tool")
    print("=" * 50)
    
    # Validate format
    format_valid = validate_key_format()
    
    if format_valid:
        # Test with curl
        curl_success = test_with_curl()
        
        if not curl_success:
            check_account_status()
    else:
        print("\n❌ API key format is invalid")
        check_account_status()
    
    print("\n" + "=" * 50)
    print("📝 Next Steps:")
    print("1. Generate a fresh API key from Groq console")
    print("2. Update your .env file with the new key")
    print("3. Run this test again to verify")
