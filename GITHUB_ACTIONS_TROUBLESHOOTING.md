# GitHub Actions Troubleshooting

## 🔧 GitHub Actions Workflow Hatası Çözümü

### ❌ Yaşanan Problem:
GitHub Actions "Create Release" workflow'u başarısız oldu.

### ✅ Çözüm:
Workflow dosyası güncellendi ve modern GitHub Actions kullanılıyor.

## 🔄 Güncellemeler:

### 1️⃣ Eski Workflow Sorunları:
- `actions/create-release@v1` - Deprecated (kullanımdan kaldırıldı)
- `actions/upload-release-asset@v1` - Deprecated
- Eski API kullanımı

### 2️⃣ Yeni Workflow Özellikleri:
- ✅ `softprops/action-gh-release@v1` - Modern ve aktif
- ✅ Tek adımda release ve asset upload
- ✅ Daha basit ve güvenilir
- ✅ `permissions: contents: write` eklendi

## 🧪 Test Etme:

### Yeni Tag Oluşturarak Test:
```bash
# Yeni bir test tag'i oluştur
git tag v1.1.1
git push origin v1.1.1
```

### Workflow Durumunu Kontrol:
1. GitHub repository → **Actions** sekmesi
2. "Create Release" workflow'unu izle
3. Başarılı olursa otomatik release oluşacak

## 🔍 Workflow Adımları:

### 1. Environment Setup:
- ✅ Windows runner
- ✅ Python 3.11 kurulumu
- ✅ PyInstaller ve psutil kurulumu

### 2. Build Process:
- ✅ EXE dosyası oluşturma
- ✅ Release klasörü hazırlama
- ✅ ZIP paketi oluşturma

### 3. Release Creation:
- ✅ GitHub release oluşturma
- ✅ Assets yükleme (ZIP + EXE)
- ✅ Release notes ekleme

## 🚨 Olası Hatalar ve Çözümleri:

### Hata: "Permission denied"
**Çözüm**: Repository Settings → Actions → General → Workflow permissions → "Read and write permissions" seç

### Hata: "Tag already exists"
**Çözüm**: Farklı bir tag kullan (v1.1.2, v1.2.0 vb.)

### Hata: "PyInstaller failed"
**Çözüm**: Dependencies eksik, workflow'da pip install komutu var

### Hata: "File not found"
**Çözüm**: Dosya yolları Windows için düzeltildi

## 📋 Manuel Release (Backup Plan):

Eğer workflow çalışmazsa manuel olarak:

1. **Yerel build**:
   ```bash
   python build_exe.py
   ```

2. **GitHub'da manuel release**:
   - Releases → Create new release
   - Tag: v1.1.1
   - Upload: ZIP ve EXE dosyaları

## ✅ Başarı Kontrolleri:

Workflow başarılı olduğunda:
- [ ] GitHub Actions yeşil ✅ gösterir
- [ ] Yeni release otomatik oluşur
- [ ] ZIP ve EXE dosyaları yüklenir
- [ ] Release notes otomatik eklenir

## 🔄 Gelecek Releases:

Artık sadece tag push'layarak otomatik release:
```bash
git tag v1.2.0
git push origin v1.2.0
```

---

**Workflow artık modern ve güvenilir! 🚀**

Bir sonraki tag push'ında otomatik olarak çalışacak.