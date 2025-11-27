"""
Minimal test to understand Google ADK API
Run: python minimal_test.py
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
    print(f"✅ API key loaded\n")
else:
    print("⚠️  Warning: API key not found\n")

from google.adk.agents import Agent
from google.adk.agents.invocation_context import InvocationContext

# Create a very simple agent for testing
test_agent = Agent(
    name="test_agent",
    model="gemini-2.0-flash-exp",
    description="A simple test agent",
    instruction="You are a helpful assistant. Answer questions concisely."
)

async def test_simple():
    """Test with a simple query"""
    print("🧪 Testing Google ADK API...")
    print("=" * 60)
    
    query = "What is 2+2?"
    
    try:
        print(f"Query: {query}\n")
        print("Creating context...")
        
        # Try different ways to create context
        context = InvocationContext(
            query=query,
            agent=test_agent
        )
        
        print("Running agent...\n")
        
        event_count = 0
        async for event in test_agent.run_async(context):
            event_count += 1
            print(f"Event {event_count}: {type(event).__name__}")
            
            # Try to extract content
            if hasattr(event, 'content'):
                print(f"  Content: {event.content}")
            if hasattr(event, 'text'):
                print(f"  Text: {event.text}")
            if hasattr(event, 'message'):
                print(f"  Message: {event.message}")
            
            print()
        
        print(f"✅ Test completed! Received {event_count} events")
        
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Details: {str(e)}")
        
        import traceback
        traceback.print_exc()
        
        print("\n" + "=" * 60)
        print("Let's check what's available:")
        print("=" * 60)
        
        # Inspect the Agent class
        print("\nAgent.run_async signature:")
        import inspect
        sig = inspect.signature(test_agent.run_async)
        print(f"  {sig}")
        
        print("\nInvocationContext fields:")
        if hasattr(InvocationContext, '__annotations__'):
            for field, ftype in InvocationContext.__annotations__.items():
                print(f"  {field}: {ftype}")

async def test_nutrichef():
    """Test NutriChef agent"""
    print("\n" + "=" * 60)
    print("🧪 Testing NutriChef Agent...")
    print("=" * 60)
    
    try:
        from nutrichef_agent import root_agent
        
        query = "Hello, can you help me with meal planning?"
        
        print(f"Query: {query}\n")
        
        context = InvocationContext(
            query=query,
            agent=root_agent
        )
        
        print("Running NutriChef agent...\n")
        
        event_count = 0
        async for event in root_agent.run_async(context):
            event_count += 1
            print(f"Event {event_count}: {type(event).__name__}")
            
            if hasattr(event, 'content') and event.content:
                print(f"  Content: {str(event.content)[:100]}...")
            
        print(f"\n✅ NutriChef test completed! Received {event_count} events")
        
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Details: {str(e)}")
        import traceback
        traceback.print_exc()

async def main():
    """Run all tests"""
    await test_simple()
    await test_nutrichef()

if __name__ == "__main__":
    asyncio.run(main())