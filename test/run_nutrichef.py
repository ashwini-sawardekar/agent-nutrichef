"""
Clean runner for NutriChef Agent - suppresses warnings
Run: python run_nutrichef.py
"""
import warnings
import asyncio
from pathlib import Path
from dotenv import load_dotenv
import sys

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

# Load environment
load_dotenv(Path('.') / '.env', encoding='utf-8')

from nutrichef_agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

async def main():
    """Run NutriChef with full agent stack"""
    
    user_message = """
    Create a high-protein, low-budget plan for the week for 2 people. I have Peanut allergy. I have chicken breasts.
    """
    
    print("🍳 NutriChef Agent - Full Meal Planning System")
    print("=" * 60)
    print("\n📋 Your Requirements:")
    print("   • Budget: low-budget")
    print("   • Diet: high-protein")
    print("   • Allergies: Peanuts")
    print("   • Servings: 2 people")
    print("   • Inventory: Chicken breast")
    print("\n" + "-" * 60)
    print("🤖 Processing your request...")
    print("   (This uses multiple AI agents and may take 1-2 minutes)")
    print("-" * 60 + "\n")
    
    try:
        # Create session
        session_service = InMemorySessionService()
        session = await session_service.create_session(
            app_name="nutrichef_app",
            user_id="user_001",
            session_id="session_001"
        )
        
        # Create runner
        runner = Runner(
            agent=root_agent,
            app_name="nutrichef_app",
            session_service=session_service
        )
        
        # Create message
        message = types.Content(
            role="user",
            parts=[types.Part(text=user_message)]
        )
                
        
        # Run agent
        responses = []
        event_count = 0
        
        async for event in runner.run_async(
            user_id="user_001",
            session_id="session_001",
            new_message=message
        ):
            event_count += 1
            
            if hasattr(event, 'content') and event.content:
                if hasattr(event.content, 'parts') and event.content.parts is not None:
                    
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text and part.text is not None:
                            responses.append(part.text.strip())
                                
                            # Show progress indicator
                            if len(responses) == 1:
                                print("📝 Generating meal plan...")
                            elif len(responses) == 2:
                                print("📝 Checking constraints...")
                            elif len(responses) == 3:
                                print("📝 Optimizing shopping list...")
                            elif len(responses) == 4:
                                print("📝 Compiling final report...")
        
        print("\n" + "=" * 60)
        print(f"✅ Complete! (Processed {event_count} events)")
        print("=" * 60)
        
        if responses:
            print("\n📋 YOUR MEAL PLAN & SHOPPING LIST:")
            print("=" * 60)
            full_response = "\n\n".join(responses)
            print(full_response)
            print("\n" + "=" * 60)
        else:
            print("\n⚠️  No response generated")
            print("The agents may need more configuration.")
        
    except Exception as e:
        error_msg = str(e)
        
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print("\n⏰ API Rate Limit Reached")
            print("=" * 60)
            print("The free tier API quota has been exceeded.")
            print("\nThis is normal - you're making multiple AI requests.")
            print("\n✅ Solutions:")
            print("   1. Wait 60-120 seconds for quota to reset")
            print("   2. Try the simple test: python simple_agent_test.py")
            print("   3. Check usage: https://ai.dev/usage")
            print("\n💡 The quota resets every minute automatically.")
            print("=" * 60)
        else:
            print(f"\n❌ Error: {type(e).__name__}")
            print(f"Details: {error_msg[:200]}")
            print("\n💡 Try: python simple_agent_test.py")

    finally:
        # Add this to allow the underlying HTTP client to close gracefully
        await asyncio.sleep(0.250)
        
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
