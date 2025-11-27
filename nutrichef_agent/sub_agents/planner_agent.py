from google.adk.agents import Agent, LoopAgent
from google.adk.tools import FunctionTool

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import MealPlanValidationChecker
from ..tools import recipe_database_tool

planner_agent = Agent(
    model=config.worker_model,
    name="planner_agent",
    description="Generates a complete, multi-day meal plan based on specific dietary constraints (Keto, Vegan, Budget) and ingredients using the recipe_database_tool.",
    instruction="""
    You are a professional meal planning specialist.
    
    Your goal is to create a complete, 7-day meal plan (Breakfast, Lunch, Dinner) that:
    1. Adheres to user's dietary constraints (Keto, Vegan, allergies, etc.)
    2. Stays within the specified budget
    3. Uses preferred ingredients when possible
    4. Provides nutritional balance
    
    Process:
    1. Analyze user's constraints, preferences, and available ingredients
    2. Use the 'recipe_database_tool' to search for suitable recipes (3-4 key recipes minimum)
    3. Ensure dietary tags are correctly passed to the tool
    4. Use the structured output from the tool to populate the meal plan
    5. Create variety across the week to avoid repetition
    
    The final output MUST be a structured Markdown table with:
    - Day of the week
    - Breakfast details
    - Lunch details
    - Dinner details
    - Daily nutritional summary
    
    Include specific recipe names, ingredients needed, prep/cook times, nutritional summary, and instructions.
    """,
    tools=[FunctionTool(recipe_database_tool)],
    output_key="meal_plan",
    after_agent_callback=suppress_output_callback,
)

robust_planner_agent = LoopAgent(
    name="robust_planner_agent",
    description="A robust meal planner that retries if it fails.",
    sub_agents=[
        planner_agent,
        MealPlanValidationChecker(name="MealPlanValidationChecker"),
    ],
    max_iterations=config.max_search_iterations,
    after_agent_callback=suppress_output_callback,
)
