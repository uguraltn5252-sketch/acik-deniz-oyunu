# FOULWAKE Çalışma Hatları ve İletişim Protokolü

## 1. Zorunlu başlangıç

Her hat çalışmadan önce şu sırayı okur:

1. `AI_HANDOFF.md`
2. `PROJECT_STATE.md`
3. `governance/EDITORIAL_CHARTER.md`
4. `governance/DECISION_REGISTER.md`
5. `governance/ACTIVE_WORKSTREAMS.json`
6. `governance/WORKSTREAM_ASSIGNMENTS.md`
7. Bu protokol ve ilgili hat kaynakları

Aktif branch/head ve son `STABLE / LOCKED` baseline exact olarak doğrulanır.
Kaynak çelişkisi otomatik çözülmez; iş durur ve Baş Editöre handoff edilir.

## 2. Görünür sohbet ve ajan kuralı

- Resmî uzman alanları `Foulwake Hikâye Editör`, `FOULWAKE Sanat Yönetmeni`,
  `FOULWAKE görsel tasarım` ve `Simülasyon Testi` görünür sohbetleridir.
- Geçici alt ajan oluşturulmaz. Çok zorunlu istisna proje sahibinin önceden
  açık iznini gerektirir; sonuç `TEMPORARY_SUBAGENT` kalır ve uzman teslimi,
  PASS veya blocker kapanışı sayılamaz.
- GitHub iş emri bir sohbete otomatik mesaj veya ACK değildir. İlgili sohbet
  kendi geçmişinde okuyup exact handoff vermeden `ACKNOWLEDGED/DELIVERED`
  kaydedilemez.

## 3. Dal ve yazma sınırları

| Görünür sohbet | Dal | Yazma kapsamı | Yasak alan |
|---|---|---|---|
| Hikâye | `work/v2.7-story` | Onaylı hikâye ve mekanik olmayan görünen metin | Görsel, QA, governance, releases, main, mekanik |
| Sanat Yönetimi | `work/v2.7-art-direction` | `working/v2.7/visual/art_direction/**` sanat yönü, brief ve yaratıcı eleştiri | Final görsel/PDF, metin, lore, mekanik, QA, governance, releases, main |
| Görsel | `work/v2.7-visual` | Özgün illüstrasyon, yerleşim, baskı, görsel manifest | Hikâye hükmü, mekanik, QA hükmü, governance, releases, main |
| Simülasyon | `work/v2.7-simulation` | `working/v2.7/qa/**` kanıtları | Ürün içeriği, mekanik değişiklik, governance, releases, main |

Entegrasyon hedefi `v2.7-design`dır. `PROJECT_STATE.md`, `AI_HANDOFF.md`,
`CHANGELOG.md`, `README.md` kanonik durumu, `governance/**`, `releases/**`,
`main` ve kilit alanları yalnız Baş Editör kapsamındadır.

## 4. Hikâye hattı

Birincil kaynaklar:

- `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md`
- `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md`
- `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json`
- `working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md` — yalnız kayıtlı kanıt

Kart adedi/kimliği, `effect`, zamanlama, grup, başlangıç havuzu, desteye dönüş,
deste davranışı ve kural akışı değiştirilemez. `SRC-002` GUC-22/GUC-23
çelişkisi Hikâye hattında tahminle çözülmez.

## 5. Sanat Yönetimi hattı

Birincil kaynaklar:

- `working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`
- `working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md`
- exact kart metni, kabul edilmiş hikâye kaynakları ve değişmeyen v2.6 baseline
- kullanıcı tarafından aynı görünür sohbete eklenen KAPTAN STYLE_ONLY referansı
- incelenecek exact Görsel branch/commit ve contact sheetleri

Sanat Yönetmeni teknik checklist uygulamakla yetinmez; dünya hissi, görsel
dramaturji, karakter/olay ayrışması, kompozisyon, çizgi-tarama-malzeme dili,
mat palet, dönem doğruluğu, mizah ölçüsü ve deste ritmi için yaratıcı hüküm
üretir. Genel sıfat değil, korunacak/çıkarılacak/yeniden çizilecek unsurları
somutlaştıran brief verir.

Yazma kapsamı yalnız `working/v2.7/visual/art_direction/**`dır. Final sanat,
render, PDF ve baskı Görsel Tasarıma aittir. Exact metin/mekanik/lore ile
governance/release/kilit alanları değiştirilemez. Sanat Yönetmeni tavsiyesi
proje sahibinin nihai estetik kararı veya Baş Editör/release PASS'i değildir.

İlk kapı iletişim testidir. `VISIBLE_CHAT_ACK: YES` gelmeden yaratıcı iş bu
hatta mal edilemez. Görsel pilot daha önce başlamışsa exact teslim ilk review
girdisi olur; çalışma otomatik olarak geçersiz veya kabul edilmiş sayılmaz.

## 6. Görsel hattı

Birincil kaynaklar:

- `working/v2.7/SOURCE_HIERARCHY_v2.7.json`
- `working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md`
- `working/v2.7/FOULWAKE_VISUAL_SYSTEM.md`
- exact görünen metin ve v2.6 değişmeyen baseline kaynakları

### 6.1 Korunan içerik

- Metin kısaltılmaz, düzeltilmez, yeniden yazılmaz; noktalama ve anlam
  değiştirilmez.
- Taşma, eksik glif veya okunabilirlik sorunu dosya/kart/alan adıyla Baş
  Editöre iletilir.
- Lore veya mekanik hakkında yeni hüküm üretilmez.

### 6.2 Sanat üretimi

- KAPTAN görseli `STYLE_ONLY`; karakter, yüz, poz, kompozisyon veya piksel
  kopyalanmaz.
- Her kart ayrı art brief ve ayrı özgün sahne alır. Reddedilmiş aile plakası,
  kırpım, recolor, mirror, kostüm değişimi veya türev temel kullanılamaz.
- İllüstrasyon alanında tabela, slogan, konuşma balonu, açıklama veya
  saçma/anlamsız okunabilir yazı yoktur.
- Mizah karttan türetilir; en fazla bir ikincil şaka vardır; aynı hayvan/tayfa/
  poz/şaka maskota dönüşmez.
- `unique render SHA`, sanatsal özgünlük kanıtı değildir.

### 6.3 Pilot ve tam yayılım

Önce 121 brief, 12 ön-yüz pilotu ve 7 arka-yüz taslağı teslim edilir. Sanat
Yönetmeninin bağımsız yaratıcı incelemesi ile kullanıcı ve Baş Editörün açık
pilot kabulü olmadan kalan kartlar veya tam PDF üretilmez.
Tam yayılımda aile ve tam deste contact sheetleri başlık/metin kapalı semantik
QA'dan geçer.

### 6.4 Arka yüz sözleşmesi

Yedi binary eşleme zorunludur: `BACK_CHARACTER=20`, `BACK_POWER=31`,
`BACK_LOYALTY=15`, `BACK_SEA_ROCK=42`, `BACK_ISLAND=6`,
`BACK_LIGHTHOUSE=4`, `BACK_SUPPORT=3`.

Arka yüzler metinsiz, önlerle aynı sanat dilinde, aile içinde exact aynı,
180° yön güvenli ve kesim/parlaklık/duplex sızıntısızdır. Sea=Rock ile Sadakat
özellikle kör fiziksel sınıflandırma testine tabidir.

## 7. Simülasyon hattı

Okuma kapsamı bütün projedir; yazma kapsamı `working/v2.7/qa/**`dır.

- Doğru baseline ve exact candidate belirlenir.
- Kimlik/mekanik, matematik, strateji, sosyal deneyim, öğretilebilirlik, görsel
  semantik kalite, okunabilirlik, PDF, baskı, manifest ve provenance ayrı
  katmanlarda denetlenir.
- 121 farklı hash, 121 özgün sanat olarak kabul edilmez; contact sheet ve
  kör insan semantik incelemesi gerekir.
- Resim-içi okunabilir yazı, dönem dışı nesne, tekrar eden yüz/poz/sahne/şaka,
  arka-yüz yön/kesim/parlaklık sızıntısı ayrı bulgudur.
- Sonuç `PASS`, `PASS_WITH_MINOR_ISSUES`, `FAIL` veya `BLOCKER` olur.
- Mekanik/görsel değişiklik uygulanmaz; kanıt ve öneri Baş Editöre gönderilir.
- Nihai kanıt `working/v2.7/qa/SIM_QA_ATTESTATION_v2.7.json` içinde exact
  candidate commitine bağlanır. Candidate değişirse eski attestation geçersizdir.

## 8. Baş Editör

- Handoffun görünür sohbet, dal, exact commit, kapsam ve kanıtını doğrular.
- Alan ihlalini geri çevirir; çakışmada kaynak önceliğini uygular.
- Kullanıcının yaratıcı/mekanik kararını kayda alır fakat kendiliğinden yeni
  kanon üretmez.
- Pilot ve tam aday için ayrı kabul/ret dispozisyonu verir.
- Simülasyon kapısından sonra release/kilit değerlendirmesi yapar.

## 9. Zorunlu handoff biçimi

```text
WORKSTREAM:
VISIBLE_CHAT:
VISIBLE_CHAT_ACK: YES
EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM
SOURCE_BRANCH:
SOURCE_COMMIT:
BASELINE_RELEASE:
SCOPE:
CHANGED_FILES:
PROTECTED_FIELDS_CONFIRMED:
TESTS_RUN:
RESULT:
OPEN_RISKS:
NEXT_RECIPIENT:
LOCK_REQUESTED: NO
```

Sanat Yönetimi teslimi ayrıca `ART_DIRECTION_STAGE`, `INPUT_VISUAL_COMMIT`,
`CREATIVE_VERDICT`, `FOULWAKE_WORLD_FIT`, `MATERIAL_AND_LINE_LANGUAGE`,
`COMPOSITION_AND_DECK_RHYTHM`, `KEEP`, `REMOVE` ve `REDRAW_BRIEF` verir.
Görsel teslim ayrıca `PILOT_OR_FULL`, `ART_BRIEF_MANIFEST`,
`CONTACT_SHEETS`, `TEXT_IN_ILLUSTRATION_CHECK`, `BACK_MAPPING_CHECK` ve
`REJECTED_ASSET_REUSE_CHECK` kanıtlarını verir. Simülasyon teslimi candidate
commit, komut, seed/örneklem, ham çıktı hashleri ve attestation yolunu verir.

## 10. Çakışma ve teslim kuralı

- Başka hattın alanı sessizce değiştirilmez.
- Sorun exact dosya/alan/commit ile handoff edilir.
- Baş Editör yönlendirmeden iki çözüm aynı dosyaya uygulanmaz.
- Sanat Yönetmeni ile Görsel Tasarım birbirinin yerine PASS veremez; yaratıcı
  yön ile final üretim ayrı exact handofflarla izlenir.
- Görünür sohbet + exact branch commit + zorunlu handoff + Baş Editör
  dispozisyonu birlikte yoksa iş tamamlanmış sayılmaz.
- GitHub'a yazılmış çıktı kendiliğinden kanon, PASS, release veya kilit değildir.
