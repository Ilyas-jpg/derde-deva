[Derde Deva](../README.md) › Dert 4 / 12

# “Format USB'si hazırladım, bilgisayar görmüyor”

*USB takılı, bilgisayar açılıyor ama USB'den başlamıyor. Ya da “önyüklenebilir aygıt bulunamadı” diyor.*

## Doğru hazırlamak

1. Windows dosyasını (ISO) sadece **[microsoft.com](https://www.microsoft.com/tr-tr/software-download/windows11)**'dan indir. “Hazır, etkinleştirilmiş Windows” dağıtan siteler [birinci bölüme](01-hesabim-calindi.md) kapı açar.
2. USB'yi **Rufus** ile hazırla, adresi **[rufus.ie](https://rufus.ie/tr/)**. Rufus'un da sahte reklam siteleri çıktı ([ikinci bölüm](02-indirdigim-programdan-virus-cikti.md)).[^3]
3. Rufus'ta bir tek “Bölüm düzeni” ayarı insanların kafasını karıştırır. Basit kural: Windows 11 kuruyorsan ve bilgisayar son on yılda alındıysa **GPT**'yi bırak. On yıldan eski bir bilgisayar USB'yi görmüyorsa **MBR** ile yeniden hazırla. Yanlış seçim tam olarak “aygıt bulunamadı” hatasını verir.[^7]

## USB'den başlatmak: markanın tuşu

Bilgisayarı açarken ekrana logo gelir gelmez markanın tuşuna art arda basarsan bir menü açılır, USB'yi oradan seçersin. Sık rastlanan tuşlar: **Dell** F12 · **Lenovo** F12 · **Acer** F12 · **HP** Esc, ardından F9 · **MSI** F11 · **ASUS** dizüstü Esc, masaüstü anakart F8. Tuş tutmazsa model adı ve “boot menu” diye aratmak yeterli.

> **Bunu çoğu kişi bilmiyor**
>
> Format sorunlarının çoğu USB'den değil, bu iki küçük seçimden çıkar: yanlış bölüm düzeni ve yanlış başlatma tuşu. Bir de önce [üçüncü bölüme](03-windows-bozuldu-format-sart-mi.md) bak; belki USB'ye hiç gerek yoktur.

## Bu sayfadaki resmî adresler

Programı indirirken tarayıcının adres çubuğunda yazan, buradakiyle harfi harfine aynı olmalı.

- Windows 11 kurulum dosyası: [microsoft.com/tr-tr/software-download/windows11](https://www.microsoft.com/tr-tr/software-download/windows11)
- Rufus: [rufus.ie](https://rufus.ie/tr/)

---

Bu sayfadaki bağlantılar en son 15 Kasım 2026'da denetlendi. Yanlış, eksik ya da eskimiş bir şey gördüysen [bildir](https://github.com/Ilyas-jpg/derde-deva/issues/new/choose).

[← Önceki dert](03-windows-bozuldu-format-sart-mi.md) · [Bütün dertler](../README.md#dertler) · [Sonraki dert →](05-formattan-sonra-ses-internet-yok.md)

## Kaynaklar

[^3]: [BleepingComputer: VLC, 7-Zip, CCleaner, Rufus için sahte Google reklamları](https://www.bleepingcomputer.com/news/security/hackers-push-malware-via-google-search-ads-for-vlc-7-zip-ccleaner/)
[^7]: [Technopat: Rufus ve GPT/MBR](https://www.technopat.net/sosyal/konu/rufus-yuzunden-format-atamiyorum.1124998/)
