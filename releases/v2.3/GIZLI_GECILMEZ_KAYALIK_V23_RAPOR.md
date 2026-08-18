# Gizli Geçilmez Kayalık - v2.3 Teknik Test Raporu

**Tarih:** 2026-08-18  
**Durum:** **PASS / v2.3 stabil prototip kilidi.** İnsan masa testi sonraki iyileştirmeler için önerilir.  
**Önceki stabil temel:** v2.2 değişmeden korunur; v2.3 yeni stabil prototiptir.

## Kesin v2.3 değişikliği

- Geçilmez Kayalık artık ayrı işaret/token değildir.
- İki mevcut Kayalık kartı Geçilmez Kayalığa dönüştürülür: `HAR-KY-01` ve `HAR-KY-03`.
- Harita havuzu yine **52**, Kayalık kategorisi yine **12**, toplam kart kimliği yine **118**.
- İki Geçilmez Kayalığın kategori yüzü diğer bütün Kayalıklarla aynıdır; kapalıyken ayırt edilemez.
- Normal Harita bilgi, Ufuk, Pusula, bakma, yer değiştirme ve gizlilik kuralları aynen geçerlidir.
- Kart rota/olay içi hareketle açılırsa Gemi kareye girmez; önceki konumunda kalır. Normal rota günündeyse hareket harcanır. Kart açık kalır ve bundan sonra kamusal engeldir.
- Acil geri dönüş yalnız **açılmış/bilinen** Geçilmez Kayalıkların bütün ileri rotaları kapatması halinde çalışır.

## Kart çifti seçimi

Dört makul hasarsız/tekrarlı dönüşüm çifti, 6 temsilî hücrede 300'er oyunla karşılaştırıldı: toplam **7.200 oyun**.

| Dönüşüm | Tayfa | Kayalığa çarpılan oyun | İlk rota çarpması | Geri dönüş | Kalıcı kilit |
|---|---:|---:|---:|---:|---:|
| **Ufak Kayalık + Batık Kalyon #1** | **%54,7** | **%30,3** | **%5,5** | **%2,9** | **0** |
| Ufak Kayalık + Kaçakçı Oyuğu | %55,4 | %31,2 | %5,4 | %4,2 | 0 |
| Ufak Kayalık + Kırılan Sandıklar | %54,8 | - | - | - | 0 |
| İki Batık Kalyon | %53,3 | - | - | - | 0 |

**Seçim:** `HAR-KY-01` (Ufak Kayalık) + `HAR-KY-03` (ikinci Batık Kalyon). Böylece bütün 5 doğrudan hasar Kayalığı ve bütün benzersiz Kayalık mekanikleri korunur; yalnız bir etkisiz kart ile tekrarlı Batık Kalyon kopyası dönüştürülür.

Yeni olay yüzleri:

- `HAR-KY-01` -> **Duvar Gibi Kayalık** / Geçilmez Kayalık
- `HAR-KY-03` -> **Yolun Bittiği Yer** / Geçilmez Kayalık
- `HAR-KY-02` -> tek kalan **Dibi Görünen Servet** / Batık Kalyon

## 6.000 oyun temsilî doğrulama

Seçilen çiftle 6 hücre x 1.000 oyun:

- Tayfa zaferi: **%55,47**
- Ortalama gün: **5,58**
- Ortalama gece: **5,15**
- En az bir gizli Geçilmez Kayalığa çarpılan oyun: **%31,63**
- İlk rotada gizli Geçilmez Kayalığa çarpma: **%5,17**
- Acil geri dönüş yaşanan oyun: **%3,43**
- Kalıcı rota kilidi: **0**
- Kurulum hatası: **0**

## 6-15 oyuncu tam duyarlılık

10 oyuncu sayısı x 3 süre x 300 oyun = **9.000 oyun**:

- Ortalama Tayfa zaferi: **%55,51**
- Ortalama gün: **5,57**
- Ortalama gece: **5,14**
- Gizli Geçilmez Kayalığa çarpılan oyun: **%32,21**
- İlk rota çarpması: **%5,26**
- Acil geri dönüş: **%3,50**
- Kalıcı rota kilidi: **0**
- Kurulum hatası: **0**

Süre bandı Tayfa ortalaması:

- Hızlı: **%57,23**
- Standart: **%55,20**
- Uzun: **%54,10**

Gizli Kayalığa çarpma uzun oyunlarda doğal olarak artar: Hızlı yaklaşık %22,3; Standart %31,4; Uzun %42,9.

## Geometri güvenliği

v2.3 doğrulayıcısındaki tam statik tarama:

- teorik kurulum: **51.204**
- başlangıç-Ada-Liman gerçek ileri yolu bırakan: **51.102**
- Moderatörce reddedilecek: **102**
- kalıcı kilit üreten kabul edilmiş kurulum: **0**

Geçilmez Kayalıkların konumu oyunculara açıklanmaz; bu kontrol yalnız Moderatör kurulum doğrulamasıdır.

## PDF/prototip doğrulaması

- Kart PDF: **32 sayfa**, açılabilir, şifreli değil.
- Kural kitabı: **32 sayfa**, açılabilir, şifreli değil.
- Kart önünde iki yeni Geçilmez olay yüzü doğrulandı.
- Aynı kartların kategori yüzü diğer Kayalıklarla görsel olarak aynıdır; özel sembol/işaret yoktur.
- Kural kitabının bütün 32 sayfası render edilip görsel olarak tarandı; görünür taşma, kırık glif veya çakışma görülmedi.

## Hüküm

**PASS / v2.3 stabil prototip olarak kilitlendi.** Bu testler insan blöfü, güven, şüphe ve masa eğlencesini tam olarak kanıtlamaz; insan masa testi v2.4+ iyileştirmeleri için önerilir.
