# Project State

**Son güncelleme:** 2026-08-18  
**Son stabil prototip:** **v2.2**  
**Kanonik kaynak:** `releases/v2.2/`  
**Durum:** v2.2 release kilidi tamamlandı; yeni değişiklikler v2.3+ olarak başlamalıdır.

## v2.2 release gate

- [x] İnsan kural metni
- [x] Makine JSON/spec
- [x] v2.2 doğrulayıcı
- [x] Çekirdek statik/geometri regresyonu
- [x] Geçilmez Kayalık davranışsal teknik testi
- [x] v2.2 masa kural kitabı PDF - 32 sayfa
- [x] v2.2 kart PDF - 32 sayfa
- [x] Geçilmez Kayalık fiziksel işaret sayfası - 1 sayfa / 12 işaret
- [x] PDF görsel taşma/glif/baskı kontrolü
- [x] Kaynak ↔ PDF çapraz doğrulaması
- [x] `releases/v2.2/` stabil prototip kilidi

## v2.2 kesin omurga

- Kaptan rolü kalıcıdır ve asla kaldırılmaz.
- İlk rotayı Kaptan tek başına, olay bilgisi olmadan seçer.
- Kaptanın rota oyu 2; diğer resmî oyları 1'dir; rota beraberliğini berabere yasal rotalar arasında Kaptan çözer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferi durumunda yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.
- Gemi bütün Haritalarda 2 Gövdeyle başlar.
- Gemi alt kenarın dışında herhangi bir sütun hizasında başlayabilir; ilk Ufuk ve ilk Sis yasağı dinamikleşir.
- `5×5`, `5×6`, `6×5` = 1 Geçilmez Kayalık; `5×7`, `6×6`, `6×7` = 2 Geçilmez Kayalık.
- Geçilmez Kayalık 52 Harita kartından ayrı, görünür işarettir; 118 kart kimliği değişmez.
- Son Liman/Ufuk hattına Geçilmez Kayalık konulamaz; ilk rota kapatılamaz; başlangıçtan erişilebilir Ada üzerinden Limana en az bir ileri yol kalmalıdır.
- Normal geri hareket yasaktır; yalnız Kayalık kaynaklı tam ileri çıkmazda Gemi bir önceki kareye bir tam hareket/gün harcayarak geri çekilebilir.
- Geri dönülen çözülmüş olay yeniden çalışmaz; bilinen çıkmaz kola başka yasal rota varken tekrar girilemez.
- Girdap/olay içi ek hareket Kayalık yüzünden hedef bulamazsa ek hareket boşa düşer; aynı gün acil geri dönüş başlamaz.

## Doğrulama özeti

- Kesin geometri: 51.204 toplam / 51.102 yasal / 102 kurulumda reddedilecek.
- Davranışsal teknik test: 15.000 yeni-kural + 6.000 kontrol; kalıcı rota kilidi 0.
- Temsilî Tayfa ortalaması: %54,8.
- Acil geri dönüş: yaklaşık %4,2 oyun.
- Kart PDF sayfa 2-32 baseline ile eşleşiyor; yalnız v2.2 kapak yenilendi.
- Release çapraz doğrulaması: PASS.

## Binary artefakt konumu

Tam v2.2 ZIP paketi ve üç baskı PDF'si kalıcı Library altında `/Oyun-GitHub/` içinde tutulur. Tam yollar ve SHA-256 değerleri `releases/v2.2/BINARY_ARTIFACTS.md` dosyasındadır.

Bu sürüm hâlâ kör masa testi prototipidir. "Stabil" ifadesi sürümün dondurulduğunu belirtir, oyunun ticari/final baskı olduğu anlamına gelmez.
