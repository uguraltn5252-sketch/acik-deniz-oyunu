# AI Handoff Protocol

Bu dosya, farklı ChatGPT oturumları veya model sürümleri arasında oyunun bağlamının kaybolmaması için zorunlu çalışma protokolüdür.

## Her yeni çalışma oturumunda

1. Bu dosyayı oku.
2. `PROJECT_STATE.md` dosyasını oku.
3. En yeni kilitli release olan `releases/v2.2/README_RELEASE_v2.2.md` dosyasını oku.
4. `releases/v2.2/V22_RELEASE_VALIDATION.md` ve `V22_RELEASE_MANIFEST.json` dosyalarını kontrol et.
5. `python releases/v2.2/oyun_simulasyon_v2_2.py --validate-only --geometry-audit` çalıştır.
6. Son commit/PR/issue durumunu incele.
7. Kullanıcının yeni isteğini v2.2 ile karşılaştır; yeni değişikliği v2.3+ çalışma hattında aç.

## Değiştirilemez release kuralı

- `releases/v2.2/` güncel kanonik stabil prototiptir ve yerinde düzenlenmez.
- `releases/v2.1/` önceki stabil geri dönüş sürümüdür ve yerinde düzenlenmez.
- Sohbet hafızası repository'den üstün kaynak değildir.
- Eski v1.0/v2.0/v2.1 denge sonuçları v2.2 sonucu gibi sunulmaz.
- Bir kural yalnız PDF'de, yalnız JSON'da veya yalnız kodda değiştirilmez; ilgili kaynaklar birlikte güncellenir.
- Test geçmeden değişiklik tamamlandı sayılmaz.

## v2.2 omurgası

- Kaptan rolü kalıcıdır ve asla kaldırılmaz.
- İlk rotayı Kaptan tek başına ve olay bilgisi olmadan seçer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferi durumunda yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Ufuk bilgisi vermez.
- Gemi bütün Haritalarda 2 Gövdeyle başlar.
- Gemi alt kenarın dışında herhangi bir sütun hizasında başlayabilir.
- `5×5`, `5×6`, `6×5` haritalarda 1; `5×7`, `6×6`, `6×7` haritalarda 2 Geçilmez Kayalık bulunur.
- Geçilmez Kayalık son Liman yaklaşım hattına konulamaz ve kurulum baştan çözümsüz olamaz.
- Normal geri hareket yasaktır; yalnız Geçilmez Kayalık kaynaklı tam ileri çıkmazda bir önceki kareye bir tam hareket/gün harcayarak geri dönülebilir.
- Geri dönülen çözülmüş olay tekrar çalışmaz.

## Binary baskı artefaktları

Baskı PDF'leri ve tam v2.2 ZIP paketi kalıcı ChatGPT Library'de saklanır. Tam yollar ve SHA-256 değerleri `releases/v2.2/BINARY_ARTIFACTS.md` dosyasındadır.

## Kullanıcının kısa komutu

> GitHub'daki Açık Deniz oyun reposunu aç, `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını okuyup kaldığımız yerden devam et.

Bu komut yeni bir modelin v2.2 release'inden bağlamı yeniden kurması için yeterli olmalıdır.
