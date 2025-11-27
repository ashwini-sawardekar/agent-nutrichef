"""
Simple agent test - Makes minimal API calls
Run from Projects directory: python simple_agent_test.py
"""
import asyncio
from pathlib import Path
from dotenv import load_dotenv
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

# Load environment
load_dotenv(Path('.') / '.env', encoding='utf-8')

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Create a simple single agent (no sub-agents = fewer API calls)
simple_agent = Agent(
    name="simple_nutrichef",
    model="gemini-flash-latest",    #"gemini-1.5-flash",  # Stable model with better quota
    description="Simple meal planning assistant",
    instruction="""
    You are a helpful meal planning assistant.
    
    When users ask for meal plans:
    1. Acknowledge their requirements (budget, diet, allergies, servings)
    2. Suggest 2-3 meal ideas that fit their criteria
    3. Keep responses concise and practical
    
    Focus on being helpful and accurate.
    """
)

async def main():
    """Test with a simple single agent"""
    
    print("🍳 Simple NutriChef Test")
    print("=" * 60)
    print("This version makes minimal API calls for testing\n")
    
    user_query = """
    I need meal ideas for:
    - Budget: $100
    - Diet: Keto
    - Servings: 2 people
    
    Can you suggest 2-3 dinner ideas?
    """
    
    try:
        # Create session
        session_service = InMemorySessionService()
        session = await session_service.create_session(
            app_name="simple_test",
            user_id="user_001",
            session_id="test_session"
        )
        
        # Create runner
        runner = Runner(
            agent=simple_agent,
            app_name="simple_test",
            session_service=session_service
        )
        
        # Create message
        message = types.Content(
            role="user",
            parts=[types.Part(text=user_query)]
        )
        
        print("🤖 Sending request to AI...\n")
        
        # Run and collect responses
        responses = []
        async for event in runner.run_async(
            user_id="user_001",
            session_id="test_session",
            new_message=message
        ):
            if hasattr(event, 'content') and event.content:
                if hasattr(event.content, 'parts'):
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            responses.append(part.text)
                            print(part.text)
        
        print("\n" + "=" * 60)
        print("✅ Test completed successfully!")
        print("=" * 60)
        
        if not responses:
            print("\n⚠️  No response received")
            
        # Clean up
        session_service = await session_service.delete_session(app_name=session.app_name,
                             user_id=session.user_id, session_id=session.id)
        print("The final status of session_service - ", session_service)

        
    except Exception as e:
        error_msg = str(e)
        
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print("\n⏰ Rate Limit Hit!")
            print("=" * 60)
            print("You've exceeded the API quota. This is normal during testing.")
            print("\nSolutions:")
            print("  1. Wait 60 seconds and try again")
            print("  2. Check usage: https://ai.dev/usage")
            print("  3. The quota resets every minute")
        else:
            print(f"\n❌ Error: {type(e).__name__}")
            print(f"Details: {error_msg}")
            
            import traceback
            traceback.print_exc()
    #finally:
     
if __name__ == "__main__":
    asyncio.run(main())