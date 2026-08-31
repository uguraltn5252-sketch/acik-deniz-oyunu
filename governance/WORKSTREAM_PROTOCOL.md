# FOULWAKE Çalışma Hatları ve İletişim Protokolü

## 1. Yetki modeli

`governance/CURRENT_STAGE.json` tek güncel görev kaynağıdır. Uzman yazması
**default-deny**dır: dalın adı veya eski iş emri tek başına yetki vermez.
Yetki için aynı anda şunlar gerekir:

1. doğru görünür sohbet ve `VISIBLE_CHAT_ACK: YES`;
2. exact branch ve reset baseline;
3. `CURRENT_STAGE` içinde aktif iş;
4. `WORKSTREAM_SCOPE_BASELINES.json` içinde exact izin;
5. cumulative farkın dosya, adet, tür ve boyut/kelime sınırlarına uyması.

Tarihsel PASS, handoff veya iş emri yalnız kanıttır. Çelişkide iş durur ve
`BLOCKED_SOURCE_CONFLICT` ile Baş Editöre dönülür.

## 2. Zorunlu başlangıç

1. `AI_HANDOFF.md`
2. `governance/CURRENT_STAGE.json`
3. `PROJECT_STATE.md`
4. `governance/DECISION_REGISTER.md`
5. `governance/ACTIVE_WORKSTREAMS.json`
6. `governance/WORKSTREAM_ASSIGNMENTS.md`
7. Bu protokol
8. `governance/SUPERSESSION_MAP.json`
9. Exact iş emri ve kaynaklar

Başlamadan remote branch head, reset baseline, locked v2.6 tree SHA ve exact
authorization doğrulanır. Drift varsa üretim yapılmadan
`BLOCKED_BRANCH_DRIFT` veya `BLOCKED_SCOPE_DRIFT` verilir.

## 3. Resmî hatlar ve alan sınırları

| Hat | Görünür sohbet | Dal | Normal sahiplik |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` | `work/v2.7-story` | Lore ve mekanik olmayan görünen metin |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` | `work/v2.7-art-direction` | Sanat yönü, brief, kadraj ve bağımsız eleştiri |
| Görsel | `FOULWAKE Görsel Tasarım 2` | `work/v2.7-visual` | Yetkili özgün illüstrasyon, layout ve baskı çıktısı |
| Simülasyon | `Simülasyon Testi` | `work/v2.7-simulation` | Bağımsız QA/analiz kanıtı |
| Baş Editör | Bu sohbet | `v2.7-design` | Kanon, governance, entegrasyon, candidate, release ve lock |

Normal sahiplik aktif yetki değildir. Exact izin yoksa yazma yoktur.
`governance/**`, `releases/**`, `.github/**`, `AI_HANDOFF.md`,
`PROJECT_STATE.md`, `README.md` ve `CHANGELOG.md` yalnız Baş Editördedir.

Geçici alt ajan, proje sahibinin önceden açık izni yoksa kullanılmaz. İzinli
çıktı bile görünür uzman handoffunun yerine geçmez.

## 4. İçerik ve copy kilidi

Kart kimliği, adet, title, section label, effect, flavor, zamanlama, grup,
deste davranışı ve kural akışı uzman tarafından yeniden yazılamaz. Kaynak
önceliği `working/v2.7/SOURCE_HIERARCHY_v2.7.json` içindedir.

`SET-KP-01` için exact v2.7 copy:
`working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json`.

Görsel model okunabilir kart metni üretmez. İllüstrasyon metinsiz hazırlanır;
copy kanonik UTF-8 kaynaktan şablonla yerleştirilir. Final ön yüzde card-id,
title, section label, effect ve flavor OCR veya doğrudan render-source ile
exact karşılaştırılır. Manifestte `exact:true` beyanı kanıt değildir. Sapma
`BLOCKED_COPY_DRIFT`tir.

`SRC-002` çözülmeden GUC-22/GUC-23 kimlikleri tahminle değiştirilemez.

## 5. Sanat Yönetimi

Sanat Yönetmeni final raster/PDF üretmez ve metin/mekanik/lore değiştirmez.
Dünya hissi, çizgi/tarama/malzeme, dönem, palet, sahne ayrışması, kompozisyon,
kadraj ve deste ritmi için uygulanabilir hüküm verir.

Yüklenen KAPTAN kartı `SET-KP-01` için bağlayıcı görsel kaynaktır; “stil-only”
değildir. Küçük crop/ölçek/renk/arka-plan temizliği dışında figür ve ana
kompozisyon korunur. Gemi ve martı diğer kartlar için zorunlu değildir; deste
genelinde mürekkep/gravür/kâğıt/mat palet dili bağlayıcıdır.

Her ön/arka illüstrasyon için Sanat Yönetimi şunları kontrol eder:

- exact kart oranı ve illüstrasyon penceresi;
- 3 mm taşma ve 4–5 mm güvenli alan;
- özne ölçeği, odak, görsel denge ve gerekli negatif alan;
- yüz/el/ana nesne üzerinde anlamsız kesim;
- title/effect/flavor/card-id çakışması;
- thumbnail ve normal masa-mesafesi okunurluğu;
- aynı plan, aynı model veya el-merkezli kadraj tekrarı.

Görsel Tasarım kendi kadrajını onaylayamaz. Sonuç yalnız `FRAMING_PASS` veya
`REFRAME_REQUIRED`dır. PASS olmadan KEEP/final/tam üretim yoktur; sapma
`BLOCKED_FRAMING_DRIFT`tir.

## 6. Görsel üretim

Yalnız `CURRENT_STAGE` exact yetki verdiğinde çalışır.

- Her kart ayrı brief ve semantik olarak ayrı sahne alır.
- Reddedilmiş assetin crop/recolor/mirror/türev kullanımı yasaktır.
- `unique render SHA` özgün sanat kanıtı değildir.
- İllüstrasyonda tabela, slogan, konuşma balonu veya anlamsız okunabilir yazı yok.
- Arka yüz topolojisi exact `20+31+15+42+6+4+3=121`, yedi binarydir.
- Aile içinde exact aynı; metinsiz; 180° güvenli; kesim, değer, parlaklık,
  opaklık ve duplex sızıntısızdır.
- `BACK_SEA_ROCK` mat olmalı; `BACK_ISLAND` sıfırdan çizilmeli;
  `BACK_LIGHTHOUSE` daha büyük okunabilir ve uzun kaya sırtına bağlı olmamalıdır.
- Teknik preflight estetik/kadraj kabulünün yerine geçmez.

## 7. Simülasyon

Aktif exact candidate ve Baş Editör emri olmadan dal açılmaz. Yetkili testte:

- Data Analytics ile yeniden üretilebilir analiz, seed, komut, ham çıktı ve hash;
- kimlik/mekanik, matematik, strateji, sosyal deneyim, öğretilebilirlik;
- copy/kadraj/semantik görsel, arka-yüz bilgi sızıntısı;
- PDF, baskı, provenance ve fiziksel kanıt

ayrı gate'lerdir. Game Studio yalnız tarayıcı prototipi açıkça istenirse
kullanılır. Sonuç `PASS`, `PASS_WITH_MINOR_ISSUES`, `FAIL` veya `BLOCKER`dır.
Candidate değişirse eski attestation geçersizdir.

## 8. Araç ve eklenti sorumluluğu

Kurulu eklenti otomatik zorunlu değildir; görev için zorunlu araç exact iş
emrinde yazılır. Her handoff şunları doldurur:

- `TOOLS_USED`
- `PLUGINS_USED`
- `PLUGINS_AVAILABLE_BUT_NOT_USED`
- `NOT_USED_REASON`

Görsel üretimde kullanılan model, Figma/Canva ve dış editörler; Simülasyonda
Data Analytics ve varsa Game Studio açıkça beyan edilir. Beyansız araç sonucu
`BLOCKED_EVIDENCE_GAP` olarak ele alınır.

## 9. Handoff şablonu

```text
WORKSTREAM:
VISIBLE_CHAT:
VISIBLE_CHAT_ACK: YES
EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM
SOURCE_BRANCH:
SOURCE_COMMIT:
AUTHORIZATION_STAGE:
AUTHORIZATION_BASELINE:
BASELINE_RELEASE: v2.6 STABLE / LOCKED
SCOPE:
CHANGED_FILES:
PROTECTED_FIELDS_CONFIRMED:
COPY_SOURCE:
COPY_AUDIT:
FRAMING_DISPOSITION:
TESTS_RUN:
TOOLS_USED:
PLUGINS_USED:
PLUGINS_AVAILABLE_BUT_NOT_USED:
NOT_USED_REASON:
RESULT:
OPEN_RISKS:
NEXT_RECIPIENT: Baş Editör
TEMPORARY_SUBAGENTS: NONE
LOCK_REQUESTED: NO
```

Sanat Yönetimi ayrıca `ART_DIRECTION_STAGE`, `INPUT_VISUAL_COMMIT`,
`CREATIVE_VERDICT`, `KEEP`, `REMOVE`, `REDRAW_BRIEF` ve görsel başına kadraj
dispozisyonu verir. Görsel ayrıca art brief, provenance, contact sheet,
copy/OCR ve back-mapping kanıtı verir. Simülasyon candidate, seed/örneklem,
komut, ham çıktı hashleri ve attestation yolunu verir.

## 10. Candidate, release ve lock

Handoff, PASS tavsiyesi, commit veya hash candidate değildir. Candidate'ı yalnız
Baş Editör exact commit ve kanıtlarla ilan eder. Release için bağımsız
Simülasyon, fiziksel kanıt, kapanmış blockerlar ve proje sahibinin açık kabulü
gerekir. Kilit yalnız proje sahibinin açık `kilitle/stable/release` talimatıyla
Baş Editörce uygulanır.
