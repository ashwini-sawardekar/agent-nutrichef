"""
Working test for NutriChef Agent
Run from Projects directory: python working_test.py
"""
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

# Load .env file from the Projects folder
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, encoding='utf-8')

print(f"📁 Loading .env from: {env_path.absolute()}")
if os.getenv('GOOGLE_API_KEY'):
    print(f"✅ API key loaded: {os.getenv('GOOGLE_API_KEY')[:10]}...{os.getenv('GOOGLE_API_KEY')[-4:]}\n")
else:
    print("⚠️  Warning: API key not found\n")

from nutrichef_agent import root_agent

async def main():
    """Main test function"""
    
    user_input = """
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
        # Collect all events from the async generator
        all_events = []
        responses = []
        
        async for event in root_agent.run_async(user_input):
            all_events.append(event)
            
            # Extract text/content from each event
            if hasattr(event, 'content') and event.content:
                content = str(event.content)
                if content.strip():
                    responses.append(content)
                    print(f"📝 {content[:100]}..." if len(content) > 100 else f"📝 {content}")
            
            elif hasattr(event, 'text') and event.text:
                text = str(event.text)
                if text.strip():
                    responses.append(text)
                    print(f"📝 {text[:100]}..." if len(text) > 100 else f"📝 {text}")
        
        print("\n" + "=" * 60)
        print(f"✅ Agent Completed! ({len(all_events)} events processed)")
        print("=" * 60)
        
        # Display the final combined response
        if responses:
            print("\n📋 FINAL MEAL PLAN & SHOPPING LIST:")
            print("=" * 60)
            full_response = "\n".join(responses)
            print(full_response)
        else:
            print("\n⚠️  No text response generated. Raw events:")
            for i, event in enumerate(all_events, 1):
                print(f"\nEvent {i}: {type(event).__name__}")
                print(f"  {event}")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"Details: {str(e)}")
        
        import traceback
        traceback.print_exc()
        
        print("\n💡 Troubleshooting tips:")
        print("  1. Verify API key: Check your .env file or environment variable")
        print("  2. Check internet connection")
        print("  3. Verify Google ADK version: pip install --upgrade google-adk")
        print("  4. Test tools only: python test_tools.py")

if __name__ == "__main__":
    asyncio.run(main())