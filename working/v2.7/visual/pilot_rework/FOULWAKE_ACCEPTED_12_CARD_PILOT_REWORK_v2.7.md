# FOULWAKE v2.7 — Dört Ana Görselli Hedefli Pilot Reworkü

## Sonuç

`TARGETED_PILOT_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`

Bu paket yalnız dört yetkili ana görseli ve source-art karşılıklarını yeniden çalışır; KAR-01 için üç ayrı beden geometrili yeni gate üretir, HAR-AA-06 gate'ini byte-exact korur ve bağlı pilot kanıtlarını yeniden türetir. Tam 121 ön yüz, tam kart PDF'si, Simülasyon handoff'u, release veya lock üretilmedi.

## Kaynaklar

- Baş Editör: `v2.7-design@74ac7eb764089a894b109990c1bc10304b7a614d`
- Kabul edilmiş Sanat Yönetimi: `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da`
- Sanat Yönetimi inceleme kanıtı: `governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`
- Bağlayıcı hedefli rework emri: `working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md`
- İncelenen Görsel / çalışma başlangıcı: `work/v2.7-visual@1b27232a53b09ac3ff00030f625bfc2703d15764`
- Hedefli rework teslim commit'i: `work/v2.7-visual@88907294edd326c118573f5ada7406e5fc42ee4d`
- Çalışma dalı: `work/v2.7-visual`

## Yetkili dört ana rework

- **KAR-01:** Üç yeni gate geometrisi üretildi (`OPEN_FORK`, `COMPRESSED_DIAGONAL`, `TWISTED_S_CURVE`). Finale `GATE_PANEL_1_OPEN_FORK` taşındı; sağ omuz halat yüküyle düştü, gövde armaya ağırlık verdi ve çıplak göz tek ince hardal ufuk kırılmasına bağlandı. Dürbün, işaret, kuş ve doğaüstü göz efekti yoktur.
- **HAR-AA-06:** Mevcut gate byte-exact korundu. `GATE_PANEL_2_OVERHEAD_CLOSED_BASKET` yönü seçildi; el doğrudan kapak aralığına gider, fazla nesne dar aralıktan geçerken görünür, sepet içi görünmez ve masa üstü tartım/inceleme puku kaldırılmıştır.
- **BACK_ISLAND:** Asimetrik alçak kara omurgası kullanıldı; köpük yalnız iki küçük kesintili bölgede kalır ve deniz dört kenara sürer. Halo/sticker/karo etkisi yoktur.
- **BACK_LIGHTHOUSE:** Küçük sade çokgen yığma-taş kule alçak çapraz kaya sırtına gömülüdür. Dairesel islet, konsantrik surf, hedef/rozet, ışın, glow, halka, yuvarlak lens ve modern beacon yoktur.

## Byte-exact KEEP

- 10 korunmuş ön: KAR-06, KAR-19, GUC-06, GUC-27, ERZ-01, SAD-H-03, HAR-AD-08, HAR-KY-06, HAR-FN-04, SET-KP-01.
- 5 korunmuş arka: BACK_CHARACTER, BACK_POWER, BACK_LOYALTY, BACK_SEA_ROCK, BACK_SUPPORT.
- KAR-01 dışındaki 9 sketch gate, HAR-AA-06 dahil, byte-exact korunmuştur.
- Paket içindeki 13 bağlı KEEP source-art dosyası byte-exact korunmuştur.

## Yeniden türetilen kanıt

- 5/5 contact sheet.
- 6/6 map-layout rasterı: COMPACT_CLUSTER, ELONGATED_ROUTE ve IRREGULAR_BRANCH; kapalı/kısmen açık durumlar.
- Aynı kart hücreleri, kimlikler, açık-yüz 180° yönleri ve üç geometri korunmuştur.
- Dört target master sonrasında source→render→contact-sheet/map-layout SHA-256 ilişkileri yeniden kaydedilmiştir.

## Dijital preflight

- 12/12 exact görünür metin; değişen önlerde illüstrasyon penceresi dışındaki frame/metin pikselleri exact korunmuştur.
- 7/7 arka yüz 300 dpi ve piksel düzeyinde exact 180° eşitliği; eşleme toplamı 121.
- Ada/Fener denizi dört kenarda BACK_SEA_ROCK değer/çizgi zarfına bağlıdır.
- Hedef dört source-art için Tesseract çıktısı boştur; manuel görsel incelemede okunabilir yazı/glyph yoktur.
- 5 contact sheet ile 6 map-layout görsel olarak açılmış; kimlik, konum, yön ve geometri korunumu doğrulanmıştır.
- SHA-256 kaydı checksum dosyasının kendisi hariç 61/61 dosyayı kapsar; `.writing.png=0`.
- `CHANGED_FILES=25`; kapsam dışı ana KEEP veya gate değişmemiştir.

## Açık riskler

- Project Owner, Sanat Yönetimi ve Baş Editör estetik kabulü henüz verilmedi.
- Fiziksel baskı, kesim, duplex, ışık ve normal masa-mesafesi testleri çalıştırılmadı; PASS sayılmadı.
- SRC-002 açıktır; tam 121 ön yüz, tam PDF ve Simülasyon blokludur.

`TEMPORARY_SUBAGENTS: NONE`  
`LOCK_REQUESTED: NO`
