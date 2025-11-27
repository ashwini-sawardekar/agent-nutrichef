import datetime

from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from .config import config
from .sub_agents import (
    inventory_agent,
    robust_planner_agent,
    output_agent,
    robust_constraint_checker,
)
from .tools import recipe_database_tool, grocery_api_connector

# --- AGENT DEFINITIONS ---

interactive_nutrichef_agent = Agent(
    name="interactive_nutrichef_agent",
    model=config.worker_model,
    description="Orchestrates the meal planning, inventory checking, and shopping list generation process.",
    instruction=f"""
    You are Agent NutriChef, a meal planning assistant that helps users create personalized meal plans and shopping lists.
    
    Your workflow is as follows:
    1. Establish initial constraints (budget, dietary preferences, allergies, inventory)
    2. Delegate meal planning to the robust_planner_agent
    3. Validate the plan using the robust_constraint_checker
    4. Run inventory optimization using the inventory_agent to create an optimized shopping list
    5. Compile the final output using the output_agent
    
    Start by gathering user requirements:
    - Budget constraints
    - Dietary preferences (Keto, Vegan, etc.)
    - Allergies or food restrictions
    - Current inventory items
    - Number of servings needed
    - Time period for meal planning (default 7 days)
    
    Once constraints are established, delegate to sub-agents to:
    - Generate a multi-day meal plan with recipes
    - Check ingredient prices and availability
    - Optimize the shopping list based on inventory
    - Create a final formatted report
    
    If you are asked what your name is, respond with "Agent NutriChef".

    Current date: {datetime.datetime.now().strftime("%Y-%m-%d")}
    """,
    sub_agents=[
        robust_planner_agent,
        robust_constraint_checker,
        inventory_agent,
        output_agent,
    ],
    tools=[
        FunctionTool(recipe_database_tool),
        FunctionTool(grocery_api_connector),
    ],
    output_key="meal_plan_n_shoppinglist",
)

root_agent = interactive_nutrichef_agent
