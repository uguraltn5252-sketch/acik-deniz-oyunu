# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.6 STABLE / LOCKED**  
**Kanonik release kaydı:** `releases/v2.6/`  
**Önceki mekanik baseline:** **v2.5 STABLE / LOCKED**

v2.6 kullanıcı tarafından açıkça kilitlenmiştir. Bundan sonra v2.6 artefaktları yerinde değiştirilmez; her yeni değişiklik v2.7+ DRAFT hattında yapılır.

## v2.6 kilitli durum

### Kural kitabı

- `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf`
- 29 sayfa A4.
- Oyuncu kuralları, Moderatörün açılış/sefer akışı, hafif storyteller rolü, referanslar ve Siyah Mühür hikâyesi aynı kitapta.
- Ayrı Moderatör kartı veya ayrı hikâye dosyası yoktur.

### Fiziksel kart seti

- `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6.pdf`
- 34 sayfa A4.
- 118 ana kart: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita.
- 3 yardımcı kart: `SET-KL-01` Kalkış Limanı, `SET-VL-01` Varış/Hedef Limanı, `SET-KP-01` Kaptan makamı.
- Toplam 121 basılabilir fiziksel kart.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- `ERZ-01` Çürümüş Erzak ve `GUC-22` Bayat Peksimet değiştirilmemiştir.
- Kayalık kartlarının mevcut **KAYALIK kategori arka yüzleri** korunur; Açık Deniz ile aynı arka yüz yapma deneyi v2.6'ya uygulanmamıştır.

### Kilitli paket

`/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`  
SHA-256: `ffc9c17c725e6093c62a3ebddc5f19c36fb0647f6a51a3e7014852fe0623d534`

## Mekanik omurga

v2.6 mekanik motor olarak v2.5 baseline'ı korur:

- Kaptan kalıcı rol; ilk gün yalnız seçim.
- İlk tarafsız gecede Sadakat bilinmeden tam 1 Yakın Ufka gizli bakış.
- Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylama, Kaptan rota oyu 2.
- İlk Hain gecesi Hainler tanışır, 1 Yakın Ufka bakar, saldırı yapamaz.
- N-1 gerçek Güç + Çürümüş Erzak başlangıç paketi; ilk yolculuk gününe herkes 1 gerçek Güçle başlar.
- Kamusal Harita açması kalıcıdır; ziyaret edilmedikçe olay çözülmez; açık Geçilmez engeldir.
- İskorbüt etkinse Ada ziyareti zorunludur; Ada girişinde olaydan önce temizlenir.
- Relocation guard ve Ada çevresi Girdap/Ters Akıntı invariantı korunur.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.

## Test durumu

- v2.5 mekanik baseline validator / geometri / relocation / 100.200 oyun denge / PDF audit: PASS.
- v2.6 final validator: PASS.
- Kör Moderatör yürüyüşü: 28/28 PASS.
- Kural ve kart PDF preflight: PASS.
- Kart PDF sayfa 2–34 görsel invariance: PASS.
- Kayalık arka yüz politikası: PASS — KAYALIK, Açık Deniz'den ayrı.

## Kilit politikası

**v2.6 STABLE / LOCKED yerinde değiştirilmez.** Yeni kart, kural, hikâye, fiziksel bileşen veya mekanik değişikliği v2.7+ DRAFT olarak açılır.
