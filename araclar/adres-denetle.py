#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rehberdeki bütün bağlantıları yoklar. Ek paket gerekmez.

Kullanım:
    python araclar/adres-denetle.py

Çıkış kodu 1 ise en az bir bağlantı ölüdür (404, 410, 5xx ya da alan adı yok).
401, 403, 406 ve 429 yanıtları çoğu zaman robot engelidir; ayrı listelenir ve
tarayıcıdan elle bakılır.
"""
import concurrent.futures
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

KOK = pathlib.Path(__file__).resolve().parent.parent
TARAYICI = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
BAGLANTI = re.compile(r"\]\((https?://[^)\s]+)\)")
ATLA = ("/issues/new",)          # giriş isteyen sayfalar
ENGEL = (401, 403, 406, 429)     # çoğu zaman robot engeli


def topla():
    adresler = {}
    for dosya in sorted(KOK.rglob("*.md")):
        if ".git" in dosya.parts:
            continue
        for adres in BAGLANTI.findall(dosya.read_text(encoding="utf-8")):
            if any(parca in adres for parca in ATLA):
                continue
            adresler.setdefault(adres, []).append(dosya.relative_to(KOK).as_posix())
    return adresler


def yokla(adres):
    istek = urllib.request.Request(adres, headers={
        "User-Agent": TARAYICI,
        "Accept": "*/*",
        "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
    })
    try:
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            return yanit.status, yanit.geturl()
    except urllib.error.HTTPError as hata:
        return hata.code, hata.geturl()
    except Exception as hata:  # alan adı yok, zaman aşımı, sertifika
        return 0, str(hata)


def alan(adres):
    ad = urllib.parse.urlsplit(adres).hostname or ""
    return ad[4:] if ad.startswith("www.") else ad


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    adresler = topla()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as havuz:
        sonuc = dict(zip(adresler, havuz.map(yokla, adresler)))

    olu, engel, yonlenen = [], [], []
    for adres, (kod, son) in sonuc.items():
        if kod in ENGEL:
            engel.append((kod, adres))
        elif kod == 0 or kod >= 400:
            olu.append((kod, adres, son))
        elif alan(son) != alan(adres):
            yonlenen.append((adres, son))

    saglam = len(sonuc) - len(olu) - len(engel)
    print("%d bağlantı yoklandı: %d sağlam, %d robot engeli, %d ölü" % (len(sonuc), saglam, len(engel), len(olu)))
    if yonlenen:
        print("\nBaşka bir alan adına yönlenenler (adres değişmiş olabilir, elle bak):")
        for adres, son in yonlenen:
            print("  %s\n    -> %s" % (adres, son))
    if engel:
        print("\nRobot engeli olabilir (tarayıcıdan elle bak):")
        for kod, adres in engel:
            print("  %d  %s  [%s]" % (kod, adres, ", ".join(adresler[adres])))
    if olu:
        print("\nÖLÜ BAĞLANTILAR:")
        for kod, adres, son in olu:
            print("  %s  %s  [%s]" % (kod or "bağlanamadı", adres, ", ".join(adresler[adres])))
            if kod == 0:
                print("      %s" % son)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
