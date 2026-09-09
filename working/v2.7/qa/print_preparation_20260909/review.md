# FOULWAKE — A4 baskı hazırlığı ve kontrol

9 Eylül 2026 · FOULWAKE-A4-PRINT-001 · SAME_OPERATOR_SELF_CHECK

121 ön ve 121 doğru arka yüz, 46 sayfalık A4 kart PDF'sinde tamamlandı. Kural kitabı 30, ayrı baskı rehberi 4 sayfadır. Kartlar ve kitabın toplam 80 PDF sayfası görüntülenerek incelendi. Bu kayıt dijital hazırlığı ve aynı operatörün görsel incelemesini belgeler; fiziksel yazıcı, bağımsız estetik değerlendirme veya insanlarla oyun testi değildir.

## Ölçüler ve ön–arka hizası

| Kart grubu | Kesilmiş boy | Adet | A4 yerleşimi |
|---|---|---:|---|
| Karakter, Liman ve Kaptan | 70 × 120 mm | 23 | Dikey, 2 × 2 |
| Güç, Erzak ve Sadakat | 63,5 × 88,9 mm | 46 | Yatay, 2 × 3 |
| Harita | 70 × 70 mm | 52 | 2 × 3 |

A4 dikey, %100 gerçek boyut, uzun kenar çevirmesi. Arka yüzün sütunu kâğıt genişliği boyunca yansıtılır. Yatay kartların ön dönüşü 90°, arka dönüşü 270°'dir. Dört asimetrik köşe tanığının 121 kartta fiziksel uzun-kenar çevrimiyle örtüştüğü doğrulandı: 484 tanık, en büyük hesaplama farkı 0,000001 mm'den küçük. Bu sayı dosya geometrisine aittir, yazıcı doğruluğu değildir. Yanlış sütun ve yanlış çeyrek dönüş kontrol örnekleri beklendiği gibi başarısız oldu.

Kesim dışında 3 mm taşma vardır. Kesim işaretlerinin kâğıt kenarına en küçük uzaklığı 7,35 mm'dir. Komşu işaretler başka kartın taşma/çizim alanına girmez. Ana destede açıklama sayfası yoktur; 1–2 ilk fiziksel yaprak, 45–46 son yapraktır. GitHub'daki 23 iki-sayfalık parça ana PDF ile görüntü karşılaştırmasında eşleşir.

## Kartların yazısı ve çizimi

121 önün tamamı bitmiş A4 PDF'den ayrı ayrı çıkarılarak görüntülendi. Her başlık, etki ve tat metni — toplam 363 alan — sabitlenmiş kaynakla doğrulandı. KAPTAN kaynağının başlık anahtarı `title`, diğerlerinin `name` olarak işlendi. Türkçe karakterler ve kullanılan yazıtiplerinin gömülü oluşu kontrol edildi. Asıl ön yüz çizimleri ve seçilebilir yazı korunur; kırpma kartın gerçek sınırını geri almak içindir, çizim yerine referans fotoğrafı koymak için değildir. Kenar uzatması yalnız kesim dışına uygulanır.

150 dpi karşılaştırmada 118 önün bütün RGB kanalları birebir aynı çıktı. Üç kartta toplam 44 pikselde, yazı ve süs sınırlarının rasterleştirilmesinden kaynaklanan küçük farklar görüldü. Bu bölgeler kaynak/sonuç/büyütülmüş fark olarak ayrıca incelendi; sözcük veya çizim kaybı yok. Tam 121 rasterin bit düzeyinde eşit olduğu iddia edilmez. Ayrıntı `raster_precision_observation.json` ve her kartın ölçümü `per_card_verification.json` içindedir.

Ada arkasında çıplak kaya ağırlığı yerine yeşil, bağlantılı bir kara parçası ve kumlu koylar kullanıldı. Yeni kaynak 1254 × 1254 pikseldir; 76 mm taşmalı genişlikte yaklaşık 419 dpi sağlar. Ortak Ada arkası altı kartta aynıdır ve 180° düzenini korur. Diğer altı arka masterın SHA-256 değerleri değişmedi. Tek dik fener, beğenilen kaynakla aynıdır. `HAR-AA` Ada, `HAR-AD` Açık Deniz kimlikleridir; adlarına bakılarak yanlış aileye geçirilmedi.

## Kural kitabı

Kaynak metin baştan sona okundu; basılı kitapta 729 kaynak metin biriminin tamamının bulunduğu doğrulandı. 18 içindekiler girişi doğru sayfaya işaret eder. Kitap A4 tek sayfa düzenindedir; 22 mm iç, 18 mm dış kenar çift taraflı yapraklarda yer değiştirir. Gövde 10,7 punto, tablo metni 9,4 puntodur. Kitapçık ölçeklemesi gerekmez.

Sayfa geçişi, tek başına kalan OKU başlığı ve prova sayfasındaki cetvel/izah çakışması düzeltildi; son PDF'ler yeniden görüntülendi. Dünya çerçevesi, Kuru Pay belirsizliği, Gusto'nun açıklanmayan akıbeti, tedavinin kanıtlanmamışlığı, Hain motivasyonları ve ince göndermeler korunur. One Piece: GUC-15; Karayip Korsanları: GUC-03; Prens: GUC-18; Moby-Dick: GUC-05. Kanonik kart metni veya mekanik değiştirilmedi. Beş kaynak düzenlemesinin gerekçesi `rulebook_copy_edits.json` içindedir; bunlar baskı metadata'sı, dil ve mevcut kurala dayalı açıklık düzenlemesidir.

## Yazıcı denemesi

Rehberin 3–4. sayfaları tek bir deneme yaprağıdır: üç kart ölçüsü, 100 mm cetveller ve yansıtılmış köşe artıları içerir. Bu yaprak %100 ve uzun kenardan basılıp ışığa tutularak kâğıt besleme kayması ölçülür. Baskı ölçeği, opaklık, kesim ve çift taraflı kalın kâğıt desteği gerçek yazıcıda sınanmalıdır. Dosyalara `PrintScaling=None` ve uzun kenar duplex tercihi yazıldı; sürücü bu tercihi değiştirebilir. Araştırılan birincil üretici kaynakları `print_research.json` ve rehberde bağlantılıdır.

## Kanıtlar ve yeniden üretim

- `imposition_manifest.json`: 242 konum, boylar, arka eşleşmeleri, 23 yaprak ve kaynak hashleri.
- `rulebook_manifest.json`: 729 metin birimi, sayfa boyu, içindekiler ve dosya hash'i.
- `verification.json`: dijital doğrulamanın sonuçları ve son PDF hashleri.
- `per_card_verification.json`: 121 ön ve 121 arkanın gerçek dosyadan ölçümleri.
- `visual_review.json`: 121 tekil kart ve 80 sayfanın görsel inceleme kapsamı.
- `front_source.json`: özgün 8 Eylül kart masterının sürüm ve hash kaydı.
- `island_generation_prompt.txt`: yalnız Ada arkasına uygulanan üretim talimatı.

`common.py`, `impose.py`, `book.py`, `guide.py` ve `verify.py` üretim/kontrol kodudur. Depo dışındaki büyük kaynak masterını `front_source.json` konumuna aynı hash ile yerleştirip `impose.py --source <kaynak-master.pdf> --island working/v2.7/print_20260909/assets/BACK_ISLAND.png`, ardından `book.py`, `guide.py` ve `verify.py` çalıştırın. `verify.py` yeni bir üretimden sonra görsel kabulü otomatik vermez; yeniden görüntü incelemesi gerekir. Gerçek dosya kimlikleri `artifact_versions.json` kaydında bulunur.
