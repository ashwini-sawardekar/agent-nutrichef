"""
Correct test for NutriChef Agent using proper Google ADK API
Run from Projects directory: python correct_test.py
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
    print("✅ API key loaded successfully")
else:
    print("⚠️  API key not found")

from nutrichef_agent import root_agent
from google.adk.agents.invocation_context import InvocationContext

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
        # Create a proper invocation context
        context = InvocationContext(
            query=user_input,
            agent=root_agent
        )
        
        # Collect all events from the async generator
        all_events = []
        responses = []
        
        async for event in root_agent.run_async(context):
            all_events.append(event)
            
            # Extract content from events
            event_text = None
            
            if hasattr(event, 'content'):
                if isinstance(event.content, str):
                    event_text = event.content
                elif hasattr(event.content, 'text'):
                    event_text = event.content.text
            
            elif hasattr(event, 'text'):
                event_text = event.text
            
            if event_text and event_text.strip():
                responses.append(event_text)
                # Print progress
                preview = event_text[:100] + "..." if len(event_text) > 100 else event_text
                print(f"📝 {preview}")
        
        print("\n" + "=" * 60)
        print(f"✅ Agent Completed! ({len(all_events)} events processed)")
        print("=" * 60)
        
        # Display the final combined response
        if responses:
            print("\n📋 FINAL MEAL PLAN & SHOPPING LIST:")
            print("=" * 60)
            full_response = "\n\n".join(responses)
            print(full_response)
        else:
            print("\n⚠️  No text response generated.")
            print("\nDebugging - Event details:")
            for i, event in enumerate(all_events[:3], 1):  # Show first 3 events
                print(f"\nEvent {i}:")
                print(f"  Type: {type(event).__name__}")
                print(f"  Attributes: {[attr for attr in dir(event) if not attr.startswith('_')]}")
                if hasattr(event, '__dict__'):
                    print(f"  Data: {event.__dict__}")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"Details: {str(e)}")
        
        import traceback
        traceback.print_exc()
        
        print("\n💡 Troubleshooting tips:")
        print("  1. Run: python check_setup.py")
        print("  2. Test tools: python test_tools.py")
        print("  3. Update ADK: pip install --upgrade google-adk")

if __name__ == "__main__":
    asyncio.run(main())