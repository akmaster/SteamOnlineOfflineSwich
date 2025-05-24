# Steam Bağlantı Kontrolcüsü

![GitHub release (latest by date)](https://img.shields.io/github/v/release/username/steam-connection-controller)
![GitHub](https://img.shields.io/github/license/username/steam-connection-controller)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/username/steam-connection-controller/test.yml)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![GitHub issues](https://img.shields.io/github/issues/username/steam-connection-controller)
![GitHub stars](https://img.shields.io/github/stars/username/steam-connection-controller)

Windows için Steam'ın internet bağlantısını kontrol eden basit ve etkili bir program.

> **Not:** Bu program sadece Windows işletim sistemlerinde çalışır ve yönetici yetkisi gerektirir.

## Özellikler

- ✅ Steam'ın internet bağlantısını tek tıkla kesme
- ✅ Steam'ın internet bağlantısını tek tıkla açma
- ✅ Gerçek zamanlı bağlantı durumu göstergesi
- ✅ Otomatik Steam yolu tespiti
- ✅ Güvenli Windows Firewall entegrasyonu
- ✅ Kullanıcı dostu arayüz

## Gereksinimler

- Windows 10/11
- Python 3.6 veya üzeri
- Yönetici yetkisi (firewall kuralları için)
- Steam kurulu olmalı

## Kurulum

1. Bu dosyaları bir klasöre indirin
2. Python'un sisteminizde kurulu olduğundan emin olun
3. `steam_controller.bat` dosyasını **yönetici olarak çalıştırın**

## Kullanım

### İlk Çalıştırma
1. `steam_controller.bat` dosyasına sağ tıklayın
2. "Yönetici olarak çalıştır" seçeneğini seçin
3. Program otomatik olarak Steam'ı bulacak ve durumu gösterecek

### Ana Özellikler

#### Bağlantıyı Kesme
- "Bağlantıyı Kes" butonuna tıklayın
- Program Steam'ın tüm internet erişimini engelleyecek
- Durum göstergesi kırmızı olacak

#### Bağlantıyı Açma
- "Bağlantıyı Aç" butonuna tıklayın
- Program Steam'ın internet erişim engelini kaldıracak
- Durum göstergesi yeşil olacak

#### Durum Kontrolü
- Program açıldığında otomatik olarak durumu kontrol eder
- "Durumu Yenile" butonu ile manuel kontrol yapabilirsiniz

## Teknik Detaylar

### Nasıl Çalışır?
Program Windows Firewall kuralları kullanarak Steam'ın internet erişimini kontrol eder:

1. **Steam Tespiti**: Yaygın Steam kurulum yollarını tarar
2. **Firewall Kuralları**: Steam executable dosyaları için gelen/giden trafiği engeller
3. **Durum Takibi**: Mevcut firewall kurallarını kontrol ederek durumu gösterir

### Güvenlik
- Sadece Windows'un yerleşik firewall özelliklerini kullanır
- Hiçbir üçüncü parti yazılım gerektirmez
- Steam dosyalarını değiştirmez
- Sistem dosyalarına müdahale etmez

### Desteklenen Steam Dosyaları
- `steam.exe` (Ana Steam uygulaması)
- `steamwebhelper.exe` (Web tarayıcı bileşeni)

## Sorun Giderme

### "Steam bulunamadı" Hatası
- Steam'ın standart konumlarda kurulu olduğundan emin olun
- Desteklenen yollar:
  - `C:\Program Files (x86)\Steam\`
  - `C:\Program Files\Steam\`
  - `D:\Steam\`
  - `E:\Steam\`

### "Yönetici yetkisi gerekli" Hatası
- Programı mutlaka "Yönetici olarak çalıştır" ile başlatın
- Windows Firewall kuralları yönetici yetkisi gerektirir

### Bağlantı Durumu Yanlış Görünüyor
- "Durumu Yenile" butonuna tıklayın
- Steam'ı yeniden başlatın
- Programı kapatıp yeniden açın

## Sık Sorulan Sorular

**S: Steam açıkken bu programı kullanabilir miyim?**
C: Evet, Steam açıkken de kullanabilirsiniz. Değişiklikler anında etkili olur.

**S: Bu program Steam'ı bozar mı?**
C: Hayır, sadece firewall kuralları oluşturur. Steam dosyalarına dokunmaz.

**S: Programı kapattıktan sonra ayarlar kalır mı?**
C: Evet, firewall kuralları Windows'ta kalıcıdır. Programı kapatmak ayarları etkilemez.

**S: Diğer oyunları etkiler mi?**
C: Hayır, sadece Steam'a özel kurallar oluşturur.

## Lisans

Bu program eğitim amaçlı oluşturulmuştur. Kendi sorumluluğunuzda kullanın.

## Destek

Sorunlarınız için:
1. README dosyasını kontrol edin
2. Sorun giderme bölümünü inceleyin
3. Programı yönetici olarak çalıştırdığınızdan emin olun