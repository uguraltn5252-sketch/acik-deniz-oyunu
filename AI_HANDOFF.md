# FOULWAKE AI Handoff Protokolü

Bu dosya yeni bir oturumun kanonik proje durumunu kısa ve doğrulanabilir
biçimde kurması için zorunlu başlangıç kaydıdır.

## Güncel hüküm

- **Son kullanıcı-onaylı sürüm:** `v2.6 STABLE / LOCKED`
- **Kanonik kilitli kaynak:** `releases/v2.6/`
- **Aktif çalışma:** `v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED`
- **Entegrasyon dalı:** `v2.7-design`
- **Aktif görsel candidate:** **YOK**
- **Gözlenen pilot paketi:** `work/v2.7-visual@0cb2bd6f03e2d84948741c162f22b8fd2ff064ad` / `THREE_TARGETED_REWORKS_KEEP_ONE_REWORK`
- **Simülasyon attestation:** **YOK**
- **Sanat Yönetimi:** `12 FRONT KEEP / 6 BACK KEEP / BACK_LIGHTHOUSE REWORK_REQUIRED`
- **Görsel üretim yetkisi:** `BACK_LIGHTHOUSE_ONLY_PILOT_REWORK`
- **Kilit izni:** **YOK**

Hikâye teslimi `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37`
üzerinde Görsel girdisi olarak kabul edilmiş ve exact kabul edilen üç Hikâye
blobu `v2.7-design`a entegre edilmiştir. Görsel teslim
`work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891`
üzerinde gerçekten yapılmıştır; ancak proje sahibi bütün ön ve arka yüz
sanatını reddetmiştir. Baş Editör dispozisyonu
`DELIVERED_REJECTED_ART_REWORK_REQUIRED`dır. Eski PDF/render/hash kayıtları
yalnız teknik üretim hattı referansıdır, release candidate değildir.

`FOULWAKE Sanat Yönetmeni` görünür sohbetinin iletişim testi önce
`ACKNOWLEDGED_COMMUNICATION_TEST_ONLY` olarak kabul edilmiştir. Ardından
`work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da`
üzerindeki Art Direction Bible, 121 kart brief manifesti, 12 pilot production
briefi ve 7 arka-yüz briefi Baş Editör incelemesini geçmiş; proje sahibi
`OPTION_2 — FAMILY-VISIBLE MAP BACKS` kararını ve nihai briefi açıkça
onaylamıştır. Paket `ART_DIRECTION_BRIEF_ACCEPTED` olarak `v2.7-design`a
entegre edilmiştir.

`work/v2.7-visual@b4afbcf49784b85338453cbf29a956cbb620c9e6`
üzerindeki brief-öncesi 12 ön-yüz + 7 arka-yüz pilotu, görünür `FOULWAKE
Sanat Yönetmeni` sohbetinde exact 22/22 Git blob doğrulamasıyla incelenmiştir.
Sonuç `REWORK_REQUIRED`dır: 3 ön yüz KEEP, 9 ön yüz REWORK; 7 arka yüzün
tamamı REWORK. Baş Editör incelemeyi kabul etmiş, ancak bağlayıcı sonraki
pilot setini kabul edilmiş zor-vaka 12'lisiyle sınırlandırmıştır. İki exact
KEEP (`SAD-H-03`, `HAR-KY-06`) yeniden kullanılacak; on kabul edilmiş pilot
kartı üretilecek/yeniden çizilecek ve yedi arka yüz sıfırdan kurulacaktır.
`GUC-24` provisional KEEP olarak sonraki tam-deste incelemesine saklanır; set
dışı altı ret bu pilot geçene kadar üretilmez. Yalnız bu pilot reworkü
etkindir; tam 121 üretim, PDF, Simülasyon, release ve kilit yetkili değildir.

Yetkili hedefli rework paketi Görsel dalında üretilmiştir: kanonik üretim
commit'i `bf944125ee35fecd722628f6a9be5f5dfcd5707a`, kanıt commit'i
`1ab579c27ee26205cbc87718995da021ef6da84d` ve temizlenmiş dal başı
`1b27232a53b09ac3ff00030f625bfc2703d15764`dır. Önceki görünür Görsel sohbet
nihai teslimi veremeden yanıt vermez hâle gelmiştir. Proje sahibinin açtığı
kalıcı halef `FOULWAKE Görsel Tasarım 2`, exact dal başını ve kaynakları
salt-okunur doğrulayıp `VISIBLE_CHAT_ACK: YES` vermiştir. Baş Editör bu devri
`PERMANENT_WORKSTREAM_SUCCESSOR_ACK_ACCEPTED` olarak kabul eder. Halef daha
sonra exact 62 dosyalık paket için görsele özgü final handoffu vermiş; Baş
Editör dal başını, grup sayımlarını, 61 dosyalık SHA-256 indeksini ve teknik
manifestleri doğrulayarak handoffu Sanat Yönetimi incelemesine giriş olarak
kabul etmiştir. Kanıt `governance/VISUAL_PILOT_HANDOFF_20260826.json`dır. Bu
kabul Sanat Yönetimi PASS'i, proje sahibi estetik kabulü, aktif candidate,
full production, Simülasyon, release veya kilit değildir.

Revize exact paket, görünür `FOULWAKE Sanat Yönetmeni` hattında 40/40
görsel açılarak bağımsız incelenmiştir. Sonuç `REWORK_REQUIRED`dır:
önlerde 10 KEEP / 2 REWORK (`KAR-01`, `HAR-AA-06`); arkalarda 5 KEEP /
2 REWORK (`BACK_ISLAND`, `BACK_LIGHTHOUSE`). On beş ana KEEP
byte-exact korunur. Dört render/source, yalnız `KAR-01` gate'i, beş contact
sheet, altı mevcut layout, bir rapor ve dört manifestten oluşan exact 25
dosyalık rework yetkilidir. Kanıt `governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`, uygulama
`working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md`dır. Tam 121, PDF, Simülasyon, release ve kilit değildir.

Dört ana varlıklı hedefli teslimin üretim commit'i
`88907294edd326c118573f5ada7406e5fc42ee4d`, rapor/manifest bağlama head'i
`0cb2bd6f03e2d84948741c162f22b8fd2ff064ad`dır. Git farkı exact 25/25 dosyadır; 15 ana KEEP ve 9 gate
byte-exact korunmuştur. Sanat Yönetmeni bu exact adayı inceleyerek
`KAR-01`, `HAR-AA-06` ve `BACK_ISLAND` varlıklarını KEEP vermiştir.
Yalnız `BACK_LIGHTHOUSE`, normal dijital masa-layout mesafesinde Fener
ailesi olarak güvenilir okunmadığı için `REWORK_REQUIRED`dır.

Yeni kapsam yalnız fener source/renderı, iki etkilenen contact sheet, altı
mevcut layout, bir rapor ve dört kanıt kaydıdır: exact 15 dosya. Diğer
18 ana görsel, 16 source-art, 10 gate ve üç etkilenmeyen contact sheet
byte-exact kalır. Kanıt `governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json`; iş emri `working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md`dır.

## Her oturumda zorunlu okuma sırası

1. `AI_HANDOFF.md`
2. `PROJECT_STATE.md`
3. `governance/EDITORIAL_CHARTER.md`
4. `governance/DECISION_REGISTER.md`
5. `governance/ACTIVE_WORKSTREAMS.json`
6. `governance/WORKSTREAM_ASSIGNMENTS.md`
7. `governance/WORKSTREAM_PROTOCOL.md`
8. `governance/CHIEF_EDITOR_AUDIT_20260825.md`
9. `governance/COORDINATION_LOG.md` içindeki en yeni kayıt
10. Sanat/Görsel çalışma için
    `working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`

Görsel çalışma ayrıca
`working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md`
dosyasını okumadan üretime başlayamaz.

## Resmî çalışma alanları

| Hat | Görünür sohbet | Dal | Yetki |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` | `work/v2.7-story` | Lore, anlatı ve mekanik olmayan görünen metin |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` | `work/v2.7-art-direction` | Sanat yönü, görsel dramaturji, brief ve bağımsız yaratıcı eleştiri |
| Görsel | `FOULWAKE Görsel Tasarım 2` | `work/v2.7-visual` | Özgün illüstrasyon, yerleşim, tipografi, baskı |
| Simülasyon | `Simülasyon Testi` | `work/v2.7-simulation` | Bağımsız QA ve kanıt; mekanik değişiklik yok |
| Baş Editör | Bu çalışma | `v2.7-design` | Kanon, çakışma, entegrasyon, release ve kilit |

Resmî uzman işi yalnız doğru görünür sohbetten
`VISIBLE_CHAT_ACK: YES`, exact dal/commit ve zorunlu handoff alanlarıyla
geldiğinde o hatta mal edilir. Geçici alt ajan oluşturmak yasaktır; çok zorunlu
istisna ancak proje sahibinin önceden açık izniyle mümkündür ve yine uzman
teslimi sayılmaz.

## Güncel kanıt kayıtları

- İlk üç hat iletişim testi: `governance/VISIBLE_CHAT_ACKS_20260820.json` —
  yalnız 3/3 `COMMUNICATION_TEST_ONLY` ACK.
- Sanat Yönetimi iletişim testi: `governance/ART_DIRECTION_ACK_20260825.json` —
  tarihsel ACK kaydıdır.
- Sanat Yönetimi brief teslimi ve proje sahibi onayı:
  `governance/ART_DIRECTION_HANDOFF_20260825.json` — exact `7418d9c2...`
  paketi kabul edildi; yalnız pilot aşaması yetkilidir.
- Exact pilot yaratıcı incelemesi:
  `governance/ART_DIRECTION_PILOT_REVIEW_20260825.json` — `b4afbcf...`
  için `REWORK_REQUIRED`; bağlayıcı uygulama emri
  `working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md`.
- Hikâye teslimi: `governance/STORY_HANDOFF_20260820.json` —
  `ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT`.
- Görsel teslim ve ret: `governance/VISUAL_HANDOFF_20260825.json` —
  `REJECTED_ART_REWORK_REQUIRED`.
- Kalıcı Görsel halef ACK'i: `governance/VISUAL_SUCCESSOR_ACK_20260826.json` —
  `PERMANENT_WORKSTREAM_SUCCESSOR_ACK_ACCEPTED`; üretim teslimi değildir.
- Revize pilotun resmî Görsel handoffu:
  `governance/VISUAL_PILOT_HANDOFF_20260826.json` — exact `1b27232a...`
  paketi yalnız Sanat Yönetimi incelemesine giriş için kabul edildi.
- Son Baş Editör denetimi: `governance/CHIEF_EDITOR_AUDIT_20260825.md`.

GitHub'a yazılmış olmak bir çıktıyı kendiliğinden kanon, PASS, STABLE veya
LOCKED yapmaz.

## Kaynak önceliği

1. Proje sahibinin en yeni açık kararı.
2. Değişmeyen mekanik ve içerik için `v2.6 STABLE / LOCKED`.
3. `governance/DECISION_REGISTER.md` içindeki aktif v2.7 DRAFT kararları.
4. `working/v2.7/SOURCE_HIERARCHY_v2.7.json` içindeki alan kaynakları.
5. Taslak üretim ve kanıt dosyaları.

Çelişki otomatik seçilmez; çalışma durur ve Baş Editöre handoff edilir.

### Açık kaynak çelişkisi: `SRC-002`

Kilitli v2.6 kayıtları Bayat Peksimet'i `GUC-22` olarak gösterirken aktif v2.7
Card Texts `GUC-22 = Kaptanın Çatlak Kupası`, `GUC-23 = Bayat Peksimet` der.
Exact baseline/script kanıtı GitHub'da yoktur. Bu kimlikler tahminle
değiştirilemez; Simülasyon/baş editör exact karşılaştırması beklenir.

## Bağlayıcı görsel rework özeti

- KAPTAN görseli yalnız sanat dili için `STYLE_ONLY`; karakter, yüz, poz,
  kompozisyon veya piksel kopyalanmaz.
- 121 kartın her biri ayrı art brief ve semantik olarak ayrı özgün sahne alır.
- Önceki altı aile plakası ve türevleri kullanılamaz.
- İllüstrasyon alanında tabela, slogan, konuşma balonu, açıklama veya saçma /
  anlamsız okunabilir yazı yoktur.
- Okunabilir metin yalnız exact başlık, effect, flavor ve kart kimliğidir.
- `unique render SHA`, özgün sanat kanıtı değildir; kör contact-sheet incelemesi
  zorunludur.
- Arka yüz topolojisi 7 binarydir: Karakter 20; Güç+Çürümüş 31; Sadakat 15;
  Deniz+Kayalık 42; Ada 6; Deniz Feneri 4; yardımcı 3.
- Arka yüzler ön yüzlerle aynı sanat dilindedir fakat ön yüzün kopyası değildir;
  metinsiz, aile içinde exact aynı ve 180° yön güvenlidir.
- Harita arka yüzlerinde aile görünürlüğü bağlayıcıdır: `BACK_SEA_ROCK` genel
  denizdir ve Açık Deniz/Kayalık ayrımını gizler; `BACK_ISLAND` anonim genel
  adayı, `BACK_LIGHTHOUSE` 1721'e uygun anonim genel feneri açıkça gösterir.
  Hiçbiri exact ön kartı veya sonucu sızdırmaz.
- Sabit 5×5/grid/kart sayısı şartı yoktur; değişken, kurala uygun masa
  düzenlerinde ortak harita-denizi, 180° güvenliği ve bilgi körlüğü test edilir.
- Sanat Yönetmeni salt kontrol listesi değil; dünya, doku, kompozisyon, karakter
  ayrışması ve deste ritmi için yaratıcı brief/eleştiri üretir. Final görseli
  Görsel Tasarım üretir; nihai estetik karar proje sahibinindir.
- Kabul edilmiş zor-vaka setindeki 12 ön-yüz pilotu ve sıfırdan yedi arka-yüz,
  Sanat Yönetmeni incelemesi ile kullanıcı + Baş Editör onayı almadan tam 121
  üretime geçilmez. `b4afbcf...` bu kapıda `REWORK_REQUIRED` almıştır.

## v2.6 kilitli omurga

- 118 ana kart: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita.
- 3 yardımcı kart: `SET-KL-01`, `SET-VL-01`, `SET-KP-01`; toplam 121 basılabilir
  fiziksel kart.
- Mahkûm için ayrı kart/token yoktur; Moderatör not alır.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- v2.6 Kayalık arka yüzü Açık Denizden ayrıdır. Sea=Rock yalnız v2.7 DRAFT
  kararıdır ve tam yeniden test gerektirir.
- Kilitli artefakt hashleri `releases/v2.6/V26_RELEASE_MANIFEST.json` ve
  `releases/v2.6/SHA256SUMS.txt` içindedir.

## Kilit kuralı

Kilit sürecini yalnız proje sahibinin açık `kilitle`, `stable yap` veya
`release et` talimatı başlatır; kilidi yalnız Baş Editör uygular. Açık
`FAIL/BLOCKER`, eksik exact candidate, eksik fiziksel kanıt veya geçersiz
Simülasyon attestation varken sürüm kilitlenmez.

## Güncel devam komutu

> `v2.7-design` üzerindeki `governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json` ve `working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md`
> kaynaklarını oku. `FOULWAKE Görsel Tasarım 2`, exact
> `work/v2.7-visual@0cb2bd6f03e2d84948741c162f22b8fd2ff064ad` başından yalnız `BACK_LIGHTHOUSE`
> source/renderı ile iki contact sheet, altı mevcut layout, bir rapor ve dört
> kanıt kaydını değiştirerek 15 dosyalık son hedefli reworkü uygulasın. Başka
> ana görsel, source-art, gate, sheet, geometri, tam 121, PDF, Simülasyon,
> release veya kilit yoktur.
