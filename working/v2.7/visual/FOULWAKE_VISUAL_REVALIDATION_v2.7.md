# FOULWAKE v2.7 — Tam Görsel Üretim Denetimi

**Durum:** FULL VISUAL DIGITAL CANDIDATE / PHYSICAL TESTS PENDING / NOT LOCKED  
**Görünür sohbet:** `FOULWAKE görsel tasarım`  
**Çalışma dalı:** `work/v2.7-visual`  
**Tam üretim taban commit:** `031c2a4d87ce7fc80d3c443723630e80f2388a70`  
**Tam üretim teslim commit:** `PENDING_FULL_PRODUCTION_COMMIT`  
**Baseline:** `v2.6 STABLE / LOCKED`

## Sonuç

Baş Editörün kabul ettiği ilk aşama kanıt onarımının ardından tam dijital görsel
aday üretildi. 121 kartın ön yüzü ve yedi arka yüz varlığı 300 dpi üretildi;
121 kartın tamamı ön/arka PDF sayfa ve duplex slotlarına bağlandı. Açık Deniz ve
Kayalık ailelerindeki 42 kart tek, metinsiz `BACK_SEA_ROCK` binary varlığını
kullanıyor. Güncel v2.7 anlatısına bağlı 29 A4 sayfalık kural kitabı adayı da
aynı kanonik ihracat konumunda saklandı.

Bu teslim dijital adaydır; fiziksel baskı/kesim/duplex/ışık ve kör yön-sızıntı
testleri yapılmadığı için release veya Simülasyon Testi handoff'u değildir.

## Bağlayıcı kaynak doğrulaması

| Kaynak | Beklenen kimlik | Sonuç |
|---|---|---|
| Card Texts | `38a03b71cd3232fd844db8d80d8e53662510b6a3` | PASS |
| Rulebook Story | `f1e0eb75434540a85e8b21484acd99ca0abc66cf` | PASS |
| Kilitli v2.6 kart PDF | `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298` | PASS |

`GUC-22 = Kaptanın Çatlak Kupası` ve `GUC-23 = Bayat Peksimet` eşlemesi
korundu. `GUC-24` flavor metni exact v2.7 kaynağındaki “Güverte kâtibi bunu
yanlış elde duran doğru eşya diye kaydetti.” cümlesidir.

## Tam deste üretim özeti

- Ön yüz: 121/121, benzersiz kart kimliği: 121/121, benzersiz render SHA-256:
  121/121.
- Aileler: 20 Karakter, 30 Güç, 1 Çürümüş Erzak, 15 Sadakat, 52 Harita ve 3
  yardımcı kart.
- Arka yüz: 7 binary varlık; eşleme toplamı 121/121.
- `BACK_SEA_ROCK`: 30 Açık Deniz + 12 Kayalık = 42 kart.
- Diğer altı arka yüz binarysi exact 180° simetrik üretildi.
- Tam baskı PDF'si: 48 A4 sayfa; her ön sayfanın hemen ardından uzun-kenar
  yatay aynalanmış duplex arka sayfası.
- Görsel inceleme PDF'si: 16 yatay A4 sayfa; 121 ön yüz.
- Kaynak paketi: 139 arşiv girdisi; 121 ön, 7 arka ve 6 özgün aile
  illüstrasyon plakası dâhil.

Kart başına exact visible-copy snapshotı, render SHA-256 değeri, ölçü/DPI,
arka yüz kimliği ve baskı sayfa/slot eşlemesi
`visual/manifests/FOULWAKE_v2.7_121_SOURCE_RENDER_PDF_MAP.json` dosyasındadır.

## Kural kitabı

Tam kural kitabı 29 A4 sayfadır. Güncel anlatı kaynaklı sayfalar 1, 3, 6, 7,
27, 28 ve 29; bağlayıcı `Mantar Can Halkası` terim bindirmeleri 16 ve 23.
Kalan mekanik sayfalar kilitli v2.6 baseline'dan görsel sistem içine alınmıştır;
mekanik veya lore hükmü üretilmemiştir.

## Kanonik save → materialize kanıtı

| Kanonik dosya | Library sürümü | Geri indirilen byte | Geri indirilen SHA-256 |
|---|---:|---:|---|
| `FOULWAKE_v2.7_FULL_DECK_PRINT_CANDIDATE.pdf` | 2 | 152036797 | `09d3bb00b198426f749698744bfda8c5d11ccaca5a29f71072f3e47162c6afa4` |
| `FOULWAKE_v2.7_FULL_DECK_VISUAL_REVIEW.pdf` | 2 | 189584635 | `a0b788b0e16c969b326869a5e21ee87e9772b1682735084e0ee475a2d3fe0ebb` |
| `FOULWAKE_v2.7_FULL_DECK_SOURCE_BUNDLE.zip` | 3 | 163319630 | `4d9f902fb73497ba48a43c0085a09d65b08aaf6b9defe69b8471fef10fe21ac8` |
| `FOULWAKE_v2.7_RULEBOOK_PRINT_CANDIDATE.pdf` | 0 | 37533254 | `00344a95563558f04c02465bf164538652c3bbab616a40e8083bf2c1862ad1fb` |

Değerler yalnız `/Oyun-GitHub/v2.7/exports/` kanonik konumundan geri
materialize edilen baytlardan hesaplandı. Bu dört dosya authored adaylarla
`cmp` üzerinden 4/4 byte-bayt eşleşti.

## Dijital preflight

- Başlangıç dal/head eşitliği:
  `work/v2.7-visual == 031c2a4d87ce7fc80d3c443723630e80f2388a70`.
- 121/121 kimlik, front render, source snapshot ve PDF page/slot eşlemesi.
- 300 dpi ve aileye göre exact piksel/taşmalı çalışma ölçüsü doğrulaması.
- Metin taşması ve kesim güvenli alanı kontrolü.
- Türkçe gliflerin kullanılan font cmap'lerinde bulunması.
- Temsilî OCR: 16/16 metin bloğu, 14/16 exact kimlik; İngilizce OCR kaynak
  otoritesi olmadığı için `PASS_WITH_SOFT_WARNING`.
- 7 arka yüz, 121 eşleme ve 42 kartlık `BACK_SEA_ROCK` ortak binary kontrolü.
- PDF sayfa/ölçü/XObject kontrolleri: kart baskı 48 A4, inceleme 16 yatay A4,
  rulebook 29 A4.
- Duplex dijital eşleme: 121/121; ön sayfa + 1 arka sayfa ve yatay ayna slotu.
- Kural kitabında dış font bağımlılığı yok; sayfalar 300 dpi raster XObject.
- Kanonik save, geri materialize, SHA-256/byte yeniden hesaplama ve local byte
  karşılaştırması: 4/4 PASS.
- Geri indirilen kaynak paketi içindeki Card Texts ve Rulebook Story dosyalarının
  Git blob kimliği doğrulaması: 2/2 exact PASS.

Dijital hüküm: `PASS_WITH_OCR_SOFT_WARNING`; dijital hard failure: `0`.

## Açık riskler

- Fiziksel baskı, kesim, duplex sapması ve opaklık/ışık testi:
  `PENDING_NOT_RUN`.
- Fiziksel kör yön-sızıntı testi: `PENDING_NOT_RUN`.
- OCR örnekleminde iki kimlik İngilizce model tarafından exact okunmadı;
  görsel kimlikler kontrol edildi, exact kaynak snapshotı/manifesti belirleyici
  kalır.

## Yetki alanı doğrulaması

Yalnız görsel çalışma alanındaki bu rapor, binary kayıtları ve görsel manifestler
değiştirildi. `releases/**`, `governance/**`, `PROJECT_STATE.md`,
`AI_HANDOFF.md`, `main`, v2.6 ve kilit alanlarına dokunulmadı. Geçici ajan
oluşturulmadı. Baş Editör kabulünden önce Simülasyon Testine geçilmez.
