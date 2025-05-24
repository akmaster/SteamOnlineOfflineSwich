# GitHub Release Yayınlama Rehberi

## 🚀 Adım Adım GitHub Release Oluşturma

### 1️⃣ GitHub Repository Oluşturma

#### Eğer henüz repository yoksa:
1. **GitHub.com**'a git
2. **"New repository"** tıkla
3. **Repository name**: `steam-connection-controller`
4. **Description**: `Control Steam's internet connection with Windows Firewall`
5. **Public** seç (herkesin görebilmesi için)
6. **Add README file** işaretini KALDIR (zaten var)
7. **Create repository** tıkla

### 2️⃣ Kodları GitHub'a Yükleme

#### Terminal/Command Prompt'ta şu komutları çalıştır:

```bash
# Git repository'sini başlat
git init

# Tüm dosyaları ekle
git add .

# İlk commit'i yap
git commit -m "Initial release: Steam Connection Controller v1.1.0"

# GitHub repository'sini remote olarak ekle (YOUR_USERNAME'i kendi kullanıcı adınla değiştir)
git remote add origin https://github.com/YOUR_USERNAME/steam-connection-controller.git

# Ana branch'i main olarak ayarla
git branch -M main

# Kodları GitHub'a yükle
git push -u origin main
```

### 3️⃣ GitHub Release Oluşturma

#### GitHub web sitesinde:

1. **Repository'ne git**: `https://github.com/YOUR_USERNAME/steam-connection-controller`

2. **"Releases" sekmesine tıkla** (sağ tarafta)

3. **"Create a new release" butonuna tıkla**

4. **Release bilgilerini doldur**:
   - **Tag version**: `v1.1.0`
   - **Release title**: `Steam Connection Controller v1.1.0`
   - **Description**: Aşağıdaki metni kopyala-yapıştır:

```markdown
# Steam Connection Controller v1.1.0

## 🎉 What's New

### ✨ Major Features
- **Standalone Executable**: No Python installation required!
- **Automatic Steam Management**: Steam is automatically closed before operations and restarted afterward
- **Complete English Translation**: All interface elements and messages in English
- **Enhanced User Experience**: Clear status updates and confirmation dialogs

### 🔧 Technical Improvements
- Built with PyInstaller for easy distribution
- Improved process management with psutil
- Thread-safe operations
- Better error handling and user feedback

## 📦 Download Options

### 🎯 Recommended Download
- **SteamConnectionController_v1.1.0.zip** - Complete package with documentation

### ⚡ Quick Download
- **SteamConnectionController.exe** - Just the executable file

## 🚀 Quick Start

1. Download the ZIP file
2. Extract to any folder
3. Right-click on `SteamConnectionController.bat`
4. Select "Run as administrator"
5. Use Block/Allow buttons to control Steam's connection

## ⚠️ Requirements

- Windows 10/11
- Administrator privileges
- Steam installed

## 🔒 Security

- Uses only Windows built-in firewall
- No network connections made
- Open source code
- No data collection

## 📞 Support

Check README.md for detailed instructions and troubleshooting.
```

5. **Assets yükle**:
   - **"Attach binaries"** linkine tıkla
   - **SteamConnectionController_v1.1.0.zip** dosyasını sürükle-bırak
   - **SteamConnectionController.exe** dosyasını da ekle (release klasöründen)

6. **Release ayarları**:
   - ✅ **"Set as the latest release"** işaretle
   - ✅ **"Create a discussion for this release"** işaretle (isteğe bağlı)

7. **"Publish release" butonuna tıkla**

### 4️⃣ Otomatik Release (Gelecek için)

#### Gelecekte otomatik release için:

```bash
# Yeni versiyon için tag oluştur
git tag v1.2.0

# Tag'i GitHub'a gönder
git push origin v1.2.0
```

Bu otomatik olarak:
- EXE dosyasını derleyecek
- Release oluşturacak
- Assets'leri yükleyecek

### 5️⃣ Release Sonrası

#### README'yi güncelle:
- Badge'lerdeki `username` kısmını gerçek kullanıcı adınla değiştir
- Download linklerini ekle

#### Paylaş:
- Reddit (r/Steam, r/software)
- Discord sunucuları
- Sosyal medya

## 🎯 Önemli Notlar

### İlk Kez Yayınlarken:
- Windows Defender uyarısı çıkabilir (normal)
- Kullanıcılara "More info" → "Run anyway" diyeceğini söyle
- Virüs tarayıcıları false positive verebilir

### Download İstatistikleri:
- GitHub'da kaç kişinin indirdiğini görebilirsin
- Release sayfasında istatistikler var

### Güncelleme:
- Yeni versiyon için yukarıdaki adımları tekrarla
- Version numarasını artır (v1.1.1, v1.2.0, vb.)

---

**Hazırsın! 🚀**

Bu adımları takip ederek Steam Connection Controller'ını GitHub'da yayınlayabilirsin. Herkes indirebilir ve kullanabilir!