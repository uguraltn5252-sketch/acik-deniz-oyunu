# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kullanıcı onaylı kilitli stabil sürüm:** `v2.6 STABLE / LOCKED` — `releases/v2.6/`.
- `v2.5` önceki kilitli mekanik baseline ve tarihsel geri dönüş referansıdır.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü **v2.6'yı** seçmelidir.
- v2.6 artefaktları yerinde değiştirilmez; yeni çalışma `v2.7+ DRAFT` olarak açılır.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. Son kilitli release için `releases/v2.6/README_RELEASE_v2.6.md`, `V26_RELEASE_MANIFEST.json`, `BINARY_ARTIFACTS.md`, `CARD_BASELINE.md`, `V26_RELEASE_VALIDATE_OUTPUT.txt` ve `V26_BLIND_RULEBOOK_AUDIT.md` dosyalarını kontrol et.
3. v2.6 oyun artefaktlarının hashlerini manifestteki değerlerle doğrula.
4. Mekanik tarihsel baseline gerektiğinde `releases/v2.5/` kayıtlarını kontrol et.
5. v2.6 üzerinde yerinde değişiklik yapma. Her yeni fikir, kart, kural, hikâye veya fiziksel bileşen değişikliği v2.7+ DRAFT hattında tutulur.

## v2.6 kilitli omurga

- Gemi `SET-KL-01` Kalkış Limanında başlar; `SET-VL-01` Varış/Hedef Limanı üst sıra hedef sütununa hizalanır.
- Kaptan makamı `SET-KP-01` açık yardımcı kartıyla takip edilir.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar.
- Sadakatler ertesi sabah dağıtılır; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan rota oyu 2 sayar.
- İlk Hain uyanışı Sadakatlerden sonraki ilk yolculuk gecesidir; Hainler birbirini tanır, 1 Yakın Ufka bakar, saldırı yapamaz.
- Başlangıç paketi N-1 gerçek Güç + Çürümüş Erzak; Çürümüş Erzak sahibi sonuçtan sonra 1 gerçek Güç çeker.
- Gövde 2.
- İskorbüt etkinse Liman Gecesinden önce Ada ziyareti zorunludur; Ada girişinde olaydan önce temizlenir.
- Kamusal Harita açmaları açık kalır; ziyaret edilmedikçe olay çözülmez; açık Geçilmez anında engeldir.
- Relocation guard ve Ada çevresi Girdap/Ters Akıntı invariantı korunur.
- Kaderi Yeniden Yaz × Geçilmez hükmü v2.5 mekanik baseline ile aynıdır.
- Kaptan ölür, Kamaraya girer, mahsur kalır, Kayıkçı seferine çıkar veya başarılı İsyanla düşerse hemen yenisi seçilir.
- Hain tablosu: 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- Ana kart seti: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita = 118 ana kart.
- Yardımcı kartlar: Kalkış Limanı + Varış Limanı + Kaptan = 3 kart; toplam 121 basılabilir fiziksel kart.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- Kayalık kartlarının mevcut kategori arka yüzleri korunur; Açık Deniz arka yüzü varyantı v2.6'ya uygulanmamıştır.

## Kilitli artefaktlar

- Kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6_DRAFT.pdf`
  - SHA-256: `f369d6947dc22afde0af4bdeb72e00fa48ca26f072c49f025b97b8d071e0347d`
- Kart PDF: `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf`
  - SHA-256: `73b88869609076aec8690ecc7812f00ba26a6226a7af94b3db7725af30874382`
- Full ZIP: `/Oyun-GitHub/OYUN_v2.6_DRAFT_GUNCEL.zip`
  - SHA-256: `cfb1fe5071270900610669ae6863f8fb96e6d7bba311276c2569b767336f7e8c`

Dosya adlarında ve PDF kapaklarında geçen `DRAFT` ibaresi kullanıcı talebi gereği **içeriğe dokunulmadan kilitlenmiştir**; kanonik statü GitHub release kayıtlarında `STABLE / LOCKED` olarak belirlenir.

## Kısa devam komutu

> GitHub'daki Açık Deniz reposunu aç. `AI_HANDOFF.md`, `PROJECT_STATE.md` ve `releases/v2.6/README_RELEASE_v2.6.md` dosyalarını oku. Son kullanıcı-onaylı kilitli sürüm olarak v2.6 STABLE / LOCKED'u kullan. v2.6'yı yerinde değiştirme; yeni çalışma gerekiyorsa v2.7+ DRAFT aç.
