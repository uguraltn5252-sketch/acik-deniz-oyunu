# Project State

**Son güncelleme:** 2026-08-18  
**Son stabil prototip:** **v2.3**  
**Kanonik kaynak:** `releases/v2.3/`  
**Önceki stabil geri dönüş:** `releases/v2.2/`  
**Durum:** **v2.3 STABLE / LOCKED.** Sonraki tasarım değişiklikleri v2.4+ olarak açılmalıdır.

## v2.3 kesin omurga

- Kaptan rolü kalıcıdır ve kaldırılmaz.
- İlk rotayı Kaptan tek başına, olay bilgisi olmadan seçer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferinde yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.
- Gemi bütün Haritalarda **2 Gövde** ile başlar.
- Gemi alt kenarın dışında herhangi bir sütun hizasında başlayabilir; ilk Ufuk ve ilk Sis yasağı dinamiktir.
- Harita havuzu **52**, Kayalık kategorisi **12**, toplam kart kimliği **118** olarak kalır.
- `HAR-KY-01` = **Duvar Gibi Kayalık / Geçilmez Kayalık**.
- `HAR-KY-03` = **Yolun Bittiği Yer / Geçilmez Kayalık**.
- Bu iki kart kapalıyken diğer Kayalıklardan hiçbir biçimde ayırt edilemez; normal Harita/Ufuk/gizli bilgi kurallarına tabidir.
- `5×5`, `5×6`, `6×5` kurulumlarında Kayalık kotasının içinde **1**; `5×7`, `6×6`, `6×7` kurulumlarında **2** Geçilmez bulunur.
- Geçilmez Kayalık son Liman/Ufuk hattına kurulamaz; Moderatör başlangıçtan erişilebilir Ada üzerinden Limana en az bir gerçek ileri yol kaldığını gizlice doğrular.
- Kapalı Geçilmez normal rota/Ufuk hedefidir. Seçilip açılırsa Gemi kareye girmez, mevcut konumda kalır; normal rota gününde hareket harcanır ve kart açık kamusal engel olur.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmez Kayalıklar bütün ileri rotaları kapatırsa çalışır; Gemi bir önceki ziyaret edilmiş kareye bir tam hareket/gün harcayarak döner ve çözülmüş olay tekrar çalışmaz.

## v2.3 doğrulama özeti

- Kart çifti karşılaştırması: **7.200 oyun**.
- Seçilen çift temsilî doğrulama: **6.000 oyun**; Tayfa %55,47; gizli Geçilmeze çarpma %31,63; ilk rota çarpması %5,17; acil geri dönüş %3,43; kalıcı kilit 0.
- 6–15 oyuncu × 3 süre tam duyarlılık: **9.000 oyun**; Tayfa %55,51; gizli Geçilmeze çarpma %32,21; acil geri dönüş %3,50; kalıcı kilit 0; kurulum hatası 0.
- Geometri: **51.204 teorik / 51.102 yasal / 102 kurulumda reddedilecek**.
- `python releases/v2.3/validate_release_v2_3.py`: **PASS**.
- Kural kitabı PDF: **32 sayfa**; kart PDF: **32 sayfa**; preflight/görsel tarama: **PASS**.

## Binary artefaktlar

- PDF'ler kalıcı Library'de `/Oyun-GitHub/v2.3/` altında tutulur.
- Tam v2.3 ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.3.zip`.
- Hash ve yollar: `releases/v2.3/BINARY_ARTIFACTS.md` ve `V23_RELEASE_MANIFEST.json`.

"Stabil" ifadesi bu prototip sürümünün dondurulduğu anlamına gelir; ticari/final baskı olduğu anlamına gelmez. İnsan masa testi sonraki v2.4+ iyileştirmeleri için önerilir.
