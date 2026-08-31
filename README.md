# Açık Deniz / FOULWAKE

Bu repository oyunun kalıcı, sürümlü ve denetlenebilir kaynak kaydıdır.

## Kanonik durum

- Son kullanıcı-onaylı sürüm: **v2.6 STABLE / LOCKED**
- Kilitli kaynak: `releases/v2.6/`
- Exact locked tree:
  `efb41c46f06174c42dcdab2859b7c0ba517f86f0`
- Aktif çalışma: **v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED**
- Entegrasyon dalı: `v2.7-design`
- Aktif v2.7 visual candidate: **YOK**
- Tam 121, Simülasyon, PDF, release ve lock: **YETKİSİZ**

## Tek güncel görev kaynağı

`governance/CURRENT_STAGE.json`, mevcut aşama ve yazma yetkisi için tek
makine-okunur kaynaktır. Eski iş emirleri, PASS kayıtları ve specialist
commitleri tarihsel kanıttır; kendi başına yeni iş başlatamaz.

Güncel aşama:
`STAGE-20260830-KAPTAN-FRAMING-PATCH-CORRECTION`.

Yalnız Sanat Yönetimi dalında, exact KAPTAN patch dosyasının tek dosya /
en fazla 700 kelimelik düzeltmesi yetkilidir. Hikâye, Görsel ve Simülasyon
yazmaya kapalıdır.

## Proje sahibi KAPTAN hükmü

Yüklenen KAPTAN kartı `SET-KP-01` için bağlayıcı ana görsel ve copy kaynağıdır:

- Başlık: **KAPTAN**
- Bölüm: **ÖZEL YETENEK**
- Etki: **Oylamada eşitlik olursa, senin tarafın geçerli olur.**
- Flavor: **Lidere et. Gemi senin emrinde.**
- Görsel:
  `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`

KAPTAN figürü ve ana kompozisyonu yalnız küçük crop/ölçek/renk/arka-plan
düzeltmesiyle korunur. Gemi ve martı diğer kartlarda zorunlu değildir.
Exact copy:
`working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json`.

Görsel model kart yazısı üretmez; copy şablonla yerleştirilir ve OCR veya
render-source karşılaştırması gerekir. Bütün kartlar bağımsız Sanat Yönetimi
kadraj kapısından geçer.

## Arka yüz düzeltmeleri

- `BACK_SEA_ROCK`: mat, ışıldamayan deniz.
- `BACK_ISLAND`: önceki varlıktan türetilmeden FULL REDRAW.
- `BACK_LIGHTHOUSE`: daha büyük fener; uzun kayalık sırt zorunlu değil.
- Diğer dört arka: HOLD; proje sahibi kabulü yok.

## Çalışmaya başlamadan

1. `AI_HANDOFF.md`
2. `governance/CURRENT_STAGE.json`
3. `PROJECT_STATE.md`
4. `governance/WORKSTREAM_PROTOCOL.md`
5. `governance/WORKSTREAM_SCOPE_BASELINES.json`
6. İlgili exact kaynak ve iş emri

Uzman değişiklikleri reset baseline'dan sonraki cumulative diff ile denetlenir.
Exact güncel yetki yoksa CI yazmayı reddeder.

## Açık kritik konular

- `SRC-002`: v2.6 `GUC-22 = Bayat Peksimet`; v2.7 `GUC-22 = Kaptanın Çatlak
  Kupası` ve `GUC-23 = Bayat Peksimet`. Proje sahibi kararı gerekir:
  `governance/SRC_002_COMPARISON_20260830.json`.
- `GOV-001`: GitHub branch protection/ruleset mevcut plan/visibility altında
  etkinleştirilemiyor. CI doğrudan pushları denetler fakat platform düzeyinde
  pushu önceden engelleyemez.
- Fiziksel baskı, kesim, duplex, opaklık, ışık ve gerçek masa-mesafesi kanıtı yok.

## v2.6 artefaktları

Kural kitabı, kart PDF'i, release manifesti ve SHA-256 kayıtları
`releases/v2.6/` içindedir. v2.6 yerinde değiştirilmez; sonraki kararlar yalnız
v2.7+ DRAFT içinde uygulanır.
