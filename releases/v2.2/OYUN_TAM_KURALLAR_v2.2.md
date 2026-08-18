# OYUN - Tam Kural Seti v2.2 — Release Pointer

**Durum:** v2.2 stabil prototip.  
**Kanonik tam metin SHA-256:** `2cb8bec576d5b8c51aa667afce1ea97b9cf7fb4f0883a78612b4acc7c953a660`

GitHub'daki tam geliştirme metni `../../working/v2.2/OYUN_TAM_KURALLAR_v2.2.md` dosyasındadır. Stabil release sırasında bu metin PDF, makine spec'i ve doğrulayıcıyla çapraz kontrol edilmiştir. Stabil kopyanın tam byte-for-byte sürümü `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.2.zip` içinde kalıcı Library artefaktı olarak saklanır.

## v2.2 kanonik omurga

- Kaptan rolü kalıcıdır ve asla kaldırılmaz.
- İlk rotayı Kaptan tek başına ve olay bilgisi olmadan seçer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferinde yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.
- Kaptanın rota oyu 2; diğer resmî oyları 1'dir; rota beraberliğini Kaptan çözer.
- Gemi bütün Harita boylarında 2 Gövdeyle başlar.
- Gemi alt kenarın dışında herhangi bir sütun hizasında başlayabilir; ilk Yakın Ufuk ve ilk Sis yasağı dinamik hesaplanır.
- `5×5`, `5×6`, `6×5` için 1; `5×7`, `6×6`, `6×7` için 2 Geçilmez Kayalık kullanılır.
- Geçilmez Kayalıklar Harita kartı değil ayrı görünür işaretlerdir; 118 kart kimliği değişmez.
- Geçilmez Kayalık son Liman/Ufuk hattına konulamaz ve başlangıçtan erişilebilir Ada üzerinden Limana en az bir ileri yol bırakılmalıdır.
- Normal geri hareket yasaktır. Yalnız Geçilmez Kayalık yüzünden bütün yasal ileri rotalar kapanmışsa Gemi geldiği bir önceki kareye bir tam hareket/gün harcayarak geri çekilebilir.
- Geri dönülen çözülmüş olay yeniden çalışmaz; bilinen çıkmaz kola başka yasal seçenek varken yeniden girilemez.
- Girdap/olay içi ek hareket yalnız Kayalık yüzünden hedef bulamazsa ek hareket boşa düşer; aynı gün acil geri dönüş başlamaz.

Tam release doğrulaması için `V22_RELEASE_VALIDATION.md`, makine kuralı için `OYUN_SIMULASYON_SPEC_v2.2.json`, baskı artefaktları için `BINARY_ARTIFACTS.md` okunmalıdır.
