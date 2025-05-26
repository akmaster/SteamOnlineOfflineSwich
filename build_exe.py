import subprocess
import os
import shutil
import sys

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building Game Client Connection Controller executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--name", "GameClientController",  # Output name
        "--add-data", "requirements.txt;.",     # Include requirements
        "--hidden-import", "psutil",            # Ensure psutil is included
        "--hidden-import", "tkinter",           # Ensure tkinter is included
        "game_client_controller.py" # Python dosya adı güncellendi
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
            ("dist/GameClientController.exe", "GameClientController.exe"), # .exe adı güncellendi
            ("README.md", "README.md"),
            ("LICENSE", "LICENSE"),
            ("CHANGELOG.md", "CHANGELOG.md"),
            ("requirements.txt", "requirements.txt"),
            ("test_program.py", "test_program.py"),
            ("game_client_controller.bat", "GameClientController.bat") # Yeni .bat dosyası eklendi (opsiyonel, aşağıdaki ile çakışabilir)
        ]
        
        for src, dst in files_to_copy:
            if src == "game_client_controller.bat" and os.path.exists(src): # Eğer ana dizindeki .bat kopyalanıyorsa
                 shutil.copy2(src, f"release/{dst}")
                 print(f"✅ Copied {dst} (from root)")
            elif os.path.exists(src):
                shutil.copy2(src, f"release/{dst}")
                print(f"✅ Copied {dst}")
        
        # Create a simple batch file for the exe (veya yukarıdakini kullan)
        # Eğer yukarıda game_client_controller.bat kopyalandıysa bu kısım gereksiz olabilir
        # veya bu kısım release içindeki .bat'ı oluşturur. Tutarlılık için birini seçmek iyi olur.
        # Şimdilik bu kısmı bırakıyorum, release içinde yeni bir .bat oluşturacak.
        with open("release/GameClientController.bat", "w") as f: # .bat adı güncellendi
            f.write("@echo off\n")
            f.write("title Game Client Connection Controller\n") # Başlık güncellendi
            f.write("echo Starting Game Client Connection Controller...\n") # Metin güncellendi
            f.write("echo.\n")
            f.write("echo Note: This program requires administrator privileges.\n")
            f.write("echo.\n")
            f.write("GameClientController.exe\n") # .exe adı güncellendi
            f.write("pause\n")
        
        print("✅ Created GameClientController.bat in release folder") # Mesaj güncellendi
        
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
    files_to_remove = ["GameClientController.spec"] # .spec adı güncellendi
    
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
    print("Game Client Connection Controller - Build Script") # Başlık güncellendi
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
