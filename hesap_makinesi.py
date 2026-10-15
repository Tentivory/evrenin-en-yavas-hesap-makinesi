#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Yavaş Hesap Makinesi
Her işlem için abartılı derecede düşünür, çay içer, felsefe yapar.
"""

import time
import random
import re

def dusun(mesaj="Düşünüyorum..."):
    print(mesaj)
    bekleme = random.uniform(1.5, 4.0)
    time.sleep(bekleme)

def hesapla(ifade):
    # Basit ifadeleri destekle: sayı + sayı, * , - , /
    ifade = ifade.strip()
    match = re.match(r"(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)", ifade)
    if not match:
        dusun("Bu ifade... çok karmaşık geldi. Belki bir fincan çay sonra tekrar denerim.")
        return None
    
    a = float(match.group(1))
    op = match.group(2)
    b = float(match.group(3))
    
    dusun("İşlem anlaşıldı. Şimdi derin bir nefes alıyorum...")
    dusun("Çay demleniyor... (hayali)")
    dusun("Evrenin derinliklerinde bu işlemin anlamını sorguluyorum...")
    
    if op == "+":
        sonuc = a + b
    elif op == "-":
        sonuc = a - b
    elif op == "*":
        sonuc = a * b
    elif op == "/":
        if b == 0:
            dusun("Sıfıra bölme... felsefi bir kriz!")
            return "Sonsuzluk (veya hata, hangisini tercih ederseniz)"
        sonuc = a / b
    else:
        return None
    
    dusun("Sonuç bulundu. Dramatik bir şekilde açıklamaya hazırlanıyorum...")
    time.sleep(1)
    return sonuc

def main():
    print("=" * 50)
    print("   EVRENİN EN YAVAŞ HESAP MAKİNESİ")
    print("   (Ciddiye alın. Ama çok da değil.)")
    print("=" * 50)
    print("\nBir işlem girin (örnek: 5 + 3, 10 * 2, 8 / 4). Çıkmak için 'q' yazın.\n")
    
    while True:
        try:
            ifade = input("📝 İşlem: ").strip()
            if ifade.lower() in ["q", "quit", "çık", "exit"]:
                print("\nHesap makinesi emekliye ayrılıyor. Yavaş yavaş...")
                time.sleep(2)
                print("Elveda.")
                break
            
            if not ifade:
                continue
                
            sonuc = hesapla(ifade)
            if sonuc is not None:
                print(f"\n✨ SONUÇ: {sonuc} ✨")
                print("(Bu sonucu elde etmek için evren bir an durdu. Tebrikler.)\n")
            else:
                print("\n❌ Bu işlemi çözemedim. Belki daha basit bir şey deneyin.\n")
                
        except KeyboardInterrupt:
            print("\n\nAniden kesildi. Hesap makinesi şokta.")
            break
        except Exception as e:
            print(f"\nBir şeyler ters gitti: {e}. Ama yavaşça.")

if __name__ == "__main__":
    main()
