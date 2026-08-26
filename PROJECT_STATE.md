# FOULWAKE Proje Durumu

**Son güncelleme:** 26 Ağustos 2026  
**Kilitli sürüm:** `v2.6 STABLE / LOCKED`  
**Aktif taslak:** `v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED`  
**Entegrasyon dalı:** `v2.7-design`  
**Aktif workspace:** `working/v2.7/`  
**Aktif görsel candidate:** YOK — exact pilot paketi `1b27232a...` üzerinde gözlendi; resmî Görsel teslim handoffu bekleniyor  
**Sanat Yönetimi:** `ART_DIRECTION BRIEF ACCEPTED / REVISED PILOT RE-REVIEW NOT STARTED`  
**Görsel kapısı:** `PILOT REWORK REQUIRED / PACKAGE OBSERVED / OFFICIAL HANDOFF PENDING`  
**Genel hüküm:** **BLOCKER — KİLİT VE RELEASE YASAK**

## Çalışma hattı durumu

| Hat | Exact kaynak | Baş Editör hükmü | Sonraki adım |
|---|---|---|---|
| Hikâye | `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37` | Kabul edildi ve exact üç Hikâye blobu entegre edildi; release PASS değil | Görsel için exact metin girdisi |
| Sanat Yönetimi | `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da` | Brief PASS korunur; exact `b4afbcf...` pilot incelemesi `REWORK_REQUIRED` | Yeni Görsel handoff doğrulandıktan sonra `1b27232a...` paketini yeniden inceleme |
| Görsel | `work/v2.7-visual@1b27232a53b09ac3ff00030f625bfc2703d15764` | Hedefli pilot paketi gözlendi; kalıcı halef ACK kabul edildi; sanat ve teslim PASS'i verilmedi | `FOULWAKE Görsel Tasarım 2` yalnız mevcut paket için final handoff verecek |
| Simülasyon | dal yok | Başlamadı | Yeni görsel aday kabulünden sonra |

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
üretim teslim handoffu değildir. Yeni üretim yetkisi yoktur; sıradaki adım
mevcut paketin görsele özgü zorunlu handoffudur.

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
| `ART-001` | Sanat Yönetimi + Görsel | PILOT PACKAGE OBSERVED / HANDOFF AND REVIEW PENDING | `1b27232a...` paketi için resmî Görsel teslim handoffu, yeniden yaratıcı inceleme ve kullanıcı/Baş Editör pilot kabulü gerekir |
| `QA-001` | Simülasyon | OPEN | Exact candidate'a bağlı yeniden üretilebilir tam attestation |
| `QA-002` | Simülasyon | OPEN | Fiziksel proof, kör sızıntı ve kör insan masa testi |
| `GOV-001` | Baş Editör | OPEN | main uzlaştırması, branch protection/ruleset, required status check |
| `COM-001` | Baş Editör | OPEN | Kalıcı Görsel halef ACK'i tamamlandı; mevcut paket için resmî Görsel teslim handoffu, pilot kabulü ve bağımsız Simülasyon teslimi bekleniyor |

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
- `governance/ART_DIRECTION_ACK_20260825.json`
- `governance/ART_DIRECTION_HANDOFF_20260825.json`
- `governance/ART_DIRECTION_PILOT_REVIEW_20260825.json`
- `working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md`
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
