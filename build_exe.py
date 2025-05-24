import subprocess
import os
import shutil
import sys

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building Steam Connection Controller executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--name", "SteamConnectionController",  # Output name
        "--add-data", "requirements.txt;.",     # Include requirements
        "--hidden-import", "psutil",            # Ensure psutil is included
        "--hidden-import", "tkinter",           # Ensure tkinter is included
        "steam_connection_controller.py"
    ]
    
    # Add icon if exists
    if os.path.exists("icon.ico"):
        cmd.insert(-1, "--icon")
        cmd.insert(-1, "icon.ico")
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Executable built successfully!")
        
        # Create release folder
        if os.path.exists("release"):
            shutil.rmtree("release")
        os.makedirs("release")
        
        # Copy files to release folder
        files_to_copy = [
            ("dist/SteamConnectionController.exe", "SteamConnectionController.exe"),
            ("README.md", "README.md"),
            ("LICENSE", "LICENSE"),
            ("CHANGELOG.md", "CHANGELOG.md"),
            ("requirements.txt", "requirements.txt"),
            ("test_program.py", "test_program.py")
        ]
        
        for src, dst in files_to_copy:
            if os.path.exists(src):
                shutil.copy2(src, f"release/{dst}")
                print(f"✅ Copied {dst}")
        
        # Create a simple batch file for the exe
        with open("release/SteamConnectionController.bat", "w") as f:
            f.write("@echo off\n")
            f.write("title Steam Connection Controller\n")
            f.write("echo Starting Steam Connection Controller...\n")
            f.write("echo.\n")
            f.write("echo Note: This program requires administrator privileges.\n")
            f.write("echo.\n")
            f.write("SteamConnectionController.exe\n")
            f.write("pause\n")
        
        print("✅ Created SteamConnectionController.bat")
        
        print("\n🎉 Release package created in 'release' folder!")
        print("📦 Files included:")
        for file in os.listdir("release"):
            print(f"   - {file}")
            
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def clean_build_files():
    """Clean up build artifacts"""
    folders_to_remove = ["build", "dist", "__pycache__"]
    files_to_remove = ["SteamConnectionController.spec"]
    
    for folder in folders_to_remove:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"🧹 Cleaned {folder}")
    
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"🧹 Cleaned {file}")

if __name__ == "__main__":
    print("=" * 50)
    print("Steam Connection Controller - Build Script")
    print("=" * 50)
    
    if build_executable():
        print("\n✅ Build completed successfully!")
        
        clean_choice = input("\nDo you want to clean build artifacts? (y/n): ")
        if clean_choice.lower() == 'y':
            clean_build_files()
            print("🧹 Build artifacts cleaned!")
    else:
        print("\n❌ Build failed!")
    
    input("\nPress Enter to exit...")