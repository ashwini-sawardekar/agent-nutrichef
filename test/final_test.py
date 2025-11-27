"""
Correct implementation using Google ADK Runner
Run from Projects directory: python final_test.py
"""
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

# Load .env file from the Projects folder (current directory)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, encoding='utf-8')

# Verify environment is loaded
if not os.getenv('GOOGLE_API_KEY'):
    print("⚠️  Warning: GOOGLE_API_KEY not found in environment")
    print(f"   Checked: {env_path.absolute()}")

from nutrichef_agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Constants
APP_NAME = "nutrichef_app"
USER_ID = "user_001"
SESSION_ID = "session_001"

async def main():
    """Main test function using proper ADK Runner"""
    
    user_message = """
    I need a 7-day meal plan with the following requirements:
    - Budget: $100
    - Diet: Keto
    - Allergies: Peanuts
    - Servings: 2 people
    - Current inventory: Chicken breast, spinach, eggs, butter
    
    Please create a meal plan and shopping list for me.
    """
    
    print("🍳 Starting NutriChef Agent...")
    print("=" * 60)
    print("\n🤖 NutriChef is working on your request...")
    print("    (This may take 1-2 minutes...)\n")
    
    try:
        # 1. Create session service
        session_service = InMemorySessionService()
        
        # 2. Create or get session
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID
        )
        
        # 3. Create runner with the agent
        runner = Runner(
            agent=root_agent,
            app_name=APP_NAME,
            session_service=session_service
        )
        
        # 4. Create user content
        user_content = types.Content(
            role="user",
            parts=[types.Part(text=user_message)]
        )
        
        # 5. Run the agent and collect responses
        print("Processing...\n")
        responses = []
        event_count = 0
        
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=user_content  # Correct parameter name
        ):
            event_count += 1
            
            # Extract content from event
            if hasattr(event, 'content') and event.content:
                if hasattr(event.content, 'parts'):
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            text = part.text.strip()
                            if text:
                                responses.append(text)
                                # Show progress
                                preview = text[:80] + "..." if len(text) > 80 else text
                                print(f"📝 {preview}")
        
        print("\n" + "=" * 60)
        print(f"✅ Completed! ({event_count} events processed)")
        print("=" * 60)
        
        # Display final output
        if responses:
            print("\n📋 FINAL MEAL PLAN & SHOPPING LIST:")
            print("=" * 60)
            full_response = "\n\n".join(responses)
            print(full_response)
        else:
            print("\n⚠️  No response text generated")
            print("This might mean the agent needs more configuration")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"Details: {str(e)}")
        
        import traceback
        traceback.print_exc()
        
        print("\n💡 Troubleshooting:")
        print("  1. Check API key is valid")
        print("  2. Test tools: python test_tools.py")
        print("  3. Verify setup: python check_setup.py")

if __name__ == "__main__":
    asyncio.run(main())