# Gizli Geçilmez Kayalık - v2.3 Teknik Test Raporu

**Tarih:** 2026-08-18  
**Durum:** Teknik kabul PASS; insan masa testi bekleniyor.  
**Stabil temel:** v2.2 değişmeden korunur.

## Kesin değişiklik

- Geçilmez Kayalık ayrı işaret/token değildir.
- `HAR-KY-01` ve `HAR-KY-03`, 52 Harita kartının 12 Kayalık kartı içindeki iki Geçilmez Kayalıktır.
- Kategori yüzleri diğer Kayalıklarla aynıdır ve kapalıyken ayırt edilemez.
- Normal Harita kartı bilgi, Ufuk, Pusula, bakma, yer değiştirme ve gizlilik kuralları geçerlidir.
- Açıldığında Gemi kareye girmez; önceki konumunda kalır. Normal rota gününde hareket harcanır ve kart açık kamusal engele dönüşür.

## Kart çifti seçimi

Dört makul kart çifti, 6 temsilî hücrede 300'er oyunla karşılaştırıldı: toplam **7.200 oyun**.

| Dönüşüm | Tayfa | Kayalığa çarpılan oyun | İlk rota çarpması | Geri dönüş | Kalıcı kilit |
|---|---:|---:|---:|---:|---:|
| **Ufak Kayalık + Batık Kalyon #1** | **%54,7** | **%30,3** | **%5,5** | **%2,9** | **0** |
| Ufak Kayalık + Kaçakçı Oyuğu | %55,4 | %31,2 | %5,4 | %4,2 | 0 |
| Ufak Kayalık + Kırılan Sandıklar | %54,8 | teknik olarak sağlıklı | - | - | 0 |
| İki Batık Kalyon | %53,3 | teknik olarak sağlıklı | - | - | 0 |

Seçim: `HAR-KY-01` + `HAR-KY-03`. Böylece bütün 5 doğrudan hasar Kayalığı ve bütün benzersiz Kayalık mekanikleri korunur.

## 6.000 oyun temsilî doğrulama

- Tayfa zaferi: **%55,47**
- Ortalama gün: **5,58**
- Ortalama gece: **5,15**
- En az bir gizli Geçilmez Kayalığa çarpılan oyun: **%31,63**
- İlk rotada çarpma: **%5,17**
- Acil geri dönüş: **%3,43** oyun
- Kalıcı rota kilidi: **0**
- Kurulum hatası: **0**

## 6-15 oyuncu tam duyarlılık - 9.000 oyun

- Tayfa ortalaması: **%55,51**
- Ortalama gün: **5,57**
- Ortalama gece: **5,14**
- Gizli Geçilmez Kayalığa çarpılan oyun: **%32,21**
- İlk rota çarpması: **%5,26**
- Acil geri dönüş: **%3,50**
- Kalıcı rota kilidi: **0**
- Kurulum hatası: **0**

Süre bandı Tayfa: Hızlı **%57,23**, Standart **%55,20**, Uzun **%54,10**.

## Geometri

- Teorik kurulum: **51.204**
- Yasal: **51.102**
- Moderatörce reddedilecek: **102**
- Kabul edilmiş kurulumda kalıcı rota kilidi: **0**

## Prototip

- v2.3 Kart PDF: 32 sayfa; iki Geçilmez olay yüzü kart havuzuna işlendi; kategori yüzleri normal Kayalıklarla aynı.
- v2.3 Kural Kitabı: 32 sayfa; tüm sayfalar render edilip görsel tarandı; preflight PASS.

## Hüküm

**PASS / v2.3 geliştirme hattına teknik kabul.** Sayısal test insan blöfünü, güveni ve eğlenceyi kanıtlamaz. Stabil kilitten önce insan masa testi önerilir.

Davranışsal deney motoru `experiments/gizli_gecilmez_kayalik_v23_sim.py` içindedir ve tarihsel denetim motoru `tam_sistem_sim.py` bağımlılığını kullanır; tam çalışma paketi kalıcı Library ZIP'inde korunur.
