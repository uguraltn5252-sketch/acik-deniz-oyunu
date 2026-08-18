# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. En yeni kilitli release olan `releases/v2.3/README_RELEASE_v2.3.md` dosyasını oku.
3. `releases/v2.3/V23_RELEASE_MANIFEST.json`, `GIZLI_GECILMEZ_KAYALIK_V23_RAPOR.md`, `SOURCE_PACKAGE.md` ve `BINARY_ARTIFACTS.md` dosyalarını kontrol et.
4. Gerekirse `python releases/v2.3/validate_release_v2_3.py` çalıştır.
5. Tam insan kuralı, tam JSON/spec, simülasyon kodları veya ham sonuçlar gerekiyorsa `SOURCE_PACKAGE.md` içindeki kilitli Library ZIP'ini kullan ve manifestteki SHA-256 ile doğrula.
6. Son commit/PR/issue durumunu incele.
7. Yeni tasarım değişikliğini v2.3'e yerinde yazma; **v2.4+** çalışma hattı aç.

## Değiştirilemez release kuralı

- `releases/v2.3/` güncel kanonik stabil prototiptir ve yerinde düzenlenmez.
- `releases/v2.2/` önceki stabil geri dönüş sürümüdür ve yerinde düzenlenmez.
- `releases/v2.1/` tarihsel stabil sürümdür.
- Sohbet hafızası repository'den üstün kaynak değildir.
- Kural, JSON/spec, doğrulayıcı/test ve etkileniyorsa PDF birlikte güncellenmeden yeni sürüm tamamlanmış sayılmaz.

## v2.3 omurgası

- Kaptan kalıcıdır; ilk rotayı tek başına ve olay bilgisi olmadan seçer.
- Başarılı İsyan, ölüm, Kamara, mahsur kalma veya Kayıkçı seferinde yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makam otomatik Ufuk bilgisi vermez.
- Bütün Haritalarda başlangıç Gövdesi 2'dir.
- Harita 52 / Kayalık 12 / toplam kart kimliği 118'dir.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalıktır; kapalıyken normal Kayalıktan ayırt edilemez ve tüm normal Harita bilgi/Ufuk kurallarına tabidir.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez Kayalık kotanın içindedir.
- Geçilmez açıldığında Gemi kareye girmez, mevcut konumunda kalır; normal rota gününde hareket harcanır ve kart kamusal engel olur.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmezlerin tam ileri çıkmazında uygulanır.

## Binary artefaktlar

PDF'ler `/Oyun-GitHub/v2.3/`, tam ZIP `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.3.zip` altında kalıcı Library'dedir. Hashler `releases/v2.3/BINARY_ARTIFACTS.md` ve manifestte kayıtlıdır.

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md`, `PROJECT_STATE.md` ve `releases/v2.3/README_RELEASE_v2.3.md` dosyalarını okuyup son stabil sürümden devam et.
