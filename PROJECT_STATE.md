# FOULWAKE Proje Durumu

**Son güncelleme:** 30 Ağustos 2026  
**Kilitli baseline:** `v2.6 STABLE / LOCKED`  
**Aktif taslak:** `v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED`  
**Entegrasyon:** `v2.7-design`  
**Aktif visual candidate:** **YOK**  
**Güncel aşama:** `STAGE-20260830-KAPTAN-FRAMING-PATCH-CORRECTION`  
**Genel hüküm:** **BLOCKER — üretim, Simülasyon, release ve kilit kapalı**

## Bağlayıcı proje sahibi düzeltmeleri

Exact `23c062f6...` pilotu estetik olarak reddedildi. Önceki
`PILOT_ART_DIRECTION_PASS` yalnız tarihsel inceleme kanıtıdır ve yeni iş,
candidate veya kabul yetkisi vermez.

Yüklenen KAPTAN kartı `SET-KP-01` için bağlayıcı görsel ve görünen copy
kaynağıdır. Önceki farklı ad/boş sandalye çözümü v2.7 için geçersizdir.

| Alan | Exact hüküm |
|---|---|
| Başlık | `KAPTAN` |
| Bölüm | `ÖZEL YETENEK` |
| Etki | `Oylamada eşitlik olursa, senin tarafın geçerli olur.` |
| Flavor | `Lidere et. Gemi senin emrinde.` |
| Görsel | Yüklenen KAPTAN figürü/kompozisyonu; yalnız küçük crop/ölçek/renk/arka-plan düzeltmesi |
| Deste dili | Kalın mürekkep, yoğun gravür taraması, sıcak kirli kâğıt, mat lacivert–oker–pas |
| Yasak | KAPTANı boş sandalye/başka figürle değiştirmek; görünen copyyi yeniden yazmak |

KAPTAN görselindeki gemi ve martı diğer kartlarda tekrarlanmak zorunda değildir.

Bütün final metin kanonik UTF-8 kaynaktan şablonla yerleştirilir. Görsel model
kart yazısı üretemez; OCR/render-source exact karşılaştırması olmadan KEEP yoktur.
Sapma `BLOCKED_COPY_DRIFT`tir.

Bütün ön/arka illüstrasyonları Sanat Yönetmeni bağımsız kadraj kapısından
geçirir. Görsel Tasarım kendi kadrajını onaylayamaz. Yalnız `FRAMING_PASS` veya
`REFRAME_REQUIRED`; sapma `BLOCKED_FRAMING_DRIFT`.

## Arka yüzler

- `BACK_SEA_ROCK`: mat ve ışıldamayan deniz için rework.
- `BACK_ISLAND`: eski varlık türetilmeden tam yeniden çizim.
- `BACK_LIGHTHOUSE`: fener büyütülür; uzun kayalık sırt şart değildir.
- Diğer dört arka: proje sahibi tarafından kabul edilmiş sayılmaz; HOLD.

## Çalışma hatları

| Hat | Reset baseline | Güncel durum | Yazma yetkisi |
|---|---|---|---|
| Hikâye | `e04eef7f...` | Tarihsel kabul; beklemede | YOK |
| Sanat Yönetimi | `11913681...` | Mevcut 437 kelimelik patch eksik | Yalnız aynı patch dosyasında 1 dosya / ≤700 kelime düzeltme |
| Görsel | `23c062f6...` | Pilot reddedildi; üretim durdu | YOK |
| Simülasyon | Dal yok | Başlamadı | YOK |
| Baş Editör | `v2.7-design` | Governance denetimi ve entegrasyon | Governance/kaynak düzeltmesi |

Sanat Yönetimi patchi, KAPTANın ana kart görsel kaynağı olduğunu ve kadraj
kapısını açıkça eklemeden kabul edilemez. Patch kabul edilse bile altı thumbnail
için yeni Baş Editör emri gerekir.

## Açık blockerlar

| ID | Durum | Kapanış |
|---|---|---|
| `ART-001` | Pilot owner-rejected | Yeni hızlı kapılar + proje sahibi kabulü |
| `SRC-002` | GUC-22/GUC-23 kimlik çelişkisi | Proje sahibi exact seçenek kararı |
| `MEC-001` | Sea=Rock tam test edilmedi | Yetkili candidate sonrası Simülasyon |
| `QA-001/002` | Candidate ve fiziksel kanıt yok | Candidate, dijital ve fiziksel QA |
| `GOV-001` | Branch protection uygulanamıyor | GitHub planı/visibility izin verdiğinde ruleset |
| `PHYSICAL-PROOF` | Baskı/kesim/duplex/ışık/masa testi yok | Gerçek fiziksel test |

`SRC-002` için doğrulanmış karşılaştırma:
`governance/SRC_002_COMPARISON_20260830.json`. Tahminle düzeltme yasaktır.

## Kanonik güncel kayıtlar

- `governance/CURRENT_STAGE.json` — tek aktif görev ve yetki.
- `governance/PROJECT_OWNER_KAPTAN_COPY_CORRECTION_20260830.json` — KAPTAN
  görsel/copy düzeltmesi.
- `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` — exact copy.
- `governance/WORKSTREAM_SCOPE_BASELINES.json` — uzman dal reset/scope sınırları.
- `governance/SUPERSESSION_MAP.json` — tarihsel PASS ve emir sınıflandırması.
- `governance/CHIEF_EDITOR_SYSTEM_AUDIT_20260830.md` — kapsamlı denetim.

## Release hükmü

v2.6 yerinde değiştirilemez. v2.7 ancak exact candidate, bağımsız Sanat
Yönetimi, proje sahibi kabulü, copy/kadraj kontrolleri, Simülasyon attestation,
fiziksel kanıt ve açık lock talimatı birlikte olduğunda değerlendirilebilir.
