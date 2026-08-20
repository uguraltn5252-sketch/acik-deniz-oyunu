# FOULWAKE v2.7 - Görsel Tasarım İlk Aşama Kanıt Onarımı

**Durum:** VISUAL WORKSTREAM DELIVERED / DRAFT / NOT LOCKED  
**Görünür sohbet:** `FOULWAKE görsel tasarım`  
**Çalışma dalı:** `work/v2.7-visual`  
**Giriş commit:** `e04eef7f1fef6ea407feaaf26558551297c44b37`  
**Rework taban commit:** `66e54d08d21370c00476769094db62d4e428cde6`  
**Görsel teslim commit:** `d3028779f371337a5abffa691067de8fc42bdec1`  
**Baseline:** `v2.6 STABLE / LOCKED`

## Sonuç

Reddedilen ilk aşama handoff'unun kanıt zinciri onarıldı. Bu teslim tam deste
veya release candidate değildir. Temsilî dosyalar kanonik
`/Oyun-GitHub/v2.7/exports/` konumuna kaydedildi, yeniden indirildi ve aşağıdaki
hash/byte kayıtları yalnız bu geri indirilen baytlardan hesaplandı.

- 121/121 benzersiz kimlik kilitli v2.6 kart PDF'siyle eşleşti.
- Aile sayıları: 20 Karakter, 30 Güç, 1 Çürümüş Erzak, 15 Sadakat, 52 Harita ve
  3 yardımcı kart.
- Açık Deniz + Kayalık toplam 42 kart, tek `BACK_SEA_ROCK` varlık kimliğine
  bağlandı. PDF içindeki dört temsilî kopya aynı image XObject'i kullanıyor.
- `KAR-01`, `GUC-24` ve `HAR-AD-09` gerçek ölçülü temsilî renderları 300 dpi.
- `GUC-24` üzerindeki eski flavor metni exact v2.7 kart kaynağına düzeltildi.
- Baş Editör kararı uygulandı: `GUC-22 = Kaptanın Çatlak Kupası`,
  `GUC-23 = Bayat Peksimet`. Kilitli v2.6 belgeleri değiştirilmedi.
- Baskı setinin üzerinde `KAR-01`/`GUC-24` v2.7 visible-copy kaynağı ile
  `HAR-AD-09` kilitli v2.6 visible-copy kaynağı ayrı ve exact gösterildi.
- Kart kimlikleri baskı güvenli alanına taşındı ve temsilî overflow/glif kontrolü
  geçti.
- Kural kitabı için `3.3`, `3.4` ve `3.6` bloklarını exact
  `f1e0eb75434540a85e8b21484acd99ca0abc66cf` blobundan kullanan 2 sayfalık A4 prova üretildi ve kanonik
  konumda gerçekten saklandı.

## Kaynak doğrulaması

| Kaynak | Beklenen blob | Sonuç |
|---|---|---|
| Story Framework | `962222d83d669763c4ac8e2765f024b9fade180c` | PASS |
| Rulebook Story | `f1e0eb75434540a85e8b21484acd99ca0abc66cf` | PASS |
| Card Texts | `38a03b71cd3232fd844db8d80d8e53662510b6a3` | PASS |
| v2.6 kart PDF | `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298` | PASS |

## Temsilî artefakt zinciri

| Kaynak | Render | PDF eşlemesi | Hüküm |
|---|---|---|---|
| Card Texts `KAR-01` | `KAR-01_Uzakgoren_front.png` | kart baskı seti s.1 | PASS |
| Card Texts `GUC-24` | `GUC-24_Islak_Corap_front.png` | kart baskı seti s.1 | PASS - stale flavor düzeltildi |
| v2.6 baseline `HAR-AD-09` | `HAR-AD-09_Deryanin_Gobek_Deligi_front.png` | kart baskı seti s.1 | PASS |
| DEC-20260820-01 | `BACK_SEA_ROCK.png` | kart baskı seti s.2, 4 aynı XObject | PASS - binary eşleme |
| Rulebook Story `3.3/3.4/3.6` | A4 temsilî sayfalar | rulebook proof s.1-2 | PASS |

Ayrıntılı SHA-256 ve sayfa eşlemeleri
`visual/manifests/FOULWAKE_SOURCE_RENDER_PDF_PROVENANCE_v2.7.json` içindedir.

## Baş Editör dispozisyonu

Bu rework için bağlayıcı eşleme `GUC-22 = Kaptanın Çatlak Kupası` ve
`GUC-23 = Bayat Peksimet` olarak uygulandı. `releases/v2.6/**` içindeki tarihsel
belge satırı değiştirilmedi. Uyuşmazlık artık görsel üretim açısından açık risk
değildir.

## Eski 29 sayfalık görsel taslak

Mevcut `FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf`, v2.6 iç sayfalarını yeniden
stilleyen tarihsel taslaktır; güncel v2.7 anlatı bloklarının yerleşimini
kanıtlamaz. Dosya silinmedi veya değiştirilmedi ancak güncel source -> render ->
PDF kanıtı olarak kullanılmayacaktır.

## Çalıştırılan kontroller

- Rework başlangıcında branch/head compare:
  `work/v2.7-visual == 66e54d08d21370c00476769094db62d4e428cde6`.
- Üç bağlayıcı hikâye blobu exact SHA karşılaştırması.
- v2.6 kart PDF SHA-256 doğrulaması ve regex ID çıkarımı.
- Envanter/PDF ID seti: 121/121, tekrar 0, eksik 0, fazla 0.
- Aile ve arka yüz eşleme sayımları.
- PNG piksel/DPI ve kaynak illüstrasyon çözünürlüğü kontrolü.
- PDF sayfa/ölçü (`pdfinfo`), efektif görsel DPI ve XObject tekrarı
  (`pdfimages -list`), font/glif ve render kontrolü.
- 180 dpi yeniden render ile görsel taşma, kesim ve hiyerarşi denetimi.
- `GUC-24` ve `HAR-AD-09` OCR spot kontrolü.
- Kanonik konuma save/replace ve ardından altı dosyanın yeniden materialize
  edilmesi.
- Geri indirilen kanonik baytların yerel authored baytlarla `cmp`, SHA-256 ve
  byte boyutu karşılaştırması: 6/6 PASS.

## Açık riskler

- Tam 121 kartın güncel sanat diliyle renderı ve tam kart PDF'si henüz yok.
- Tam 29 sayfalık v2.7 rulebook entegrasyonu henüz yok.
- Ortak arka yüzün kör kart-yönü / Deniz-Kayalık sızıntı testi yapılmadı.
- Fiziksel baskı, kesim, duplex sapması, opaklık ve gerçek ışık testi yapılmadı.

Tam 121 kart/29 sayfa üretimine ve Simülasyon Testi handoff'una bu kanıt onarımı
Baş Editör tarafından kabul edilmeden geçilmeyecektir.

Bu açık riskler nedeniyle `SRC-001` yalnız temsilî zincirde ilerlemiştir;
`ART-001`, `MEC-001` ve `QA-002` kapanmış sayılmaz.
