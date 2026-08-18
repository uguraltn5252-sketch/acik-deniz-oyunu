# AI Handoff Protocol

Bu dosya, farklı ChatGPT oturumları veya model sürümleri arasında oyunun bağlamının kaybolmaması için zorunlu çalışma protokolüdür.

## Her yeni çalışma oturumunda

1. Bu dosyayı oku.
2. `PROJECT_STATE.md` dosyasını oku.
3. Son commit/PR/issue durumunu incele.
4. `releases/v2.1/` klasörü tam paket hâlinde mevcutsa `README_SIMULASYON_v2.1.md` ve `00_BUNU_OKU_VE_BEKLE_v2.1.md` dosyalarını oku ve `python releases/v2.1/oyun_simulasyon_v2_1.py --validate-only` çalıştır.
5. v2.1 paket dosyaları repo içinde henüz yoksa ChatGPT Library'de `OYUN_SIMULASYON_PAKETI_v2.1.zip` dosyasını bul; bu paket stabil geri dönüş kaynağıdır. Paketi doğrula, fakat otomatik denge simülasyonu başlatma.
6. Kullanıcının yeni isteğini mevcut durumla karşılaştır.

## Yasaklar

- Stabil v2.1 içeriğini yerinde düzenleme.
- Sohbet hafızasını repository/kanıtlanmış paket kaynaklarından üstün kabul etme.
- Eski v1.0/v2.0 denge sonuçlarını v2.1 sonucu gibi kullanma.
- Bir kuralı yalnız PDF'de, yalnız JSON'da veya yalnız kodda değiştirip diğerlerini bırakma.
- Test geçmeden değişikliği tamamlandı diye işaretleme.

## Değişiklik akışı

Önerilen branch adı: `change/<kisa-konu>`

Her değişiklikte:

1. Sorunu/amacı tanımla.
2. Etkilenen kuralları ve kartları belirle.
3. Mümkünse önce test beklentisini yaz.
4. Değişikliği uygula.
5. Statik testleri çalıştır.
6. Denge etkisi varsa ayrı simülasyon/human-playtest planı oluştur.
7. Karar ve sonucu loglara yaz.
8. PR üzerinden ana hatta al.

## Kullanıcının kısa komutu

Kullanıcı ileride yalnızca şunu söyleyebilir:

> GitHub'daki Açık Deniz oyun reposunu aç, `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını okuyup kaldığımız yerden devam et.

Bu komut, önceki ChatGPT sürümünün iç hafızasına ihtiyaç duymadan projeyi yeniden kurmak için yeterli olmalıdır.
