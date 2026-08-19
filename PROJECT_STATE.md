# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.6 STABLE / LOCKED**  
**Kanonik locked release:** `releases/v2.6/`  
**ACTIVE_DRAFT:** **v2.7 DRAFT / NOT LOCKED**  
**ACTIVE_BRANCH:** `v2.7-design`  
**ACTIVE_WORKSPACE:** `working/v2.7/` on the active draft branch

## Locked baseline

v2.6 kullanıcı tarafından açıkça kilitlenmiştir ve yerinde değiştirilmez.

- 118 ana kart: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita.
- 3 açık yardımcı kart: Kalkış Limanı / Varış-Hedef Limanı / Kaptan Makamı.
- Toplam 121 basılabilir fiziksel kart.
- Kural kitabı: 29 sayfa A4.
- Mekanik motor: doğrulanmış v2.5 baseline.

## Active v2.7 visual draft

v2.7, v2.6 mekaniklerini sessizce değiştirmeyen görsel üretim hattıdır.

Reference mode: `STYLE_ONLY`.

Kullanıcı 19 Ağustos 2026 tarihinde representative visual gate'i **açıkça onayladı**. Bu onay tam deste ve rulebook görsel üretimine geçişi yetkilendirdi; **release lock değildir**.

Active draft içindeki ayrıntılı durum:

- `working/v2.7/TEST_STATUS.md`
- `working/v2.7/V27_DRAFT_MANIFEST.json`
- `working/v2.7/EXPORT_MANIFEST.json`
- `working/v2.7/USER_REVIEW_APPROVAL_2026-08-19.md`

### Tamamlanan v2.7 aşamalar

- Representative visual gate: PASS / USER APPROVED.
- Card backs / secrecy / line-only / real-size / table tests: PASS DIGITAL.
- Full 121-card propagation: PASS DIGITAL / MINOR ISSUE.
- 121/121 unique front binaries.
- Full-deck visual review: 15 pages.
- Full-deck A4 print candidate: 46 pages.
- Full 29-page rulebook visual draft: PASS DIGITAL / MINOR ISSUE.
- Historical / period-object audit: **PASS DIGITAL AFTER SELF-CORRECTION**.
- Final digital preflight: **PASS DIGITAL / PHYSICAL GATE PENDING**.

Historical audit sırasında iki dönem riski otomatik düzeltildi:

- `GUC-01A/B Can Simidi`: modern üretilmiş halka-can-simidi çağrışımı kaldırıldı; ip halkası + küçük ahşap yüzdürücü/fıçı yaklaşımı kullanıldı.
- `KAR-06 Dipgören`: modern dalgıç başlığı çağrışımı kaldırıldı; ağırlıklı kurtarma hattı / nefes tutarak dalış yaklaşımı kullanıldı.

### Açık kalan gate

- Physical card print / cut / duplex / real-light proof: PENDING.
- Physical rulebook proof: PENDING.

Rulebook iç tipografisinin locked kaynaktan büyük ölçüde miras kalması non-blocking bir MINOR görsel iyileştirme alanıdır; mekanik veya render hatası değildir.

## Artifact routing

Binary outputs are archived under `/Oyun-GitHub/v2.7/exports/` in the user file library. Exact hashes and paths are recorded in the active draft `EXPORT_MANIFEST.json`.

## Current result

**v2.7 = DRAFT / NOT LOCKED**

Bilinen çözülmemiş dijital MAJOR ISSUE yoktur. Dijital workflow tam deste + rulebook görsel taslağı + dönem denetimi + dijital preflight aşamasına kadar tamamlandı.

## Next gate

**Physical card/rulebook production proof.**

Only an explicit later user instruction such as `kilitle`, `stable yap` or `release et` may convert v2.7 to STABLE / LOCKED.
