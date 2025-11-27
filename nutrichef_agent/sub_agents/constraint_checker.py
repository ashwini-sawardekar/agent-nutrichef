from google.adk.agents import Agent, LoopAgent

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import ShoppingListValidationChecker

constraint_checker = Agent(
    model=config.critic_model,
    name="constraint_checker",
    description="Validates a meal plan against key constraints (Budget, Diet, Allergies). Escalates if successful.",
    instruction="""
    You are a validation specialist for meal planning.
    
    Your task is to verify that the generated meal plan adheres to all user constraints:
    
    1. **Budget Validation**: Check if the total estimated cost exceeds the user's budget
    2. **Dietary Compliance**: Ensure all meals match dietary requirements (Keto, Vegan, etc.)
    3. **Allergy Check**: Verify no allergens are present (e.g., peanuts, dairy, gluten)
    4. **Nutritional Balance**: Confirm meals provide adequate nutrition
    5. **Serving Size**: Validate portion sizes match user requirements
    
    Review the provided meal plan and original constraints carefully.
    
    If ANY violations are found:
    - Return a clear error message explaining what constraint was violated
    - Suggest specific corrections
    - Do NOT escalate
    
    If the plan is compliant:
    - Confirm all constraints are met
    - Escalate to proceed to the next stage
    
    Be thorough but concise in your validation report.
    """,
    output_key="validation_result",
    after_agent_callback=suppress_output_callback,
)

robust_constraint_checker = LoopAgent(
    name="robust_constraint_checker",
    description="A robust constraint checker that retries if validation fails.",
    sub_agents=[
        constraint_checker,
        ShoppingListValidationChecker(name="ShoppingListValidationChecker"),
    ],
    max_iterations=config.max_search_iterations,
)
