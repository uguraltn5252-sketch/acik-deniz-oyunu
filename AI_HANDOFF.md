# AI Handoff Protocol

Bu dosya, farklı ChatGPT oturumları/model sürümleri arasında oyunun bağlamının kaybolmaması için çalışma protokolüdür.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. Son stabil sürüm için `releases/v2.2/README_RELEASE_v2.2.md` ve doğrulama kayıtlarını kontrol et.
3. Açık PR/issue ve aktif branch'leri kontrol et.
4. v2.3 çalışması açıksa `working/v2.3/README_SIMULASYON_v2.3.md`, v2.3 kural sözleşmesi ve teknik raporu oku.
5. Gerekirse `python working/v2.3/oyun_simulasyon_v2_3.py --validate-only --geometry-audit` çalıştır.

## Değiştirilemez release kuralı

- `releases/v2.2/` son stabil prototiptir ve yerinde düzenlenmez.
- `releases/v2.1/` önceki stabil sürümdür ve yerinde düzenlenmez.
- Aktif v2.3 değişiklikleri yalnız çalışma branch'i/PR üzerinden yapılır.
- Sohbet hafızası repository'den üstün kaynak değildir.
- Kural, JSON/spec, kod/test ve etkileniyorsa PDF aynı değişiklikte güncellenir.

## Aktif v2.3 kararı

- Geçilmez Kayalık ayrı token değildir.
- `HAR-KY-01` ve `HAR-KY-03`, mevcut 52 Harita kartının 12 Kayalık kartı içindeki iki Geçilmez Kayalıktır.
- Kapalı kategori yüzleri normal `KAYALIK`tır; özel sembol/işaret yoktur ve diğer Kayalıklardan ayırt edilemez.
- Normal Harita kartı bilgi/gizlilik/Ufuk/yer değiştirme kurallarına tabidir.
- Seçilip olay yüzü açılırsa Gemi kareye giremez; önceki konumda kalır ve normal rota gününde hareket harcanır. Kart açık kalır.
- Açılmış Geçilmez kamusal engeldir; yalnız açılmış/bilinen Geçilmezlerin tam çıkmazında acil geri dönüş değerlendirilir.
- 52 Harita / 12 Kayalık / 118 toplam kart kimliği korunur.

## Korunan çekirdek

Kaptan kalıcıdır; ilk rotayı kör seçer; mevcut Kaptan değişim hükümleri korunur. Kaptan gece ayrıca uyanmaz ve otomatik Ufuk bilgisi almaz. Başlangıç Gövdesi her Haritada 2'dir.

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md`, `PROJECT_STATE.md` ve açık v2.3 PR'ını okuyup kaldığımız yerden devam et.
