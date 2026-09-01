# FOULWAKE Karar Kaydı

**Durum:** ACTIVE  
**Kapsam:** v2.7 DRAFT ve sonraki çalışma hatları  
**Kilitli baseline:** v2.6 STABLE / LOCKED

Bu kayıt proje sahibinin tekrar sorulmaması gereken açık kararlarını tutar.
`APPROVED FOR DRAFT`, release veya `STABLE / LOCKED` anlamına gelmez. Daha yeni
karar daha eski kararı yalnız açıkça `SUPERSEDED` olarak işaretlendiğinde
geçersiz kılar.

| Karar | Durum | Bağlayıcı hüküm | Zorunlu kapı |
|---|---|---|---|
| `DEC-20260820-01` | APPROVED FOR v2.7 DRAFT | Açık Deniz ve Kayalık aynı metinsiz binary arka yüzü kullanır. | v2.6'yı değiştirmez; exact candidate üzerinde tam Simülasyon ve kör fiziksel sızıntı testi gerekir. |
| `DEC-20260820-02` | ACTIVE SOURCE CONTRACT | Karakter/Güç görünen metni `FOULWAKE_CARD_TEXTS_v2.7.json`; rulebook anlatı blokları `FOULWAKE_RULEBOOK_STORY_v2.7.md`; ton/lore çiti `FOULWAKE_STORY_FRAMEWORK.md` kaynağından alınır. | Kimlik, adet, effect, zamanlama, deste davranışı ve kural akışı v2.6 baseline'ından korunur; çelişki durdurulur. |
| `DEC-20260820-03` | SUPERSEDED 2026-08-25 | Önceki genel mürekkep/gravür sanat yönü onayı. | Eski örnek ve tam üretim sanatı artık kabul kanıtı değildir; `DEC-20260825-01..05` uygulanır. |
| `DEC-20260820-04` | ACTIVE QA MANDATE | Simülasyon mekanik, matematik, strateji, sosyal deneyim, görsel kullanılabilirlik, PDF, baskı, manifest ve dosya bütünlüğünü denetler. | Tek validator/hash veya kazanma oranı genel PASS değildir; exact-candidate attestation gerekir. |
| `DEC-20260820-05` | LOCK POLICY | Kilit sürecini proje sahibi açık talimatla başlatır; kilidi yalnız Baş Editör uygular. | Açık FAIL/BLOCKER veya eksik candidate/attestation varken kilit yoktur. |
| `DEC-20260820-06` | WORKSTREAM IDENTITY | Resmî uzman işi yalnız kullanıcının oluşturduğu görünür sohbet ve exact branch-bound handoff ile o hatta mal edilir. Geçici alt ajan yasaktır. | Önceden izinli istisna bile uzman teslimi/PASS sayılmaz. |
| `DEC-20260820-07` | WORKSTREAM BRANCH | Uzman dalları `work/v2.7-story`, `work/v2.7-visual`, `work/v2.7-simulation`; entegrasyon hedefi `v2.7-design`dır. | Governance, releases, main ve kilit yalnız Baş Editördedir. |
| `DEC-20260820-08` | COMMUNICATION EVIDENCE | GitHub iş emri görünür sohbet ACK'i değildir. | Doğru sohbet `VISIBLE_CHAT_ACK: YES` handoff vermeden teslim kaydedilemez. |
| `DEC-20260825-01` | BINDING ART REJECTION | `work/v2.7-visual@e91581...` teslimindeki bütün ön ve arka yüz sanatı reddedildi. | Eski render/PDF/plakalar yalnız teknik tarihsel referanstır; yeni candidate olamaz. |
| `DEC-20260825-02` | BINDING FULL-DECK REWORK | 121 kartın her biri ayrı art brief ve semantik olarak ayrı, sıfırdan özgün sahne alır. | Aile plakası türevi ve `unique SHA = unique artwork` kabulü yasaktır; kör contact-sheet QA gerekir. |
| `DEC-20260825-03` | SUPERSEDED IN PART BY `DEC-20260830-06` | Kullanıcının KAPTAN görseli STYLE_ONLY referanstır. İllüstrasyon alanına tabela, slogan, konuşma balonu, açıklama veya saçma/anlamsız okunabilir yazı eklenmez. | Okunabilir metin yalnız exact başlık/effect/flavor/kimlik alanlarında olabilir. |
| `DEC-20260825-04` | BINDING BACK TOPOLOGY | 7 arka yüz: Karakter 20; Güç+Çürümüş 31; Sadakat 15; Deniz+Kayalık 42; Ada 6; Deniz Feneri 4; yardımcı 3. | Metinsiz, aile içinde exact aynı, 180° güvenli, kesim/parlaklık sızıntısız ve önlerle aynı sanat dilinde olmalıdır. |
| `DEC-20260825-05` | BINDING PRODUCTION GATE | 12 ön-yüz pilotu ve 7 arka-yüz taslağı kullanıcı ile Baş Editörce kabul edilmeden tam 121 üretim/PDF başlamaz. | Pilot ret edilirse brief/sanat düzeltilir; teknik hash başarısı bu kapıyı atlayamaz. |
| `DEC-20260825-06` | BINDING ART DIRECTION ROLE | Kalıcı görünür `FOULWAKE Sanat Yönetmeni` hattı `work/v2.7-art-direction` dalında sanat yönü, görsel dramaturji, 121+7 brief incelemesi ve somut yaratıcı rework tavsiyesi üretir. | Final sanat üretmez; metin/mekanik/lore/governance/release/kilit değiştirmez; geçici ajan kullanmaz. |
| `DEC-20260825-07` | BINDING CREATIVE GATE | Görsel Tasarımın kendi teknik/estetik kontrolü tek başına sanat kabulü değildir; pilot ve tam deste Sanat Yönetmeninin bağımsız ruh, doku, kompozisyon, ayrışma ve deste ritmi incelemesinden geçer. | Sanat Yönetmeni tavsiyesi release PASS'i değildir; nihai estetik karar proje sahibinin, kayıt/entegrasyon Baş Editöründür. |
| `DEC-20260825-08` | ART DIRECTION BRIEF ACCEPTED | `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da` üzerindeki Bible, 121 brief manifesti, 12 pilot production briefi ve 7 arka-yüz briefi proje sahibi ile Baş Editörce kabul edildi. | Kabul yalnız brief kapısını geçer; final sanat, release veya kilit PASS'i değildir. |
| `DEC-20260825-09` | BINDING FAMILY-VISIBLE MAP BACKS | `BACK_SEA_ROCK` genel denizdir ve Açık Deniz/Kayalık ayrımını gizler; `BACK_ISLAND` anonim genel ada, `BACK_LIGHTHOUSE` 1721'e uygun anonim genel fener gösterir. Aile görünür; exact ön kimlik ve sonuç gizlidir. Sabit 5×5/grid/kart sayısı şartı yoktur. | Değişken kurala uygun düzen, exact master, 180° güvenliği, normal masa mesafesinde aile görünürlüğü ve kör exact-kimlik testleri gerekir. |
| `DEC-20260825-10` | PILOT-ONLY PRODUCTION AUTHORIZATION | Proje sahibi kabul edilen sanat yönü altında kontrollü pilot aşamasını onayladı. | Yalnız 12 ön yüz, 7 arka yüz, contact sheet, değişken harita mockup'ı ve gerekli pilot reworkü yapılabilir; kullanıcı + Baş Editör pilot kabulünden önce kalan 109 ön yüz, tam 121 üretim/PDF, Simülasyon veya release yoktur. |
| `DEC-20260825-11` | BINDING PILOT REVIEW DISPOSITION | Sanat Yönetmeninin `work/v2.7-visual@b4afbcf...` exact incelemesi kabul edildi: 3 ön KEEP, 9 ön REWORK; 7 arka yüzün tamamı REWORK. | Sonraki candidate kabul edilmiş 12 zor-vaka kartıyla sınırlıdır; `SAD-H-03` ve `HAR-KY-06` exact korunur, on kart üretilir/yeniden çizilir, yedi arka yüz sıfırdan yapılır. `GUC-24` set dışı provisional KEEP; diğer set dışı reworkler pilot PASS sonrasına ertelenir. |
| `DEC-20260828-01` | BINDING REVISED PILOT REVIEW DISPOSITION | Sanat Yönetmeninin `work/v2.7-visual@1b27232a...` exact 40/40 incelemesi kabul edildi: 10 ön KEEP / 2 ön REWORK; 5 arka KEEP / 2 arka REWORK. | Mevcut pilot sanat adayı değildir. Rework yalnız `KAR-01`, `HAR-AA-06`, `BACK_ISLAND`, `BACK_LIGHTHOUSE` ve bağlı kanıtlarla sınırlıdır. |
| `DEC-20260828-02` | TARGETED PILOT REWORK AUTHORIZATION | On beş ana KEEP ve dokuz gate byte-exact kalır; dört render/source, yalnız `KAR-01` gate'i, 5 sheet, 6 layout, 1 rapor ve 4 manifest olmak üzere exact 25 dosya değişebilir. | Kapsam sapması BLOCKED olur. Tam 121, PDF, Simülasyon, release ve kilit yetkili değildir; teslim yeniden Sanat Yönetimi, proje sahibi ve Baş Editör kapısından geçer. |
| `DEC-20260830-01` | BINDING TARGETED REWORK REVIEW | `work/v2.7-visual@0cb2bd6f...` exact incelemesinde `KAR-01`, `HAR-AA-06` ve `BACK_ISLAND` KEEP; yalnız `BACK_LIGHTHOUSE` REWORK_REQUIREDdır. | Üç kabul dondurulur. Fener ailesi normal dijital masa-layout mesafesinde anlaşılmadan pilot kabul edilmez. |
| `DEC-20260830-02` | BACK_LIGHTHOUSE-ONLY AUTHORIZATION | Yalnız fener source/renderı, 2 etkilenen sheet, 6 layout, 1 rapor ve 4 kanıt kaydı; exact 15 dosya değişebilir. | 18 ana görsel, 16 source-art, 10 gate ve 3 etkilenmeyen sheet byte-exact kalır; kapsam sapması BLOCKEDdır. Tam 121/PDF/Simülasyon/release/kilit yoktur. |

| `DEC-20260830-03` | LIGHTHOUSE-ONLY HANDOFF ACCEPTANCE | `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e` exact 15-file handoff; kanonik üretim `c8081aa9f781737b0d7e14c8b224bf1fd988e8bb`, evidence/head `23c062f6de06c32eab224b3440c8474725d4fe9e` olarak teknik açıdan tutarlı bulundu. | Yalnız exact Sanat Yönetimi incelemesine giriş kabulüdür. Yeni Görsel üretim, tam 121, PDF, Simülasyon, release ve kilit yoktur; aktif candidate ve estetik PASS oluşmaz. |

| `DEC-20260830-04` | FINAL LIGHTHOUSE ART DIRECTION REVIEW | `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e` exact 9-raster incelemesinde `BACK_LIGHTHOUSE` KEEP; pilot toplamı 12 ön KEEP / 7 arka KEEP ve `PILOT_ART_DIRECTION_PASS`. | Sanat Yönetimi kapısı geçmiştir; proje sahibinin açık pilot estetik kararı ve Baş Editör pilot kabulü gelmeden aktif candidate, yeni Görsel üretim, tam 121, PDF, Simülasyon, release veya kilit yoktur. |

| `DEC-20260830-05` | PROJECT OWNER PILOT REJECTION | Exact `23c062f6...` pilotu proje sahibi tarafından estetik olarak reddedildi; önceki `PILOT_ART_DIRECTION_PASS` üretim/candidate bakımından superseded oldu. | Aktif candidate yok; 12 ön HOLD, üç harita arkası REWORK_REQUIRED, diğer dört arka HOLD; tam 121/PDF/Simülasyon/release/kilit yoktur. |
| `DEC-20260830-06` | BINDING KAPTAN ART LANGUAGE | `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg` KAPTAN kartının görsel kaynağı ve tüm deste için bağlayıcı sanat dili anahtarıdır. Gemi/martı/sahne kopyası zorunlu değildir. `SET-KP-01` teknik kimliği korunur, görünen ad KAPTAN olur, mevcut devredilebilir kaptanlık mekaniği korunur. | Sanat Yönetimi önce tek kısa style patch üretir; önceki STYLE_ONLY yorumu bu kapsamda supersededtır. |
| `DEC-20260830-07` | BINDING COPY LOCK / FAST GATE | Görsel model kart yazısı üretmez; metin kanonik UTF-8 kaynaktan şablonla yerleştirilir ve final front OCR/render-source exact karşılaştırması gerekir. | Şu anda yalnız 1 dosya/700 kelimelik Sanat Yönetimi patchi; kabulden sonra yalnız 6 düşük çözünürlüklü arka-yüz thumbnailı. Final/manifest/layout/PDF yoktur. |
| `DEC-20260830-08` | BINDING ART DIRECTION FRAMING GATE | Sanat Yönetmeni bütün ön/arka kart illüstrasyonlarında exact kart oranı, 3 mm taşma, 4–5 mm güvenli alan, odak/ölçek, istemsiz kesim, metin alanı çakışması, thumbnail/masa-mesafesi okunurluğu ve kadraj çeşitliliğini bağımsız inceler. | Görsel Tasarım kendi kadrajına PASS veremez. Yalnız `FRAMING_PASS` veya `REFRAME_REQUIRED`; PASS olmadan KEEP/final/tam 121 yoktur ve sonuç `BLOCKED_FRAMING_DRIFT`tir. |


| `DEC-20260830-09` | BINDING KAPTAN VISUAL + COPY CORRECTION | Yüklenen kart `SET-KP-01` için ana görsel ve exact visible-copy kaynağıdır: KAPTAN / ÖZEL YETENEK / “Oylamada eşitlik olursa, senin tarafın geçerli olur.” / “Lidere et. Gemi senin emrinde.” | Önceki farklı ad, boş sandalye ve eski effect/flavor v2.7 üretimi için supersededtır; v2.6 yerinde değişmez. |
| `DEC-20260830-10` | BINDING DEFAULT-DENY WORKSTREAM SCOPE | Uzman dalı yalnız CURRENT_STAGE ve WORKSTREAM_SCOPE_BASELINES içinde exact yetkili path/bütçeyi reset baseline'dan sonraki cumulative diffte değiştirebilir. | Eski iş emri, PASS veya dal sahipliği yetki değildir; direct push ve PR aynı scope kontrolünden geçer. |
| `DEC-20260830-11` | BINDING TOOL / PLUGIN EVIDENCE | Her handoff TOOLS_USED, PLUGINS_USED, PLUGINS_AVAILABLE_BUT_NOT_USED ve NOT_USED_REASON alanlarını verir. | Görevde zorunlu aracın kullanılmaması veya beyan edilmemesi BLOCKED_EVIDENCE_GAP'tir; kurulu eklenti sırf kurulu olduğu için otomatik zorunlu değildir. |

| `DEC-20260901-01` | PROJECT OWNER ART DIRECTION PATCH ACCEPTANCE | `work/v2.7-art-direction@917f8b71f47eeecdfb12b7ec930796bf111e2858` exact KAPTAN patchi; bağlayıcı görsel kaynak, exact copy, bağımsız kadraj ve yaratıcı kalite standardı kabul edildi. | Kabul Görsel/thumbnail/candidate/tam 121/PDF/Simülasyon/release/lock yetkisi vermez. |
| `DEC-20260901-02` | V3 CLEAN CLOSURE / V4 ENTRY GATE | `governance/CURRENT_STAGE.json` tek geri dönüş checkpointidir; v4 ayrı branchte paralel kurulur ve parity/negative test olmadan cutover yapılamaz. | LEAN GOVERNANCE SHALL REDUCE CONTEXT AND CEREMONY, NEVER REVIEW DEPTH, CREATIVE SCRUTINY, EVIDENCE QUALITY OR PROJECT OWNER CONTROL. |

## Açık kaynak dispozisyonu

`SRC-002`: v2.6 kayıtlarındaki `GUC-22 = Bayat Peksimet` ile v2.7 kaynağındaki
`GUC-22 = Kaptanın Çatlak Kupası`, `GUC-23 = Bayat Peksimet` çelişkisi karar
değildir. Exact kilitli kaynak karşılaştırması veya proje sahibinin açık hükmü
gelmeden Baş Editör, Hikâye veya Görsel hattı kimlik/effect alanını değiştiremez.

## Uygulama kuralı

- Daha yeni açık kullanıcı kararı önce bu dosyaya ve etkilenen aktif DRAFT
  kaynaklarına kaydedilir.
- Taslak karar v2.6'yı yerinde değiştirmez.
- Eski teslimler silinmez; yanlışlıkla yeniden aday olmamaları için açık
  sınıflandırılır.
- Sohbet özeti, geçici ajan raporu veya GitHub'a yazılmış dosya tek başına
  release kanıtı değildir.
