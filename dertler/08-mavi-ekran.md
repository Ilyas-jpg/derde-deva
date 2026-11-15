[Derde Deva](../README.md) › Dert 8 / 12

# “Mavi ekran verdi, ne demek bu?”

*Ekran maviye dönüyor, üzgün bir surat, anlaşılmaz bir yazı, bilgisayar kendini yeniden başlatıyor.*

## Mavi ekran aslında bir ipucu bırakır

1. Mavi ekran kendiliğinden kaybolduysa sorun değil: Windows her seferinde bir kayıt bırakır. **BlueScreenView**'i ([nirsoft.net](https://www.nirsoft.net/utils/blue_screen_view.html), kurulum gerektirmez) aç; son çökmeler listelenir.
2. Her satırda çökmeye karışan dosyanın adı yazar; genelde sonu **.sys** ile biten bir isim. O ismi olduğu gibi Google'a yaz. Örneğin **nvlddmkm.sys** çıkarsa suçlu NVIDIA ekran kartı sürücüsüdür; çözüm sürücüyü tamamen kaldırıp NVIDIA'nın sitesinden yeniden kurmaktır.
3. Suçlu sürekli değişiyorsa sorun bir sürücü değil, donanım olabilir: RAM'i Başlat menüsündeki “Windows Bellek Tanılama” ile test et.

> **Bunu çoğu kişi bilmiyor**
>
> Listede **ntoskrnl.exe** görürsen panik yapma: o Windows'un kalbidir, neredeyse her çökmede adı geçer ve suçlu genelde o değildir. Ona değil, yanındaki diğer dosya adına bak.

## Bu sayfadaki resmî adresler

Programı indirirken tarayıcının adres çubuğunda yazan, buradakiyle harfi harfine aynı olmalı.

- BlueScreenView: [nirsoft.net/utils/blue_screen_view.html](https://www.nirsoft.net/utils/blue_screen_view.html)
- NVIDIA sürücüleri: [nvidia.com/tr-tr/drivers](https://www.nvidia.com/tr-tr/drivers/)

---

Bu sayfadaki bağlantılar en son 15 Kasım 2026'da denetlendi. Yanlış, eksik ya da eskimiş bir şey gördüysen [bildir](https://github.com/Ilyas-jpg/derde-deva/issues/new/choose).

[← Önceki dert](07-c-diski-doldu.md) · [Bütün dertler](../README.md#dertler) · [Sonraki dert →](09-yanlislikla-sildim.md)
