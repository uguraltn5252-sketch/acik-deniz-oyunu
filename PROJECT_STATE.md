# FOULWAKE Proje Durumu

**Son güncelleme:** 30 Ağustos 2026  
**Kilitli sürüm:** `v2.6 STABLE / LOCKED`  
**Aktif taslak:** `v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED`  
**Entegrasyon dalı:** `v2.7-design`  
**Aktif workspace:** `working/v2.7/`  
**Aktif görsel candidate:** YOK — exact `23c062f6...` lighthouse-only handoffu Sanat Yönetimi incelemesini bekliyor  
**Sanat Yönetimi:** `BACK_LIGHTHOUSE FINAL EXACT REVIEW PENDING`  
**Görsel kapısı:** `15 FILE HANDOFF ACCEPTED FOR ART DIRECTION REVIEW / PRODUCTION PAUSED`  
**Genel hüküm:** **BLOCKER — KİLİT VE RELEASE YASAK**

## Çalışma hattı durumu

| Hat | Exact kaynak | Baş Editör hükmü | Sonraki adım |
|---|---|---|---|
| Hikâye | `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37` | Kabul edildi ve exact üç Hikâye blobu entegre edildi; release PASS değil | Görsel için exact metin girdisi |
| Sanat Yönetimi | `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da` | Exact `23c062f6...` final fener paketinin bağımsız estetik incelemesi yetkili | BACK_LIGHTHOUSE, 2 sheet ve 6 layout rasterını exact açıp karar verir |
| Görsel | `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e` | Exact 15 dosyalık handoff kabul edildi; kanonik üretim `c8081aa9...` | Üretim durur; Sanat Yönetimi sonucunu bekler |
| Simülasyon | dal yok | Başlamadı | Yeni görsel aday kabulünden sonra |

Lighthouse-only teslim zinciri GitHub'da exact doğrulanmıştır: başlangıç `0cb2bd6f03e2d84948741c162f22b8fd2ff064ad`, kanonik üretim `c8081aa9f781737b0d7e14c8b224bf1fd988e8bb`, kanıt ve dal başı `23c062f6de06c32eab224b3440c8474725d4fe9e`. Cumulative fark yalnız yetkili 15 dosyadır; takip commiti yalnız rapor ile dört manifest/checksum/provenance kaydını teslim hashine bağlar. Teknik handoff `governance/VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json` ile Sanat Yönetimi incelemesine kabul edilmiştir. Bu estetik kabul, proje sahibi onayı veya aktif candidate değildir.

Görsel teslimin `121/121`, 7 arka yüz ve PDF/hash zinciri teknik olarak kayıtlı
olması sanat kabulü değildir. Kaynak pakette yalnız altı aile illüstrasyon
plakası bulunması, tekrarlı/türev sanatın 121 farklı render hashine dönüşmesine
izin vermiştir. Eski teslim artık `TECHNICAL_PIPELINE_REFERENCE_ONLY`dır;
aktif release candidate yoktur.

Sanat Yönetiminin exact `7418d9c2...` paketi; dünya hissi, çizgi ve malzeme
dili, görsel dramaturji, 121 ayrı brief, 12 pilot production briefi ve 7 arka
yüz briefi olarak kabul edilmiştir. Proje sahibi aile-görünür harita arkalarını
ve sabit 5×5 şartının kaldırılmasını nihai olarak onaylamıştır. Bu brief kabulü
final görsel kabulü değildir.

Görsel dalındaki `b4afbcf...` brief-öncesi pilot exact olarak incelenmiş ve
`REWORK_REQUIRED` almıştır. Üç ön yüz (`GUC-24`, `SAD-H-03`, `HAR-KY-06`)
KEEP; dokuz ön yüz REWORK; yedi arka yüzün tamamı REWORK'tür. Sonraki pilot,
kabul edilmiş zor-vaka 12'lisine dönmek zorundadır: `SAD-H-03` ile `HAR-KY-06`
exact korunur, üç örtüşen ret düzeltilir ve yedi eksik zor-vaka kartı üretilir.
`GUC-24` set dışı provisional KEEP olarak saklanır; diğer set dışı retler pilot
kabulünden sonraya ertelenir. Görünür Görsel rework handoffu ve kullanıcı/Baş
Editör kabulü gelmeden aktif candidate veya tam üretim sayılamaz.

Hedefli rework üretimi GitHub'da tamamlanmıştır: `bf944125...` kanonik üretim,
`1ab579c2...` kanıt ve `1b27232a...` temizlenmiş nihai dal başıdır. Paket 12
ön yüzü, 7 arka yüzü, contact sheetleri ve değişken harita düzeni kanıtlarını
içerir. Önceki Görsel sohbet yanıt vermez hâle geldiği için proje sahibi
`FOULWAKE Görsel Tasarım 2` kalıcı halef sohbetini açmış; bu sohbet exact
kaynakları salt-okunur doğrulayarak rol devrini kabul etmiştir. Halef ACK'i
üretim teslim handoffu değildir. Halef daha sonra mevcut paket için zorunlu
Görsel handoffu vermiş; Baş Editör exact 62 dosyalık ağacı ve teknik kanıtı
doğrulayarak `VISUAL_PILOT_HANDOFF_ACCEPTED_FOR_ART_DIRECTION_REVIEW`
dispozisyonu vermiştir. Yeni üretim yetkisi yoktur; sıradaki adım Sanat
Yönetiminin exact yaratıcı incelemesidir.

## 28 Ağustos 2026 — Revize pilot sanat dispozisyonu

Sanat Yönetmeni exact `1b27232a53b09ac3ff00030f625bfc2703d15764` paketindeki 40/40 rasterı açtı.
Önlerde 10 KEEP / 2 REWORK, arkalarda 5 KEEP / 2 REWORK verdi. Rework:
`KAR-01_front.png`, `HAR-AA-06_front.png`, `BACK_ISLAND.png`,
`BACK_LIGHTHOUSE.png`. Beş contact sheet ile altı mevcut map-layout,
aynı kimlik/konum/yön/geometriyle yeniden türetilmelidir.

Baş Editör bu yaratıcı dispozisyonu kabul etti; mevcut pilotu sanat adayı
olarak kabul etmedi ve yalnız exact 25 dosyalık hedefli reworkü açtı. On beş
ana KEEP ile dokuz korunmuş gate byte-exact kalır. Kanıt
`governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`; iş emri `working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md`dır. Tam 121, PDF, Simülasyon,
release ve kilit kapalıdır.

## 30 Ağustos 2026 — Üç rework kabul / yalnız BACK_LIGHTHOUSE açık

Görsel üretim `88907294edd326c118573f5ada7406e5fc42ee4d` commitinde 25 dosya olarak tamamlanmış,
kanıt zinciri `0cb2bd6f03e2d84948741c162f22b8fd2ff064ad` head'inde bağlanmıştır. Exact fark ve
manifestler; 25/25 kapsamı, 15/15 önceki ana KEEP'i, 9/9 gate'i, üç değişken
geometriyi ve tam 121 üretimin başlamadığını doğrular.

Sanat Yönetmeni `KAR-01`, `HAR-AA-06` ve `BACK_ISLAND` için KEEP verdi.
`BACK_LIGHTHOUSE` üzerindeki rozet sorunu çözülmüş olsa da kule normal
dijital masa-layout mesafesinde kaybolduğu için kart ikinci bir Ada/kayalık
sırtı gibi okunuyor. Fener ailesi güvenilir anlaşılmadığından pilot kabul
edilmedi.

Baş Editör yalnız fener source/renderı, iki etkilenen contact sheet, altı
layout, bir rapor ve dört kanıt kaydından oluşan exact 15 dosyalık reworkü
açtı. On sekiz ana görsel, on altı source-art, on gate ve üç etkilenmeyen sheet
byte-exact donduruldu. Kanıt `governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json`; emir `working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md`dır.

## Bağlayıcı yeni görsel yön

`working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md` bütün
121 ön yüz ve 7 arka-yüz ailesi için bağlayıcı iş emridir.

- KAPTAN kartı yalnız STYLE_ONLY referans; karakter/poz/kompozisyon kopyası yok.
- Her kart için ayrı brief ve ayrı özgün sahne.
- Resim alanında gereksiz, komik, açıklayıcı veya anlamsız okunabilir yazı yok.
- Exact kart metni değiştirilemez.
- Mizah en fazla bir ikincil şaka; tekrar eden martı/fare/papağan/tayfa maskotu
  yok.
- Arka yüzler aynı FOULWAKE sanat dilinde, metinsiz ve 180° yön güvenli.
- `BACK_SEA_ROCK` genel deniz olarak Açık Deniz/Kayalık ayrımını gizler;
  `BACK_ISLAND` anonim genel ada, `BACK_LIGHTHOUSE` 1721'e uygun anonim genel
  fener gösterir. Aile görünür; exact ön kart ve sonuç gizlidir.
- Sabit 5×5/grid şartı yoktur; değişken kurala uygun masa düzenleri kullanılır.
- Deniz+Kayalık 42 aynı binary; Deniz Feneri 4 aynı; Ada 6 aynı. Tam topoloji:
  Karakter 20, Güç+Çürümüş 31, Sadakat 15, Deniz+Kayalık 42, Ada 6, Deniz
  Feneri 4, yardımcı 3.
- 12 ön-yüz pilotu ve 7 arka-yüz taslağı Sanat Yönetmeni incelemesi ile
  kullanıcı/Baş Editör onayı almadan tam üretim yok.

## Açık blockerlar

| Kimlik | Sahip | Durum | Kapanış koşulu |
|---|---|---|---|
| `MEC-001` | Simülasyon | OPEN | Sea=Rock için exact adayda tam ve kör fiziksel test |
| `SRC-001` | Görsel | OPEN | Yeni adayda tutarlı source→render→PDF ve iç/dış provenance |
| `SRC-002` | Baş Editör + Simülasyon | OPEN | GUC-22/GUC-23 için kilitli v2.6 exact kaynak karşılaştırması veya açık kullanıcı kararı |
| `ART-001` | Sanat Yönetimi + Görsel | BACK_LIGHTHOUSE-ONLY REWORK AUTHORIZED | Fener source/renderı ve yalnız bağlı 13 kanıt dosyası düzeltilip yeniden incelenmelidir |
| `QA-001` | Simülasyon | OPEN | Exact candidate'a bağlı yeniden üretilebilir tam attestation |
| `QA-002` | Simülasyon | OPEN | Fiziksel proof, kör sızıntı ve kör insan masa testi |
| `GOV-001` | Baş Editör | OPEN | main uzlaştırması, branch protection/ruleset, required status check |
| `COM-001` | Baş Editör | OPEN | `0cb2bd6f...` sanat dispozisyonu kaydedildi; fener-only Görsel handoffu, kullanıcı/Baş Editör pilot kabulü ve bağımsız Simülasyon bekleniyor |

`CAN-001` çözülmüştür: CAN-08/09 v2.7 DRAFT `TASLAK` koruma ilkeleridir.

## Kaynak çelişkisi — sessiz düzeltme yasak

`releases/v2.6/CARD_BASELINE.md` ve `CHANGELOG.md`, Bayat Peksimet'i `GUC-22`
olarak kaydeder. `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json` ise
`GUC-22 = Kaptanın Çatlak Kupası`, `GUC-23 = Bayat Peksimet` der. v2.7 anlatı
doğrulaması buna rağmen Güç kimlik/effect alanlarını baseline ile aynı ilan
eder; karşılaştırma scripti ve sabit baseline GitHub'da yoktur. Baş Editör
hangi kaynağın yanlış olduğunu tahmin etmez. `SRC-002` çözülene kadar ilgili
kartlar release kanıtı sayılmaz.

## GitHub koruma gerçeği

`CODEOWNERS`, PR şablonu ve governance workflow vardır; ancak denetim tarihinde
`main` ve `v2.7-design` korumasızdır ve repository ruleset yoktur. Bu nedenle
Baş Editörün kilit yetkisi dosyalarda tanımlı olsa da GitHub ayarlarında zorunlu
değildir. Platform koruması açılmadan `GOV-001` kapanmaz.

## Korunan baseline

`releases/v2.6/` salt okunurdur ve bu denetimde değiştirilmemiştir. v2.7
workspace içindeki v2.6 kopyalarının dokuzu kilitli bloblarla birebirdir;
`working/v2.7/BINARY_ARTIFACTS.md` aktif taslak kaydı olduğu için bilinçli olarak
ayrıdır.

## Kanıt yolları

- `governance/ACTIVE_WORKSTREAMS.json`
- `governance/CHIEF_EDITOR_AUDIT_20260825.md`
- `governance/STORY_HANDOFF_20260820.json`
- `governance/VISUAL_HANDOFF_20260825.json`
- `governance/VISUAL_SUCCESSOR_ACK_20260826.json`
- `governance/VISUAL_PILOT_HANDOFF_20260826.json`
- `governance/ART_DIRECTION_ACK_20260825.json`
- `governance/ART_DIRECTION_HANDOFF_20260825.json`
- `governance/ART_DIRECTION_PILOT_REVIEW_20260825.json`
- `governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`
- `governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json`
- `working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md`
- `working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md`
- `working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md`
- `working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`
- `working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md`
- `working/v2.7/visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json`
- `working/v2.7/visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md`
- `working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md`
- `working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md`

## Kilit hükmü

Proje sahibinin açık `kilitle`, `stable yap` veya `release et` talimatı yalnız
süreci başlatır. Açık blocker, eksik exact candidate, eksik fiziksel kanıt veya
Simülasyon PASS/attestation yokken Baş Editör kilit uygulamaz.
