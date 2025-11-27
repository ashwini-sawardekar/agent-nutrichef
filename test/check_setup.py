"""
Check NutriChef Agent setup and dependencies
Run: python check_setup.py
"""
import os
import sys
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings('ignore')

def check_python_version():
    """Check Python version"""
    print("🐍 Python Version:")
    print(f"   {sys.version}")
    version_info = sys.version_info
    if version_info.major == 3 and version_info.minor >= 9:
        print("   ✅ Python version is compatible")
    else:
        print("   ⚠️  Python 3.9+ recommended")
    print()

def check_dependencies():
    """Check if required packages are installed"""
    print("📦 Checking Dependencies:")
    print("-" * 60)
    
    required = {
        'google.adk': 'google-adk',
        'google.auth': 'google-auth',
        'google.generativeai': 'google-generativeai',
        'dotenv': 'python-dotenv',
    }
    
    missing = []
    
    for module, package in required.items():
        try:
            mod = __import__(module)
            version = getattr(mod, '__version__', 'unknown')
            print(f"   ✅ {package}: {version}")
        except ImportError:
            print(f"   ❌ {package}: NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print(f"\nInstall with: pip install {' '.join(missing)}")
    else:
        print("\n✅ All dependencies installed")
    print()

def check_environment():
    """Check environment variables"""
    print("🔧 Environment Configuration:")
    print("-" * 60)
    
    use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE").upper() == "TRUE"
    api_key = os.getenv("GOOGLE_API_KEY")
    project = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    print(f"   Using Vertex AI: {use_vertex}")
    
    if use_vertex:
        if project:
            print(f"   ✅ Project ID: {project}")
        else:
            print("   ❌ GOOGLE_CLOUD_PROJECT not set")
    else:
        if api_key:
            print(f"   ✅ API Key: {api_key[:10]}...{api_key[-4:] if len(api_key) > 14 else ''}")
        else:
            print("   ❌ GOOGLE_API_KEY not set")
            print("\n   Please set your API key:")
            print("   PowerShell: $env:GOOGLE_API_KEY='your_key'")
            print("   Or create .env file with: GOOGLE_API_KEY=your_key")
    print()

def check_project_structure():
    """Check if project structure is correct"""
    print("📁 Project Structure:")
    print("-" * 60)
    
    expected_files = [
        'nutrichef_agent/__init__.py',
        'nutrichef_agent/agent.py',
        'nutrichef_agent/config.py',
        'nutrichef_agent/tools.py',
        'nutrichef_agent/sub_agents/__init__.py',
    ]
    
    all_good = True
    for file in expected_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - MISSING")
            all_good = False
    
    if all_good:
        print("\n✅ Project structure is correct")
    else:
        print("\n⚠️  Some files are missing")
    print()

def test_imports():
    """Test if nutrichef_agent can be imported"""
    print("🧪 Testing Imports:")
    print("-" * 60)
    
    try:
        from nutrichef_agent import root_agent
        print("   ✅ nutrichef_agent imported successfully")
        print(f"   ✅ root_agent: {type(root_agent).__name__}")
        
        from nutrichef_agent.tools import recipe_database_tool, grocery_api_connector
        print("   ✅ Tools imported successfully")
        
        print("\n✅ All imports working")
    except Exception as e:
        print(f"   ❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
    print()

def check_google_adk():
    """Check Google ADK specific details"""
    print("🔍 Google ADK Details:")
    print("-" * 60)
    
    try:
        import google.adk
        print(f"   Version: {getattr(google.adk, '__version__', 'unknown')}")
        
        # Check what's available in sessions
        try:
            from google.adk import sessions
            available = dir(sessions)
            print(f"   Available in google.adk.sessions:")
            for item in available:
                if not item.startswith('_'):
                    print(f"     • {item}")
        except Exception as e:
            print(f"   ⚠️  Could not inspect sessions: {e}")
        
        print("   ✅ Google ADK is available")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    print()

def main():
    """Run all checks"""
    print("\n" + "=" * 60)
    print("🔍 NutriChef Agent - Setup Verification")
    print("=" * 60)
    print()
    
    check_python_version()
    check_dependencies()
    check_environment()
    check_project_structure()
    test_imports()
    check_google_adk()
    
    print("=" * 60)
    print("🎯 Summary:")
    print("=" * 60)
    print("""
If all checks passed:
  ✅ Run: python working_test.py

If there are issues:
  1. Install missing packages
  2. Set environment variables
  3. Check project structure
  4. Run this script again
    """)

if __name__ == "__main__":
    main()