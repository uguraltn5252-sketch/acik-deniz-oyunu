# Geçilmez Kayalık + Acil Geri Dönüş — v2.2 Teknik Test Raporu

**Tarih:** 2026-08-18  
**Durum:** Yeni çekirdek kural için teknik kabul testi  
**Stabil temel:** v2.1 değişmeden korunur.

## Test edilen kesin kurallar

1. Gemi bütün Harita boylarında **2 Gövde** ile başlar.
2. Gemi alt kenarın dışındaki herhangi bir sütundan başlayabilir.
3. İlk rotayı Kaptan tek başına, olay bilgisi olmadan seçer.
4. Geçilmez Kayalık sayısı:
   - `5×5`, `5×6`, `6×5`: **1**
   - `5×7`, `6×6`, `6×7`: **2**
5. Geçilmez Kayalık son Harita satırına / Limanın kıçındaki son yaklaşım hattına konulamaz.
6. Geçilmez Kayalık rota olarak seçilemez.
7. Normalde geri hareket yasaktır.
8. Yalnız hiçbir yasal ileri rota kalmadığında ve bunun yapısal nedeni Geçilmez Kayalık olduğunda Gemi geldiği bir önceki kareye **1 adım geri** dönebilir.
9. Acil geri dönüş bir tam hareket/gün tüketir; gece normal oynanır.
10. Geri dönülen açık kartın olayı yeniden çalışmaz.
11. Kayalık nedeniyle çıkmaz olduğu görülmüş kola, başka yasal seçenek varken hemen yeniden girilmez.
12. Başlangıçtan Limana en az bir ileri yol bırakmayan kurulum kabul edilmez.

## Motor

Davranışsal temel olarak 14 Ağustos'taki `tam_sistem_sim.py` kullanıldı; yeni kurallar ayrı deney sınıfında uygulandı. İnsan sohbetini veya eğlenceyi kanıtladığı iddia edilmez. Ölçülenler: rota kilidi, yolculuk süresi, gece sayısı, geri dönüş sıklığı, kazanma dengesi ve kurulum geometrisi.

## 1. Kesin geometri taraması

Son satır Kayalığa kapalı tutularak bütün başlangıç sütunu × bütün Liman sütunu × teorik Geçilmez Kayalık konumları tarandı.

| Harita | Kayalık | Teorik yerleşim | Baştan çözümsüz | İlk hareket tamamen kapalı |
|---|---:|---:|---:|---:|
| 5×5 | 1 | 500 | 0 | 0 |
| 5×6 | 1 | 625 | 0 | 0 |
| 6×5 | 1 | 864 | 8 | 2 |
| 5×7 | 2 | 10.875 | 20 | 10 |
| 6×6 | 2 | 15.660 | 50 | 12 |
| 6×7 | 2 | 22.680 | 24 | 12 |

Toplam **51.204** teorik yerleşimin **51.102'si (%99,80)** doğrudan ileri bir yol bırakıyor. Kalan 102 yerleşim kurulum doğrulamasıyla reddedilmelidir. Bu sonuç, "geri gidebiliyoruz, o hâlde her kurulum serbest" denemeyeceğini gösterir: bazı haritalar daha oyun başlamadan çözümsüz olabilir ve bunlar kurulamaz.

## 2. Temsilî davranışsal karşılaştırma

Her Harita boyu için orta oyuncu sayısında **1.000 kontrol + 1.000 yeni-kural oyunu** çalıştırıldı. Kontrol de yeni dinamik başlangıcı ve 2 Gövdeyi kullanır; fark Geçilmez Kayalık + geri dönüş sistemidir.

| Harita | Oyuncu | Kontrol Tayfa | Yeni Tayfa | Fark | Gün farkı | Gece farkı | Geri dönüş görülen oyun |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5×5 | 8 | %59,3 | %56,6 | -2,7 puan | +0,05 | +0,03 | %2,8 |
| 5×6 | 8 | %57,2 | %54,3 | -2,9 puan | +0,09 | +0,07 | %3,7 |
| 5×7 | 8 | %57,0 | %52,0 | -5,0 puan | +0,13 | +0,09 | %4,2 |
| 6×5 | 13 | %60,8 | %56,6 | -4,2 puan | +0,04 | ~0,00 | %3,2 |
| 6×6 | 13 | %58,7 | %52,9 | -5,8 puan | +0,14 | +0,08 | %6,0 |
| 6×7 | 13 | %55,3 | %56,3 | +1,0 puan | +0,28 | +0,29 | %5,3 |

Altı temsilî hücrenin ortalamasında:

- Yeni kural Tayfa zaferi: **%54,8**
- Kontrole göre fark: **-3,3 yüzde puanı**
- Yolculuk: **+0,12 gün**
- Gece: **+0,09 gece**
- Tahmini masa süresi: yaklaşık **+0,70 dakika**
- Geri dönüş görülen oyun: **%4,2**

Bu, mekanizmanın sık tekrarlanan bir geri-gitme oyununa dönüşmediğini; çoğu oyunda yalnız rota baskısı olarak var olup yaklaşık her 24 oyundan birinde gerçek acil geri dönüş ürettiğini gösteriyor.

## 3. Bütün oyuncu sayıları duyarlılık taraması

6–15 oyuncunun tamamında, Hızlı/Standart/Uzun olmak üzere **30 hücre × 300 oyun = 9.000 yeni-kural oyunu** çalıştırıldı.

| Harita | Tayfa ortalaması | Hücre aralığı* | Ortalama gün | Geri dönüş görülen oyun | Kalıcı rota kilidi |
|---|---:|---:|---:|---:|---:|
| 5×5 | %54,1 | %49,3–60,3 | 4,40 | %4,1 | 0 |
| 6×5 | %54,3 | %48,7–62,0 | 4,48 | %3,5 | 0 |
| 5×6 | %53,0 | %47,7–56,0 | 5,16 | %1,7 | 0 |
| 6×6 | %54,9 | %48,0–57,7 | 5,37 | %4,9 | 0 |
| 5×7 | %55,7 | %47,0–60,3 | 6,06 | %3,8 | 0 |
| 6×7 | %58,1 | %55,7–60,3 | 6,15 | %4,6 | 0 |

\* 300 oyunluk hücreler yön taramasıdır; tek tek uç değerler nihai kazanma oranı kabul edilmez.

## 4. Kilit ve hata sonucu

Yeni kuralla toplam:

- **15.000** yeni-kural davranışsal oyunu
- **6.000** karşılaştırma kontrol oyunu
- **51.204** kesin teorik geometri yerleşimi

çalıştırıldı.

Yeni-kural davranışsal oyunlarında:

- kalıcı `route_lock`: **0**
- kurulum hatası: **0**
- başlangıçta geri dönememe kilidi: **0**
- Geçilmez Kayalık yüzünden yapılamayan zorunlu ek hareket: nadir; bu durumda zorunlu ek hareket boşa düşürüldü, oyun kilitlenmedi.

## 5. Hüküm

**Teknik olarak KABUL.** Mevcut veride kuralı geri çekmeyi gerektiren yapısal bir sorun görülmedi.

Önerilen çekirdek kural aynen korunabilir:

> Harita boyuna göre her oyunda 1 veya 2 Geçilmez Kayalık bulunur. Gemi normalde geri gidemez. Ancak Geçilmez Kayalıklar yüzünden hiçbir yasal ileri rota kalmazsa, Gemi geldiği bir önceki kareye bir adım geri çekilebilir. Bu hareket günü tüketir ve dönülen kartın olayı yeniden çalışmaz.

### Kalıcı kurulum güvenliği

Aşağıdaki iki koşul da zorunlu kalmalıdır:

1. Geçilmez Kayalık son Harita/Liman yaklaşım hattına konulamaz.
2. Kayalıklar yerleştirildikten sonra başlangıçtan Limana en az bir ileri yol olduğu doğrulanır.

Acil geri dönüş, kötü/yanlış rota seçiminin bedelini çözmek içindir; baştan matematiksel olarak çözümsüz harita kurmaya izin vermez.

## Sonraki aşama

Bu rapor yalnız teknik/sayısal kabul verir. Bir sonraki adım yeni hükümlerin insan kuralı + JSON/spec + asıl doğrulayıcıya uygulanması ve ardından kör masa testinde şu üç şeyin gözlenmesidir:

- oyuncular Geçilmez Kayalığı gerçekten rota tartışmasına katıyor mu,
- geri dönmek "ceza ama adil" mi hissediliyor,
- iki Kayalıklı haritalar görsel/karar yükünü gereğinden fazla artırıyor mu.
