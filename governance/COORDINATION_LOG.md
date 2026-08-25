# FOULWAKE Baş Editör Koordinasyon Kaydı

## 25 Ağustos 2026 — GITHUB DENETİMİ / GÖRSEL TESLİM RET VE TAM REWORK

**Denetim parent'ı:** `v2.7-design@fb73852d76c45977a0ed3bcf0af8cae68f813fb0`  
**Hikâye:** `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37`  
**Görsel:** `work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891`  
**Kanıt:** `governance/CHIEF_EDITOR_AUDIT_20260825.md` ve
`governance/VISUAL_HANDOFF_20260825.json`

Baş Editör aktif dalları, yönetişim, kaynak hiyerarşisi, Görsel manifestler,
QA/release kapıları ve GitHub koruma dosyalarını yeniden denetledi.

**Dispozisyonlar:**

- Hikâye teslimi kabulünü korur; exact değişen üç Hikâye blobu entegrasyon
  dalına alınmıştır.
- Görsel teslim gerçek bir görünür sohbet teslimidir fakat sanat kabulü
  `FAIL`dır. Bütün ön ve arka yüzler rework olacaktır.
- e91581 çıktıları silinmez; `TECHNICAL_PIPELINE_REFERENCE_ONLY` olarak kalır
  ve yeni candidate'a kaynak olamaz.
- KAPTAN yalnız STYLE_ONLY referanstır; 121 kart ayrı brief/sahne alır.
- İllüstrasyon alanında gereksiz veya anlamsız okunabilir yazı yasaktır.
- Yedi back topolojisi `20+31+15+42+6+4+3=121`; aile içinde exact aynı,
  metinsiz ve 180° yön güvenlidir.
- 12 ön-yüz pilotu + 7 back taslağı kullanıcı ve Baş Editörce kabul edilmeden
  tam üretim/PDF yoktur.
- `SRC-002` GUC-22/GUC-23 kimlik çelişkisi exact baseline kanıtı gelmeden
  sessizce düzeltilemez.
- Simülasyon yeni tam adaydan önce başlamaz; release ve kilit BLOCKERdır.

`main` ile `v2.7-design` ayrışması ve branch protection/ruleset yokluğu
`GOV-001` altında açık kalır. Bu dosya düzeltmesi repository ayarlarını
değiştirmez ve kullanıcıyı platform düzeyinde kilitlemez.

## 20 Ağustos 2026 — HİKÂYE WORKSTREAM PASS KABULÜ / GÖRSEL BAŞLANGIÇ

**Görünür sohbet:** `Foulwake Hikâye Editör`  
**Hikâye kaynağı:** `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37`  
**Entegrasyon tabanı:** `v2.7-design@bc148e33343b4066259a996a9c299aab17fd8e3d`  
**Kanıt:** `governance/STORY_HANDOFF_20260820.json`

Proje sahibi, görünür Hikâye Editörü sohbetinin zorunlu handoffunu Baş Editöre
iletti. Handoff `VISIBLE_CHAT_ACK: YES`, `EVIDENCE_TYPE:
VISIBLE_CHAT_WORKSTREAM`, exact çalışma dalı/commiti ve `LOCK_REQUESTED: NO`
alanlarını içerir.

Baş Editör GitHub üzerinde bağımsız olarak şunları doğruladı:

- Hikâye dalı entegrasyon tabanından bir commit ileride ve geride değildir.
- Commit yalnız iki mevcut Hikâye kaynağını ve yeni revalidasyon kaydını değiştirir.
- `governance/**`, `releases/**`, görsel, QA ve kilit alanları değişmemiştir.
- Kaydedilen Story Framework, Rulebook Story, Card Texts ve Narrative
  Validation blobları gerçek branch bloblarıyla eşleşir.
- Card Texts kaynağında 20 Karakter, 30 Güç ve 50 benzersiz kimlik vardır.
- 3.6 anlatısındaki sabit grup ima eden “sonuncusuna” sayımı mekanik akışa
  dokunmadan kaldırılmıştır.

**Baş Editör dispozisyonu:**
`ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT`.

Bu kabul resmî Hikâye revalidasyonunu ve branch-bound Hikâye teslimini
tamamlar. Release PASS'i, mekanik eşdeğerlik, Simülasyon attestation'ı,
`v2.7-design` içerik entegrasyonu veya kilit değildir. `COM-001`, Görsel ve
Simülasyon gerçek teslimleri tamamlanana kadar açık kalır.

`work/v2.7-visual`, kabul edilen Hikâye commiti üzerinde oluşturulmuştur.
Görsel Tasarımın görünür sohbet teslimi henüz beklenmektedir;
`work/v2.7-simulation` henüz oluşturulmamıştır.

## 20 Ağustos 2026 — 3/3 GÖRÜNÜR SOHBET ACK / İLETİŞİM TESTİ

**Kaynak:** `v2.7-design@52f6c3b3c196a5af9c48d4694cd3091eb3da8129`

Proje sahibi salt-okunur iletişim testini üç resmî görünür sohbete ayrı ayrı
iletti. Her sohbet kendi görünür geçmişinde zorunlu handoff alanlarıyla cevap
verdi; Baş Editör yanıtları kapsam ve yetki sınırı açısından denetledi.

| Hat | Görünür sohbet | Atanmış çalışma dalı | Baş Editör dispozisyonu |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` | `work/v2.7-story` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY` |
| Görsel | `FOULWAKE görsel tasarım` | `work/v2.7-visual` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY` |
| Simülasyon | `Simülasyon Testi` | `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY` |

Üç yanıtta da `VISIBLE_CHAT_ACK: YES`, doğru kaynak commit, `CHANGED_FILES:
NONE` ve `LOCK_REQUESTED: NO` vardır. Geçici ajan veya test ajanı
oluşturulmamış; dosya, commit/push, PR/issue, üretim, simülasyon ya da release
işlemi yapılmamıştır. Uzman dalları henüz oluşturulmamıştır.

**Sınır:** Bu 3/3 sonuç yalnız iletişim ve yetki alanı ACK'sidir. Hikâye
revalidasyonu, görsel candidate, Simülasyon testi, uzmanlar arası teslim, PASS,
blocker kapanışı veya release kanıtı değildir. `COM-001`in iletişim ACK alt
adımı tamamlandı; bağımsız uzman revalidasyonları ve branch-bound gerçek
teslimler tamamlanana kadar blocker açık kalır. Tam kayıt
`governance/VISIBLE_CHAT_ACKS_20260820.json` içindedir.

## 20 Ağustos 2026 — KAYIT DÜZELTMESİ / ÖNCEKİ ATIFLARI GEÇERSİZ KILAR

**Düzeltme kaynağı:** Proje sahibinin görünür sohbet zorunluluğu ve geçici alt
ajan yasağı

**Denetlenen head:** `v2.7-design@9758b848f0395525b395e3f2ccf9e9f7408fed99`

Bu dosyanın aşağıdaki eski bölümlerinde kullanılan “Hikâye, Görsel Tasarım ve
Simülasyon hatları denetledi”, “iletilen”, `ACKNOWLEDGED`, `DELIVERED` ve
“önerilerini birbirlerine iletti” ifadeleri kullanıcı tarafından oluşturulan
görünür sohbetler açısından doğru değildir. İncelemeler Baş Editör sohbetinde
çalıştırılmış geçici alt ajanlardan gelmiştir. Teknik bulgular ön bulgu olarak
kalabilir; uzman sohbet teslimi, bağımsız onay veya release kanıtı sayılamaz.

Bu nedenle önceki çapraz handoff durumları geri alınmış ve
`PENDING_VISIBLE_CHAT_ACK` olarak yeniden sınıflandırılmıştır. Geçici alt ajan
oluşturmak bundan sonra yasaktır; çok zorunlu istisna proje sahibinin önceden
açık iznini gerektirir ve yine uzman sohbet adına çalışmış sayılmaz.

| Hat | Önceki yanlış kayıt | Geçerli durum |
|---|---|---|
| Hikâye | Teslim/çapraz onay verilmiş gibi gösterildi | `PENDING_VISIBLE_CHAT_ACK` |
| Görsel | Teslim/çapraz onay verilmiş gibi gösterildi | `PENDING_VISIBLE_CHAT_ACK` |
| Simülasyon | QA planı ve hüküm resmî teslim gibi gösterildi | `PENDING_VISIBLE_CHAT_DELIVERY` |

Baş Editör bu sohbetten diğer görünür sohbetlerin geçmişine mesaj ekleyemez.
GitHub kaydı yalnız iş emridir; ilgili sohbet kendi geçmişinde okuyup
`VISIBLE_CHAT_ACK: YES` handoffu vermeden kabul edilmiş sayılmaz. Uzman
çalışmaları `work/v2.7-story`, `work/v2.7-visual` ve
`work/v2.7-simulation` dallarında üretilecek; yalnız Baş Editör doğrulanmış
teslimleri `v2.7-design`a entegre edecek ve release/kilit alanını yönetecektir.

Bu düzeltme `COM-001` blockerını açar. Aşağıdaki tarihsel bulgular, görünür
uzman sohbetlerce yeniden doğrulanana kadar **Baş Editörün geçici ön
bulguları**dır.

## 20 Ağustos 2026 — Baş editörlük düzeninin yürürlüğe alınması

**Kanonik baseline:** v2.6 STABLE / LOCKED  
**Aktif çalışma:** v2.7 STORY + VISUAL DRAFT / NOT LOCKED  
**Aktif branch:** `v2.7-design`

### Hikâye Editörü için GitHub iş emri — görünür sohbet kabulü bekliyor

- Mevcut v2.7 hikâye ve kart dili dosyaları Görsel Tasarımın metin kaynağıdır.
- Kural kitabı akışı, kart sayıları, kimlikler, etkiler, zamanlamalar, başlangıç havuzu ve deste davranışları korunacaktır.
- Görsel dosyalarda doğrudan değişiklik yapılmayacak; görsel ihtiyaçlar handoff ile iletilecektir.
- Mekanik risk olarak görülen konular kural değişikliğine çevrilmeden Simülasyon Testine aktarılacaktır.

### Görsel Tasarım için GitHub iş emri — görünür sohbet kabulü bekliyor

- `FOULWAKE_STORY_FRAMEWORK.md`, `FOULWAKE_RULEBOOK_STORY_v2.7.md`, `FOULWAKE_CARD_TEXTS_v2.7.json` ve anlatı doğrulama raporu metin/lore kaynağıdır.
- `FOULWAKE_VISUAL_SYSTEM.md` onaylı sanat yönüdür; release kilidi değildir.
- Mizah yalnız fareye dayanmayacaktır. Fare, martı, beceriksiz veya hırsız tayfa, sessiz bakış ve nesne kaynaklı kuru mizah dönüşümlü kullanılacaktır.
- Tam 121 kartlık yayılım aile bazında okunabilirlik ve tutarlılık kontrolüyle ilerleyecektir.
- Mekanik veya kanonik metin değiştirilmeden taşma/okunabilirlik sorunu Baş Editöre bildirilecektir.

### Simülasyon Testi için GitHub iş emri — görünür sohbet teslimi bekliyor

- Denetim yalnız kazanma oranı veya eski statik validator ile sınırlı değildir.
- Mekanik, matematik, mantık, strateji, sosyal deneyim, sıkılma, adalet, moderatör yükü, görsel okunabilirlik, PDF ve manifest bütünlüğü ayrı katmanlarda test edilecektir.
- Hikâye ve Görsel Tasarım çıktıları aktif v2.7 DRAFT olarak denetlenecek; v2.6 yalnız değişmeyen baseline olacaktır.
- Sonuç `PASS`, `PASS WITH MINOR ISSUES`, `FAIL` veya `BLOCKER` olarak raporlanacaktır.
- FAIL/BLOCKER kapanmadan Baş Editör release kilidi uygulamayacaktır.

### Baş Editör kararı

- Hiçbir çalışma hattı tek başına kanonik durum, release manifesti veya `STABLE / LOCKED` kaydı oluşturamaz.
- Başka hattın alanında sorun görüldüğünde sessiz düzenleme yapılmaz; handoff oluşturulur.
- Bu kayıt, yeni çalışma oturumlarında zorunlu okunacaktır.

## 20 Ağustos 2026 — Çapraz çalışma hattı denetimi

Baş Editör sohbetindeki üç geçici alt ajan `v2.7-design` dalındaki
`1a5b23051a3a625d6de9b98c2503a0181956af3c` commitini salt okunur biçimde
inceledi. Bu, görünür Hikâye, Görsel Tasarım ve Simülasyon Testi sohbetlerinin
bağımsız denetimi veya aralarındaki iletişim değildir. Aşağıdaki ortak hüküm
Baş Editörün geçici blocker değerlendirmesi olarak korunur.

**Ortak hüküm:** `v2.7 = BLOCKER / RELEASE VE KİLİT İÇİN UYGUN DEĞİL`.

| Kimlik | Ortak bulgu | Kapanma koşulu |
|---|---|---|
| `MEC-001` | Ortak Deniz + Kayalık arka yüzü, v2.6'nın ayrı Kayalık arka yüzü ve gizli bilgi mimarisiyle çakışıyor. | Proje sahibinin açık mekanik kararı, kaynak hizalama ve tam yeniden test |
| `SRC-001` | Görsel sistem v2.6 metnini kaynak gösteriyor; aktif v2.7 kart/rulebook metni ve üretilmiş PDF arasında provenance yok. | Tek kaynak sırası ve source → render → PDF birebir kanıtı |
| `ART-001` | Tam 121 kartlık aday ve GitHub'dan doğrulanabilir görsel artefakt seti yok. | Tam aday, manifest/hash, baskı ve duplex prova |
| `QA-001` | v2.7 anlatı PASS'i yeniden üretilemiyor; exact candidate'a bağlı tam Simülasyon QA attestation yok. | Sürümlü script/baseline, ham çıktılar, hashli attestation |
| `QA-002` | Yeni düzen için kör insan masa testi ve fiziksel prova yok. | Sosyal deneyim ölçümleri ile gerçek baskı/kesim/ışık kaydı |
| `GOV-001` | `main` ve `v2.7-design` durum kayıtları çakışıyor; dal 45 ahead / 2 behind, v2.7 PR ve zorunlu check yok. | Bilinçli dal uzlaştırması, release PR ve zorunlu yönetişim check'i |
| `CAN-001` | Genel olarak DRAFT olan Story Framework, özellikle yeni `CAN-08/09` maddelerini kullanıcı kilidi olmadan KANON etiketliyor. | Taslak kısıta yeniden sınıflandırma veya proje sahibinin açık kanon kararı |

### Baş Editör dispozisyonu

- Bu bulgular `governance/ACTIVE_WORKSTREAMS.json` içinde açık BLOCKER olarak kaydedildi.
- Hiçbiri sessizce mekanik, hikâye veya görsel değişikliğe çevrilmedi.
- `releases/v2.6/` değiştirilmedi.
- Proje sahibinin açık `kilitle/stable/release` talimatı gelse bile açık BLOCKER'lar kapanmadan kilit uygulanmayacak.
- Yeni bir candidate commit, önceki bütün v2.7 PASS/attestation sonuçlarını geçersiz kılar.

## 20 Ağustos 2026 — Sorumlu hatlara çözüm dağıtımı

Proje sahibi açık engellerin sorumlularına iletilmesini ve hatların uyumlu
çalışmasını istedi. Önceki uygulamada görünür uzman sohbetlerine mesaj
gönderilmedi; `af064df83ac4132c7d8d75aec67a3f1b51150fdb` üzerindeki öneriler geçici
alt ajanlardan alındı ve Baş Editör tarafından birleştirildi. Bu kayıt şimdi
resmî teslim değil, yeniden doğrulanacak ön çalışma olarak sınıflandırılmıştır.

### Baş Editörün kaynak ve karar dispozisyonu

- Önceki kullanıcı kararı doğrulandı: v2.7 DRAFT için Açık Deniz ve Kayalık aynı
  binary arka yüzü kullanır. Bu konu yeniden karar beklemez.
- Ortak arka yüz v2.6'nın ayrı Kayalık arka yüz modelinden bilinçli bir
  bilgi-mimarisi değişikliğidir; `MEC-001` tam Simülasyon ve kör fiziksel sızıntı
  testi bitene kadar açık kalır.
- `CAN-08/09`, release kanonu değil v2.7 DRAFT koruma ilkesidir; `TASLAK`
  sınıfına alınır.
- Görsel üretimin metin sırası: v2.6 değişmeyen mekanik baseline → v2.7 Card
  Texts → tanımlı v2.7 Rulebook Story blokları → Story Framework ton/lore çiti →
  Visual System yerleşim/sanat standardı.
- `FOULWAKE_NARRATIVE_VALIDATION_v2.7.md` üretim metni veya bağlayıcı release
  PASS'i değildir; yeniden üretilebilir kanıt bekler.
- Reset öncesi 121/121 üretim ve final preflight tarihsel kanıttır; güncel branch
  ve exact candidate'a yeniden bağlanmadan `ART-001`i kapatmaz.

### Geçici öneriler ve görünür sohbet doğrulama durumu

| Hat | Ön çalışma | Geçerli durum |
|---|---|---|
| Hikâye | CAN-08/09 `KANON → TASLAK`; kesin metin alanları ve korunan mekanik alanlar | İçerik düzeltildi; görünür Hikâye sohbeti yeniden doğrulaması bekliyor |
| Görsel | Kaynak hiyerarşisi; Sea=Rock draft/retest çiti; 121 manifest ve provenance şartı | Spec ön çalışması var; görünür Görsel sohbeti teslimi bekliyor |
| Simülasyon | Paired A/B, mekanik/fuzz, strateji, sosyal, kör insan ve fiziksel sızıntı planı | Baş Editör taslak planı; görünür Simülasyon sohbeti kabulü/uygulaması bekliyor |
| Baş Editör | Karar kaydı, görev haritası ve yanlış atıf düzeltmesi | Yönetişim düzeltmesi uygulandı; entegrasyon ve release hâlâ BLOCKER |

Uzman sohbetlerin ayrı commit/push oluşturmasının yasaklandığı önceki hüküm
geçersizdir. Uzmanlar yalnız kendi çalışma dalları ve yetki alanlarında teslim
üretebilir; Baş Editör entegrasyon, kanonik durum, release ve kilit yetkisini
korur. Güncel hüküm BLOCKER olarak kalır; bu koordinasyon bir release veya kilit
değildir.
