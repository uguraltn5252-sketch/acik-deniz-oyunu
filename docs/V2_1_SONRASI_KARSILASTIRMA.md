# v2.1 Sonrası Karşılaştırma

Tarih: 2026-08-18

Amaç: Kilitli/stabil v2.1 kaynaklarını, v2.1 paketinden sonra kullanıcı tarafından konuşulan veya kararlaştırılan değişikliklerle karşılaştırmak. Bu belge **oyun kuralını değiştirmez**; yalnız hangi maddelerin `develop` hattına taşınmaya hazır olduğunu ayırır.

## Durum etiketleri

- **TAŞINACAK**: v2.1 sonrasında açık kullanıcı kararı bulundu; develop sürümüne uygulanmalı.
- **KORU**: v2.1 hükmünü değiştiren doğrulanmış daha yeni karar bulunmadı.
- **DENEYSEL**: fikir/test adayı; çekirdek kurala alınmamalı.
- **DOĞRULAMA GEREKİYOR**: konuşmalarda anılmış olabilir fakat güvenilir son karar zinciri bulunmadan uygulanmamalı.

---

## 1. Gemi başlangıç konumu — TAŞINACAK

### v2.1

Gemi Haritanın en alt satırının hemen dışında başlar ancak sütunu sabittir:

- 5 sütunlu Harita: 3. sütunun altında.
- 6 sütunlu Harita: sağ orta olan 4. sütunun altında.
- 6 sütunlu Haritada Moderatör bu konumu değiştiremez.
- İlk Yakın Ufuklar buna göre sabit 2-3-4 veya 3-4-5 sütunlarıdır.

### v2.1 sonrası kullanıcı kararı

2026-08-15 tarihli sonraki çalışma kararında gemi yine Haritanın dışından, alt kenardan başlar fakat **alt taraftaki herhangi bir hizada başlayabilir**. Başlangıç yerinin Moderatör veya zarla belirlenmesi seçenek olarak bırakılmıştır; kesin olan kısım sabit merkez başlangıcının kaldırılmasıdır.

### Sonuç

**TAŞINACAK.** Bu, doğrulanmış v2.1 sonrası değişikliktir.

Etkilenecek alanlar:

- İnsan kuralı: kesin başlangıç geometrisi bölümü.
- JSON/spec: başlangıç sütunu ve ilk Ufuk türetimi.
- Python doğrulayıcı: sabit sütun kontrolleri kaldırılmalı; seçilen başlangıç sütununa göre dinamik ilk Yakın Ufuk kontrolü eklenmeli.
- Limana erişilebilirlik doğrulaması: her izin verilen başlangıç konumunda veya seçilen başlangıç konumu için yeniden hesaplanmalı.
- İlk üç Yakın Ufukta Sis yasağı: başlangıç konumuna göre dinamik uygulanmalı.
- Moderatör kurulum metni.

Açık tasarım noktası: Moderatör seçimi mi, zar mı, yoksa iki yöntemden biri mi resmi yöntem olacak? Bu ayrıntı kesinleşmeden de "herhangi bir alt hizadan başlayabilir" çekirdek hükmü uygulanabilir.

---

## 2. Kaptan sistemi — KORU / DOĞRULAMA GEREKİYOR

### v2.1

Kaptan tamamen oyundadır. v2.1'de:

- Kör/açık Kaptan seçimi yapılır.
- Kaptanın rota oyu 2'dir.
- Rota beraberliğini Kaptan bozar.
- İlk rotayı Kaptan tek başına ve kör seçer.
- İsyan yalnız Kaptana karşı yapılır.
- Kaptan değişimini tetikleyen ölüm/Kamara/mahsur/Kayıkçı durumları vardır.
- Çürümüş Erzak/İskorbüt açılışında Kaptan özel durumdur.
- Bazı Güç ve Harita etkileri doğrudan Kaptanı referans alır.

v2.1'de kaldırılmış olanlar yalnız şunlardır:

- Kaptan gece ayrıca uyanmaz.
- Kaptan makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.

### v2.1 sonrası durum

Elde edilen güvenilir kaynaklarda Kaptanın **tamamen kaldırıldığı** açık ve tarihlenebilir bir v2.1 sonrası karar doğrulanamadı. Bu nedenle "Kaptanı kaldır" şeklinde bir değişiklik doğrudan uygulanırsa çok sayıda bağlı kuralı yanlışlıkla bozma riski vardır.

### Sonuç

Şimdilik **KORU**: v2.1 Kaptan sistemi devam eder; gece uyanışı ve otomatik Ufuk bilgisi yoktur.

"Kaptanı tamamen çıkar" kararı yeniden açıkça teyit edilirse bu tek satırlık değişiklik değildir; aşağıdakiler birlikte yeniden tasarlanmalıdır:

- Kurulum sırası.
- İlk rota seçimi.
- Rota oyu ağırlığı ve beraberlik.
- İsyan sistemi.
- İskorbüt açılışı.
- Kaptan hedefleyen Harita/Güç kartları.
- Kaptan işareti bileşeni.
- Kaptan değişimi hükümleri.
- JSON/spec ve doğrulayıcı.

---

## 3. Geçilmez Kayalık / Geçilmez Sığlık — DENEYSEL

### v2.1

Kayalık kartları olay üretir; çekirdek harita geometrisinde "bu kareye asla girilemez" türünde sabit engel yoktur. Rota yasallığı Harita sınırı, Limana erişim ve geçici/yazılı rota kısıtlarıyla çözülür.

### Test/fikir geçmişi

"Asla geçilemez" bir Kayalık/Sığlık ekleyip oyuncuların yanından dolaşması ve seferin uzaması fikri test edilmiştir. Mevcut denetim sonucunda:

- İlk iki satırda ve en fazla 1 adet kullanıldığında test edilen kurulumlarda Limanı kapatmamıştır.
- Ortalama süreyi/gece sayısını az miktarda artırmıştır.
- Son satırda bazı Limanları kesin kapatabildiği görülmüştür.
- Son hüküm: **çekirdek kural değil, güvenli deney modülü**.

### Sonuç

**DENEYSEL.** v2.1 sonrası çekirdek `develop` kuralına otomatik eklenmeyecek.

İnsan masa testinde rota baskısı yetersiz bulunursa ayrı modül/branch olarak yeniden test edilebilir. Kullanılırsa yalnız ilk iki satır + en fazla 1 adet kısıtı korunmalıdır.

---

## 4. Başlangıç Gövdesi — KORU

### v2.1

Gemi **2 Gövdeyle** başlar:

- 2 = sağlam
- 1 = su alıyor
- 0 = battı

Tersane Koyu da en fazla başlangıç değeri olan 2 Gövdeye kadar onarır.

### v2.1 sonrası durum

v2.1 sonrası 2'den 3'e çıkarıldığına dair doğrulanmış son kullanıcı kararı bulunmadı. Aksine v2.1 güncellemesinde başlangıç Gövdesinin değiştirilmemesi özellikle korunmuştu.

### Sonuç

**KORU: 2 Gövde.**

---

## 5. Hain sayısı — KORU

### v2.1 kesin tablo

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

### v2.1 sonrası durum

Bu tabloyu değiştiren doğrulanmış daha yeni bir kullanıcı kararı bulunmadı. Daha eski deneysel Hain dağılımları v2.1'in yerine geçirilemez.

### Sonuç

**KORU.**

Özet grup gösterimi:

- 6: 1 Hain
- 7: 2 Hain
- 8-10: 3 Hain
- 11-13: 4 Hain
- 14-15: 5 Hain

---

## 6. İlk Hain uyanışı ve Sis — KORU

v2.1'de ilk Hain uyanışında Hainler birbirini tanır ve takım olarak bir Yakın Ufka bakar; **saldırı yapamazlar**. Sis olsa bile ilk uyanış saldırı yasağını kaldırmaz.

Bunu değiştiren doğrulanmış daha yeni karar bulunmadı.

**KORU.**

---

## 7. Ufuk geometrisi — KISMEN DEĞİŞECEK

Yakın/Uzak Ufkun tanımı değişmiyor:

- Yakın Ufuk: bir normal hareket ilerideki yasal İskele/Pruva/Sancak karşılıkları.
- Uzak Ufuk: bunların hemen arkasındaki iki sıra ilerideki karşılıklar ve yasal iki-hamle yolu şartı.

Ancak gemi başlangıcı artık sabit sütunda olmayacağı için **ilk Ufuk koordinatları sabit değer olarak tutulamaz**.

Sonuç:

- Genel Ufuk tanımı: **KORU**.
- Başlangıçtaki sabit 2-3-4 / 3-4-5 sütun hükmü: **KALDIR / DİNAMİKLEŞTİR**.

---

# İlk geçiş sonucu

Şu anda doğrudan develop sürümüne uygulanmaya hazır tek kesin v2.1 sonrası mekanik değişiklik:

> **Gemi Haritanın alt kenarının dışındaki herhangi bir hizada başlayabilir; sabit merkez/sağ-orta başlangıç kaldırılır.**

Buna bağlı olarak ilk Ufuk, Sis yasağı ve başlangıç erişilebilirlik doğrulaması dinamikleşmelidir.

Şu aşamada çekirdek kural olarak değiştirilmemesi gerekenler:

- Başlangıç Gövdesi: 2.
- Hain tablosu: v2.1 tablosu.
- Kaptan: v2.1'deki biçimiyle mevcut; yalnız gece uyanışı ve otomatik Ufuk bilgisi yok.
- Geçilmez Kayalık/Sığlık: deneysel modül, çekirdek değil.
- İlk Hain uyanışındaki saldırı yasağı.

## Sonraki teknik iş

Ayrı bir değişiklik branch'inde yalnız **dinamik alt-kenar başlangıcı** uygulanmalı ve şu testler yazılmalı:

1. Her Harita genişliğinde tüm izin verilen alt başlangıç sütunları için en az bir yasal ilk rota bulunması.
2. Seçilen Limana erişim geometrisinin korunması.
3. İlk Yakın Ufukta Sis yasağının seçilen başlangıca göre doğru üç/iki hedefe uygulanması.
4. Kenar başlangıçlarında Yakın Ufkun 2 hedefe düşebilmesinin kurallarla uyumu.
5. Harita kurulum üreticisinin hiçbir başlangıçta zorunlu kilit üretmemesi.
6. Girdap/Ters Akıntı ve diğer rota kısıtlarının yeni başlangıçla sıfır yasal rota oluşturmaması.
