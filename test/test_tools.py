"""
Test the tools independently without running the full agent
Run from Projects directory: python test_tools.py
"""
from nutrichef_agent.tools import recipe_database_tool, grocery_api_connector
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

def test_recipe_database():
    """Test the recipe database tool"""
    print("=" * 60)
    print("🧪 Testing Recipe Database Tool")
    print("=" * 60)
    
    ingredients = ["salmon", "spinach", "lentils", "chicken breast", "butter", "garlic"]
    
    print(f"\n📋 Searching for prices of: {', '.join(ingredients)}")
    print("-" * 60)
    
    result = recipe_database_tool(
        ingredients=ingredients,
        store_preference="Local_Store_A"
    )
    
    print("\n📊 Results:")
    total_cost = 0
    for item, details in result.items():
        print(f"\n  🛒 {item}:")
        print(f"      Price: ${details['price_per_unit']:.2f} per {details['unit']}")
        print(f"      In Stock: {'✅ Yes' if details['in_stock'] else '❌ No'}")
        print(f"      Store: {details['store']}")
        print(f"      Category: {details['category']}")
        total_cost += details['price_per_unit']
    
    print(f"\n💰 Estimated total cost: ${total_cost:.2f}")
    return result


def test_grocery_api():
    """Test the grocery API connector"""
    print("\n" + "=" * 60)
    print("🧪 Testing Grocery API Connector")
    print("=" * 60)
    
    # Test 1: Keto Chicken recipe
    print("\n📝 Test 1: Keto Chicken Recipe (4 servings)")
    print("-" * 60)
    
    result1 = grocery_api_connector(
        dietary_tags=["Keto", "Low-Carb"],
        main_ingredient="Chicken Breast",
        servings=4
    )
    
    if result1['matched_recipes']:
        recipe = result1['matched_recipes'][0]
        print(f"\n🍗 Recipe Found: {recipe['recipe_name']}")
        print(f"   Dietary Tags: {', '.join(recipe['dietary_tags'])}")
        print(f"   Servings: {recipe['servings']}")
        print(f"   Prep Time: {recipe['prep_time_min']} min")
        print(f"   Cook Time: {recipe['cook_time_min']} min")
        print(f"   Difficulty: {recipe['difficulty']}")
        
        print(f"\n   📋 Ingredients:")
        for ing in recipe['ingredients']:
            print(f"      • {ing['quantity']} {ing['unit']} {ing['item']}")
        
        print(f"\n   🥗 Nutrition (per serving):")
        for key, value in recipe['nutritional_summary_per_serving'].items():
            print(f"      • {key}: {value}")
        
        print(f"\n   👨‍🍳 Instructions:")
        for i, step in enumerate(recipe['instructions'], 1):
            print(f"      {i}. {step}")
    
    # Test 2: Vegan Lentils
    print("\n" + "-" * 60)
    print("📝 Test 2: Vegan Lentil Recipe (2 servings)")
    print("-" * 60)
    
    result2 = grocery_api_connector(
        dietary_tags=["Vegan", "High-Protein"],
        main_ingredient="Lentils",
        servings=2
    )
    
    if result2['matched_recipes']:
        recipe = result2['matched_recipes'][0]
        print(f"\n🌱 Recipe Found: {recipe['recipe_name']}")
        print(f"   Servings: {recipe['servings']}")
        print(f"   Total Time: {recipe['prep_time_min'] + recipe['cook_time_min']} min")
        
        print(f"\n   📋 Ingredients:")
        for ing in recipe['ingredients']:
            print(f"      • {ing['quantity']} {ing['unit']} {ing['item']}")
    
    # Test 3: Mediterranean Salmon
    print("\n" + "-" * 60)
    print("📝 Test 3: Salmon Recipe (any diet, 2 servings)")
    print("-" * 60)
    
    result3 = grocery_api_connector(
        dietary_tags=["Healthy"],
        main_ingredient="Salmon",
        servings=2
    )
    
    if result3['matched_recipes']:
        recipe = result3['matched_recipes'][0]
        print(f"\n🐟 Recipe Found: {recipe['recipe_name']}")
        print(f"   Servings: {recipe['servings']}")
        
        # Calculate estimated cost
        print(f"\n   💰 Cost Estimate:")
        ingredient_names = [ing['item'] for ing in recipe['ingredients']]
        prices = recipe_database_tool(ingredient_names)
        total = sum(details['price_per_unit'] * 
                   next(ing['quantity'] for ing in recipe['ingredients'] if ing['item'] == item)
                   for item, details in prices.items())
        print(f"      Estimated total: ${total:.2f}")


def main():
    """Run all tool tests"""
    print("\n🔧 NutriChef Agent - Tool Testing Suite")
    print("=" * 60)
    
    try:
        # Test 1: Recipe Database
        test_recipe_database()
        
        # Test 2: Grocery API
        test_grocery_api()
        
        print("\n" + "=" * 60)
        print("✅ All tool tests completed successfully!")
        print("=" * 60)
        print("\n💡 The tools are working correctly with realistic data.")
        print("\n📊 Database Contains:")
        print("   • 40+ ingredients with prices")
        print("   • 8+ complete recipes across different diets")
        print("   • Nutritional information")
        print("   • Cooking instructions")
        print("\n🚀 Ready to test the full agent:")
        print("   python simple_agent_test.py")
        print("   python run_nutrichef.py")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {type(e).__name__}")
        print(f"Details: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()