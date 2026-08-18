# Test Log

## T-20260818-001 — v2.1 stabil paket doğrulaması

- **Komut:** `python releases/v2.1/oyun_simulasyon_v2_1.py --validate-only`
- **Sonuç:** PASS
- **Kontrol edilenler:** oyuncu/Hain/Gövde tabloları, 118 kart kimliği, kanonik kart metni karması, harita başlangıcı, Ufuk yasallığı, her Liman sütununda kurulum, manifest SHA-256, PDF bütünlüğü.
- **Not:** Bu test denge simülasyonu veya kazanma oranı üretmez.

## T-20260818-002 — Dinamik başlangıç + tek Geçilmez Kayalık erişilebilirliği

- **Yöntem:** 5×5, 5×6, 5×7, 6×5, 6×6 ve 6×7 Haritalarda bütün alt başlangıç sütunları × bütün Liman sütunları × tek bloklu kareler kesin grafik aramasıyla tarandı.
- **Hareket:** yalnız bir sonraki satıra; sütun farkı en fazla 1; Limana kalan adımla erişilemeyen kareler yasal değil.
- **Sonuç:**
  - 5×5: son satır dışındaki tek blokla yol kaybı 0.
  - 5×6: 0.
  - 5×7: 0.
  - 6×6: 0.
  - 6×7: 0.
  - 6×5: karşı uç başlangıç/Liman çiftlerinde 8 kritik blok vakası bulundu.
- **6×5 kritik örnek:** başlangıç sütun 1 → Liman sütun 6 (ve simetriği). En kısa/tek çapraz koridor üzerinde her ara satırdaki zorunlu karelerden biri bloklanırsa Limana yol kalmıyor.
- **Hüküm:** `Geçilmez Kayalık son yaklaşım satırında olamaz` kuralına ek olarak yerleştirme sonrası başlangıç→Liman erişilebilirlik doğrulaması zorunlu.

## T-20260818-003 — Harita boyuna göre 2/3 Gövde duyarlılığı

- **Motor:** Library'deki korunmuş `tam_sistem_sim.py` + `prototype_balance_sim.py`.
- **Önemli sınır:** Test henüz yeni dinamik alt-kenar başlangıç kuralını içermez. Bu nedenle nihai değil, Gövde baskısının yönünü ölçen duyarlılık testidir.

### A. Uzun Harita, mevcut uzun-harita hasar kotası

Her hücre 3.000 oyun:

| Oyuncu | Harita | Hasar kotası | 2 Gövde Tayfa | 3 Gövde Tayfa |
|---:|---|---:|---:|---:|
| 6 | 5×7 | 9 | %53,5 | %77,0 |
| 8 | 5×7 | 8 | %55,9 | %78,1 |
| 10 | 5×7 | 9 | %59,5 | %85,5 |
| 12 | 6×7 | 11 | %61,3 | %85,6 |
| 15 | 6×7 | 13 | %58,3 | %81,7 |

**Hüküm:** Haritayı yalnız uzatıp Gövdeyi 3 yapmak Hainin batırma yolunu fazla zayıflatıyor.

### B. 3 Gövde + fiziksel havuzdaki maksimum 14 hasar kartı

Aday havuz maksimumu: `9 Açık Deniz + 5 Kayalık = 14` doğrudan hasar kartı.

5×7 sonuçları:

| Oyuncu | Tayfa zaferi |
|---:|---:|
| 6 | %59,4 |
| 7 | %53,3 |
| 8 | %52,9 |
| 9 | %59,4 |
| 10 | %62,8 |

6×7 sonuçları:

| Oyuncu | Tayfa zaferi |
|---:|---:|
| 11 | %74,8 |
| 12 | %76,2 |
| 13 | %80,3 |
| 14 | %78,6 |
| 15 | %81,0 |

**Hüküm:** 3 Gövde mevcut kart havuzuyla yalnız 5×7 için gerçekçi adaydır. 6×7 çok güvenli kalır.

### C. 6×7 + 3 Gövde için gereken ek baskı

Mevcut maksimum 14 hasarın üstüne sentetik olarak hasara çevrilen kartlar test edildi. Temsilî sonuçlar:

- 12 oyuncu: +4 hasar ≈ %59,0 Tayfa; +5 ≈ %56,1.
- 15 oyuncu: +5 hasar ≈ %60,8 Tayfa.

**Hüküm:** 6×7'de 3 Gövde için toplam yaklaşık 18–19 doğrudan hasar olayı gerekir. Mevcut 52 kartlık fiziksel havuzda yalnız 14 hasar kartı bulunduğu için bu, 4–5+ kartın yeniden tasarlanmasını gerektirir.

### Öneri

- 5×5 = 2 Gövde
- 5×6 = 2 Gövde
- 5×7 = 3 Gövde **yalnız 14 hasar kartıyla**
- 6×5 = 2 Gövde
- 6×6 = 2 Gövde
- 6×7 = 2 Gövde

Bu öneri kullanıcı onayına kadar test statüsündedir.
