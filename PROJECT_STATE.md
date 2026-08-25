# FOULWAKE Proje Durumu

**Son güncelleme:** 25 Ağustos 2026  
**Kilitli sürüm:** `v2.6 STABLE / LOCKED`  
**Aktif taslak:** `v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED`  
**Entegrasyon dalı:** `v2.7-design`  
**Aktif workspace:** `working/v2.7/`  
**Aktif görsel candidate:** YOK  
**Genel hüküm:** **BLOCKER — KİLİT VE RELEASE YASAK**

## Çalışma hattı durumu

| Hat | Exact kaynak | Baş Editör hükmü | Sonraki adım |
|---|---|---|---|
| Hikâye | `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37` | Kabul edildi ve exact üç Hikâye blobu entegre edildi; release PASS değil | Görsel için exact metin girdisi |
| Görsel | `work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891` | Teslim gerçek; bütün ön/arka yüz sanatı reddedildi | Tam deste rework pilotu |
| Simülasyon | dal yok | Başlamadı | Yeni görsel aday kabulünden sonra |

Görsel teslimin `121/121`, 7 arka yüz ve PDF/hash zinciri teknik olarak kayıtlı
olması sanat kabulü değildir. Kaynak pakette yalnız altı aile illüstrasyon
plakası bulunması, tekrarlı/türev sanatın 121 farklı render hashine dönüşmesine
izin vermiştir. Eski teslim artık `TECHNICAL_PIPELINE_REFERENCE_ONLY`dır;
aktif release candidate yoktur.

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
- Deniz+Kayalık 42 aynı binary; Deniz Feneri 4 aynı; Ada 6 aynı. Tam topoloji:
  Karakter 20, Güç+Çürümüş 31, Sadakat 15, Deniz+Kayalık 42, Ada 6, Deniz
  Feneri 4, yardımcı 3.
- 12 ön-yüz pilotu ve 7 arka-yüz taslağı kullanıcı/Baş Editör onayı almadan
  tam üretim yok.

## Açık blockerlar

| Kimlik | Sahip | Durum | Kapanış koşulu |
|---|---|---|---|
| `MEC-001` | Simülasyon | OPEN | Sea=Rock için exact adayda tam ve kör fiziksel test |
| `SRC-001` | Görsel | OPEN | Yeni adayda tutarlı source→render→PDF ve iç/dış provenance |
| `SRC-002` | Baş Editör + Simülasyon | OPEN | GUC-22/GUC-23 için kilitli v2.6 exact kaynak karşılaştırması veya açık kullanıcı kararı |
| `ART-001` | Görsel | REWORK REQUIRED | 121 özgün ön yüz, 7 kabul edilmiş arka yüz, kör contact-sheet QA |
| `QA-001` | Simülasyon | OPEN | Exact candidate'a bağlı yeniden üretilebilir tam attestation |
| `QA-002` | Simülasyon | OPEN | Fiziksel proof, kör sızıntı ve kör insan masa testi |
| `GOV-001` | Baş Editör | OPEN | main uzlaştırması, branch protection/ruleset, required status check |
| `COM-001` | Baş Editör | OPEN | Yeni Görsel ve bağımsız Simülasyon branch-bound teslimleri |

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
- `working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md`

## Kilit hükmü

Proje sahibinin açık `kilitle`, `stable yap` veya `release et` talimatı yalnız
süreci başlatır. Açık blocker, eksik exact candidate, eksik fiziksel kanıt veya
Simülasyon PASS/attestation yokken Baş Editör kilit uygulamaz.
