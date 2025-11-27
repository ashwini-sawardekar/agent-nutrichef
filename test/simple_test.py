"""
Simple synchronous test for NutriChef Agent
Run from Projects directory: python simple_test.py
"""
from nutrichef_agent import root_agent
from google.adk.sessions import InMemorySession
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

def main():
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
    print("    (This may take a minute...)\n")
    
    try:
        # Create a session for the agent
        session = InMemorySession()
        
        # Run the agent synchronously
        events = list(root_agent.run(
            query=user_input,
            session=session
        ))
        
        print("=" * 60)
        print("✅ Agent Completed!")
        print("=" * 60)
        
        # Process and display events
        for i, event in enumerate(events, 1):
            print(f"\n--- Event {i} ---")
            
            # Try different ways to extract content
            if hasattr(event, 'content') and event.content:
                print(event.content)
            elif hasattr(event, 'text') and event.text:
                print(event.text)
            elif hasattr(event, 'output') and event.output:
                print(event.output)
            else:
                print(f"Event type: {type(event)}")
                print(f"Event: {event}")
        
        # Try to get final output from session state
        print("\n" + "=" * 60)
        print("📋 Final Output:")
        print("=" * 60)
        
        if hasattr(session, 'state') and session.state:
            if 'meal_plan_n_shoppinglist' in session.state:
                print(session.state['meal_plan_n_shoppinglist'])
            else:
                print("Available state keys:", list(session.state.keys()))
                for key, value in session.state.items():
                    print(f"\n{key}:")
                    print(value)
        
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"Details: {str(e)}")
        import traceback
        traceback.print_exc()
        
        print("\n💡 Troubleshooting tips:")
        print("  1. Check your API key is valid")
        print("  2. Check you have internet connection")
        print("  3. Try running: pip install --upgrade google-adk google-generativeai")

if __name__ == "__main__":
    main()