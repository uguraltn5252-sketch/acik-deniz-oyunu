# FOULWAKE — 8 Eylül güncel baskı ve görsel dosyaları

121 ayrı resimli ön, yedi ortak arka; fenerde tek kule. Bu dizin önceki 7 Eylül baskılarının güncel karşılığıdır.

[Kural kitabı — 30 sayfa](pdf/FOULWAKE_KURAL_KITABI_v2.7.pdf) · [Uygulanan düzeltmeler](../../qa/whole_game_polish_20260908/review.md)

## 121 kartın A4 baskısı

Ana dosya 48 sayfadır. Aşağıdaki on bölümün tamamı 121 kartı içerir. Her bölüm ilk iki kullanım sayfasını ve tam ön–arka çiftlerini korur. Bölümleri ayrı ayrı, A4 / %100 / uzun kenardan çift taraflı yazdırın. İlk bölümün 3–4. sayfasıyla hizayı deneyin.

| Bölüm | Ana dosyadaki sayfalar | Boyut |
|---|---|---|
| [FOULWAKE_KARTLAR_01.pdf](pdf/FOULWAKE_KARTLAR_01.pdf) | 1, 2, 3, 4, 5, 6, 7, 8 | 9.3 MB |
| [FOULWAKE_KARTLAR_02.pdf](pdf/FOULWAKE_KARTLAR_02.pdf) | 1, 2, 9, 10, 11, 12, 13, 14 | 9.3 MB |
| [FOULWAKE_KARTLAR_03.pdf](pdf/FOULWAKE_KARTLAR_03.pdf) | 1, 2, 15, 16, 17, 18 | 8.9 MB |
| [FOULWAKE_KARTLAR_04.pdf](pdf/FOULWAKE_KARTLAR_04.pdf) | 1, 2, 19, 20, 21, 22, 23, 24 | 10.6 MB |
| [FOULWAKE_KARTLAR_05.pdf](pdf/FOULWAKE_KARTLAR_05.pdf) | 1, 2, 25, 26, 27, 28 | 10.1 MB |
| [FOULWAKE_KARTLAR_06.pdf](pdf/FOULWAKE_KARTLAR_06.pdf) | 1, 2, 29, 30, 31, 32 | 7.4 MB |
| [FOULWAKE_KARTLAR_07.pdf](pdf/FOULWAKE_KARTLAR_07.pdf) | 1, 2, 33, 34, 35, 36 | 8.8 MB |
| [FOULWAKE_KARTLAR_08.pdf](pdf/FOULWAKE_KARTLAR_08.pdf) | 1, 2, 37, 38, 39, 40 | 9.1 MB |
| [FOULWAKE_KARTLAR_09.pdf](pdf/FOULWAKE_KARTLAR_09.pdf) | 1, 2, 41, 42, 43, 44 | 9.2 MB |
| [FOULWAKE_KARTLAR_10.pdf](pdf/FOULWAKE_KARTLAR_10.pdf) | 1, 2, 45, 46, 47, 48 | 8.9 MB |

## Görsel inceleme

24 sayfalık ana inceleme: 121 ön resim, yedi ortak arka ve deniz komşuluğu. Her bölümde kapak tekrarlanır. Baskı yapmak için yukarıdaki kart dosyalarını kullanın.

| Bölüm | Ana dosyadaki sayfalar | Boyut |
|---|---|---|
| [FOULWAKE_GORSEL_01.pdf](pdf/FOULWAKE_GORSEL_01.pdf) | 1, 2, 3 | 8.5 MB |
| [FOULWAKE_GORSEL_02.pdf](pdf/FOULWAKE_GORSEL_02.pdf) | 1, 4, 5 | 8.3 MB |
| [FOULWAKE_GORSEL_03.pdf](pdf/FOULWAKE_GORSEL_03.pdf) | 1, 6, 7 | 8.1 MB |
| [FOULWAKE_GORSEL_04.pdf](pdf/FOULWAKE_GORSEL_04.pdf) | 1, 8, 9, 10 | 10.2 MB |
| [FOULWAKE_GORSEL_05.pdf](pdf/FOULWAKE_GORSEL_05.pdf) | 1, 11, 12 | 8.6 MB |
| [FOULWAKE_GORSEL_06.pdf](pdf/FOULWAKE_GORSEL_06.pdf) | 1, 13, 14 | 7.4 MB |
| [FOULWAKE_GORSEL_07.pdf](pdf/FOULWAKE_GORSEL_07.pdf) | 1, 15, 16 | 8.6 MB |
| [FOULWAKE_GORSEL_08.pdf](pdf/FOULWAKE_GORSEL_08.pdf) | 1, 17, 18 | 8.7 MB |
| [FOULWAKE_GORSEL_09.pdf](pdf/FOULWAKE_GORSEL_09.pdf) | 1, 19, 20 | 8.7 MB |
| [FOULWAKE_GORSEL_10.pdf](pdf/FOULWAKE_GORSEL_10.pdf) | 1, 21, 22, 23, 24 | 10.1 MB |

## Yeniden üretme ve kontrol

Depo kökünden `python3 -B working/v2.7/qa/whole_game_polish_20260908/build_print.py` ana dosyaları ve bölümleri üretir. `verify_print.py` kaynak metinlerini, resim kimliklerini, kesim/güvenli alanları ve bölüm eşitliğini denetler. Ana dosyalar `artifacts/polish_20260908/` altında oluşur. Ön kaynaklar tarihsel klasörlerden değişmeden okunur.

Nihai tek kuleli arka [BACK_LIGHTHOUSE.pdf](pdf/BACK_LIGHTHOUSE.pdf) dosyasıdır. Alt deniz PNG’si tek başına nihai master değildir. Fiziksel baskı, opaklık ve insan masası henüz doğrulanmadı.
