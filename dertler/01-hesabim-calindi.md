[Derde Deva](../README.md) › Dert 1 / 12

# “İki adımlı doğrulama açıktı, hesabım yine çalındı”

*Instagram, Steam, Discord. Şifre değişmiş, telefona kod gelmemiş, hesap başkasının elinde.*

> **Gerçek vaka**
>
> Check Point'in araştırmacıları 2025'te YouTube'da 3.000'den fazla videodan oluşan bir ağ buldu. Videolar “bedava Photoshop”, “oyun hilesi”, “ücretsiz FL Studio” vaat ediyordu. Bazıları 129 bin aboneli, ele geçirilmiş gerçek kanallarda yayındaydı. Açıklamadaki bağlantı şifreli bir zip dosyasına gidiyordu, şifre de hemen altında yazıyordu: “şifre 1234”. Videodaki adımlardan biri de şuydu: “Kurmadan önce antivirüsünü geçici olarak kapat.”[^1]

## Aslında ne oluyor?

Bir siteye giriş yaptığında site tarayıcına bir “giriş kartı” verir. Her seferinde şifre ve kod sormamasının sebebi bu karttır. Bu tür virüslerin aradığı şey şifreden çok o karttır. Kartı kopyalayan kişi siteye senmişsin gibi girer; şifre de iki adımlı doğrulama da devreye girmez, çünkü girişi zaten yapmışsındır.[^2] Virüs birkaç saniyede kartları, tarayıcıya kayıtlı şifreleri, kripto cüzdanlarını toplar, gönderir ve çoğu zaman iz bırakmadan kendini siler.

## Başına geldiyse

1. Şüpheli bilgisayara dokunma. Şifreleri **telefondan** ya da başka, temiz bir cihazdan değiştir.
2. Asıl önemli adım: her hesapta **bütün oturumlardan çıkış** yap. Şifre değiştirmek kopyalanan kartı her zaman geçersiz kılmaz, oturumu kapatmak kılar.<br> **Instagram:** Ayarlar › Hesaplar Merkezi › Şifre ve güvenlik › Giriş yaptığın yerler. **Google:** Hesap › Güvenlik › Cihazlarınız. **Steam:** Steam Guard › Diğer tüm cihazların yetkisini kaldır. **Discord:** Ayarlar › Cihazlar › Bilinen tüm cihazlardan çıkış yap.
3. Önce e-postanı kurtar; diğer bütün hesapların anahtarı o.
4. Bilgisayara gelince en sağlam yol temiz kurulumdur ([üçüncü bölüm](03-windows-bozuldu-format-sart-mi.md)). Önce bir fikir edinmek istersen ESET Online Scanner ya da Emsisoft Emergency Kit gibi, kurulu antivirüsünle çakışmayan ücretsiz “ikinci görüş” tarayıcıları kullan.

> **Bunu çoğu kişi bilmiyor**
>
> Virüsü silmek hesabı kurtarmaz. Çalınan giriş kartı, virüs silindikten sonra da çalışmaya devam eder.[^2] Bir de şunu bil: bir dosya sana şifreli zip olarak, şifresi de yanında gelirse bunun tek bir anlamı vardır: biri antivirüsün o dosyanın içine bakmasını istemiyor.

## Bu sayfadaki resmî adresler

Programı indirirken tarayıcının adres çubuğunda yazan, buradakiyle harfi harfine aynı olmalı.

- ESET Online Scanner: [eset.com/tr/home/online-scanner](https://www.eset.com/tr/home/online-scanner/)
- Emsisoft Emergency Kit: [emsisoft.com/en/emergency-kit](https://www.emsisoft.com/en/emergency-kit/)

---

Bu sayfadaki bağlantılar en son 15 Kasım 2026'da denetlendi. Yanlış, eksik ya da eskimiş bir şey gördüysen [bildir](https://github.com/Ilyas-jpg/derde-deva/issues/new/choose).

[Bütün dertler](../README.md#dertler) · [Sonraki dert →](02-indirdigim-programdan-virus-cikti.md)

## Kaynaklar

[^1]: [Check Point Research: YouTube Ghost Network](https://research.checkpoint.com/2025/youtube-ghost-network/) · [Fox News özeti](https://www.foxnews.com/tech/3000-youtube-videos-deliver-malware-disguised-free-software)
[^2]: [Recorded Future: oturum çerezi hırsızlığı ve 2FA](https://recordedfuture.com/session-hijacking-mfa-bypass) · [Notebookcheck: 2FA'ya rağmen çalınan hesap](https://www.notebookcheck.net/Account-hijacked-despite-2FA-a-stolen-cookie-is-enough.1364307.0.html)
