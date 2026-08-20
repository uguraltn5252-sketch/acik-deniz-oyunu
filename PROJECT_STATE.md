# Project State

**Son güncelleme:** 20 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.6 STABLE / LOCKED**  
**Kanonik locked release:** `releases/v2.6/`  
**ACTIVE_DRAFT:** **v2.7 DRAFT / NOT LOCKED**  
**ACTIVE_BRANCH:** `v2.7-design`  
**ACTIVE_WORKSPACE:** `working/v2.7/`

## Baş editörlük ve release hazırlığı

Baş editörlük yönetişimi `governance/` altında yürürlüktedir. Hikâye, Görsel
Tasarım ve Simülasyon Testi hatları `af064df83ac4132c7d8d75aec67a3f1b51150fdb`
commitini çapraz denetlemiştir.

**Güncel release hükmü:** **BLOCKER — v2.7 kilitlenemez.**

Açık engellerin bağlayıcı listesi `governance/ACTIVE_WORKSTREAMS.json`, ayrıntılı
dispozisyonu `governance/COORDINATION_LOG.md` içindedir. Özet:

- `MEC-001`: Sea=Rock v2.7 DRAFT kararı kaydedildi; v2.6'dan bilgi-mimarisi farkı için tam yeniden test bekliyor.
- `SRC-001`: Kaynak sırası düzeltildi; güncel source → render → PDF kanıtı hâlâ eksik.
- `ART-001`: Tam 121 kartlık doğrulanabilir candidate yok.
- `QA-001`: v2.7 PASS yeniden üretilemiyor; exact commite bağlı tam QA attestation yok.
- `QA-002`: Fiziksel prova ve kör insan sosyal deneyim testi yok.
- `GOV-001`: `main` ile aktif dal çelişkili ve ayrışmış; release PR/status kapısı yok.

`CAN-001` çözüldü: `CAN-08/09` yalnız v2.7 DRAFT koruma ilkesi olarak
`TASLAK` sınıfına alındı; release kanonu iddiası kaldırıldı.

Bağlayıcı kullanıcı kararları `governance/DECISION_REGISTER.md`, sorumlu ve
teslimler `governance/WORKSTREAM_ASSIGNMENTS.md`, test eşikleri ise
`working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md` içindedir.

GitHub'a yazılan bir dosya kendiliğinden kanon veya release olmaz. Kilit için
proje sahibinin açık talimatı, kapanmış engeller, exact candidate commite bağlı
Simülasyon QA attestation'ı ve Baş Editör kilit tutanağı birlikte zorunludur.

## Locked baseline

v2.6 kullanıcı tarafından açıkça kilitlenmiştir, yalnızca okunur ve yerinde değiştirilmez.

Kanonik kaynak:

`releases/v2.6/`

## v2.7 temiz yeniden kuruluşu

Kullanıcının açık talimatıyla önceki `working/v2.7/` çalışma ağacı tamamen kaldırılmıştır.

Yeni `working/v2.7/`, `releases/v2.6/` Git ağacının eksiksiz ve birebir kopyası olarak yeniden oluşturulmuştur.

- v2.6 içindeki GitHub tarafından izlenen bütün dosyalar alınmıştır.
- Dosya içerikleri yeniden yazılmamış veya sürüm adı topluca değiştirilmemiştir.
- Kopyalanan dosyalar v2.6 kaynaklarıyla aynı Git blob kimliklerini taşır.
- Önceki v2.7 tasarım, hikâye, test, onay ve üretim kayıtları yeni çalışma ağacına aktarılmamıştır.
- Kilitli `releases/v2.6/` ağacı değiştirilmemiştir.
- Önceki v2.7, Git geçmişinden geri alınabilir durumdadır.

## Binary artefaktlar

GitHub deposunda büyük binary dosyaların kendileri yerine kanonik yol, boyut ve SHA-256 kayıtları tutulur.

Kilitli binary kaynaklar taşınmamış, yeniden yazılmamış veya silinmemiştir. Güncel v2.7 görsel taslak kayıtları `working/v2.7/BINARY_ARTIFACTS.md` içindedir.

## Current result

**v2.7 = ACTIVE STORY + VISUAL DRAFT / NOT LOCKED**

Temiz v2.6 kopyasına v2.7 anlatı ve görsel çalışma kaynakları eklenmiştir:

- `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md`
- `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md`
- `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json`
- `working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md`
- `working/v2.7/FOULWAKE_VISUAL_SYSTEM.md`
- `working/v2.7/BINARY_ARTIFACTS.md`
- `working/v2.7/V27_MECHANIC_DECISIONS.json`
- `working/v2.7/SOURCE_HIERARCHY_v2.7.json`
- `working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md`

Kural kitabının mevcut akışı korunarak yalnız 3.1, 3.3, 3.4 anlatı notu, 3.6 ve Bölüm 17 için v2.7 hikâye metni hazırlanmıştır. 20 Karakter ve 30 Güç kartının tam metin kaynağı v2.7'ye alınmış; yalnız seçili görünen ad ve flavor alanları güncellenmiştir.

Mevcut anlatı doğrulama kaydı kart sayıları, kimlikler, etkiler, zamanlamalar, başlangıç havuzu ve desteye dönüş alanlarını baseline ile aynı bildirir. Ancak kullanılan karşılaştırma scripti ve sabit baseline JSON'u GitHub'da bulunmadığından bu PASS yeniden üretilebilir veya release için bağlayıcı sayılmaz. Harita, Sadakat, Çürümüş Erzak ve yardımcı kartların değiştirilmediği beyan edilmiştir.

Görsel metin kaynağı netleştirilmiştir: değişmeyen mekanikler ve diğer kart
aileleri v2.6 baseline'ından; Karakter/Güç görünen metni v2.7 kart JSON'undan;
tanımlı anlatı blokları v2.7 rulebook story dosyasından alınır.

20 Ağustos 2026 tarihinde kullanıcı v2.7 kart ve kural kitabı için özgün görsel yönü onaylamıştır. Bu onay kilit değildir.

Aynı tarihte Açık Deniz ve Kayalık için ortak arka yüz v2.7 DRAFT kararı olarak
kaydedilmiştir. Bu karar v2.6'yı değiştirmez ve tam yeniden test olmadan release
edilemez.

Üretim örnekleri:

- KAR-01 Uzakgören karakter kartı yüzü
- GUC-24 Islak Çorap güç kartı yüzü
- HAR-AD-09 Deryanın Göbek Deliği harita kartı yüzü
- Deniz + Kayalık ortak arka yüzü
- 2 sayfalık gerçek ölçülü A4 baskı seti
- 29 sayfalık A4 kural kitabı görsel taslağı

Mizah tek bir fare maskotuna bağlanmaz. Fare, martı, beceriksiz veya hırsız tayfa, sessiz bakış ve nesne kaynaklı kuru mizah kart ailesi boyunca dönüşümlü kullanılır. Her illüstrasyonda en fazla bir ikincil görsel şaka bulunur.

Güncel branch'e bağlı tam 121 kartlık görsel candidate henüz tamamlanmamıştır.
Temiz reset öncesi tam deste/preflight yalnız tarihsel kanıttır. Aile aile üretim,
manifest, exact source eşlemesi ve fiziksel baskı provası beklemektedir.

Kilitli v2.6 hikâyesi, mekanikleri ve binary artefaktları değiştirilmemiştir. v2.7 hikâye ve görsel çalışmaları kanonlaştırılmamış ve kilitlenmemiştir.

## Lock rule

Yalnız kullanıcının açıkça `kilitle`, `stable yap` veya `release et` demesi v2.7 kilit sürecini başlatabilir.

Onay, beğeni veya `devam et` ifadesi kilitleme yetkisi değildir. Açık BLOCKER/FAIL, eksik candidate kanıtı veya geçersiz Simülasyon QA attestation'ı varken Baş Editör kilidi uygulamaz.
