# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kullanıcı onaylı kilitli stabil sürüm:** `v2.5 STABLE / LOCKED` — `releases/v2.5/`.
- `v2.6` **DRAFT / NOT LOCKED** durumundadır.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü **v2.5'i** seçmelidir.
- v2.6 kullanıcı açıkça “kilitle” demeden release veya kanonik stabil sürüm sayılmaz.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. Kilitli mekanik kaynak için `releases/v2.5/README_RELEASE_v2.5.md`, `V25_RELEASE_MANIFEST.json`, `SOURCE_PACKAGE.md`, `BINARY_ARTIFACTS.md` ve test raporlarını kontrol et.
3. Güncel tasarım çalışması için `releases/v2.6/README_RELEASE_v2.6.md`, `BINARY_ARTIFACTS.md`, `CARD_BASELINE.md` ve `V26_RELEASE_MANIFEST.json` dosyalarını oku.
4. v2.6 mekanik hükmü v2.5 ile çelişirse v2.5 geçerlidir; kullanıcı yeni mekanik kararı açıkça onaylarsa taslakta kaydedilir.
5. Kullanıcı açıkça istemeden hiçbir taslak sürümü STABLE/LOCKED ilan etme.

## v2.5 kilitli omurga

- Gemi `SET-KL-01` Kalkış Limanında başlar; Hedef Liman üst sıradadır.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar.
- Sadakatler ertesi sabah dağıtılır; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan rota oyu 2 sayar.
- İlk Hain uyanışı Sadakatlerden sonraki ilk yolculuk gecesidir; Hainler birbirini tanır, 1 Yakın Ufka bakar, saldırı yapamaz.
- Başlangıç paketi N-1 gerçek Güç + Çürümüş Erzak; Çürümüş Erzak sahibi sonuçtan sonra 1 gerçek Güç çeker.
- Gövde 2.
- İskorbüt etkinse Liman Gecesinden önce Ada ziyareti zorunludur; Ada girişinde olaydan önce temizlenir.
- Kamusal Harita açmaları açık kalır; ziyaret edilmedikçe olay çözülmez; açık Geçilmez anında engeldir.
- Relocation guard ve Ada çevresi Girdap/Ters Akıntı invariantı korunur.
- Kaderi Yeniden Yaz × Geçilmez hükmü v2.5 ile aynıdır.
- Kaptan ölür, Kamaraya girer, mahsur kalır, Kayıkçı seferine çıkar veya başarılı İsyanla düşerse hemen yenisi seçilir.
- Hain tablosu: 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- Ana kart seti: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 118 ana kimlik.

## Güncel v2.6 DRAFT

### Kural kitabı

- Güncel kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6_DRAFT.pdf`
- 29 sayfa A4.
- Tek kitap içinde: oyuncu kuralları + Moderatör/storyteller açılışı + normal sefer yönetimi + tüm referanslar + Siyah Mühür arka plan hikâyesi.
- Ayrı Moderatör masa kartı güncel taslakta yoktur.
- Moderatör hafif storyteller'dır: atmosfer ve geçişleri yönetir; gizli bilgi veya şüphe yönlendirmez.
- Açılış akışı: Dünya ve Görev → Karakterler → Gusto → Kaptan → başlangıç Gücü/Çürümüş Erzak → tarafsız gece → Sadakat → ilk rota → ilk Hain gecesi.

### Kart seti

- Güncel kart PDF: `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf`
- 34 sayfa A4.
- 118 ana oyun kimliği korunur.
- Ana kimliğin dışında açık yardımcı fiziksel kartlar:
  - mevcut `SET-KL-01` Kalkış Limanı,
  - yeni Varış / Hedef Limanı,
  - yeni Kaptan makamı.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- `ERZ-01` Çürümüş Erzak değiştirilmedi.
- `GUC-22` Bayat Peksimet değiştirilmedi.

### Güncel paket

- `/Oyun-GitHub/OYUN_v2.6_DRAFT_GUNCEL.zip`
- SHA-256: `ba39598ba0d5be7f592a5ab52fec65230e46d61b8885545321ea8734c024d483`

## Kilitli artefakt

v2.5 Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`

## Kısa devam komutu

> GitHub'daki Açık Deniz reposunu aç. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku. Son kilitli sürüm olarak v2.5'i kullan; güncel tasarım taslağı için `releases/v2.6/` kayıtlarını yükle. Kullanıcı açıkça “kilitle” demeden v2.6'yı STABLE/LOCKED yapma.
