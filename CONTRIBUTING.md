# Katkıda Bulunma Rehberi

Steam Bağlantı Kontrolcüsü projesine katkıda bulunmak istediğiniz için teşekkürler! 🎉

## 📋 İçindekiler
- [Katkı Türleri](#katkı-türleri)
- [Geliştirme Ortamı](#geliştirme-ortamı)
- [Kod Standartları](#kod-standartları)
- [Pull Request Süreci](#pull-request-süreci)
- [Issue Raporlama](#issue-raporlama)
- [Topluluk Kuralları](#topluluk-kuralları)

## 🤝 Katkı Türleri

### 🐛 Hata Raporları
- Karşılaştığınız hataları [bug report template](/.github/ISSUE_TEMPLATE/bug_report.md) kullanarak bildirin
- Hatayı tekrarlama adımlarını detaylı olarak açıklayın
- Sistem bilgilerinizi ekleyin

### ✨ Özellik Önerileri
- Yeni özellik fikirlerinizi [feature request template](/.github/ISSUE_TEMPLATE/feature_request.md) ile paylaşın
- Özelliğin neden gerekli olduğunu açıklayın
- Mümkünse mockup veya tasarım örnekleri ekleyin

### 📝 Dokümantasyon
- README dosyasını iyileştirin
- Kod yorumlarını geliştirin
- Kullanım kılavuzunu genişletin

### 💻 Kod Katkıları
- Hata düzeltmeleri
- Yeni özellikler
- Performans iyileştirmeleri
- Kod refactoring

## 🛠️ Geliştirme Ortamı

### Gereksinimler
- Windows 10/11
- Python 3.6+
- Git
- Yönetici yetkisi (test için)

### Kurulum
1. Repository'yi fork edin
2. Yerel makinenize clone edin:
   ```bash
   git clone https://github.com/KULLANICI_ADINIZ/steam-connection-controller.git
   cd steam-connection-controller
   ```
3. Test programını çalıştırın:
   ```bash
   python test_program.py
   ```

### Geliştirme Dalları
- `main`: Stabil sürüm
- `develop`: Geliştirme dalı
- `feature/özellik-adı`: Yeni özellikler
- `bugfix/hata-adı`: Hata düzeltmeleri

## 📏 Kod Standartları

### Python Kod Stili
- PEP 8 standartlarını takip edin
- Fonksiyon ve değişken isimleri Türkçe olabilir
- Docstring'leri Türkçe yazın

### Örnek Kod Formatı
```python
def steam_baglantisini_kes(self):
    """Steam'ın internet bağlantısını keser.
    
    Returns:
        bool: İşlem başarılı ise True, değilse False
    """
    try:
        # Kod burada
        return True
    except Exception as e:
        print(f"Hata: {e}")
        return False
```

### Commit Mesajları
Türkçe commit mesajları kullanın:
- `feat: yeni özellik eklendi`
- `fix: hata düzeltildi`
- `docs: dokümantasyon güncellendi`
- `style: kod formatı düzeltildi`
- `refactor: kod yeniden düzenlendi`
- `test: test eklendi`

## 🔄 Pull Request Süreci

### 1. Hazırlık
- Issue oluşturun veya mevcut bir issue'yu seçin
- Feature branch oluşturun:
  ```bash
  git checkout -b feature/yeni-ozellik
  ```

### 2. Geliştirme
- Değişikliklerinizi yapın
- Kod standartlarına uyun
- Test edin

### 3. Test
- Programı farklı senaryolarda test edin
- `test_program.py` ile sistem testlerini çalıştırın
- Mevcut özelliklerin bozulmadığından emin olun

### 4. Commit ve Push
```bash
git add .
git commit -m "feat: yeni özellik açıklaması"
git push origin feature/yeni-ozellik
```

### 5. Pull Request
- GitHub'da PR oluşturun
- [PR template](/.github/pull_request_template.md) doldurun
- Reviewerları bekleyin

## 🐛 Issue Raporlama

### Hata Raporları
1. Önce mevcut issue'ları kontrol edin
2. Hatayı tekrarlayabildiğinizden emin olun
3. Template'i eksiksiz doldurun
4. Ekran görüntüleri ekleyin

### Özellik İstekleri
1. Özelliğin gerekliliğini açıklayın
2. Kullanım senaryolarını belirtin
3. Teknik detayları ekleyin

## 👥 Topluluk Kuralları

### Davranış Kuralları
- Saygılı ve yapıcı olun
- Türkçe iletişim kurun
- Yardımlaşmaya açık olun
- Eleştirileri yapıcı şekilde alın

### İletişim Kanalları
- GitHub Issues: Hata raporları ve özellik istekleri
- GitHub Discussions: Genel tartışmalar
- Pull Request yorumları: Kod incelemeleri

## 🏷️ Etiketler (Labels)

### Issue Etiketleri
- `bug`: Hata raporları
- `enhancement`: Özellik istekleri
- `question`: Sorular ve destek
- `documentation`: Dokümantasyon
- `good first issue`: Yeni başlayanlar için
- `help wanted`: Yardım istenen konular

### Öncelik Etiketleri
- `priority: low`: Düşük öncelik
- `priority: medium`: Orta öncelik
- `priority: high`: Yüksek öncelik
- `priority: critical`: Kritik

## 🎯 Geliştirme Hedefleri

### Kısa Vadeli
- [ ] Daha fazla Steam yolu desteği
- [ ] Gelişmiş hata yönetimi
- [ ] UI iyileştirmeleri

### Uzun Vadeli
- [ ] Diğer oyun platformları desteği
- [ ] Zamanlayıcı özelliği
- [ ] Profil sistemi

## 📞 Yardım

Sorularınız için:
1. [Support template](/.github/ISSUE_TEMPLATE/support_request.md) kullanın
2. Mevcut dokümantasyonu kontrol edin
3. GitHub Discussions'ı kullanın

---

**Teşekkürler!** 🙏
Katkılarınız bu projeyi daha iyi hale getiriyor.