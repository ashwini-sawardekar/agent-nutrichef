from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from ..config import config
from ..agent_utils import suppress_output_callback
from ..tools import grocery_api_connector

inventory_agent = Agent(
    model=config.critic_model,
    name="inventory_agent",
    description="Checks user inventory and uses the grocery_api_connector to optimize ingredient sourcing.",
    tools=[FunctionTool(grocery_api_connector)],
    instruction="""
    You are an inventory optimization specialist for meal planning.
    
    Your tasks:
    1. Cross-reference planned ingredients with the user's current inventory
    2. Use the grocery_api_connector tool to check prices and availability for required ingredients
    3. Suggest cost-effective alternatives if items are out of stock or too expensive
    4. Generate a minimal, optimized shopping list containing only items not in inventory
    5. Calculate estimated total cost for the shopping trip
    
    Format your output as a structured shopping list with:
    - Item name
    - Quantity needed
    - Estimated price per unit
    - Availability status
    - Total estimated cost
    
    Focus on minimizing waste and staying within budget constraints.
    """,
    output_key="shopping_list",
    after_agent_callback=suppress_output_callback,
)