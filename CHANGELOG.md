# Değişiklik Günlüğü

Bu dosya Steam Bağlantı Kontrolcüsü projesindeki tüm önemli değişiklikleri içerir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardına dayanır,
ve bu proje [Semantic Versioning](https://semver.org/spec/v2.0.0.html) kullanır.

## [Unreleased]

### Planlanmış Özellikler
- Zamanlayıcı özelliği (belirli saatlerde otomatik açma/kapama)
- Profil sistemi (farklı ayar setleri)
- Sistem tray entegrasyonu
- Daha fazla Steam yolu desteği
- Diğer oyun platformları desteği (Epic Games, Origin, vb.)

## [1.0.0] - 2025-01-24

### Eklenen Özellikler
- ✨ Steam'ın internet bağlantısını tek tıkla kesme/açma
- 🎯 Gerçek zamanlı bağlantı durumu göstergesi
- 🔍 Otomatik Steam yolu tespiti
- 🛡️ Güvenli Windows Firewall entegrasyonu
- 🖥️ Kullanıcı dostu GUI arayüzü
- ⚡ Yönetici yetkisi otomatik kontrolü
- 📊 Sistem uyumluluğu test aracı
- 🔄 Durum yenileme özelliği

### Teknik Özellikler
- Python 3.6+ desteği
- tkinter tabanlı GUI
- Windows Firewall API entegrasyonu
- Çoklu Steam kurulum yolu desteği
- Thread-safe işlemler
- Hata yönetimi ve kullanıcı geri bildirimi

### Desteklenen Steam Dosyaları
- `steam.exe` (Ana Steam uygulaması)
- `steamwebhelper.exe` (Web tarayıcı bileşeni)

### Desteklenen Steam Yolları
- `C:\Program Files (x86)\Steam\`
- `C:\Program Files\Steam\`
- `D:\Steam\`
- `E:\Steam\`

### Güvenlik
- Sadece Windows yerleşik firewall kullanımı
- Hiçbir üçüncü parti yazılım gerektirmez
- Steam dosyalarına müdahale etmez
- Sistem dosyalarını değiştirmez

### Dokümantasyon
- 📖 Kapsamlı README dosyası
- 🤝 Katkıda bulunma rehberi
- 🐛 Issue template'leri
- 📋 Pull request template'i
- 🔧 Sistem test aracı

### GitHub Entegrasyonu
- 🔄 Otomatik test workflow'u
- 📦 Otomatik release oluşturma
- 🏷️ Issue ve PR template'leri
- 📊 Kod kalitesi kontrolleri
- 🔒 Güvenlik taramaları

## Sürüm Notları

### [1.0.0] Hakkında
Bu ilk stabil sürüm, Steam'ın internet bağlantısını güvenli ve kolay bir şekilde kontrol etmek için gerekli tüm temel özellikleri içerir. Program Windows Firewall kuralları kullanarak Steam'ın internet erişimini yönetir ve kullanıcı dostu bir arayüz sunar.

### Bilinen Sınırlamalar
- Sadece Windows işletim sistemlerinde çalışır
- Yönetici yetkisi gerektirir
- Standart Steam kurulum yollarını destekler
- Firewall kuralları manuel olarak silinebilir

### Gelecek Sürümler
Gelecek sürümlerde daha fazla özellik, daha iyi hata yönetimi ve genişletilmiş platform desteği planlanmaktadır.

---

## Etiket Açıklamaları

- `Added` - Yeni özellikler
- `Changed` - Mevcut işlevsellikte değişiklikler
- `Deprecated` - Yakında kaldırılacak özellikler
- `Removed` - Kaldırılan özellikler
- `Fixed` - Hata düzeltmeleri
- `Security` - Güvenlik ile ilgili değişiklikler

## Katkıda Bulunma

Değişiklik günlüğüne katkıda bulunmak için:
1. Her PR'da ilgili değişiklikleri `[Unreleased]` bölümüne ekleyin
2. Uygun etiketleri kullanın
3. Kullanıcı dostu açıklamalar yazın
4. Teknik detayları gerekirse ekleyin

Daha fazla bilgi için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.