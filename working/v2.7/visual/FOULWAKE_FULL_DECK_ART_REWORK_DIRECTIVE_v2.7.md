# FOULWAKE v2.7 — Tam Deste Görsel Rework Direktifi

**Durum:** BAĞLAYICI v2.7 DRAFT İŞ EMRİ / NOT LOCKED  
**Karar tarihi:** 25 Ağustos 2026  
**Yetkili karar:** Proje sahibi; Baş Editör kaydı  
**Uygulayan görünür sohbet:** `FOULWAKE görsel tasarım`  
**Çalışma dalı:** `work/v2.7-visual`  
**Reddedilen teknik referans:** `work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891`

Bu direktif yalnız karakter kartlarını değil, **121 kartın bütün ön yüzlerini ve
bütün arka yüz ailelerini** kapsar. Önceki tam dijital teslim teknik üretim
zinciri için tarihsel referans olarak kalır; sanatı, illüstrasyon plakaları,
renderları, PDF'leri veya arka yüzleri yeni adayda kullanılamaz.

## 1. Değiştirilemeyen kaynak sözleşmesi

- Kart kimliği, adet, mekanik etki, zamanlama, grup, başlangıç havuzu, deste
  davranışı ve kural akışı değiştirilemez.
- Karakter ve Güç kartlarının bağlayıcı görünen metni
  `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json` dosyasından kelimesi kelimesine
  alınır.
- Tanımlı kural kitabı anlatı blokları
  `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md`; ton ve lore çiti
  `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md` kaynağından alınır.
- Diğer kart ailelerinin değişmeyen içeriği v2.6 STABLE / LOCKED baseline'ından
  alınır.
- Taşma veya okunabilirlik sorunu metni kısaltarak çözülmez; kart kimliği ve
  alan adıyla Baş Editöre handoff edilir.

## 2. Ana sanat dili

Kullanıcının gönderdiği KAPTAN karakter kartı **yalnız STYLE_ONLY** referanstır.
Karakter, yüz, beden, poz, kompozisyon, kadraj, nesne, dekor, piksel veya çizgi
kopyalanmaz ve izlenmez.

- Belirgin çizgisel, elde çizilmiş mürekkep illüstrasyonu.
- İnce ama karakterli kontur, çapraz tarama ve eski gravür dokusu.
- Hacim boya gradyanı veya sinematik ışık yerine çizgi ve taramayla kurulur.
- Mat ve sınırlı palet: eskimiş kâğıt, lacivert, kirli mavi-gri, pas/kahverengi;
  çok kontrollü hardal ve kırmızımsı vurgular.
- Parlak yapay zekâ renderı, dijital boya, fotogerçekçilik, temiz vektör, 3B,
  neon ve çocuk kitabı estetiği kullanılmaz.
- 1721 dönemine uygun gemi, liman, kıyafet, araç ve malzeme kullanılır; modern
  nesne, büyü efekti ve çağdaş tabela dili yoktur.
- Kartlar tek çizerin aynı dünyasına ait görünür; fakat isimler kapatıldığında
  dahi aynı görselin veya aynı insan modelinin varyasyonları gibi görünmez.

## 3. Ön yüz özgünlüğü

Her kart için ayrı `art brief` ve ayrı özgün sahne gerekir. Önceki teslimdeki
altı aile illüstrasyon plakası veya onların kırpılmış, renklendirilmiş,
döndürülmüş, aynalanmış ya da kostümü değiştirilmiş türevleri kullanılamaz.

Her brief şu sırayla kayıt altına alınır:

`kart kimliği → görsel anlatı amacı → özne/beden/yüz → ana hareket → gerçek
mekân → karta özgü nesne → atmosfer → en fazla bir ikincil görsel şaka`

Karakterlerde yaş, yüz geometrisi, saç, sakal/bıyık durumu, beden yapısı,
boyun/omuz oranı, siluet, duruş, ifade, kıyafet kullanımı ve mesleğe bağlı
el/beden özellikleri ayrı ayrı belirlenir. Sakal ve bıyık varsayılan denizci
özelliği değildir. Aynı yüz, poz, sahne, siluet veya kostüm tabanı tekrar
edemez.

Güç, Çürümüş Erzak, Sadakat, Harita ve yardımcı kartlarda da yalnız başlık veya
metni değişmiş aile plakası kabul edilmez. Kartın kendi metni, rolü veya işlevi
ayrı görsel olaya çevrilir. Gizli bilgiye ait illüstrasyonlar kartın mekanik
cevabını arka yüzden veya kapalı hâlden sızdırmaz.

## 4. Resim içindeki yazı yasağı

- İllüstrasyon alanına sırf komik olsun diye tabela, pankart, etiket, konuşma
  balonu, isimlik, slogan, açıklama veya saçma/anlamsız yazı eklenmez.
- Okunabilir metin yalnız kart şablonunun bağlayıcı alanlarında bulunabilir:
  başlık, effect, flavor ve kart kimliği.
- Harita, defter, kitap, sandık, fıçı veya gemi üstündeki dokular okunabilir
  harf, sayı ya da kelime üretemez. Gerekliyse yalnız okunamayan çizgisel iz,
  leke veya sembolik doku kullanılır.
- Görsel şaka yazıyla açıklanmaz; beden dili, nesne ilişkisi veya küçük bir
  arka-plan davranışıyla anlatılır.

## 5. Mizah sınırı

- Her illüstrasyonda en fazla bir ikincil görsel şaka bulunur; şaka zorunlu
  değildir.
- Mizah kartın flavor metninden, işlevinden veya karakter zaafından türetilir.
- Martı, fare, papağan, aynı beceriksiz tayfa, aynı düşme/kayma pozu veya aynı
  çalınan nesne kalıbı maskota dönüşmez.
- Ana karakteri, kartın işlevini ve tehlikeli deniz atmosferini gölgeleyen
  şaka kabul edilmez.

## 6. Arka yüz topolojisi

Arka yüzler ön yüzlerin kopyası değildir; **ön yüzlerle aynı mürekkep, tarama,
mat palet ve eski baskı sanat dilinde** yeni, metinsiz desenlerdir. Aynı aile
içindeki bütün kartlar byte/piksel olarak aynı binary varlığı kullanır.

| Arka yüz varlığı | Kartlar | Adet |
|---|---|---:|
| `BACK_CHARACTER` | 20 Karakter | 20 |
| `BACK_POWER` | 30 Güç + 1 Çürümüş Erzak | 31 |
| `BACK_LOYALTY` | 15 Sadakat | 15 |
| `BACK_SEA_ROCK` | 30 Açık Deniz + 12 Kayalık | 42 |
| `BACK_ISLAND` | 6 Ada | 6 |
| `BACK_LIGHTHOUSE` | 4 Deniz Feneri | 4 |
| `BACK_SUPPORT` | Kalkış Limanı + Varış Limanı + Kaptan | 3 |
| **Toplam** | **7 binary arka yüz / 121 eşleme** | **121** |

Zorunlu arka yüz koşulları:

- yazı, logo, harf, sayı, kart türü etiketi veya okunabilir işaret yok;
- her varlık exact 180° dönüş güvenli; yön sızıntısı yok;
- aile içindeki bütün kopyalar exact aynı binary;
- kesim, kenar koyuluğu, parlaklık, opaklık ve duplex sapması aile veya yön
  sızdırmaz;
- `BACK_SEA_ROCK` Deniz/Kayalık ayrımı üretmez;
- `BACK_LOYALTY` Sadakat kimliğini veya tarafını sızdırmaz;
- Ada ve Deniz Feneri birbirinden ayrılır, kendi aileleri içinde aynıdır.

## 7. Aşamalı üretim kapısı

Tam 121 üretime doğrudan geçilmez.

1. **Brief kapısı:** 121 satırlık art-brief envanteri ve 7 arka yüz briefi
   hazırlanır; tekrar eden özne/sahne/şaka işaretlenir.
2. **Pilot kapısı:** 3 Karakter, 2 Güç ve Çürümüş Erzak, Sadakat, Açık Deniz,
   Kayalık, Ada, Deniz Feneri ve yardımcı aileden birer örnek olmak üzere 12 ön
   yüz; ayrıca 7 arka yüz taslağı üretilir.
3. **Görsel onay:** Pilot contact sheet kullanıcı ve Baş Editör tarafından
   kabul edilmeden kalan 109 ön yüze ve baskı PDF'sine geçilmez.
4. **Tam yayılım:** 121/121 özgün ön yüz, 7 arka yüz ve aile contact sheetleri
   üretilir.
5. **Teknik preflight:** Exact metin, ölçü, DPI, taşma, glif, PDF, duplex,
   source→render→PDF ve hash zinciri doğrulanır.
6. **Fiziksel/Simülasyon kapısı:** Baskı, kesim, gerçek ışık, kör arka-yüz
   sızıntısı ve bağımsız Simülasyon Testi yapılır.

## 8. Görsel QA kabul ölçütleri

- `unique render SHA = unique artwork` varsayımı yasaktır.
- Ön yüzler aile ve tam deste contact sheetlerinde, başlık/metin kapalı biçimde
  insan gözüyle incelenir.
- Aynı yüz, saç/sakal kalıbı, beden, poz, kadraj, sahne, siluet, arka-plan,
  hayvan veya şaka tekrarları bulgu olarak işaretlenir.
- Her kart manifestinde `art_brief_id`, `original_artwork_id`,
  `rejected_asset_reused=false`, `text_in_illustration=false`, manuel semantik
  inceleme sonucu ve benzerlik bulguları bulunur.
- 121 kart birbirinden ayırt edilebilir; çizgi, tarama, palet, tipografi,
  çerçeve ve yerleşim tek FOULWAKE sistemi olarak tutarlıdır.
- Tek bir MAJOR sanat tekrarı, okunabilir resim-içi yazı, bilgi sızıntısı veya
  reddedilmiş varlık yeniden kullanımı `ART-001 BLOCKER` sonucudur.

## 9. Teslim hükmü

Yeni Görsel handoffu pilot onayı ve tam yayılımı ayrı commitlerle belirtir.
`work/v2.7-visual@e91581...` veya onun binary/PDF çıktıları yeni aday olarak
sunulamaz. Görsel Tasarım release, PASS, STABLE veya LOCKED ilan edemez;
`LOCK_REQUESTED: NO` kalır.
