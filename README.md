# 👨‍🍳 NutriChef: The Autonomous Meal Planner & Grocery Agent

**Track:** Concierge Agents

**NutriChef** is a sophisticated, autonomous multi-agent system designed to streamline and automate the entire weekly meal planning and grocery shopping process for individuals with specific dietary needs, budgets, and pantry inventories.

## 💡 Problem Statement

Planning healthy, consistent meals is time-consuming and difficult to align with individual needs (dietary restrictions, budget, available ingredients, minimizing waste). Manually searching for recipes, checking multiple store flyers, cross-referencing pantry contents, and compiling a shopping list is a laborious, multi-step process that often leads to unhealthy choices and increased food waste.

## ✨ Solution Statement

NutriChef eliminates this friction by leveraging specialized AI agents. The system autonomously plans a full week's worth of meals, cross-references existing inventory, checks local grocery prices, and generates an optimized, cost-minimized shopping list—all while guaranteeing adherence to user-defined health constraints.

## ⚙️ Architecture

Core to NutriChef is the **Profile Agent**—the central orchestrator that manages user state and delegates tasks. The system utilizes **four specialized sub-agents** in a sequential and parallel flow, ensuring maximum efficiency.

### Multi-Agent Coordination

| Agent | Role | Key Course Concept |
| :--- | :--- | :--- |
| **Profile Agent** | **Orchestrator & Memory Keeper** | **Sessions & Memory** |
| **Planner Agent** | **Menu Creator** | LLM-Powered Agent |
| **Inventory Agent** | **Parallel Optimizer** | **Multi-Agent System** (Parallel Execution) |
| **Output Agent** | **Finalizer** | **Context Engineering** (Compaction) |

### Essential Tools and Utilities

The agents are equipped with the following tools to perform their complex tasks:

1.  **Memory Bank:** Used by the Profile Agent to store and retrieve long-term user constraints (allergies, budget, past successful menus) and current inventory.
2.  **Grocery API Connector (Custom Tool):** Used by the Inventory Agent to simulate real-time price and availability checks, allowing for cost-optimization and ingredient swapping.
3.  **ConstraintChecker (Validation Agent):** Implemented as a simple LoopAgent validation checker to ensure the **Planner Agent** adheres to specific rules (e.g., max carb count for a Keto plan).

## 🚀 Getting Started (Simulated ADK Structure)

### Prerequisites

* Python 3.x
* Google Agent Development Kit (ADK) – *Requires ADK setup and environment configuration.*
* Google Gemini API Key – *For powering the LLM-based Planner Agent.*

### Setup

1.  Clone the repository:
    ```bash
    git clone [https://github.com/ashwini-sawardekar/agent-nutrichef.git](https://github.com/ashwini-sawardekar/agent-nutrichef.git)
    cd NutriChef
    ```
2.  Install dependencies (assuming ADK is available):
    ```bash
    # Replace with actual ADK setup command
    pip install google-genai-adk
    ```
3.  Set your environment variable for the API Key:
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```
4.  Run the main orchestrator script:
    ```bash
    python run_nutrichef.py
    ```

## ⭐ Value Statement

**NutriChef** reduced my weekly meal planning and grocery list creation time by **6-8 hours** per week, enabling me to consistently adhere to a complex dietary regimen (e.g., macro counting) with minimal effort. I have also reduced food waste by **20%** by integrating my kitchen inventory, as the agent drives efficiency and planning that I'd otherwise not be able to do given time constraints and the complexity of cross-referencing hundreds of ingredients.

If I had more time I would add an additional agent to scan various health sites for the latest nutritional studies and use that research to inform my meal plan recommendations. This would require integrating applicable MCP servers or building custom tools.