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
- **Önemli sınır:** Test yeni dinamik alt-kenar başlangıç kuralını içermez; Gövde baskısının yönünü ölçen eski duyarlılık testidir.
- **Sonuç:** 3 Gövde birçok hücrede Tayfayı aşırı güçlendirdi.
- **Son karar:** Kullanıcı daha sonra bütün Haritalarda **2 Gövde**yi kesinleştirdi. Bu nedenle T-003'teki `5×7 = 3 Gövde` önerisi **geçersiz/superseded** kabul edilir; yeni sürüme taşınmayacaktır.

## T-20260818-004 — 1/2 Geçilmez Kayalık + yalnız Kayalık çıkmazında acil geri dönüş

- **Motor:** `experiments/gecilmez_kayalik_v22_sim.py`; temel davranışsal motor `tam_sistem_sim.py`.
- **Kesin kurallar:** 2 Gövde; dinamik alt-kenar başlangıcı; Kaptan ilk rotayı tek başına seçer; 30 kareye kadar 1, 35+ karede 2 Geçilmez Kayalık; son Harita satırında Kayalık yok; yalnız Kayalık kaynaklı tam ileri çıkmazda bir önceki kareye tek adım geri; geri hareket günü tüketir; açık kart olayı tekrarlanmaz.

### A. Kesin geometri

Altı Harita boyunda toplam **51.204** teorik başlangıç/Liman/Kayalık yerleşimi tarandı.

- İleri yol bırakan: **51.102 (%99,80)**
- Baştan çözümsüz: **102**
- İlk hareketi tamamen kapatan: **36**

Bu 102 kurulum oyun kurulurken reddedilmelidir. Geri dönüş kuralı, baştan çözümsüz Haritayı meşrulaştırmaz.

### B. Temsilî 1.000 + 1.000 karşılaştırmaları

Her Harita boyunda orta oyuncu sayısı için 1.000 kontrol ve 1.000 yeni-kural oyunu:

| Harita | Oyuncu | Kontrol Tayfa | Yeni Tayfa | Fark | Geri dönüş oyunu |
|---|---:|---:|---:|---:|---:|
| 5×5 | 8 | %59,3 | %56,6 | -2,7 puan | %2,8 |
| 5×6 | 8 | %57,2 | %54,3 | -2,9 | %3,7 |
| 5×7 | 8 | %57,0 | %52,0 | -5,0 | %4,2 |
| 6×5 | 13 | %60,8 | %56,6 | -4,2 | %3,2 |
| 6×6 | 13 | %58,7 | %52,9 | -5,8 | %6,0 |
| 6×7 | 13 | %55,3 | %56,3 | +1,0 | %5,3 |

Ortalama yeni-kural Tayfa zaferi **%54,8**; kontrole göre değişim **-3,3 yüzde puanı**. Ortalama yolculuk **+0,12 gün**, gece **+0,09**, tahmini masa süresi yaklaşık **+0,70 dakika**. Geri dönüş yaklaşık **%4,2** oyunda görüldü.

### C. 6–15 oyuncu tam duyarlılık taraması

30 oyuncu/süre hücresinde `300` oyun = **9.000 yeni-kural oyunu** çalıştırıldı. Harita boyu ortalamaları:

- 5×5: Tayfa %54,1; geri dönüş %4,1
- 6×5: Tayfa %54,3; geri dönüş %3,5
- 5×6: Tayfa %53,0; geri dönüş %1,7
- 6×6: Tayfa %54,9; geri dönüş %4,9
- 5×7: Tayfa %55,7; geri dönüş %3,8
- 6×7: Tayfa %58,1; geri dönüş %4,6

### D. Kilit/hata kontrolü

Toplam yeni-kural davranışsal oyun: **15.000**. Kontrol oyunları: **6.000**.

- Kalıcı `route_lock`: **0**
- Kurulum hatası: **0**
- Başlangıç kilidi: **0**

Zorunlu ek hareket (ör. Girdap) tam Kayalık çıkmazına çarparsa ek hareket boşa düşürülür; oyun kilitlenmez. Bu kenar hükmü yeni kural metninde açık yazılmalıdır.

### Hüküm

**PASS / teknik kabul.** Geçilmez Kayalık + acil geri dönüş sistemi çekirdek kurala taşınabilir. İnsan masa testi hâlâ gereklidir; sayısal test eğlenceyi kanıtlamaz.

- Ayrıntılı rapor: `docs/GECILMEZ_KAYALIK_V22_RAPOR.md`
- Deney kodu: `experiments/gecilmez_kayalik_v22_sim.py`
- Sonuç özeti: `experiments/GECILMEZ_KAYALIK_V22_SONUCLARI.csv`
