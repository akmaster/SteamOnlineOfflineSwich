import subprocess
import os
import sys

def test_python_installation():
    """Python kurulumunu test et"""
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Python kurulu: {result.stdout.strip()}")
            return True
        else:
            print("❌ Python bulunamadı!")
            return False
    except Exception as e:
        print(f"❌ Python test hatası: {e}")
        return False

def test_admin_rights():
    """Yönetici yetkilerini test et"""
    try:
        import ctypes
        if ctypes.windll.shell32.IsUserAnAdmin():
            print("✅ Yönetici yetkisi mevcut")
            return True
        else:
            print("⚠️  Yönetici yetkisi yok (firewall işlemleri için gerekli)")
            return False
    except Exception as e:
        print(f"❌ Yetki kontrolü hatası: {e}")
        return False

def test_steam_detection():
    """Steam tespitini test et"""
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
        print(f"✅ Steam bulundu: {len(found_paths)} konum")
        for path in found_paths:
            print(f"   📁 {path}")
        return True
    else:
        print("⚠️  Steam bulunamadı (standart konumlarda)")
        return False

def test_firewall_access():
    """Firewall erişimini test et"""
    try:
        # Basit bir firewall komutu test et
        result = subprocess.run("netsh advfirewall firewall show rule name=all", 
                               shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Firewall komutları erişilebilir")
            return True
        else:
            print("❌ Firewall komutlarına erişim yok")
            return False
    except Exception as e:
        print(f"❌ Firewall test hatası: {e}")
        return False

def main():
    print("=" * 50)
    print("Steam Bağlantı Kontrolcüsü - Sistem Testi")
    print("=" * 50)
    print()
    
    tests = [
        ("Python Kurulumu", test_python_installation),
        ("Yönetici Yetkisi", test_admin_rights),
        ("Steam Tespiti", test_steam_detection),
        ("Firewall Erişimi", test_firewall_access)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"🔍 {test_name} test ediliyor...")
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Sonucu: {passed}/{total} başarılı")
    
    if passed == total:
        print("🎉 Tüm testler başarılı! Program kullanıma hazır.")
    elif passed >= total - 1:
        print("⚠️  Küçük sorunlar var ama program çalışabilir.")
    else:
        print("❌ Ciddi sorunlar var. Lütfen gereksinimleri kontrol edin.")
    
    print("\n💡 Program çalıştırmak için:")
    print("   1. steam_controller.bat dosyasına sağ tıklayın")
    print("   2. 'Yönetici olarak çalıştır' seçeneğini seçin")
    print("=" * 50)

if __name__ == "__main__":
    main()
    input("\nÇıkmak için Enter tuşuna basın...")