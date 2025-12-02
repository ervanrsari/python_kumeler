# Proje Sahibi: [Ervanur Sarı]
# Tarih: 30.11.2025
# Konu: Kümelerle Temel İşlemler Projesi



import json
import time

def kume_islemleri():
    print("--- Kümelerle Temel İşlemler Projesi ---")
    
    
    dosya_adi = input("Lütfen JSON dosyasının adını girin (örneğin: veri.json): ")

    try:
    
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            veri = json.load(f)
        
    
        liste1 = veri.get("liste1", [])
        liste2 = veri.get("liste2", [])
        
        kume1 = set(liste1)
        kume2 = set(liste2)
        
        print(f"\nDosya başarıyla okundu.")
        print(f"Küme 1: {kume1}")
        print(f"Küme 2: {kume2}\n")

        sonuclar = {}

    
        baslangic = time.perf_counter()
        birlesim = kume1.union(kume2)
        bitis = time.perf_counter()
        sonuclar["birlesim"] = list(birlesim)
        sonuclar["birlesim_suresi"] = f"{bitis - baslangic:.10f} saniye"

    
        baslangic = time.perf_counter()
        kesisim = kume1.intersection(kume2)
        bitis = time.perf_counter()
        sonuclar["kesisim"] = list(kesisim)
        sonuclar["kesisim_suresi"] = f"{bitis - baslangic:.10f} saniye"

    
        baslangic = time.perf_counter()
        fark1 = kume1.difference(kume2) 
        bitis = time.perf_counter()
        sonuclar["fark_kume1_kume2"] = list(fark1)
        sonuclar["fark_kume1_suresi"] = f"{bitis - baslangic:.10f} saniye"

    
        cikti_dosyasi = "sonuc.json"
        with open(cikti_dosyasi, 'w', encoding='utf-8') as f:
            json.dump(sonuclar, f, indent=4, ensure_ascii=False)

        print("İşlemler tamamlandı!")
        print(f"Sonuçlar ve süreler '{cikti_dosyasi}' dosyasına kaydedildi.")

    except FileNotFoundError:
        print("HATA: Dosya bulunamadı! 'veri.json' yazdığından emin misin?")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    kume_islemleri()