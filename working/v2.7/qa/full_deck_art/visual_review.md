# FOULWAKE — tam deste incelemesi

7 Eylül 2026 · FOULWAKE-FULL-DECK-ART-001 · SAME_OPERATOR_SELF_CHECK

121 ön yüzün tamamında ayrı resim var: 109 yeni üretim, 12 korunmuş kaynak.
Yedi ortak arkadan Fener yenilendi; diğer altısı değişmedi. Güncel 121 kart
metni, hikâye, kural kitabı, KAPTAN kaynağı ve önceki simülasyon kanıtı korundu.

## Görsel karar

Fenerin yandan görünümü, alçak kayalık üstündeki taş kule ve küçük sıcak
ışıkla kuruldu. Modern ışın veya optik kopyalanmadı. Dört Fener kartının
arkası aynı kaynaktır; önler çalışan bekçi, boş oda, donanım zulası ve sahte
ışık olarak ayrılır. Kullanıcının yönlendirmesi ve dönem araştırması
[sanat kararında](../../visual/art_direction/FOULWAKE_FULL_DECK_DECISIONS_v2.7.md) kayıtlıdır.

Her yeni sonuç seçilmeden önce görüldü. 14 yeniden üretim; dönem lambası,
gereksiz sembol, benzeşen portre, sis içindeki fazladan kanıt, pusula yönü,
ayakkabı tabanı ve yelkenin fiziksel kuruluşu gibi somut sorunları giderdi.
Özgün PNG'ler değiştirilmedi; sonuçlar ve exact istemler
[üretim kaydında](../../visual/full_deck_20260907/prompts.json) tutulur.

24 inceleme sayfasının tamamında kimlik etiketi, resmin bütünlüğü ve deste
ritmi gözle kontrol edildi. Baskı dosyasında 2, 3, 4, 15, 16, 29, 30, 47,
48. sayfalar; ayrıca KAR-02, GUC-27, HAR-AA-02, SAD-H-01, HAR-FN-01 ve
SET-KP-01 büyütülerek incelendi. Başlık, resim, etki, flavor ve kimlik
birbirine taşmıyor. KAPTAN'ın sabit kaynak kırpımı değişmedi.

Uzun iki kartın resim alanı ilk dizgide yaklaşık 9,3 mm idi. Yazılar
küçültülmeden başlık, açıklama ve ayırıcı boşlukları düzenlendi; HAR-AA-02
13,853 mm, GUC-27 14,79 mm oldu. Tam sahne korunur; bu iki kartın resmi
diğerlerinden küçüktür. Bütün çizimler inceleme PDF'sinde daha büyük görülür.

## Teknik sonuç

[print_checks.json](print_checks.json): PASS / SAME_OPERATOR_TECHNICAL_SELF_CHECK.

- 121 kanonik kimlik ve exact PDF metni; 121 farklı ön resim nesnesi.
- 109 yeni ön ve yeni Fener arkasının 110 ayrı kaynak özeti doğrulandı.
- 30 korunan çalışma girdisi, görevdeki Git bloblarıyla değişmeden eşleşir.
- Kesim ölçüleri, güvenli metin alanı, aynalanmış arka sütunlar ve yedi aile eşleşir.
- En düşük ön resim çözünürlüğü 386,94 DPI; etki 8,6, flavor 8 punto.
- 48 sayfalık baskı ve 24 sayfalık inceleme ana dosyası; onar indirme bölümü.
- Bölümlerdeki 99 sayfanın tamamı, aynı koşulda render edilen ana sayfayla birebir eşleşir.

İlk karşılaştırmada 14 sayfa için sıcak MuPDF önbelleğiyle fark görüldü.
Kaynak içerik ve resim akışları aynıydı; görüntü ve yazı önbellekleri her
renderdan önce temizlenince bütün karşılaştırmalar eşleşti. Denetim bunu
tekrarlar; hata toleransı yükseltilmedi ve farklar göz ardı edilmedi.

Arkalarda aynı kaynak ve yarım dönüş yerleşimi doğrulanır. Piksel düzeyinde
kusursuz dönme eşitliği iddia edilmez; ölçülen farklar rapordadır. Önceki
çalışma alanı kesintisinden kurtarma kanıtı [runtime_recovery.json](runtime_recovery.json)
içindedir; seçilmiş dosyalar yayımlanmış bloblarından aynen geri alınmıştır.

## Sınırlar

İnsanlarla masa denemesi, fiziksel çift taraflı hizalama, opaklık, baskı rengi
ve bağımsız estetik kabul yapılmadı. Önceki 27 hedefli test ve 3.600 sezgisel
yolculuk bu sanat görevinde yeniden çalıştırılmadı; tam kural motoru veya
insan eğlencesi kanıtı değildir. Kilitli v2.6 ve uzman dal uçları korunur.
Bu teslim tamamlanmış çalışma destesi; release/lock kararı değildir.
