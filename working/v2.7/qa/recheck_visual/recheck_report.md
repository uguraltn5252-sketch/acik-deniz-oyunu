# FOULWAKE — ikinci kontrol ve uygulanmış görsel çalışma

7 Eylül 2026 · FOULWAKE-RECHECK-VISUAL-001 · SAME_OPERATOR_SELF_CHECK

## Sonuç

Hikâye, sistem, 121 kart ve tam kural kitabı tekrar kontrol edildi. Güncel Kuru Pay anlatısı, beş Hainin ve on Tayfanın özel gerekçeleri korunarak kalan açıklık ve zamanlama sorunları giderildi. Tam 30 sayfalık kural kitabı, 48 sayfalık 121 kart baskı prototipi ve 16 sayfalık resimli inceleme dosyası üretildi. Sanat ve grafik uygulama bu görevde fiilen yapıldı.

Kaynak yetki `v2.7-design@ac43b7d2d39451b62eadec1ce2872b06b99d6598`; görev etkinleştirme `367d8edd00f756552c1df84954ec438128fa7745`. Sonraki commit numarası kapanıştaki teslim kanıtında yer alır. Kilitli v2.6 ve dört uzman dalı değişmedi.

## Bu kontrolde düzeltilenler

| Sorun | Uygulanan sonuç |
|---|---|
| Bir Daha Say ve oy değiştiricileri | Bütün uygun seçmenler yeniden oy verir. Aynı oylamanın Şapka, Kupa, Papağan, Rom ve Karga etkileri korunur; ikinci bir yeni kart penceresi açılmaz. Papağan nedeniyle sıfır olan oy Şapkayla geri gelmez. ED-18, mevcut sahibi yetkisiyle alınmış açıklık kararıdır. |
| Rota sayımı | Kaptan yalnız berabere lider seçeneklerden seçer; Karga sıfır oy alan seçenek yaratmaz. Yeniden sayım tam bir oy farkında ve bir kez çalışır. |
| Anahtar Deliği | Gündüz Kamara girişinden sonra, gece başlamadan kullanılır. Kazanılan bilgi yalnız sahibine gider. |
| Şüpheli Martı | Tetiklenirken uygun hedef havuzu boşsa kart tüketilir; sonsuza kadar bekleyen işaret olmaz. |
| Kayıkçı adı | KAR-08 Kırık Kürek'in aynı kişi olduğu açıklanır; yeni kart/karakter sayılmaz. |
| Üç küçük tat metni | ERZ-01'de yanlış özne, GUC-12'de tek mercek/çoklu cam iması ve GUC-06'da yazı/resim uyuşmazlığı giderildi. |
| Sanat ile yeni Sadakat gerekçeleri | 15 sahnenin eski talimatları güncel özel gerekçelere bağlandı. SAD-H-03 artık sağlık kâğıdı şantajıdır; eski masumu savunma pozu kullanılmaz. |
| Eski kaynak statüleri | 121 manifest kaydı güncel exact copy bloblarına bağlandı. Tarihsel SRC-002 çelişki kaydı güncel açık engel gibi sunulmaz; 22 Kupa / 23 Peksimet / 24 Çorap eşlemesi korunur. |

Önceki teslimde uygulanan gece adı, KAPTAN yetkisi, §5.3 anlatıcı kesinliği ve 70 kart kaynak açığı düzeltmeleri yeniden doğrulandı. Gusto'nun akıbeti, Veyr'in terkibinin başarısı ve aracıların ortak örgütü kesinleştirilmedi. Kara komedi ihtiyaç, borç, kayıt ve alışkanlıktan gelir. Dört kısa kültürel çağrışım kaynaklarıyla önceki araştırma notundadır; bu görev yeni alıntı eklemez.

## Teknik oyun kontrolü

**27 hedefli test geçti.** Önceki gizli ön yüzleri yer değiştirerek bilgi sızıntısını arayan test, gece ayrımları ve kaynak kuralları korunur. Yedi yeni test oy sayımı/tekrar oylama, sıfır oy, boş hedef havuzu ve gündüz özel bilgi penceresini kapsar.

6–15 oyuncu × üç uzunluk × üç davranış profili × 20 tohum × iki arka bilgi modeli = **3.600 tamamlanmış model yolculuğu**. Ham dosyalar `../editorial_revision/simulation_games.csv` ve `simulation_results.json` içindedir.

| Model | Tayfa zaferi | Batma | İskorbüt | Tayfa tükenmesi | Ortalama gün |
|---|---:|---:|---:|---:|---:|
| A — eski ayrı kategori bilgisi | 1059 / 1800 | 602 | 116 | 23 | 5,577 |
| B — ortak Deniz/Kayalık bilgisi | 1010 / 1800 | 639 | 127 | 24 | 5,591 |

Sonuçsuz güvenlik durdurması, boş gemi kilidi, kimlik kartı atımı ve sonuç sınıfı dışına çıkış görülmedi. **Bu sayılar denge veya eğlence kabulü değildir.** Rastgele akışlar kararlar sonrası ayrılır; fark nedensel A/B sonucu diye sunulmaz.

Motor hâlâ bir karar sezgisidir: konuşma ve ikna, Kaptan seçimi, siyasi yeniden oylamalar, Rom'da önceki açık oylara insan tepkisi, Üç Anahtar/Güvertebaşı seçimlerinin tamamı ve Seyir Zabtı'nın bütün önleme/ek hareket zincirleri tam temsil edilmez. Bazı yardım kartları iyimser harcama politikası kullanır. Bu nedenle tam kural motoru eşdeğerliği iddia edilmez. Bir Daha Say'ın rota sayımı ve gündüz Anahtar Deliği için önceki somut eksiklikler ise bu görevde kapatıldı.

## Görsel ve baskı teslimi

- 11 yeni özgün ön illüstrasyon + değiştirilmeden yerleştirilen kabul edilmiş KAPTAN resmi = **12 resimli ön pilotu**.
- **7 ortak arka master**; aynı aile içinde aynı resim nesnesi. Deniz/Kayalık 42, Tayfa/Hain 15 kartta aynıdır.
- **121 okunabilir ön yerleşimi**. Kalan **109 ön yüzde özgün illüstrasyon tamamlanmış değildir**; bunlar metin prototipidir.
- Türkçe metin resim modeline yazdırılmaz; güncel JSON'dan PDF'nin seçilebilir metnine yerleşir.
- Harita 70×70 mm, Karakter/Yardımcı 70×120 mm, Güç/Sadakat 63,5×88,9 mm; 3 mm taşma. Metin için 4,5 mm başlangıç güvenliği.
- Etki 8,6 pt, tat 8 pt; uzun kartlarda yazıyı küçültmek yerine resim alanı daralır. Resimli önlerin en düşük etkin çözünürlüğü 426,04 DPI.

`print_checks.json`: 121 başlık/etki/tat/metadata/kimlik eşleşmesi, 121 güvenlik alanı, 728 kural kitabı metin parçası, PDF yapısı ve sayfa sayıları, gömülü fontlar, aile bazında tek resim nesnesi ve ön/arka eşlemesi kontrol edildi. Yedi masterın aynı görüntüyü 180 derece döndüren PDF dönüşümleri ayrıca kontrol edildi.

Raster karşılaştırması gizlenmez: 1000×1000 kontrol görüntüsünde Deniz, Ada, Güç ve Sadakat sıfır fark verir. Fenerin en büyük kanal farkı 1; Karakter 6, Yardımcı 6'dır. Bunlar kesirli PDF koordinatlarının örneklenmesinde oluşan farklardır; yedi arka için “piksel piksel kusursuz” sonucu yazılmadı. Ortak masterın bütün ailede aynı olması kimlik sızıntısını engelleyen dijital kanıttır; fiziksel baskı farkını kanıtlamaz.

Bütün PDF sayfaları küçük sayfa panolarıyla; pilotlar, KAPTAN ve uzun metinler daha büyük ölçekte görsel olarak incelendi. Türkçe glif, metin taşması, kesim alanına etiket girişi ve eksik PDF sorunları giderildi. Kural kitabında otomatik akışla boş devam sayfaları azaltıldı. Ayrıntılı kadraj ve estetik öz değerlendirme `visual_review.md` içindedir.

## Yeniden üretim

```bash
python working/v2.7/qa/editorial_revision/render_texts.py
python working/v2.7/qa/editorial_revision/verify_content.py
FOULWAKE_SOURCE_ZIP=/path/OYUN_SIMULASYON_PAKETI_v2.6.zip PYTHONDONTWRITEBYTECODE=1 python working/v2.7/qa/editorial_revision/test_rules.py
PYTHONDONTWRITEBYTECODE=1 python working/v2.7/qa/editorial_revision/run_simulation.py --package /path/OYUN_SIMULASYON_PAKETI_v2.6.zip --seeds 20
PYTHONDONTWRITEBYTECODE=1 python working/v2.7/qa/recheck_visual/build_print.py
PYTHONDONTWRITEBYTECODE=1 python working/v2.7/qa/recheck_visual/verify_print.py
```

ReportLab, PyMuPDF, Pillow, NumPy, Matplotlib ve DejaVu fontları gerekir. PNG kaynakları değiştirilmez; PDF içinde piksel sayısı korunarak JPEG quality 80, 4:4:4 kodlaması kullanılır. Baskı paketi CMYK ayrımı, matbaa PDF/X kabulü veya fiziksel renk provası değildir.

## Açık kalan gerçek karar

Aynı Başeditör bu görevde hikâye, simülasyon, sanat yönü ve grafik uygulamayı yürüttü. Bağımsız ikinci inceleyici, yeni insan oyunu, fiziksel kesim/duplex/opaklık kanıtı veya proje sahibi estetik kabulü oluşturulmadı. Somut pilot, depodaki pilot-önce üretim sırasına göre tam illüstrasyon yayılımından önce sahibine sunulur. Bu çalışma sürümü release veya lock değildir.
