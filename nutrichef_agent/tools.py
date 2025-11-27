from typing import List, Dict
import random


# ==================== INGREDIENT PRICE DATABASE ====================

INGREDIENT_DATABASE = {
    # Proteins
    "chicken breast": {"price": 3.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    "chicken thighs": {"price": 2.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    "ground beef": {"price": 4.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    "salmon": {"price": 8.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    "cod": {"price": 6.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    "pork chops": {"price": 4.49, "unit": "lb", "in_stock": True, "category": "Protein"},
    "bacon": {"price": 5.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    "eggs": {"price": 3.49, "unit": "dozen", "in_stock": True, "category": "Protein"},
    "tofu": {"price": 2.99, "unit": "lb", "in_stock": True, "category": "Protein"},
    
    # Vegetables
    "spinach": {"price": 2.99, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "broccoli": {"price": 1.99, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "cauliflower": {"price": 2.49, "unit": "head", "in_stock": True, "category": "Vegetables"},
    "zucchini": {"price": 1.49, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "asparagus": {"price": 3.99, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "bell peppers": {"price": 1.99, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "mushrooms": {"price": 2.99, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "brussels sprouts": {"price": 2.49, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "kale": {"price": 2.99, "unit": "bunch", "in_stock": True, "category": "Vegetables"},
    "lettuce": {"price": 1.99, "unit": "head", "in_stock": True, "category": "Vegetables"},
    "tomatoes": {"price": 2.49, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "carrots": {"price": 1.49, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "onions": {"price": 1.29, "unit": "lb", "in_stock": True, "category": "Vegetables"},
    "garlic": {"price": 0.99, "unit": "bulb", "in_stock": True, "category": "Vegetables"},
    
    # Dairy & Alternatives
    "butter": {"price": 4.99, "unit": "lb", "in_stock": True, "category": "Dairy"},
    "heavy cream": {"price": 3.99, "unit": "pint", "in_stock": True, "category": "Dairy"},
    "cheese": {"price": 5.99, "unit": "lb", "in_stock": True, "category": "Dairy"},
    "cream cheese": {"price": 2.99, "unit": "8oz", "in_stock": True, "category": "Dairy"},
    "almond milk": {"price": 3.49, "unit": "half gallon", "in_stock": True, "category": "Dairy"},
    "coconut milk": {"price": 2.99, "unit": "can", "in_stock": True, "category": "Dairy"},
    
    # Grains & Legumes
    "lentils": {"price": 1.99, "unit": "lb", "in_stock": True, "category": "Grains"},
    "quinoa": {"price": 3.99, "unit": "lb", "in_stock": True, "category": "Grains"},
    "rice": {"price": 2.49, "unit": "lb", "in_stock": True, "category": "Grains"},
    "chickpeas": {"price": 1.49, "unit": "can", "in_stock": True, "category": "Grains"},
    "black beans": {"price": 1.29, "unit": "can", "in_stock": True, "category": "Grains"},
    
    # Pantry Staples
    "olive oil": {"price": 8.99, "unit": "bottle", "in_stock": True, "category": "Pantry"},
    "coconut oil": {"price": 7.99, "unit": "jar", "in_stock": True, "category": "Pantry"},
    "soy sauce": {"price": 2.99, "unit": "bottle", "in_stock": True, "category": "Pantry"},
    "balsamic vinegar": {"price": 4.99, "unit": "bottle", "in_stock": True, "category": "Pantry"},
    "salt": {"price": 1.99, "unit": "container", "in_stock": True, "category": "Pantry"},
    "pepper": {"price": 3.99, "unit": "container", "in_stock": True, "category": "Pantry"},
    
    # Nuts & Seeds
    "almonds": {"price": 6.99, "unit": "lb", "in_stock": True, "category": "Nuts"},
    "walnuts": {"price": 7.99, "unit": "lb", "in_stock": True, "category": "Nuts"},
    "peanuts": {"price": 4.99, "unit": "lb", "in_stock": False, "category": "Nuts"},  # Out of stock
    "chia seeds": {"price": 5.99, "unit": "lb", "in_stock": True, "category": "Seeds"},
}


# ==================== RECIPE DATABASE ====================

RECIPE_DATABASE = {
    "keto": [
        {
            "recipe_name": "Keto Lemon Butter Chicken with Asparagus",
            "source": "DB_ID_789",
            "dietary_tags": ["Keto", "Low-Carb", "Gluten-Free"],
            "servings": 4,
            "prep_time_min": 15,
            "cook_time_min": 25,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "chicken breast", "quantity": 1.5, "unit": "lb"},
                {"item": "asparagus", "quantity": 1, "unit": "bunch"},
                {"item": "butter", "quantity": 0.25, "unit": "lb"},
                {"item": "lemon", "quantity": 1, "unit": "whole"},
                {"item": "garlic", "quantity": 2, "unit": "bulb"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 450,
                "protein_g": 55,
                "fat_g": 25,
                "net_carbs_g": 5,
                "fiber_g": 3,
            },
            "instructions": [
                "Season chicken with salt and pepper",
                "Melt butter in pan over medium-high heat",
                "Cook chicken 6-7 minutes per side",
                "Add asparagus and garlic to pan",
                "Squeeze lemon over everything and serve"
            ]
        },
        {
            "recipe_name": "Creamy Keto Salmon with Spinach",
            "source": "DB_ID_790",
            "dietary_tags": ["Keto", "Low-Carb", "High-Protein"],
            "servings": 2,
            "prep_time_min": 10,
            "cook_time_min": 20,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "salmon", "quantity": 0.75, "unit": "lb"},
                {"item": "spinach", "quantity": 0.5, "unit": "lb"},
                {"item": "heavy cream", "quantity": 1, "unit": "cup"},
                {"item": "butter", "quantity": 2, "unit": "tbsp"},
                {"item": "garlic", "quantity": 1, "unit": "bulb"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 520,
                "protein_g": 42,
                "fat_g": 38,
                "net_carbs_g": 4,
                "fiber_g": 2,
            },
            "instructions": [
                "Season salmon with salt and pepper",
                "Pan-sear salmon 4 minutes per side",
                "Remove and set aside",
                "Sauté garlic and spinach in butter",
                "Add cream and simmer 3 minutes",
                "Serve salmon over creamy spinach"
            ]
        },
        {
            "recipe_name": "Keto Cauliflower Fried Rice",
            "source": "DB_ID_791",
            "dietary_tags": ["Keto", "Low-Carb", "Vegetarian"],
            "servings": 4,
            "prep_time_min": 15,
            "cook_time_min": 15,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "cauliflower", "quantity": 1, "unit": "head"},
                {"item": "eggs", "quantity": 4, "unit": "whole"},
                {"item": "bell peppers", "quantity": 0.5, "unit": "lb"},
                {"item": "onions", "quantity": 0.25, "unit": "lb"},
                {"item": "soy sauce", "quantity": 3, "unit": "tbsp"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 180,
                "protein_g": 10,
                "fat_g": 8,
                "net_carbs_g": 8,
                "fiber_g": 4,
            },
            "instructions": [
                "Rice cauliflower in food processor",
                "Scramble eggs and set aside",
                "Stir-fry vegetables until tender",
                "Add cauliflower rice and soy sauce",
                "Mix in eggs and serve hot"
            ]
        },
    ],
    "vegan": [
        {
            "recipe_name": "Vegan Lentil Curry",
            "source": "DB_ID_101",
            "dietary_tags": ["Vegan", "High-Protein", "Gluten-Free"],
            "servings": 4,
            "prep_time_min": 10,
            "cook_time_min": 30,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "lentils", "quantity": 1, "unit": "lb"},
                {"item": "coconut milk", "quantity": 1, "unit": "can"},
                {"item": "tomatoes", "quantity": 0.5, "unit": "lb"},
                {"item": "spinach", "quantity": 0.5, "unit": "lb"},
                {"item": "onions", "quantity": 0.25, "unit": "lb"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 320,
                "protein_g": 18,
                "fat_g": 12,
                "net_carbs_g": 35,
                "fiber_g": 15,
            },
            "instructions": [
                "Cook lentils according to package",
                "Sauté onions until golden",
                "Add tomatoes and spices",
                "Stir in coconut milk and lentils",
                "Add spinach and simmer 5 minutes"
            ]
        },
        {
            "recipe_name": "Vegan Buddha Bowl",
            "source": "DB_ID_102",
            "dietary_tags": ["Vegan", "High-Fiber", "Nutrient-Dense"],
            "servings": 2,
            "prep_time_min": 15,
            "cook_time_min": 25,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "quinoa", "quantity": 0.5, "unit": "lb"},
                {"item": "chickpeas", "quantity": 1, "unit": "can"},
                {"item": "broccoli", "quantity": 0.5, "unit": "lb"},
                {"item": "carrots", "quantity": 0.25, "unit": "lb"},
                {"item": "tahini", "quantity": 3, "unit": "tbsp"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 450,
                "protein_g": 20,
                "fat_g": 15,
                "net_carbs_g": 55,
                "fiber_g": 12,
            },
            "instructions": [
                "Cook quinoa according to package",
                "Roast chickpeas with spices at 400°F for 20 min",
                "Steam broccoli and carrots",
                "Assemble bowl with all ingredients",
                "Drizzle with tahini dressing"
            ]
        },
    ],
    "mediterranean": [
        {
            "recipe_name": "Mediterranean Baked Cod",
            "source": "DB_ID_201",
            "dietary_tags": ["Mediterranean", "Heart-Healthy", "Low-Carb"],
            "servings": 4,
            "prep_time_min": 10,
            "cook_time_min": 20,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "cod", "quantity": 1.5, "unit": "lb"},
                {"item": "tomatoes", "quantity": 0.5, "unit": "lb"},
                {"item": "olive oil", "quantity": 3, "unit": "tbsp"},
                {"item": "garlic", "quantity": 1, "unit": "bulb"},
                {"item": "lemon", "quantity": 1, "unit": "whole"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 280,
                "protein_g": 35,
                "fat_g": 12,
                "net_carbs_g": 6,
                "fiber_g": 2,
            },
            "instructions": [
                "Preheat oven to 400°F",
                "Place cod in baking dish",
                "Top with tomatoes, garlic, and olive oil",
                "Bake for 20 minutes",
                "Squeeze lemon juice before serving"
            ]
        },
    ],
    "general": [
        {
            "recipe_name": "Healthy Stir-Fry",
            "source": "DB_ID_301",
            "dietary_tags": ["Balanced", "Quick", "Customizable"],
            "servings": 4,
            "prep_time_min": 15,
            "cook_time_min": 15,
            "difficulty": "Easy",
            "ingredients": [
                {"item": "chicken breast", "quantity": 1, "unit": "lb"},
                {"item": "broccoli", "quantity": 0.5, "unit": "lb"},
                {"item": "bell peppers", "quantity": 0.5, "unit": "lb"},
                {"item": "carrots", "quantity": 0.25, "unit": "lb"},
                {"item": "soy sauce", "quantity": 3, "unit": "tbsp"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 280,
                "protein_g": 30,
                "fat_g": 8,
                "net_carbs_g": 18,
                "fiber_g": 4,
            },
            "instructions": [
                "Cut chicken into bite-sized pieces",
                "Heat oil in wok or large pan",
                "Stir-fry chicken until cooked through",
                "Add vegetables and cook until tender-crisp",
                "Toss with soy sauce and serve"
            ]
        },
    ]
}


# ==================== TOOL FUNCTIONS ====================

def recipe_database_tool(ingredients: List[str], store_preference: str = "Local_Store_A") -> Dict[str, Dict]:
    """
    Looks up the current price and stock status for a list of ingredients.
    
    This tool simulates checking a grocery store's inventory system to find
    prices and availability of ingredients needed for meal planning.
        
    Args:
        ingredients: A list of ingredient names (e.g., ["salmon", "spinach", "butter"])
        store_preference: The user's preferred store (default: "Local_Store_A")
            
    Returns:
        A dictionary mapping each ingredient to its price, stock status, and store info.
        Format: {
            "ingredient_name": {
                "price_per_unit": float,
                "unit": str,
                "in_stock": bool,
                "store": str,
                "category": str
            }
        }
        
    Example:
        >>> recipe_database_tool(["salmon", "spinach"])
        {
            "salmon": {
                "price_per_unit": 8.99,
                "unit": "lb",
                "in_stock": True,
                "store": "Local_Store_A",
                "category": "Protein"
            },
            "spinach": {
                "price_per_unit": 2.99,
                "unit": "lb",
                "in_stock": True,
                "store": "Local_Store_A",
                "category": "Vegetables"
            }
        }
    """
    results = {}
    
    for item in ingredients:
        item_lower = item.lower().strip()
        
        # Try exact match first
        if item_lower in INGREDIENT_DATABASE:
            db_entry = INGREDIENT_DATABASE[item_lower]
            results[item] = {
                "price_per_unit": db_entry["price"],
                "unit": db_entry["unit"],
                "in_stock": db_entry["in_stock"],
                "store": store_preference,
                "category": db_entry["category"]
            }
        else:
            # Try partial match
            found = False
            for db_item, db_entry in INGREDIENT_DATABASE.items():
                if item_lower in db_item or db_item in item_lower:
                    results[item] = {
                        "price_per_unit": db_entry["price"],
                        "unit": db_entry["unit"],
                        "in_stock": db_entry["in_stock"],
                        "store": store_preference,
                        "category": db_entry["category"]
                    }
                    found = True
                    break
            
            # If not found, use default values
            if not found:
                results[item] = {
                    "price_per_unit": 3.99,
                    "unit": "item",
                    "in_stock": True,
                    "store": store_preference,
                    "category": "Other"
                }
    
    print(f"✓ Recipe Database Tool: Checked prices for {len(ingredients)} items at {store_preference}")
    return results


def grocery_api_connector(dietary_tags: List[str], 
                          main_ingredient: str, 
                          servings: int = 4) -> Dict:
    """
    Fetches detailed recipe data from the recipe database based on dietary preferences
    and main ingredients. This simulates an API call to a recipe service.
    
    This tool searches through a curated database of recipes and returns structured
    recipe information including ingredients, nutrition facts, and cooking instructions.
        
    Args:
        dietary_tags: List of dietary requirements/preferences 
                     (e.g., ['Keto', 'Dairy-Free'], ['Vegan', 'High-Protein'])
        main_ingredient: Primary protein or ingredient for the dish
                        (e.g., 'Chicken Breast', 'Salmon', 'Tofu')
        servings: Number of servings needed (default: 4)
            
    Returns:
        A structured dictionary containing matching recipes with full details:
        {
            "matched_recipes": [
                {
                    "recipe_name": str,
                    "source": str,
                    "dietary_tags": List[str],
                    "servings": int,
                    "prep_time_min": int,
                    "cook_time_min": int,
                    "difficulty": str,
                    "ingredients": List[Dict],
                    "nutritional_summary_per_serving": Dict,
                    "instructions": List[str]
                }
            ]
        }
        
    Example:
        >>> grocery_api_connector(["Keto", "Low-Carb"], "Chicken Breast", 4)
        {
            "matched_recipes": [{
                "recipe_name": "Keto Lemon Butter Chicken with Asparagus",
                "servings": 4,
                "prep_time_min": 15,
                "cook_time_min": 25,
                ...
            }]
        }
    """
    tag_str = ", ".join(dietary_tags).lower()
    main_ingredient_lower = main_ingredient.lower()
    
    matched_recipes = []
    
    # Search for recipes matching dietary tags
    for diet_type, recipes in RECIPE_DATABASE.items():
        if diet_type in tag_str or any(tag.lower() in diet_type for tag in dietary_tags):
            for recipe in recipes:
                # Check if main ingredient is in the recipe
                ingredient_match = any(
                    main_ingredient_lower in ing["item"].lower() 
                    for ing in recipe["ingredients"]
                )
                
                if ingredient_match:
                    # Scale recipe to requested servings
                    scaled_recipe = recipe.copy()
                    scale_factor = servings / recipe["servings"]
                    
                    scaled_recipe["servings"] = servings
                    scaled_recipe["ingredients"] = [
                        {
                            "item": ing["item"],
                            "quantity": round(ing["quantity"] * scale_factor, 2),
                            "unit": ing["unit"]
                        }
                        for ing in recipe["ingredients"]
                    ]
                    
                    matched_recipes.append(scaled_recipe)
    
    # If no exact match found, find recipes by main ingredient
    if not matched_recipes:
        for diet_type, recipes in RECIPE_DATABASE.items():
            for recipe in recipes:
                ingredient_match = any(
                    main_ingredient_lower in ing["item"].lower() 
                    for ing in recipe["ingredients"]
                )
                
                if ingredient_match:
                    scaled_recipe = recipe.copy()
                    scale_factor = servings / recipe["servings"]
                    
                    scaled_recipe["servings"] = servings
                    scaled_recipe["ingredients"] = [
                        {
                            "item": ing["item"],
                            "quantity": round(ing["quantity"] * scale_factor, 2),
                            "unit": ing["unit"]
                        }
                        for ing in recipe["ingredients"]
                    ]
                    
                    matched_recipes.append(scaled_recipe)
                    break
    
    # If still no match, return a generic recipe
    if not matched_recipes:
        matched_recipes = [{
            "recipe_name": f"Healthy {main_ingredient} Dish",
            "source": "DB_ID_DEFAULT",
            "dietary_tags": dietary_tags,
            "servings": servings,
            "prep_time_min": 15,
            "cook_time_min": 20,
            "difficulty": "Easy",
            "ingredients": [
                {"item": main_ingredient.lower(), "quantity": 1.5, "unit": "lb"},
                {"item": "olive oil", "quantity": 2, "unit": "tbsp"},
                {"item": "garlic", "quantity": 1, "unit": "bulb"},
                {"item": "spinach", "quantity": 0.5, "unit": "lb"},
            ],
            "nutritional_summary_per_serving": {
                "calories": 350,
                "protein_g": 35,
                "fat_g": 15,
                "net_carbs_g": 20,
                "fiber_g": 5,
            },
            "instructions": [
                f"Prepare {main_ingredient} as desired",
                "Heat olive oil in pan",
                "Add garlic and cook until fragrant",
                "Add main ingredient and cook through",
                "Serve with sautéed spinach"
            ]
        }]
    
    print(f"✓ Grocery API Connector: Found {len(matched_recipes)} recipe(s) for {main_ingredient} with tags: {tag_str}")
    
    return {"matched_recipes": matched_recipes}