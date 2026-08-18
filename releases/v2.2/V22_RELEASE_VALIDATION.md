# OYUN v2.2 - Release Doğrulama Raporu

**Tarih:** 18 Ağustos 2026  
**Sonuç:** PASS  
**Sürüm:** v2.2 stabil prototip

## Çekirdek doğrulama

```text
SONUC: PASS
- v2.2 stabil prototip / v2.1 baseline sözleşmesi doğru.
- 118 kart kimliği ve v2.1 kanonik kart karması miras yoluyla kilitli.
- Gövde 2; dinamik başlangıç; 1/2 Geçilmez Kayalık; Kaptan omurgası doğru.
- Acil geri dönüş yalnız Kayalık kaynaklı tam çıkmaz koşuluna bağlı.
GEOMETRY_AUDIT: {"invalid": 102, "invalid_by_shape": {"5x5": 0, "5x6": 0, "5x7": 20, "6x5": 8, "6x6": 50, "6x7": 24}, "legal": 51102, "total": 51204}
```

## PDF kontrolleri

- Kural kitabı: **32 sayfa**; tüm sayfalar render edilip iki temas sayfası üzerinden görsel tarandı.
- Kart PDF: **32 sayfa**; tüm sayfalar render edilip görsel tarandı. Sayfa 2-32 metin ve sayfa ölçüsü baseline kart PDF ile birebir eşleşiyor; yalnız kapak v2.2 olarak yenilendi.
- Geçilmez Kayalık işaretleri: **1 sayfa**, 12 kesilebilir işaret; Türkçe glifler ve kesim çizgileri görsel olarak kontrol edildi.
- Üç PDF de açılabilir, şifresiz ve A4 boyutundadır.
- Release PDF'lerinde görünür `v2.1` ibaresi yoktur.
- Siyah kare / bozuk Türkçe glif sorunu yoktur.

## Kaynak -> PDF kural çapraz kontrolü

Aşağıdaki v2.2 omurga hükümleri kural kitabı PDF metninde doğrulandı:

- [x] kaptan rolü oyunun kalıcı omurgasıdır ve kaldırılmaz
- [x] ilk rotayı kaptan tek başına ve olay bilgisi olmadan seçer
- [x] başarılı isyan
- [x] kaptanın ölümü
- [x] 2 gövdeyle başlar
- [x] herhangi bir sütun hizasında
- [x] geçilmez kayalık
- [x] acil geri dönüş

## Kart bütünlüğü

- 118 kart kimliği v2.1 kanonik kart karması üzerinden makine spec'inde kilitlidir.
- Kart içerikleri v2.2'de değiştirilmedi.
- v2.2 Kart PDF sayfa 2-32 baseline ile eşleşme: **PASS**.
- Geçilmez Kayalık kart değildir; ayrı fiziksel işarettir.

## Geçilmez Kayalık teknik kanıtı

- 51.204 teori/geometri yerleşimi.
- 51.102 yasal; 102 kurulum baştan reddedilir.
- 15.000 yeni-kural davranışsal oyun + 6.000 kontrol.
- Kalıcı rota kilidi: 0.
- Temsilî Tayfa ortalaması: %54,8.
- Acil geri dönüş yaklaşık %4,2 oyunda.

## Hüküm

**PASS - v2.2 `releases/v2.2/` altında stabil prototip olarak kilitlenebilir.**

Bu sürüm hâlâ kör masa testi prototipidir; "stabil" ifadesi proje sürümünün dondurulduğunu belirtir, oyunun ticari/final baskı olduğu anlamına gelmez.
