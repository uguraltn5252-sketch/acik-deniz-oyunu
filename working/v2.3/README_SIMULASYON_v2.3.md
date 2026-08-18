# OYUN v2.3 - Geliştirme / Gizli Geçilmez Kayalık

Bu klasör v2.2 stabil prototipten sonra açılan v2.3 çalışma hattıdır.

## En önemli fark

Geçilmez Kayalıklar artık ayrı işaret değildir. İki tanesi mevcut **52 Harita kartının**, **12 Kayalık kartının** içindedir. Kategori yüzleri diğer Kayalıklarla aynıdır ve açılmadan ayırt edilemez.

Kanonik kartlar:
- `HAR-KY-01` Duvar Gibi Kayalık
- `HAR-KY-03` Yolun Bittiği Yer

## Çalıştırma

```bash
python oyun_simulasyon_v2_3.py --validate-only --geometry-audit
```

Beklenen sonuç: `V2.3 DOĞRULAMA OK`.

## Test durumu

- statik/kart sözleşmesi: PASS
- kesin geometri: PASS
- 7.200 kart-çifti karşılaştırması: PASS
- 6.000 temsilî davranış testi: PASS
- 9.000 tam oyuncu/süre duyarlılığı: PASS
- PDF görsel kontrol: PASS
- insan masa testi: BEKLİYOR

Bu nedenle v2.3 henüz stabil release değildir; v2.2 stabil geri dönüş noktası olarak korunur.
