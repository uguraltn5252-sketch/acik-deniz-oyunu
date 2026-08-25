# v2.7 Draft Binary Artifacts

**Durum:** DRAFT / NOT LOCKED / ACTIVE VISUAL CANDIDATE: NONE  
**Mekanik baseline:** v2.6 STABLE / LOCKED  
**Son görsel teslim:** `work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891`  
**Baş Editör dispozisyonu:** `REJECTED_ART / TECHNICAL_PIPELINE_REFERENCE_ONLY`

Bu kayıt, reddedilmiş binaryleri silmeden yanlışlıkla aktif aday sanılmalarını
önler. Aşağıdaki dosyalar teknik üretim/provenance tarihidir; sanat kaynağı,
pilot, release candidate veya kilitli artefakt değildir. Yeni reworkte
kopyalanamaz, dönüştürülemez veya aile plakası olarak kullanılamaz.

## Reddedilmiş tam dijital teslim

| Artefakt | SHA-256 | Boyut / sayfa | Sınıf |
|---|---|---|---|
| `FOULWAKE_v2.7_FULL_DECK_PRINT_CANDIDATE.pdf` | `09d3bb00b198426f749698744bfda8c5d11ccaca5a29f71072f3e47162c6afa4` | 152036797 byte / 48 A4 | REJECTED ART |
| `FOULWAKE_v2.7_FULL_DECK_VISUAL_REVIEW.pdf` | `a0b788b0e16c969b326869a5e21ee87e9772b1682735084e0ee475a2d3fe0ebb` | 189584635 byte / 16 A4 yatay | REJECTED ART |
| `FOULWAKE_v2.7_FULL_DECK_SOURCE_BUNDLE.zip` | `4d9f902fb73497ba48a43c0085a09d65b08aaf6b9defe69b8471fef10fe21ac8` | 163319630 byte / 139 girdi | REJECTED ART + STALE SELF-PROVENANCE |
| `FOULWAKE_v2.7_RULEBOOK_PRINT_CANDIDATE.pdf` | `00344a95563558f04c02465bf164538652c3bbab616a40e8083bf2c1862ad1fb` | 37533254 byte / 29 A4 | TECHNICAL REFERENCE ONLY |

Kayıt yolu `/Oyun-GitHub/v2.7/exports/` idi. Bu dosyalar yeniden aday yapılmaz.
Kaynak paketin 121 ön yüz üretmesine rağmen yalnız 6 aile illüstrasyon plakası
içermesi, `unique render SHA` değerlerinin özgün sanat kanıtı olmadığını
göstermiştir.

## Reddedilmiş önceki örnekler

| Örnek | SHA-256 | Sınıf |
|---|---|---|
| `KAR-01_Uzakgoren_front.png` | `b3605fb05e9baa77a60fa696d6851179501d57e1c6fa647ef54d3ff58c34e20d` | REJECTED ART |
| `GUC-24_Islak_Corap_front.png` | `a812249cda1f24cc64f4f5fe747d110f9b67ee3a24b285776be3f0e2e4c916a3` | REJECTED ART |
| `HAR-AD-09_Deryanin_Gobek_Deligi_front.png` | `b5d0aff9c531f9079ed416726362644e00103ecf95cb2cc4991ea5c7330f52ea` | REJECTED ART |
| `BACK_SEA_ROCK.png` | `c3cf3399c294874bb12194f9bdf369a00110b7c78d2a234590c16be864e74c45` | REJECTED / ROTATION-SAFETY FAIL |
| `FOULWAKE_v2.7_APPROVED_ART_DIRECTION_PRINT_SET.pdf` | `5d0aac67b5c746209c35662ebf2680f0819259e98ea3c5f4d629496c811cf5e2` | SUPERSEDED; NOT APPROVED |
| `FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf` | `cc3b36fb317c6469a34e51ec9c4baa49f2d420e2cbffec400e9ff629f93f5690` | TECHNICAL REFERENCE ONLY |

Dosya adındaki `APPROVED` sözcüğü güncel hüküm değildir; bu kayıttaki
`SUPERSEDED; NOT APPROVED` sınıfı üstündür.

## Bilinen provenance kusurları

- Eski preflight `font_table_has_embedded_dejavu=false` kaydı ile materialize
  edilen baskı PDF incelemesi çelişir.
- Kaynak ZIP içindeki self-provenance/final-commit alanları dış nihai kayıtla
  aynı sürüm değildir.
- Fiziksel baskı/kesim/duplex/ışık ve kör yön-sızıntı testleri yapılmamıştır.

Yeni üretim bu kayıtları düzeltmez veya üzerine yazmaz; yeni exact candidate
için iç/dış manifestler sıfırdan ve aynı commit/hashlerle oluşturulur.

## Yeni rework için beklenen kayıt

Aktif aday alanı şu anda `NONE`dır. Yeni aday kaydedilirken en az:

- 121 art brief, 121 özgün ön yüz ve 7 arka-yüz manifesti;
- 7 binary / 121 exact arka-yüz eşlemesi;
- text-in-illustration ve reddedilmiş varlık reuse kontrolleri;
- kör contact sheet semantik QA;
- exact source/blob → render SHA → PDF page/slot zinciri;
- iç/dış provenance eşitliği;
- fiziksel proof ve Simülasyon attestation

bulunur.

## Kilitli v2.6 artefaktları — yalnız referans

- Kural PDF SHA-256: `192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a`
- Kart PDF SHA-256: `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298`
- Full ZIP SHA-256: `ffc9c17c725e6093c62a3ebddc5f19c36fb0647f6a51a3e7014852fe0623d534`

`releases/v2.6/` değiştirilmemiştir.
