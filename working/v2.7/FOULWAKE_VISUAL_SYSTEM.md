# FOULWAKE Görsel Sistem

**Durum:** v2.7 DRAFT / NOT LOCKED  
**Görsel yön onayı:** 20 Ağustos 2026  
**Mekanik baseline:** v2.6 STABLE / LOCKED  
**v2.7 görünen kart metni:** `FOULWAKE_CARD_TEXTS_v2.7.json`  
**v2.7 kural kitabı anlatı metni:** `FOULWAKE_RULEBOOK_STORY_v2.7.md`  
**Ton ve lore çiti:** `FOULWAKE_STORY_FRAMEWORK.md`  
**Kapsam:** Kartlar ve kural kitabı

Bu dosya ayrı bir dünya ansiklopedisi değildir. FOULWAKE kartları ile kural kitabının aynı üretim dilinde kalması için gereken kısa görsel standardıdır. Kullanıcının açık `kilitle`, `stable yap` veya `release et` talimatı olmadan kilitlenmez.

## Kaynak önceliği ve değişiklik sınırı

Kaynaklar arasında fark görüldüğünde aşağıdaki sıra bağlayıcıdır:

1. `releases/v2.6/` ve `AI_HANDOFF.md`; kart kimliği, adet, `effect`, zamanlama, başlangıç havuzu, deste davranışı, kural akışı ve diğer mekanik alanların baseline'ıdır.
2. `FOULWAKE_CARD_TEXTS_v2.7.json`; 20 Karakter ve 30 Güç kartının v2.7 görünen metin kaynağıdır. Harita, Sadakat, Çürümüş Erzak ve yardımcı kart metinleri v2.6 baseline'ından alınır.
3. `FOULWAKE_RULEBOOK_STORY_v2.7.md`; yalnız 3.1, 3.3, 3.4 anlatı notu, 3.6 ve Bölüm 17 için v2.7 anlatı katmanıdır. Diğer işlem, tablo ve hızlı referanslar v2.6 mekanik kaynağından alınır.
4. `FOULWAKE_STORY_FRAMEWORK.md`; ton ve lore kısıtıdır. DRAFT içindeki etiketler tek başına mekaniği veya release kanonunu değiştirmez.
5. Bu dosya; illüstrasyon, yerleşim, tipografi ve baskı sunumunu yönetir; üstteki kaynakların metin veya mekanik hükmünü değiştirmez.

Bir çelişki otomatik seçilmez. Üretim durdurulur ve dosya/alan adıyla Baş Editöre handoff edilir.

## 1. Temel sanat dili

- Hızlı ve karakterli mürekkep çizgisi; gravür etkisi taşıyan yoğun tarama.
- Eskimiş kâğıt ve mat baskı hissi; yüzey dokusu okunurluğun önüne geçmez.
- Sınırlı, kirli ve denizci paleti: lacivert, kemik, pas, hardal ve zeytin tonları.
- Yetişkin karikatürü: iri yüz ifadeleri, yıpranmış bedenler ve yaşanmış kıyafetler.
- Dünya ciddi ve tehlikelidir; komedi, karakterlerin küçük zaaflarından ve arka plandaki sessiz aksiliklerden doğar.
- 1721 dönemine uygun gemi, liman, giysi, araç ve malzeme kullanılır. Modern nesne, çağdaş davranış, büyü efekti veya parlak fantastik görsel yoktur.

## 2. Referans kullanımı

Kullanıcı tarafından verilen görseller yalnızca **STYLE_ONLY** referanstır. Piksel, karakter, poz, kompozisyon, çerçeve veya hazır dekor doğrudan alınmaz; her FOULWAKE illüstrasyonu özgün olarak kurulur.

## 3. Mizah dağılımı

Fare bir komedi maskotu değildir ve her kartta kullanılmaz. Komedi kaynakları kart ailesi boyunca dönüşümlü dağıtılır:

- fare veya başka küçük liman hayvanları;
- martıların yiyecek, belge ya da küçük eşya çalması;
- arka planda yanlış işi yapan veya beceriksizce hırsızlık eden tayfa;
- iki karakter arasındaki sessiz bakış ve yanlış anlaşılma;
- ana olayla çelişen küçük, fiziksel bir arka plan davranışı;
- eşyanın kendi durumundan doğan kuru mizah.

Her illüstrasyonda en fazla bir ikincil görsel şaka bulunur. Şaka ana olayı, kart etkisini veya tehlike duygusunu gölgeleyemez. Aynı hayvan ya da aynı şaka kalıbı arka arkaya kullanılmaz.

## 4. Kesin ölçüler

| Bileşen | Kesim ölçüsü | Taşma paylı çalışma ölçüsü |
|---|---:|---:|
| Harita kartı | 70 × 70 mm | 76 × 76 mm |
| Karakter kartı | 70 × 120 mm | 76 × 126 mm |
| Poker kartı | 63,5 × 88,9 mm | 69,5 × 94,9 mm |
| Kural kitabı | A4 | 210 × 297 mm |

Kartlar `%100` ölçekte basılır; `sayfaya sığdır / fit-to-page` kapalıdır. Taşma payı her kenarda 3 mm'dir.

## 5. Kart yüzü

Görsel sıra değişmez: **başlık → illüstrasyon → kart etkisi → tat metni → kart kimliği**. Başlık, etki, tat metni ve kart kimliği yukarıdaki kaynak önceliğinden birebir alınır; Görsel Tasarım bunları kısaltmaz, yeniden yazmaz veya yeniden yorumlamaz. FOULWAKE logosu kart yüzlerinde kullanılmaz.

- Başlık, eskimiş kâğıt şerit üzerinde yüksek kontrastlıdır.
- İllüstrasyon kartın en büyük alanıdır fakat metin kutusunu sıkıştırmaz.
- Etki metni açık zemin ve koyu mürekkeple basılır.
- Tat metni ikincil ve italiktir; mekanik metinle karıştırılmaz.
- Kart kimliği küçük ama baskıda okunabilir tutulur.

## 6. Kart arka yüzü

- Arka yüzde yazı, logo veya kart türünü açık eden etiket bulunmaz.
- **Bağlayıcı v2.7 DRAFT kararı:** Açık Deniz ve Kayalık aynı binary kesintisiz deniz arka yüzünü kullanır; Görsel Tasarım ayrı Kayalık arka yüzüne dönmez.
- Bu karar, v2.6'nın ayrı Kayalık kategori arka yüzünden bilinçli olarak ayrılır ve gizli bilgi mimarisini değiştiren bir v2.7 mekanik değişikliğidir. Kilitli v2.6'yı geriye dönük değiştirmez.
- Ortak arka yüz, exact candidate üzerinde tam Simülasyon yeniden testi ve kör insan bilgi-sızıntısı testi geçmeden release için onaylanmış sayılmaz. O zamana kadar karar DRAFT içinde uygulanır, release hükmü BLOCKER kalır.
- Ada ve Deniz Feneri aileleri kendi desen sistemine sahip olabilir; aynı aile içindeki binary görsel aynıdır.
- Yön bilgisi istemeden açığa çıkmamalı; desen döndürüldüğünde fark yaratmamalıdır.

## 7. Kural kitabı

- A4 ve mevcut 29 sayfalık içerik akışı korunur.
- Kapak illüstrasyonu oyunun ciddiyetini taşır; tek bir küçük arka plan şakası yeterlidir.
- İç sayfalarda ince çerçeve, sıcak kâğıt ve sınırlı pas rengi vurgu kullanılır.
- Şema, tablo ve örnekler bezeme uğruna küçültülmez.
- v2.6 mekanik işlem, tablo ve hızlı referansları korunur; v2.7 anlatı blokları ve güncellenmiş görünen ad başvuruları yukarıdaki kaynaklardan birebir yerleştirilir. Görsel Tasarım metni yeniden yazmaz.
- Güncel 29 sayfalık akış metni eksiltmeden yerleştirilemiyorsa metin budanmaz veya okunamayacak kadar küçültülmez; taşma dosya ve bölüm adıyla Baş Editöre handoff edilir.

## 8. Kullanılmayacak yaklaşımlar

- Fotogerçekçi, parlak 3B, temiz vektör, neon, büyü parlaması veya çocuk kitabı estetiği.
- Her karta gelişigüzel çapa, pusula, kafatası, papağan, göz bandı veya kanca eklemek.
- Aynı farenin, kuşun ya da tayfanın her görselde tekrar eden maskota dönüşmesi.
- Görsel şakanın kart metnini açıklaması, gizemi çözmesi veya Gusto/Siyah Mühür cevaplarını açığa çıkarması.
- Baskı dosyası yerine sahte masa, kutu veya elde tutulan kart mockup'ı üretmek.

## 9. Mevcut v2.7 üretim örnekleri

- `visual/cards/KAR-01_Uzakgoren_front.png`
- `visual/cards/GUC-24_Islak_Corap_front.png`
- `visual/cards/HAR-AD-09_Deryanin_Gobek_Deligi_front.png`
- `visual/cards/BACK_SEA_ROCK.png`
- `visual/cards/FOULWAKE_v2.7_APPROVED_ART_DIRECTION_PRINT_SET.pdf`
- `visual/rulebook/FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf`

Bu örnekler sanat yönünü ve üretim hiyerarşisini onaylar; v2.7'yi kilitlemez. Tam deste uygulaması aile aile ilerler ve fiziksel prova sonrası sonlandırılır.

## 10. Candidate ve kanıt durumu

Güncel dalda GitHub'dan doğrulanabilir tam 121 kartlık release candidate yoktur. Yukarıdaki örnekler sanat yönü kanıtıdır; tam deste, kaynak izlenebilirliği veya final preflight kanıtı değildir. Temiz v2.7 sıfırlamasından önceki tam deste ve final preflight kayıtları yalnız tarihsel kanıttır; `SRC-001` veya `ART-001` engelini kapatmaz.

Bir görsel candidate ancak aşağıdaki kanıtlar birlikte üretildiğinde Baş Editöre teslim edilir:

- exact source commit ile bütün kaynak dosyaların blob/SHA-256 kayıtları;
- 121 fiziksel kart kimliğinin her biri için ön yüz, arka yüz eşlemesi, ölçü, piksel, DPI, taşma payı ve SHA-256 manifesti;
- kart kimliği → kaynak kaydı → render → baskı PDF sayfası ve kural bölümü → kaynak blok → render → PDF sayfası izlenebilirliği;
- tam kart PDF'si ile 29 sayfalık kural kitabı PDF'sinin hash, sayfa, font/glif, taşma ve metin eşleme preflight'ı;
- `%100` ölçekte fiziksel baskı, kesim, duplex hizalama ve gerçek ışıkta okunabilirlik kanıtı;
- ortak Açık Deniz + Kayalık arka yüzü için tam Simülasyon ve kör insan bilgi-sızıntısı yeniden test kaydı.
