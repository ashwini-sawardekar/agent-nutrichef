"""
Verify that .env file is loaded correctly
Run: python verify_env.py
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

def main():
    print("=" * 60)
    print("🔍 Environment Variable Verification")
    print("=" * 60)
    
    # Get current directory
    current_dir = Path.cwd()
    print(f"\n📁 Current Directory: {current_dir}")
    
    # Check if .env exists
    env_path = current_dir / '.env'
    print(f"📄 .env Path: {env_path}")
    
    if env_path.exists():
        print("✅ .env file exists")
        
        # Check file size and encoding
        file_size = env_path.stat().st_size
        print(f"   Size: {file_size} bytes")
        
        # Try to read the file
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f"   Lines: {len(lines)}")
                print("\n📝 .env File Contents (masked):")
                print("-" * 60)
                for i, line in enumerate(lines, 1):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            # Mask the value for security
                            if 'KEY' in key or 'SECRET' in key:
                                masked_value = value[:6] + '...' + value[-4:] if len(value) > 10 else '***'
                            else:
                                masked_value = value
                            print(f"   {i}. {key}={masked_value}")
                        else:
                            print(f"   {i}. {line}")
        except Exception as e:
            print(f"⚠️  Could not read .env: {e}")
    else:
        print("❌ .env file NOT FOUND")
        print("\nCreate .env file with:")
        print("  GOOGLE_GENAI_USE_VERTEXAI=FALSE")
        print("  GOOGLE_API_KEY=your_api_key_here")
    
    print("\n" + "-" * 60)
    print("🔧 Loading Environment Variables...")
    print("-" * 60)
    
    # Load the .env file
    loaded = load_dotenv(dotenv_path=env_path, encoding='utf-8', override=True)
    
    if loaded:
        print("✅ .env file loaded successfully")
    else:
        print("⚠️  .env file not loaded (might not exist or be empty)")
    
    print("\n" + "-" * 60)
    print("📊 Environment Variables Status:")
    print("-" * 60)
    
    # Check key environment variables
    variables = {
        'GOOGLE_GENAI_USE_VERTEXAI': 'Configuration flag',
        'GOOGLE_API_KEY': 'API Key (sensitive)',
        'GOOGLE_CLOUD_PROJECT': 'GCP Project ID',
        'GOOGLE_CLOUD_LOCATION': 'GCP Region',
    }
    
    all_good = True
    for var_name, description in variables.items():
        value = os.getenv(var_name)
        if value:
            if 'KEY' in var_name or 'SECRET' in var_name:
                # Mask sensitive values
                display_value = f"{value[:6]}...{value[-4:]}" if len(value) > 10 else "***"
            else:
                display_value = value
            print(f"✅ {var_name}")
            print(f"   {description}: {display_value}")
        else:
            if var_name in ['GOOGLE_API_KEY', 'GOOGLE_GENAI_USE_VERTEXAI']:
                print(f"❌ {var_name}")
                print(f"   {description}: NOT SET")
                all_good = False
            else:
                print(f"⚪ {var_name}")
                print(f"   {description}: Not set (optional)")
    
    print("\n" + "=" * 60)
    if all_good:
        print("✅ Configuration is correct!")
        print("\nYou can now run:")
        print("  python final_test.py")
        print("  python cli.py")
    else:
        print("⚠️  Configuration incomplete")
        print("\nPlease set required environment variables in .env file")
    print("=" * 60)

if __name__ == "__main__":
    main()