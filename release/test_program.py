import subprocess
import os
import sys

def test_python_installation():
    """Test Python installation"""
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Python installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Python not found!")
            return False
    except Exception as e:
        print(f"❌ Python test error: {e}")
        return False

def test_admin_rights():
    """Test administrator privileges"""
    try:
        import ctypes
        if ctypes.windll.shell32.IsUserAnAdmin():
            print("✅ Administrator privileges available")
            return True
        else:
            print("⚠️  No administrator privileges (required for firewall operations)")
            return False
    except Exception as e:
        print(f"❌ Privilege check error: {e}")
        return False

def test_steam_detection():
    """Test Steam detection"""
    possible_paths = [
        "C:\\Program Files (x86)\\Steam\\steam.exe",
        "C:\\Program Files\\Steam\\steam.exe",
        "D:\\Steam\\steam.exe",
        "E:\\Steam\\steam.exe"
    ]
    
    found_paths = []
    for path in possible_paths:
        if os.path.exists(path):
            found_paths.append(path)
    
    if found_paths:
        print(f"✅ Steam found: {len(found_paths)} location(s)")
        for path in found_paths:
            print(f"   📁 {path}")
        return True
    else:
        print("⚠️  Steam not found (in standard locations)")
        return False

def test_firewall_access():
    """Test firewall access"""
    try:
        # Test a simple firewall command
        result = subprocess.run("netsh advfirewall firewall show rule name=all", 
                               shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Firewall commands accessible")
            return True
        else:
            print("❌ No access to firewall commands")
            return False
    except Exception as e:
        print(f"❌ Firewall test error: {e}")
        return False

def test_psutil_library():
    """Test psutil library"""
    try:
        import psutil
        print("✅ psutil library available")
        return True
    except ImportError:
        print("❌ psutil library not found (run: pip install psutil)")
        return False
    except Exception as e:
        print(f"❌ psutil test error: {e}")
        return False

def main():
    print("=" * 50)
    print("Steam Connection Controller - System Test")
    print("=" * 50)
    print()
    
    tests = [
        ("Python Installation", test_python_installation),
        ("Administrator Privileges", test_admin_rights),
        ("Steam Detection", test_steam_detection),
        ("Firewall Access", test_firewall_access),
        ("psutil Library", test_psutil_library)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"🔍 Testing {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Result: {passed}/{total} successful")
    
    if passed == total:
        print("🎉 All tests successful! Program ready to use.")
    elif passed >= total - 1:
        print("⚠️  Minor issues exist but program should work.")
    else:
        print("❌ Serious issues exist. Please check requirements.")
    
    print("\n💡 To run the program:")
    print("   1. Right-click on steam_controller.bat")
    print("   2. Select 'Run as administrator'")
    print("=" * 50)

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")