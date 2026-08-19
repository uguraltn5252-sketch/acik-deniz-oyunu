# FOULWAKE v2.7 — DRAFT WORKSPACE

**Durum:** DRAFT / NOT LOCKED

Bu çalışma alanı, kilitli **v2.6 STABLE / LOCKED** sürümünü yerinde değiştirmeden FOULWAKE'ın yeni görsel üretim hattını yürütür.

## Kaynakların görev ayrımı

- **GitHub = kanonik oyun içeriği + kanonik görsel tasarım standardı + sürüm kontrolü.** Kart kimlikleri, adları, kuralları, etkileri, adetleri, oyun mekaniği, hikâye, tasarım standardı, değişiklik kayıtları, testler ve onaylı exportlar burada tutulur.
- **Canva = ana düzenlenebilir tasarım çalışma alanı.** Kart ön/arka yüzleri, kart setleri, baskı sayfaları, kural kitabı ve görsel denemeler burada üretilebilir.
- **Adobe Express = yardımcı görsel üretim ve alternatif tasarım çalışma alanı.** Özellikle illüstrasyon varyasyonları, görsel stil denemeleri ve gerektiğinde üretim desteği için kullanılabilir.

## Çalışma yönü

`v2.6 STABLE / LOCKED -> v2.7-design GitHub branch -> Canva / Adobe Express tasarım -> test/onay -> PDF/PNG/SVG export -> GitHub working/v2.7 -> doğrulama -> kullanıcı onayı -> v2.7 STABLE / LOCKED`

## Değişiklik kuralı

- Mekanik veya kart içeriği değişikliği: **önce GitHub**, sonra tasarım dosyalarına aktarılır.
- Yalnız görsel değişiklik: **Canva veya Adobe Express'te yapılır**, onaylanan karar `DESIGN_SYSTEM_MASTER.md` ile uyumlu tutulur ve export GitHub'a alınır.
- Aynı mekanik metin iki yerde bağımsız elle yönetilmez.
- `releases/v2.6/` ve v2.6 binary artefaktları değiştirilemez.

## Kanonik görsel standart

Ana kaynak: `working/v2.7/DESIGN_SYSTEM_MASTER.md`

Bu dosya; renk, tipografi, kart ölçüleri, art direction, arka yüz politikası, hiyerarşi, mizah tonu, baskı ve test kurallarının uygulama-bağımsız kaynağıdır.

## İlk hedefler

1. v2.6 kart/veri içeriğini v2.7 için yapılandırılmış kanonik veri setine çıkarmak.
2. MASTER görsel tasarım standardını GitHub'da uygulama-bağımsız biçimde sabitlemek.
3. Canva'da Character / Power / Loyalty / Map / Support ana şablonlarını kurmak.
4. Kart arka yüz ailelerini kurmak.
5. Kural kitabını aynı görsel evren içinde yeniden tasarlamak.
6. Gerçek boy print test ve table test yapmak.
7. Onaylanan PDF/SVG/PNG exportları GitHub'a almak.
