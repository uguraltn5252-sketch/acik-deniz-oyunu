# FOULWAKE v2.7 — DRAFT WORKSPACE

**Durum:** DRAFT / NOT LOCKED

Bu çalışma alanı, kilitli **v2.6 STABLE / LOCKED** sürümünü yerinde değiştirmeden FOULWAKE'ın yeni görsel üretim hattını yürütür.

## Kaynakların görev ayrımı

- **GitHub = kanonik oyun içeriği ve sürüm kontrolü.** Kart kimlikleri, adları, kuralları, etkileri, adetleri, oyun mekaniği, değişiklik kayıtları, testler ve onaylı exportlar burada tutulur.
- **Figma = kanonik görsel üretim kaynağı.** Kart component'leri, illüstrasyon yerleşimleri, tipografi, renk değişkenleri, bleed/safe-area, arka yüzler, kural kitabı sayfa sistemi ve baskı düzeni burada tutulur.

## Çalışma yönü

`v2.6 STABLE / LOCKED -> v2.7-design GitHub branch -> Figma tasarım -> test/onay -> Figma export -> GitHub working/v2.7 -> doğrulama -> kullanıcı onayı -> v2.7 STABLE / LOCKED`

## Değişiklik kuralı

- Mekanik veya kart içeriği değişikliği: **önce GitHub**, sonra Figma senkronu.
- Yalnız görsel değişiklik: **Figma'da yapılır**, onaylanan export GitHub'a alınır.
- Aynı mekanik metin iki yerde bağımsız elle yönetilmez.
- `releases/v2.6/` ve v2.6 binary artefaktları değiştirilemez.

## Figma

- Dosya: `FOULWAKE v2.7 DESIGN SYSTEM`
- URL: https://www.figma.com/design/LOJtIBKKfN2KVGx8wD6rU9

## İlk hedefler

1. v2.6 kart/veri içeriğini v2.7 için yapılandırılmış kanonik veri setine çıkarmak.
2. MASTER görsel tasarım standardını Figma design system'e kurmak.
3. Character / Power / Loyalty / Map / Support master component'lerini üretmek.
4. Kart arka yüz ailelerini kurmak.
5. Kural kitabını aynı görsel evren içinde yeniden tasarlamak.
6. Gerçek boy print test ve table test yapmak.
7. Onaylanan PDF/SVG/PNG exportları GitHub'a almak.
