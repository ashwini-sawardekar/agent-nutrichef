"""
Helper script to create a properly formatted .env file
Run: python create_env.py
"""
import os

def create_env_file():
    """Create .env file with proper UTF-8 encoding"""
    
    print("=" * 60)
    print("🔧 NutriChef Agent - Environment Setup")
    print("=" * 60)
    print("\nThis script will help you create a .env file.")
    print("\nYou need a Google AI Studio API key.")
    print("Get one here: https://aistudio.google.com/app/apikey")
    print("-" * 60)
    
    # Get API key from user
    api_key = input("\nEnter your Google API Key: ").strip()
    
    if not api_key:
        print("\n❌ Error: API key cannot be empty!")
        return
    
    # Confirm
    print(f"\n✓ API Key: {api_key[:10]}...{api_key[-4:]}")
    confirm = input("\nIs this correct? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("\n❌ Cancelled. Please run the script again.")
        return
    
    # Create .env content
    env_content = f"""# NutriChef Agent Configuration
# Created by create_env.py

# Use AI Studio (set to TRUE for Vertex AI)
GOOGLE_GENAI_USE_VERTEXAI=FALSE

# Your Google AI Studio API Key
GOOGLE_API_KEY={api_key}

# Optional: Enable debug mode
# DEBUG=FALSE
"""
    
    # Write file with UTF-8 encoding
    env_path = os.path.join(os.getcwd(), '.env')
    
    try:
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(env_content)
        
        print("\n" + "=" * 60)
        print("✅ Success! .env file created")
        print("=" * 60)
        print(f"\nLocation: {env_path}")
        print("\nYou can now run:")
        print("  python test.py")
        print("  python cli.py")
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error creating .env file: {e}")
        print("\nManual steps:")
        print("1. Open Notepad")
        print("2. Copy and paste this content:")
        print("-" * 60)
        print(env_content)
        print("-" * 60)
        print("3. Save As → '.env' (with quotes)")
        print("4. Encoding → UTF-8")
        print(f"5. Save in: {os.getcwd()}")


if __name__ == "__main__":
    try:
        create_env_file()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")