# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.6 STABLE / LOCKED**  
**Kanonik locked release:** `releases/v2.6/`  
**ACTIVE_DRAFT:** **v2.7 DRAFT / NOT LOCKED**  
**ACTIVE_BRANCH:** `v2.7-design`  
**ACTIVE_WORKSPACE:** `working/v2.7/`

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

Onay kaydı: `working/v2.7/USER_REVIEW_APPROVAL_2026-08-19.md`.

### Tamamlanan v2.7 görsel aşamalar

- Design System / Reference Use Policy: PASS.
- Representative five-card gate: PASS / USER APPROVED.
- Card-back secrecy: PASS.
- Line-only / 2–3 second / digital real-size tests: PASS.
- 5x5 / 5x6 / 6x6 map table tests: PASS.
- Full 121-card inventory resolution: PASS.
- Full 121-card digital propagation: PASS DIGITAL / MINOR ISSUE.
- 121 front binary uniqueness: 121/121 unique SHA-256.
- Canonical text-fit validation: PASS.
- Full-deck visual review: 15 pages / PASS DIGITAL.
- Full-deck A4 print candidate: 46 pages / PASS DIGITAL.
- Full 29-page rulebook visual draft: PASS DIGITAL / MINOR ISSUE.
- Rulebook render QA: PASS.
- Historical / period-object audit: **PASS DIGITAL AFTER SELF-CORRECTION**.
- Final digital preflight: **PASS DIGITAL / PHYSICAL GATE PENDING**.

Historical audit sırasında iki dönem riski otomatik düzeltildi:

- `GUC-01A/B Can Simidi`: modern üretilmiş halka-can-simidi çağrışımı kaldırıldı; ip halkası + küçük ahşap yüzdürücü/fıçı yaklaşımı kullanıldı.
- `KAR-06 Dipgören`: modern dalgıç başlığı çağrışımı kaldırıldı; ağırlıklı kurtarma hattı / nefes tutarak dalış yaklaşımı kullanıldı.

### Açık kalan gerçek gate

- Physical card print / cut / duplex / real-light proof: **PENDING**.
- Physical rulebook proof: **PENDING**.

Rulebook iç tipografisinin locked kaynaktan büyük ölçüde miras kalması non-blocking bir MINOR görsel iyileştirme alanıdır; mekanik veya render hatası değildir.

## Artifact routing

Binary review/production outputs are archived under:

`/Oyun-GitHub/v2.7/exports/`

Exact hashes and paths are recorded in:

`working/v2.7/EXPORT_MANIFEST.json`

Current GitHub connector does not expose binary PDF upload; no GitHub binary upload is falsely claimed.

## Current result

**v2.7 = DRAFT / NOT LOCKED**

Dijital workflow tam deste + rulebook görsel taslağı + dönem denetimi + dijital preflight aşamasına kadar tamamlandı. Bilinen çözülmemiş dijital MAJOR ISSUE yoktur.

## Next gate

**Physical card/rulebook production proof.**

Only an explicit later user instruction such as `kilitle`, `stable yap` or `release et` may convert v2.7 to STABLE / LOCKED.
