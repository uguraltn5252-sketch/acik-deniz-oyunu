# FOULWAKE v2.7 Release Blocker Çözüm Planı

**Durum:** CHIEF EDITOR PROVISIONAL QA PLAN / CURRENT VERDICT BLOCKER  
**Güncelleme:** 25 Ağustos 2026  
**Baseline:** v2.6 STABLE / LOCKED; mekanik motor v2.5  
**Aktif product candidate:** NONE

Bu plan **RESMÎ SİMÜLASYON TESLİMİ DEĞİLDİR**. Görünür `Simülasyon Testi`
sohbeti exact yeni candidate üzerinde `VISIBLE_CHAT_ACK: YES` handoffuyla
uygulamadan PASS, attestation veya blocker kapanışı üretmez.

`work/v2.7-visual@e91581...` teknik teslimi sanat yönü nedeniyle reddedilmiştir
ve test candidate'ı değildir. Önce yeni görsel pilot/tam aday Baş Editörce kabul
edilir, sonra ürün commit'i `C` olarak dondurulur.

## 1. Candidate ve kontrol modeli

- **C:** kabul edilmiş tam v2.7 ürün commit'i; metin, sanat, render, PDF ve
  manifestler sabit.
- **A kontrolü:** C ile aynı kart/metin/sanat; yalnız v2.6 ayrı Deniz/Kayalık
  bilgi modeli.
- **B adayı:** C ile aynı kaynaklar; v2.7 ortak Sea=Rock arka yüz modeli.

Candidate commit değişirse bütün önceki test, hash ve attestation geçersizdir.

## 2. Kaynak ve kimlik kapısı

- `releases/v2.6/**` Git blob ağacı değişmemiş olmalı.
- 121 basılabilir kimlik: 20 Karakter, 30 Güç, 1 Çürümüş Erzak, 15 Sadakat,
  52 Harita, 3 yardımcı.
- Kart kimliği, effect, zamanlama, grup, start/returns ve deste davranışı exact
  baseline ile karşılaştırılır; whitelist dışı fark `BLOCKER`dır.
- `SRC-002`: Kilitli v2.6 PDF/source paketinden exact Güç tablosu çıkarılır;
  `GUC-22` ve `GUC-23` ad/effect eşlemesi v2.7 Card Texts ile raporlanır.
  Tahmin veya sessiz yeniden numaralandırma yapılmaz.
- Narrative whitelist yalnız onaylı ad/flavor ve rulebook 3.1, 3.3, 3.4, 3.6,
  17 anlatı bloklarıdır.

## 3. Mekanik ve gizli bilgi

- Geometri sonucu `51.204 teorik / 51.102 yasal / 102 reddedilen` değişmez.
- 6–15 oyuncu, altı harita şekli ve kısa/standart/uzun süreler test edilir.
- Yetkisiz oyuncuya kapalı kart kategorisi/kimliği sızıntısı: `0`.
- Yetkili Ufuk bakışı, kamusal açma ve Geçilmez davranışında yanlış bilgi: `0`.
- En az `1.000.000` stateful fuzz eylemi; motor/invariant hatası ve kalıcı rota
  kilidi: `0`.
- Birden fazla rota varken rota-relevant bilgi olmadan salt tahmin kararları en
  fazla `%40`.

## 4. Sayısal ve stratejik paired A/B

10 oyuncu sayısı × 6 harita × 3 süre × en az 2.500 eşlenmiş oyun =
`450.000` A/B oyun çifti; üç ayrı seed bloğu.

- Dengeli/sosyal genel Tayfa kazanması `%45–55`; her hücre `%40–60`.
- Hücre başına %95 güven aralığı yarı genişliği en fazla 2 puan.
- B–A genel fark en fazla 5 puan; tek hücrede en fazla 10 puan.
- Medyan oyun süresi/gün artışı en fazla `%15`.
- `social – random` en az 8; `crew_omniscient – social` en az 10;
  `social – traitor_omniscient` en az 20 puan.
- Sabit sol/orta/sağ politika sosyal politikayı 3 puandan fazla geçemez.
- Özel/kamusal bilgi karşı-olgusal rota kararlarının en az `%15`ini değiştirir.

Sınır aşımı `FAIL`; illegal durum, sızıntı veya motor hatası `BLOCKER`dır.

## 5. Görsel sanat ve semantik QA

### 5.1 Rejected-asset guard

- e91581 teslimindeki ön/arka render, altı aile illüstrasyon plakası, kırpım,
  recolor, mirror, rotate, kostüm varyasyonu ve türev temel reuse: `0`.
- Her kartta `art_brief_id`, `original_artwork_id`,
  `rejected_asset_reused=false` ve kaynak kayıtları bulunur.

### 5.2 Contact-sheet incelemesi

- 121 ön yüz aile bazında ve tam deste contact sheet olarak oluşturulur.
- İkinci sette başlık, effect, flavor ve kimlik kapatılır.
- En az iki bağımsız insan inceleyici aynı yüz, saç/sakal, beden, poz, kadraj,
  sahne, siluet, arka-plan, hayvan veya şaka tekrarlarını işaretler.
- Karakterlerde isimler kapalıyken 20/20 ayırt edilebilirlik zorunludur.
- Diğer ailelerde yalnız farklı başlık/metin nedeniyle farklı görünen türev
  sahne kabul edilmez.
- `unique render SHA`, özgünlük PASS'i üretemez.

### 5.3 Stil, dönem, yazı ve mizah

- KAPTAN yüklenen owner source'a exact bağlıdır; ana figür/kompozisyon korunur,
  diğer kartlarda KAPTAN yüzü/pozu/gemi/martı tekrarı: `0`.
- Çizgi/tarama/mat palet ve eski baskı tutarlılığı: bütün ailelerde PASS.
- Modern nesne, büyü, parlak 3B/dijital boya sapması: `0`.
- İllüstrasyonda tabela, slogan, konuşma balonu, açıklama veya anlamsız
  okunabilir harf/sayı/kelime: `0`.
- Okunabilir copy yalnız exact şablon alanlarında bulunur.
- İllüstrasyon başına ikincil şaka en fazla 1; tekrar eden maskot/şaka serisi
  MAJOR, bilgi veya ana olayı bastırması BLOCKERdır.

Bir tek reddedilmiş varlık reuse, okunabilir resim-içi yazı, bilgi sızıntısı ya
da aynı temel sanatın sistematik tekrarı `ART-001 BLOCKER`dır.

## 6. Arka yüz kapısı

Exact topoloji:

`BACK_CHARACTER=20`, `BACK_POWER=31`, `BACK_LOYALTY=15`,
`BACK_SEA_ROCK=42`, `BACK_ISLAND=6`, `BACK_LIGHTHOUSE=4`,
`BACK_SUPPORT=3`; toplam 7 binary / 121 eşleme.

- Aile içindeki bütün kopyalar byte/piksel exact aynı.
- Yedi varlığın tamamı metinsiz ve exact 180° dönüş güvenli.
- Kesim/kenar/parlaklık/opaklık/duplex yön veya aile sızıntısı üretmez.
- Sea/Rock ve yön için en az 800 kör sınıflandırma / en az 10 kişi; %95 üst
  güven sınırı `%55`i geçmez.
- Sadakat kimliği/tarafı kör sınıflandırmada şansın üstünde tahmin edilemez.
- Arka yüzler önlerle aynı sanat dilinde fakat ön-yüz kopyası olmadan üretilir.

## 7. Kör insan oyun testi

- En az 24 oturum / 12 eşlenmiş A-B çifti.
- Oyuncu bantları 6–7, 8–10, 11–13, 14–15; her bantta üç çift.
- En az dört moderatör; ikisi yalnız candidate kural kitabından ilk kez yönetir.
- Katılımcıların en az yarısı yeni oyuncudur; sıra karşı dengelenir ve hipotez
  açıklanmaz.

Kabul: yarıda kalan/dış müdahaleli oyun `0`; anlamlı rota kararı medyanı en az
4/5 ve hiçbir bant 3,5 altı değil; adalet en az 3,5/5; sıkılma en fazla 2,5/5;
saf tahmin diyenler en fazla %20; gerekçe gösterebilenler en az %75; tek
oyuncunun konuşma payı en fazla %35; pasif bekleme p90 toplam sürenin en fazla
%20'si.

## 8. Üretim, PDF ve provenance

- Tam envanter ve source→render→PDF: `121/121`.
- Kesim toleransı `±0,75 mm`; taşma 3 mm; çözünürlük en az 300 dpi; duplex
  sapması en fazla 1,5 mm.
- Eksik font/glif, overflow, kesilen mekanik metin veya unauthorized copy: `0`.
- Gerçek ışıkta mekanik metin doğru okuma en az `%95`.
- İç ZIP manifesti ile dış provenance aynı exact source/product commit, blob,
  SHA-256, byte boyutu ve self-version değerlerini taşır.
- PDF font tablosu ile preflight boolean/metadata alanları birebir uyuşur.
- Fiziksel baskı, kesim, duplex, opaklık ve gerçek ışık kanıtı bulunur.

## 9. Blocker kapanış matrisi

| Engel | Zorunlu kanıt |
|---|---|
| `MEC-001` | Sea=Rock A/B, bilgi sözleşmesi ve kör fiziksel sızıntı |
| `SRC-001` | Exact kaynak blobları, iç/dış provenance, normalize copy diff |
| `SRC-002` | Kilitli v2.6 exact Güç kimlik/effect tablosu ve dispozisyon |
| `ART-001` | 121 özgün brief/sahne, 7 kabul edilmiş back, contact-sheet QA |
| `QA-001` | Sürümlü validator, baseline, komut, seed, ham çıktı hashleri |
| `QA-002` | Fiziksel proof, kör arka-yüz ve kör insan playtest |
| Final | `EVIDENCE_MANIFEST_v2.7.json` + `SIM_QA_ATTESTATION_v2.7.json` |

## 10. Attestation sırası

1. Ürün kaynakları ve artefaktlar `C` commitinde dondurulur.
2. QA yalnız `C`yi checkout ederek çalışır.
3. Ham kanıt ve attestation sonraki `Q` commitine yazılır;
   `candidate_commit=C` olur.
4. C sonrası ürün kaynağı/render/binary değişirse C2 oluşur ve önceki
   attestation iptal edilir.
5. Q yalnız `working/v2.7/qa/**` ve Baş Editörün yetkili yönetişim kanıtlarını
   değiştirir.
6. Release, C ürün ağacı + Q kanıtı + açık blocker listesi boş olduğunda
   değerlendirilebilir.


## 2026-08-30 owner reset ek kapıları

- Aktif candidate yok; bu plan şu anda Simülasyon yetkisi vermez.
- SET-KP-01 exact copy kaynağı:
  `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json`.
- Her front için OCR/render-source → canonical UTF-8 exact karşılaştırması;
  sapma `BLOCKED_COPY_DRIFT`.
- Her front/back için bağımsız Sanat Yönetimi kadraj dispozisyonu;
  `FRAMING_PASS` veya `REFRAME_REQUIRED`; sapma
  `BLOCKED_FRAMING_DRIFT`.
- BACK_SEA_ROCK matlık, BACK_ISLAND FULL REDRAW ve BACK_LIGHTHOUSE daha büyük /
  uzun sırt zorunlu değil hükümleri ayrı test edilir.
- Yetkili Simülasyon başladığında Data Analytics, seed, komut, ham çıktı ve
  hash beyanı zorunludur; Game Studio yalnız tarayıcı prototipi istenirse.
