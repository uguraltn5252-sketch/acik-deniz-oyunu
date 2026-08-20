# v2.7 Draft Binary Artifacts

**Durum:** **FULL VISUAL DIGITAL CANDIDATE / DRAFT / NOT LOCKED**  
**Mekanik baseline:** v2.6 STABLE / LOCKED  
**Çalışma dalı:** `work/v2.7-visual`  
**Tam üretim taban commit:** `031c2a4d87ce7fc80d3c443723630e80f2388a70`  
**Tam üretim teslim commit:** `PENDING_FULL_PRODUCTION_COMMIT`

GitHub deposunda büyük binary dosyaların kendileri yerine kanonik yol, Library
kimliği, sürüm, byte boyutu ve SHA-256 kayıtları tutulur. Aşağıdaki dört güncel
kayıt yalnız dosyalar kanonik `/Oyun-GitHub/v2.7/exports/` konumuna
kaydedildikten sonra geri indirilen baytlardan hesaplanmıştır. Geri indirilen
dosyalar yerel authored adaylarla 4/4 byte-bayt eşleşmiştir.

## Tam görsel üretim adayı

- Tam deste baskı adayı: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_FULL_DECK_PRINT_CANDIDATE.pdf`  
  Library file: `libfile_9a53fef0e28c8191b62eb09c56cb8c1f`, version `2`  
  File id: `file_00000000d7a081fdbfb19ac1f4daa3e6`  
  SHA-256: `09d3bb00b198426f749698744bfda8c5d11ccaca5a29f71072f3e47162c6afa4`  
  Boyut: `152036797` byte  
  Sayfa: `48` A4; 24 ön/arka duplex yaprağı; 121 kart.

- Tam deste görsel inceleme adayı: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_FULL_DECK_VISUAL_REVIEW.pdf`  
  Library file: `libfile_805a250bf34481919db90a099011b450`, version `2`  
  File id: `file_00000000b9bc81fda46bd93a94d69869`  
  SHA-256: `a0b788b0e16c969b326869a5e21ee87e9772b1682735084e0ee475a2d3fe0ebb`  
  Boyut: `189584635` byte  
  Sayfa: `16` yatay A4; 121 ön yüzün görsel taraması.

- Tam deste kaynak paketi: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_FULL_DECK_SOURCE_BUNDLE.zip`  
  Library file: `libfile_e453647b8ba88191922a7512dd2c1640`, version `3`  
  File id: `file_00000000d92c81fbb1bef534fdd2762e`  
  SHA-256: `4d9f902fb73497ba48a43c0085a09d65b08aaf6b9defe69b8471fef10fe21ac8`  
  Boyut: `163319630` byte  
  İçerik: 121 ön yüz, 7 arka yüz, 6 özgün aile illüstrasyon plakası,
  kaynak/üretim dosyaları ve manifestler; toplam `139` arşiv girdisi. Paket
  içindeki Card Texts ve Rulebook Story baytları bağlayıcı Git bloblarıyla exact
  eşleşir.

- Güncel v2.7 kural kitabı baskı adayı: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_RULEBOOK_PRINT_CANDIDATE.pdf`  
  Library file: `libfile_e75c184fe0588191b9cb6ae37c8ed2d7`, version `0`  
  File id: `file_0000000004208230bc59a423b9c6d678`  
  SHA-256: `00344a95563558f04c02465bf164538652c3bbab616a40e8083bf2c1862ad1fb`  
  Boyut: `37533254` byte  
  Sayfa: `29` A4; v2.7 anlatı kaynağı
  `f1e0eb75434540a85e8b21484acd99ca0abc66cf` ile bağlı.

## İzlenebilirlik kayıtları

- `working/v2.7/visual/manifests/FOULWAKE_CARD_INVENTORY_v2.7.json`:
  121 kartın kimlik, kaynak, ölçü ve arka yüz envanteri.
- `working/v2.7/visual/manifests/FOULWAKE_v2.7_121_SOURCE_RENDER_PDF_MAP.json`:
  121/121 source → render SHA-256 → PDF ön/arka sayfa/slot zinciri.
- `working/v2.7/visual/manifests/FOULWAKE_v2.7_FULL_PRODUCTION_PROVENANCE.json`:
  kanonik Library kimlikleri, geri indirilmiş byte/hash değerleri ve commit
  ayrımı.
- `working/v2.7/visual/manifests/FOULWAKE_v2.7_FULL_PRODUCTION_PREFLIGHT.json`:
  dijital preflight sonuçları ve açık fiziksel riskler.

## Bağlayıcı kaynaklar ve korunan hükümler

- Card Texts blob: `38a03b71cd3232fd844db8d80d8e53662510b6a3`
- Rulebook Story blob: `f1e0eb75434540a85e8b21484acd99ca0abc66cf`
- Kilitli v2.6 kart PDF SHA-256:
  `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298`
- `GUC-22 = Kaptanın Çatlak Kupası`; `GUC-23 = Bayat Peksimet`.
- `GUC-24` flavor exact kaynağa bağlıdır: “Güverte kâtibi bunu yanlış elde
  duran doğru eşya diye kaydetti.”
- Açık Deniz ve Kayalık toplam 42 kart, aynı metinsiz binary
  `BACK_SEA_ROCK` varlığına eşlenmiştir.

Metin, mekanik, zamanlama, kart kimliği/adedi, deste davranışı ve lore hükmü
üretilmemiş veya değiştirilmemiştir. Kilitli v2.6 dosyaları ve
`releases/**`, `governance/**`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, `main`
alanları değiştirilmemiştir.

## Dijital sonuç ve açık fiziksel riskler

Dijital preflight sonucu `PASS_WITH_OCR_SOFT_WARNING`dır. 121/121 kart, 7 arka
yüz, 48 sayfalık duplex PDF ve 29 sayfalık kural kitabı yapısal olarak geçti.
Temsilî OCR örnekleminde 16/16 metin bloğu okundu, 14/16 kimlik exact okundu;
İngilizce OCR exact-copy otoritesi değildir, bağlayıcı kaynak snapshotları
belirleyicidir.

Fiziksel baskı, kesim, duplex sapması, opaklık/ışık ve kör yön-sızıntı testleri
çalıştırılmadı; `PENDING_NOT_RUN` açık riski olarak kalır. Bu aday kilitli
release değildir ve Baş Editör kabulünden önce Simülasyon Testine devredilmez.

## Kilitli v2.6 kaynakları

- Kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf`  
  SHA-256: `192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a`  
  Boyut: `1104041` byte; `29` A4 sayfa.

- Tam Kart PDF: `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6.pdf`  
  SHA-256: `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298`  
  Boyut: `1768745` byte; `34` A4 sayfa.

Kilitli `releases/v2.6/` ağacı ve v2.6 binary kaynakları değiştirilmemiştir.
