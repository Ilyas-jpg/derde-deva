[Derde Deva](../README.md) › Dert 10 / 12

# “Ucuza 2 TB flaş bellek aldım”

*Bilgisayar “2 TB” diyor, dosyalar kopyalanıyor. Birkaç hafta sonra videoların yarısı açılmıyor.*

## Aslında ne oluyor?

Sahte belleğin içinde örneğin 32 GB'lık ucuz bir çip vardır ama bilgisayara kendini 2 TB diye tanıtır. Gerçek kapasite dolunca yeni dosyaları eskilerin üstüne yazmaya başlar. Hiçbir hata vermez. Fotoğraflar küçük önizlemede düzgün görünür, açınca gri çıkar; videonun ilk dakikaları oynar, sonrası bozuktur.

## Birkaç dakikalık test

1. **ValiDrive**'ı ([grc.com](https://www.grc.com/validrive.htm), ücretsiz) aç, belleği seç. Belleğin farklı yerlerine küçük denemeler yazıp okur; birkaç dakikada gerçek kapasiteyi söyler.
2. Kesin sonuç için **H2testw** belleği baştan sona doldurup geri okur. Uzun sürer ama yanılmaz. İkisi de bellekteki verileri silebilir; önce yedek al.
3. Yeni aldığın SSD için **CrystalDiskInfo** ([crystalmark.info](https://crystalmark.info/en/software/crystaldiskinfo/)): yeni sürümleri sahte Samsung SSD'leri yakalayıp ekranda **[FAKE]** yazıyor.[^12]

> **Bunu çoğu kişi bilmiyor**
>
> Sahte bellek ilk gün hiçbir sorun çıkarmaz; dosyalar kopyalanır, açılır. Sorun aylar sonra, kapasite dolduğunda başlar. O yüzden test, belleği alır almaz, içine bir şey koymadan yapılmalı.

## Bu sayfadaki resmî adresler

Programı indirirken tarayıcının adres çubuğunda yazan, buradakiyle harfi harfine aynı olmalı.

- ValiDrive: [grc.com/validrive.htm](https://www.grc.com/validrive.htm)
- H2testw: [heise.de/download/product/h2testw-50539](https://www.heise.de/download/product/h2testw-50539)
- CrystalDiskInfo: [crystalmark.info](https://crystalmark.info/en/software/crystaldiskinfo/)

---

Bu sayfadaki bağlantılar en son 15 Kasım 2026'da denetlendi. Yanlış, eksik ya da eskimiş bir şey gördüysen [bildir](https://github.com/Ilyas-jpg/derde-deva/issues/new/choose).

[← Önceki dert](09-yanlislikla-sildim.md) · [Bütün dertler](../README.md#dertler) · [Sonraki dert →](11-yedek.md)

## Kaynaklar

[^12]: [Tom's Hardware: CrystalDiskInfo [FAKE] uyarısı](https://www.tomshardware.com/pc-components/ssds/fake-samsung-ssd-spotting-comes-to-crystaldiskinfo-as-ai-crunch-drives-sophisticated-counterfeit-market-free-open-source-software-can-flag-clones-by-checking-firmware-pci-vendor-id)
