"""
Main script for NutriChef Agent - Synchronous version
Run from the Projects directory: python main.py
"""
from nutrichef_agent import root_agent
from google.adk.sessions import InMemorySession
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

def main():
    """Main function to run NutriChef agent"""
    
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
    
    try:
        # Create a session
        session = InMemorySession()
        
        # Run the agent with the session
        result = root_agent.run(
            query=user_input,
            session=session
        )
        
        print("\n✅ Meal Plan Generated!")
        print("=" * 60)
        
        # Extract the final output
        if hasattr(result, 'output'):
            print(result.output)
        elif hasattr(result, 'content'):
            print(result.content)
        else:
            print(result)
            
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"Details: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()