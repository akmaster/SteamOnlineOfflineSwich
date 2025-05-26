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

def test_client_detection():
    """Test detection for all supported game clients."""
    clients_found = 0
    
    # Test Steam
    steam_possible_paths = [
        "C:\\Program Files (x86)\\Steam\\steam.exe",
        "C:\\Program Files\\Steam\\steam.exe",
        "D:\\Steam\\steam.exe",
        "E:\\Steam\\steam.exe"
    ]
    steam_found_paths = [p for p in steam_possible_paths if os.path.exists(p)]
    if steam_found_paths:
        print(f"✅ Steam found: {len(steam_found_paths)} location(s)")
        clients_found +=1
    else:
        print("⚠️  Steam not found (in standard locations)")

    # Test Ubisoft Connect
    ubisoft_possible_dirs = [
        "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher",
        "C:\\Program Files\\Ubisoft\\Ubisoft Game Launcher",
    ]
    ubisoft_exes = ["upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe"]
    ubisoft_found = False
    for u_dir in ubisoft_possible_dirs:
        if os.path.isdir(u_dir):
            for u_exe in ubisoft_exes:
                if os.path.exists(os.path.join(u_dir, u_exe)):
                    print(f"✅ Ubisoft Connect found (in {u_dir})")
                    ubisoft_found = True
                    clients_found +=1
                    break
        if ubisoft_found: break
    if not ubisoft_found:
        print("⚠️  Ubisoft Connect not found (in standard locations)")

    # Test EA Play
    ea_possible_dirs = [
        "C:\\Program Files\\Electronic Arts\\EA Desktop\\EA Desktop",
        "C:\\Program Files (x86)\\Electronic Arts\\EA Desktop\\EA Desktop",
    ]
    ea_exes = ["EADesktop.exe", "EALauncher.exe"]
    ea_found = False
    for e_dir in ea_possible_dirs:
        if os.path.isdir(e_dir):
            for e_exe in ea_exes:
                if os.path.exists(os.path.join(e_dir, e_exe)):
                    print(f"✅ EA Play found (in {e_dir})")
                    ea_found = True
                    clients_found +=1
                    break
        if ea_found: break
    if not ea_found:
        print("⚠️  EA Play not found (in standard locations)")

    # Test Rockstar Launcher
    rockstar_possible_dirs = [
        "C:\\Program Files\\Rockstar Games\\Launcher",
        "C:\\Program Files (x86)\\Rockstar Games\\Launcher",
    ]
    rockstar_exes = ["Launcher.exe", "LauncherPatcher.exe"]
    rockstar_found = False
    for r_dir in rockstar_possible_dirs:
        if os.path.isdir(r_dir):
            for r_exe in rockstar_exes:
                if os.path.exists(os.path.join(r_dir, r_exe)):
                    print(f"✅ Rockstar Launcher found (in {r_dir})")
                    rockstar_found = True
                    clients_found +=1
                    break
        if rockstar_found: break
    if not rockstar_found:
        print("⚠️  Rockstar Launcher not found (in standard locations)")
        
    return clients_found > 0 # En az bir istemci bulunduysa başarılı say

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
    print("Game Client Connection Controller - System Test") # Başlık güncellendi
    print("=" * 50)
    print()
    
    tests = [
        ("Python Installation", test_python_installation),
        ("Administrator Privileges", test_admin_rights),
        ("Client Detection", test_client_detection), # Test adı güncellendi
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
        print("⚠️  Minor issues exist but program should work.") # Girinti düzeltildi
    else:
        print("❌ Serious issues exist. Please check requirements.")
    
    print("\n💡 To run the program:")
    print("   1. Right-click on game_client_controller.bat") # .bat adı güncellendi
    print("   2. Select 'Run as administrator'")
    print("=" * 50)

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
