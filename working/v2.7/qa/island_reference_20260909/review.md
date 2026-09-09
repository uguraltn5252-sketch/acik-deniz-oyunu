# Ada referansı revizyonu — kontrol kaydı

FOULWAKE-ISLAND-REFERENCE-001 · 9 Eylül 2026 · SAME_OPERATOR_SELF_CHECK

Ortak Ada arkası özgün olarak yeniden çizildi. Geniş kumlu koy, üç palmiye ve alçak bitki örtüsü, kartı kayalıktan ayırıyor. Referanslar konu ve okunurluk için kullanıldı; çizimleri veya pikselleri alınmadı. [Araştırma ve tasarım kararı](research.md), [tam üretim istemi](generation_prompt.txt) ve [üretim kaydı](generation_provenance.json).

Görsel, üretilen PNG'nin aynı byte'larıyla 76 × 76 mm mastera yerleştirildi. 70 × 70 mm kesim çevresinde 3 mm taşma vardır. Altı Ada kartı tek görüntü nesnesini paylaşır; hiçbirinin arkasında farklı olay veya kimlik ayrıntısı bulunmaz. Tek sahne doğal yönünde kalır; karşıt yarım görüntüler birleştirilmedi.

Yeni tam dosyada yalnız 44. sayfa değişti. Diğer 45 sayfa native PDF olarak kopyalandı; metin ve 96 dpi RGB karşılaştırması yapıldı. Böylece 121 ön yüzün tamamı önceki teslimdeki yerleşim ve içerikle korunur. Ayrı 22. yaprak, tam dosyanın 43–44. sayfalarıdır. A4, %100 ve uzun kenar tercihleri; altı arka yerleşimin yansıma koordinatları, 70 mm kesimi, taşması ve görüntü kimliği kontrol edildi. Teknik sonuç [verification.json](verification.json) içindedir.

Üretilen sahne, 43 ve 44. tam baskı sayfaları 150 dpi'de, altı kesilmiş Ada arkası 300 dpi'de tek tek gözle incelendi. Kum, gövde ve yapraklar kesimde kalıyor; beyaz kenar, ikinci ada, dikiş, eksik görsel veya olay ipucu görülmedi. [Tekil inceleme kaydı](visual_review.json).

İlk teknik çalıştırmada, uzun bir karma çözünürlük/kırpım dizisinden sonra ayrı yaprak karşılaştırması aynı işlemde eşleşmedi. PDF'ler değiştirilmeden yeni bir renderer işleminde iki sayfa da sıfır piksel farkıyla eşleşti. Kontrol bu karşılaştırmayı yeni bir işlemde yürütür; kıyas toleransı gevşetilmedi. Bu gözlem dosyanın bozuk olduğuna kanıt değildir; süreç içi renderer durumunun kesin nedeni ayrıca saptanmadı.

Kural kitabı, baskı rehberi, kart metinleri ve diğer altı arka masterın byte'ları korunur. Önceki [A4 baskı incelemesi](../print_preparation_20260909/review.md) geçerli tarihsel tabandır; bu küçük revizyon için tüm oyunun yeniden insanlarla test edildiği iddia edilmez. Fiziksel yazıcı kayması, kâğıt opaklığı ve bağımsız estetik kabul bu dijital kontrolün dışındadır. İlk tam baskıdan önce mevcut rehberin 3–4. sayfalarıyla bir deneme yaprağı basılır.
