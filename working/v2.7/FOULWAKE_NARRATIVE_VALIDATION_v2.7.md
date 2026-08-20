# FOULWAKE v2.7 - Anlatı / Mekanik Sınır Doğrulaması

**Durum:** RECORDED PASS / REPRODUCTION PENDING — DRAFT / NOT LOCKED  
**Tarih:** 20 Ağustos 2026  
**Kaynak:** v2.6 STABLE / LOCKED ve doğrulanmış v2.5 mekanik kart JSON'u  
**Release kapısı:** `QA-001 OPEN`

## Kanıt sınırı

Bu dosya önceki karşılaştırmanın kayda alınmış sonucudur. Karşılaştırmayı çalıştıran
script, sabit baseline JSON'u, komut ve ham çıktı hashleri güncel GitHub ağacında
bulunmadığı için sonuç bağımsız olarak yeniden üretilemez. Bu kayıt üretim metni
değildir ve exact candidate'a bağlı Simülasyon attestation'ı oluşmadan bağlayıcı
release `PASS` sayılmaz.

## Kapsam

- Kural kitabının bölüm akışı korundu.
- Yalnız `3.1`, `3.3`, `3.4` anlatı notu, `3.6` ve `17. Siyah Mühür` hikâye katmanı güncellendi.
- Karakter ve Güç kartlarında yalnız görünen ad/flavor alanları güncellendi.
- Harita, Sadakat, Çürümüş Erzak ve yardımcı kartlar değiştirilmedi.

## Kayda alınmış kart karşılaştırması

| Denetim | Sonuç |
|---|---|
| Karakter sayısı | 20 / PASS |
| Güç sayısı | 30 / PASS |
| Karakter kimlikleri | 20 benzersiz, baseline ile aynı / PASS |
| Güç kimlikleri | 30 benzersiz, baseline ile aynı / PASS |
| Karakter `effect` alanları | Birebir aynı / PASS |
| Güç `effect` alanları | Birebir aynı / PASS |
| Zamanlama, grup, başlangıç havuzu ve desteye dönüş alanları | Birebir aynı / PASS |
| Yeni veya silinen kart | Yok / PASS |

## Bilinçli metin güncellemeleri

Karakter flavor alanı:

- `KAR-14` Fare Nazırı
- `KAR-18` Karayı Özleyen

Güç kartı görünen adı:

- `GUC-01A/B` Can Simidi -> Mantar Can Halkası

Güç kartı flavor alanı:

- `GUC-01A/B`
- `GUC-06`
- `GUC-15`
- `GUC-20`
- `GUC-24`
- `GUC-25`

## Mekanik bütünlük sonucu

Kaptan, rota oylaması, Sadakat, Hain tanışması, Ufuk bilgisi, İskorbüt, kurtarma, Gövde hasarı, Güç destesi ve Liman Gecesi mekanikleri değişmemiştir. `Mantar Can Halkası` yalnız görünen ad güncellemesidir; `GUC-01A/B` etkisi ve iki kartlık adedi aynıdır.

v2.6 `releases/v2.6/` ağacı yerinde değiştirilmemiştir. Bu çalışma yalnız `working/v2.7/` altında tutulur ve kullanıcı açıkça kilitlemeden STABLE / LOCKED olamaz.

`QA-001` ancak sürümlü karşılaştırma scripti, sabit baseline, çalıştırma komutu,
ham çıktı ve SHA-256 kayıtları exact candidate'a bağlandığında kapanır.

