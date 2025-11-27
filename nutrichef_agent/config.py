import os
from dataclasses import dataclass
from dotenv import load_dotenv
import google.auth

# Load environment variables from .env file
load_dotenv()

# Try to get default Google Cloud credentials
try:
    _, project_id = google.auth.default()
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
except Exception:
    # If no default credentials, that's okay if using AI Studio
    pass

# Set default values
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "us-central1")

# Check configuration
use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE").upper() == "TRUE"

if not use_vertex and not os.getenv("GOOGLE_API_KEY"):
    raise ValueError(
        "\n❌ Configuration Error!\n"
        "GOOGLE_API_KEY must be set in .env file when not using Vertex AI.\n"
        "Please create a .env file with:\n"
        "  GOOGLE_GENAI_USE_VERTEXAI=FALSE\n"
        "  GOOGLE_API_KEY=your_api_key_here\n"
    )


@dataclass
class ResearchConfiguration:
    """Configuration for research-related models and parameters.

    Attributes:
        critic_model (str): Model for evaluation tasks.
        worker_model (str): Model for working/generation tasks.
        max_search_iterations (int): Maximum search iterations allowed.
    """

    # Use stable models instead of experimental ones to avoid quota issues
    critic_model: str = "gemini-2.5-flash"  # Changed from gemini-2.0-flash-exp
    worker_model: str = "gemini-2.5-flash"  # Changed from gemini-2.0-flash-exp
    max_search_iterations: int = 5


config = ResearchConfiguration()

# Print configuration status (only in debug mode)
if os.getenv("DEBUG", "").upper() == "TRUE":
    print(f"✅ Configuration loaded:")
    print(f"   - Using Vertex AI: {use_vertex}")
    print(f"   - Critic Model: {config.critic_model}")
    print(f"   - Worker Model: {config.worker_model}")