# FOULWAKE v2.7 — Tam Deste Görsel Rework Direktifi

**Durum:** BAĞLAYICI TASARIM SÖZLEŞMESİ / GÜNCEL ÜRETİM YETKİSİ DEĞİL / NOT LOCKED  
**Güncel görev:** `governance/CURRENT_STAGE.json`; Visual production paused  
**Karar tarihi:** 25 Ağustos 2026  
**Yetkili karar:** Proje sahibi; Baş Editör kaydı  
**Yaratıcı inceleme:** `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction`  
**Uygulayan görünür sohbet:** `FOULWAKE Görsel Tasarım 2`  
**Çalışma dalı:** `work/v2.7-visual`  
**Reddedilen teknik referans:** `work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891`

Bu direktif gelecekte yetki verildiğinde uygulanacak tasarım sözleşmesidir;
kendi başına Görsel dalını açmaz. Yalnız karakter kartlarını değil,
**121 kartın bütün ön yüzlerini ve bütün arka yüz ailelerini** kapsar. Önceki tam dijital teslim teknik üretim
zinciri için tarihsel referans olarak kalır; sanatı, illüstrasyon plakaları,
renderları, PDF'leri veya arka yüzleri yeni adayda kullanılamaz.

Kabul edilen ayrıntılı sanat yönü kaynağı
`work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da`
üzerindeki Art Direction Bible, 121 brief manifesti, 12 pilot production briefi
ve 7 arka-yüz briefidir. Çelişkide üretim durur ve Baş Editöre handoff edilir.

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

Yüklenen KAPTAN kartı `SET-KP-01` için bağlayıcı görsel ve copy kaynağıdır.
KAPTAN figürü ile ana kompozisyon korunur; yalnız küçük crop, ölçek, renk ve
arka-plan temizliği yapılabilir. Boş sandalye veya başka özneyle değiştirilmez.
Aynı kart bütün deste için mürekkep, yoğun gravür taraması, sıcak kirli kâğıt ve
mat lacivert–oker–pas sanat dili anahtarıdır. Gemi, martı ve sahne diğer
kartlarda kopyalanmak zorunda değildir.

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

### 2A. Proje sahibi güncel override

- Görünen KAPTAN copy'si yalnız
  `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` kaynağından
  şablonla yerleştirilir. Görsel model copy üretmez; OCR/render-source exact
  karşılaştırma zorunludur. Sapma `BLOCKED_COPY_DRIFT`.
- BACK_SEA_ROCK mat ve ışıldamayan denizdir.
- BACK_ISLAND önceki varlıktan türetilmeden FULL REDRAW yapılır.
- BACK_LIGHTHOUSE normal mesafede daha büyük okunur; uzun kayalık sırt zorunlu
  değildir.
- Diğer dört arka yüz owner-accepted değildir; HOLD.
- Bütün ön/arka illüstrasyonlar bağımsız Sanat Yönetimi kadraj kapısından geçer.
  Görsel Tasarım self-PASS veremez; yalnız `FRAMING_PASS` veya
  `REFRAME_REQUIRED`. Sapma `BLOCKED_FRAMING_DRIFT`.

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
- `BACK_SEA_ROCK` genel keşfedilmemiş deniz gösterir; kaya, sığlık, kırıcı
  köpük veya jeolojik ipucu içermez ve Açık Deniz/Kayalık subtype'ını gizler.
- `BACK_ISLAND` açıkça görülen fakat altı ön yüzden hiçbirine özgü olmayan
  anonim genel ada gösterir; aile görünür, exact ön kimlik ve sonuç gizlidir.
- `BACK_LIGHTHOUSE` açıkça görülen fakat dört ön yüzden hiçbirine özgü olmayan,
  1721'e uygun anonim genel fener gösterir; aile görünür, exact ön kimlik ve
  sonuç gizlidir. Argand, Fresnel, elektrik ve modern beacon yoktur.
- Üç harita arkası aynı deniz, mürekkep, tarama, mat palet, kâğıt ve kenar
  ritmini paylaşır; ada/fener ikon, rozet veya madalyon gibi yapıştırılmaz.
- Sabit 5×5, grid, satır/sütun veya kart sayısı kabul koşulu değildir. Kompakt,
  genişleyen, uzayan ve farklı komşuluklu kurala uygun değişken masa düzenleri
  ile kısmi açılma mockup'ları kullanılır.
- Harita arkasında yazı, sayı, rota, pusula, koordinat, yön oku, logo, halo veya
  gereksiz dekoratif şekil yoktur.

## 7. Aşamalı üretim kapısı

Tam 121 üretime doğrudan geçilmez.

1. **Sanat yönü kapısı:** Sanat Yönetmeni FOULWAKE dünyası, çizgi/tarama/
   malzeme, palet, görsel dramaturji, kompozisyon çeşitliliği ve deste ritmi
   omurgasını kurar.
2. **Brief kapısı:** 121 satırlık art-brief envanteri ve 7 arka yüz briefi
   hazırlanır. Sanat Yönetmeni bunları inceler, yeniden yazar veya somut rework
   briefi verir; tekrar eden özne/sahne/şaka ve jenerik fikirler işaretlenir.
3. **Pilot kapısı:** 3 Karakter, 2 Güç ve Çürümüş Erzak, Sadakat, Açık Deniz,
   Kayalık, Ada, Deniz Feneri ve yardımcı aileden birer örnek olmak üzere 12 ön
   yüz; ayrıca 7 arka yüz taslağı üretilir.
4. **Bağımsız yaratıcı inceleme:** Pilot contact sheet Sanat Yönetmeni tarafından
   ruh, doku, anlatı, insan/sahne ayrışması, kompozisyon ve deste ritmi açısından
   değerlendirilir; `PASS_RECOMMENDATION` veya `REWORK_REQUIRED` verilir.
5. **Görsel onay:** Sanat Yönetmeni tavsiyesi sonrasında kullanıcı ve Baş Editör
   açık kabul vermeden kalan 109 ön yüze ve baskı PDF'sine geçilmez.
6. **Tam yayılım:** 121/121 özgün ön yüz, 7 arka yüz ve aile contact sheetleri
   üretilir; Sanat Yönetmeni tam deste yaratıcı incelemesini tekrarlar.
7. **Copy ve kadraj preflight:** Canonical UTF-8 → template → OCR/render-source
   exact karşılaştırması ile bağımsız Sanat Yönetimi kadraj dispozisyonu
   doğrulanır.
8. **Teknik preflight:** Ölçü, DPI, taşma, glif, PDF, duplex,
   source→render→PDF ve hash zinciri doğrulanır.
9. **Fiziksel/Simülasyon kapısı:** Baskı, kesim, gerçek ışık, kör arka-yüz
   sızıntısı ve bağımsız Simülasyon Testi yapılır.

Daha önceki Baş Editör emriyle başlamış bir pilot geçersiz sayılmaz; exact
Görsel commit ve contact sheet Sanat Yönetmeninin ilk inceleme girdisi olur.

## 8. Görsel QA kabul ölçütleri

- `unique render SHA = unique artwork` varsayımı yasaktır.
- Ön yüzler aile ve tam deste contact sheetlerinde, başlık/metin kapalı biçimde
  Sanat Yönetmeni ve daha sonraki bağımsız QA tarafından insan gözüyle incelenir.
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
Sanat Yönetmeni değerlendirmesi kendi dalında exact Görsel girdi commitine
bağlanır; final kullanıcı onayı veya release PASS'i olarak sunulamaz.
`work/v2.7-visual@e91581...` veya onun binary/PDF çıktıları yeni aday olarak
sunulamaz. Görsel Tasarım release, PASS, STABLE veya LOCKED ilan edemez;
`LOCK_REQUESTED: NO` kalır.
