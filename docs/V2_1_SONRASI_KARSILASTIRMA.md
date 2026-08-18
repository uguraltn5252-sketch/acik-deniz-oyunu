# v2.1 Sonrası Karşılaştırma

Tarih: 2026-08-18

Amaç: Kilitli/stabil v2.1 kaynaklarını, v2.1 sonrasında alınan yeni kararlarla karşılaştırmak. Bu belge `develop` için geçiş planıdır; `releases/v2.1/` yerinde değiştirilmez.

## Durum etiketleri

- **TAŞINACAK**: açık kullanıcı kararı var; yeni geliştirme hattına uygulanacak.
- **KORU / OMURGA**: kaldırılmayacak veya değiştirilmeyecek çekirdek kural.
- **TESTTE**: yön belli, sayısal eşik henüz kilitlenmedi.

---

## 1. Gemi başlangıç konumu — TAŞINACAK

### v2.1

Gemi Haritanın alt kenarının dışında ancak sabit merkez/sağ-orta sütunda başlar.

### Yeni karar

Gemi Haritanın alt kenarının dışındaki **herhangi bir hizada** başlayabilir. Sabit merkez başlangıcı kaldırılır.

Başlangıç sütunu seçildikten sonra ilk Yakın Ufuk, ilk Sis yasağı ve Limana erişilebilirlik o başlangıca göre dinamik hesaplanır.

---

## 2. Kaptan — KORU / OMURGA

Kaptan rolü **asla kaldırılmayacak**.

Kesin hükümler:

- Kaptan oyunun kalıcı çekirdek rolüdür.
- Oyun başında Kaptan açık oylamayla seçilir.
- **Geminin ilk rotasını Kaptan tek başına seçer.** İlk rota olay bilgisi olmadan kör seçimdir.
- Sonraki rota oylamalarında Kaptanın rota oyu 2'dir.
- Rota beraberliğini Kaptan yalnız berabere seçenekler arasından bozar.
- İsyan sistemi Kaptana bağlı kalır.
- Kaptan ölür/Kamaraya girer/mahsur kalır/Kayıkçı seferine giderse yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz.
- Kaptan makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.

Bu maddeler yeni sürümlerde "Kaptanı kaldır" şeklinde yorumlanamaz.

---

## 3. Geçilmez Kayalık — TAŞINACAK, güvenlik kontrolü zorunlu

Geçilmez Kayalık fiziksel olarak girilemeyen bir Harita karesidir; gemi bu kareyi rota olarak seçemez ve yanından dolaşmak zorundadır.

### Yeni yerleşim kuralı

**Geçilmez Kayalık, Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.** Başka deyişle Limana son yaklaşımı oluşturan en üst Harita satırı Geçilmez Kayalık içeremez.

### Ek zorunlu güvenlik kontrolü

Dinamik alt-kenar başlangıcı nedeniyle yalnız "son satıra koyma" yasağı her Harita biçiminde tek başına yeterli değildir. Özellikle `6×5` Haritada gemi bir uç sütundan başlayıp Liman karşı uç sütundaysa tek bir zorunlu çapraz koridor oluşabilir. Bu koridordaki bir Geçilmez Kayalık Limanı tamamen kilitleyebilir.

Bu nedenle Moderatör, Geçilmez Kayalığı yerleştirdikten sonra:

> **Seçilen başlangıç karesinden seçilen Limana en az bir normal ileri yasal yol kaldığını doğrulamak zorundadır.**

Bu doğrulama geçmiyorsa Geçilmez Kayalık başka kareye taşınır.

Tek Geçilmez Kayalık için yapılan kesin grafik kontrolünde `5×5`, `5×6`, `5×7`, `6×6` ve `6×7` biçimlerinde son satır dışındaki tek engel bütün başlangıç/Liman çiftlerinde yolu korudu. `6×5` biçiminde ise iki karşı-uç başlangıç/Liman durumunda zorunlu çapraz koridor üzerindeki dört konum kilit üretebildi. Bu nedenle erişilebilirlik kontrolü kural metninde kalıcı olmalıdır.

---

## 4. Başlangıç Gövdesi — TESTTE

### Mevcut v2.1

Bütün Haritalarda 2 Gövde.

### Yeni tasarım talebi

Gövde değeri Harita boyuna göre 3 olabilsin.

### Eski yüksek örneklem sonucu

Mevcut normal kurulumlarda 3 Gövde Tayfa zaferini ortalama yaklaşık `%82,3` seviyesine çıkarmıştı; dolayısıyla **yalnız Gövdeyi 3 yapmak dengeli değil**.

### 2026-08-18 yeniden hesaplama

Korunmuş `tam_sistem_sim.py` motoruyla uzun Haritalarda 2 ve 3 Gövde yeniden sınandı. Mevcut uzun-harita hasar kotalarıyla 3 Gövde hâlâ fazla güvenli çıktı:

| Oyuncu | Harita | 2 Gövde Tayfa | 3 Gövde Tayfa |
|---:|---|---:|---:|
| 6 | 5×7 | %53,5 | %77,0 |
| 8 | 5×7 | %55,9 | %78,1 |
| 10 | 5×7 | %59,5 | %85,5 |
| 12 | 6×7 | %61,3 | %85,6 |
| 15 | 6×7 | %58,3 | %81,7 |

Her hücre 3.000 yapay oyunla ölçüldü. Bu test dinamik başlangıç değişikliği uygulanmadan önceki kanonik motor üzerindedir; nihai denge testi değildir ama yön çok nettir.

### Mevcut 14 doğrudan-hasar kartının tamamı kullanılırsa

Aday 52 kartlık havuzda en fazla `9 Açık Deniz + 5 Kayalık = 14` doğrudan Gövde-hasarı kartı vardır.

`5×7` Haritada 3 Gövde + 14 hasar kartı kabul edilebilir banda yaklaşır:

| Oyuncu | Tayfa zaferi |
|---:|---:|
| 6 | %59,4 |
| 7 | %53,3 |
| 8 | %52,9 |
| 9 | %59,4 |
| 10 | %62,8 |

Buna karşılık `6×7` Haritada aynı 3 Gövde + mevcut maksimum 14 hasar kartı hâlâ fazla güvenlidir:

| Oyuncu | Tayfa zaferi |
|---:|---:|
| 11 | %74,8 |
| 12 | %76,2 |
| 13 | %80,3 |
| 14 | %78,6 |
| 15 | %81,0 |

Ek sentetik hasar denemelerinde `6×7 + 3 Gövde`yi yaklaşık `%55–61` banda çekmek için mevcut 14 hasar kartına ek yaklaşık **4–6 hasar olayı** gerekti. Bu, mevcut fiziksel havuzla doğrudan mümkün değildir; 4–6 kartın hasara çevrilmesi veya yeni çoklu-hasar mekanikleri gerekir.

### Şimdilik önerilen Gövde kuralı

**En temiz aday:**

- `5×5`: 2 Gövde
- `5×6`: 2 Gövde
- `5×7`: **3 Gövde yalnız 14 doğrudan-hasar kartı (9 Deniz + 5 Kayalık) kullanılıyorsa**
- `6×5`: 2 Gövde
- `6×6`: 2 Gövde
- `6×7`: 2 Gövde

Böylece 3 Gövde gerçekten Harita boyuna bağlı özel bir "uzun sefer" kuralı olur fakat Hainin gemiyi batırma yolu ortadan kalkmaz.

`6×7` için 3 Gövde istenirse önce Harita havuzunun hasar yapısı ayrıca yeniden tasarlanmalıdır.

**Durum: TESTTE.** Kullanıcı onayından sonra bu tablo çekirdek kurala dönüştürülecek.

---

## 5. Hain sayısı — KORU

| Oyuncu | Hain | Tayfa |
|---:|---:|---:|
| 6 | 1 | 5 |
| 7 | 2 | 5 |
| 8 | 3 | 5 |
| 9 | 3 | 6 |
| 10 | 3 | 7 |
| 11 | 4 | 7 |
| 12 | 4 | 8 |
| 13 | 4 | 9 |
| 14 | 5 | 9 |
| 15 | 5 | 10 |

---

## 6. İlk Hain uyanışı ve Sis — KORU

İlk Hain uyanışında Hainler birbirini tanır ve takım olarak bir Yakın Ufka bakar; saldırı yapamazlar. Sis ilk uyanıştaki saldırı yasağını kaldırmaz.

---

## 7. Ufuk geometrisi — KISMEN DEĞİŞECEK

Genel Yakın/Uzak Ufuk tanımı korunur. Yalnız ilk Ufuk artık sabit sütunlara bağlı değildir; geminin seçilen alt-kenar başlangıcına göre dinamik türetilir.

---

# Son durum

Doğrudan yeni sürüme taşınacak kararlar:

1. Gemi alt kenarın dışında herhangi bir hizada başlayabilir.
2. İlk rotayı Kaptan tek başına seçer.
3. Kaptan rolü kalıcı omurgadır ve asla kaldırılmaz.
4. Geçilmez Kayalık Limanın hemen kıçındaki son Ufuk/Harita hattına konulamaz.
5. Geçilmez Kayalık yerleştirildikten sonra başlangıç→Liman erişimi mutlaka yeniden doğrulanır.

Gövde ölçeklemesi için öneri:

> `5×7` uzun Harita = 3 Gövde + 14 hasar kartı; diğer mevcut Harita boyları = 2 Gövde.

Bu madde kullanıcı onayına kadar **TESTTE** kalır.
