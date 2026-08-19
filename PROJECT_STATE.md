# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.5 STABLE / LOCKED**  
**Kanonik mekanik kaynak:** `releases/v2.5/`  
**Güncel tasarım hattı:** **v2.6 DRAFT / NOT LOCKED**

v2.5 oyunun son kilitli mekanik baseline'ıdır. v2.6; kural kitabı, Moderatör/storyteller deneyimi, Siyah Mühür/Gusto anlatısı ve fiziksel yardımcı kart standardı üzerinde güncel taslaktır. Kullanıcı açıkça kilitlemeden release sayılmaz.

## v2.5 kilitli kararları

- Kaptan kalıcı rol; ilk gün yalnız seçim.
- İlk tarafsız gecede Sadakat bilinmeden tam 1 Yakın Ufka gizli bakış; sonraki gecelerde makam otomatik bilgi vermez.
- Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylama, Kaptan rota oyu 2.
- İlk Hain gecesi: Hainler tanışır, 1 Yakın Ufka bakar, saldırı yapamaz.
- N-1 gerçek Güç + Çürümüş Erzak başlangıç paketi; ilk yolculuk gününe herkes 1 gerçek Güçle başlar.
- Kalkış Limanı `SET-KL-01` ana 118 kimliğin dışındaki fiziksel kurulum bileşenidir.
- Kamusal Harita açması kalıcıdır; ziyaret edilmedikçe olay çözülmez; açık Geçilmez engeldir.
- İskorbüt etkinse Ada ziyareti zorunludur; Ada girişinde olaydan önce temizlenir.
- Relocation guard ve Ada çevresi Girdap/Ters Akıntı invariantı korunur.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- Ana kart seti: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 118 ana kimlik.

## Güncel v2.6 taslağı

### Kural kitabı

- `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6_DRAFT.pdf`
- 29 sayfa A4.
- Tüm oyuncu kuralları, Moderatörün ilk oyun/sefer akışı, hafif storyteller rolü ve arka plan hikâyesi aynı kitapta.
- Ayrı Moderatör kartı güncel taslağın parçası değildir.
- Moderatör açılış sırası tek bölümde tutulur; ilk Hain gecesinden sonra normal sefer bölümünde kalır.
- Siyah Mühür hikâyesi kitabın sonunda tek parça anlatıdır.

### Fiziksel kart taslağı

- `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf`
- 34 sayfa A4.
- 118 ana kart kimliği korunur.
- Ana sayının dışında üç açık yardımcı kart: Kalkış Limanı + Varış/Hedef Limanı + Kaptan makamı.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- Çürümüş Erzak / İskorbüt kartı değiştirilmez.
- Bayat Peksimet (`GUC-22`) değiştirilmez.

### Güncel taslak paket

`/Oyun-GitHub/OYUN_v2.6_DRAFT_GUNCEL.zip`  
SHA-256: `ba39598ba0d5be7f592a5ab52fec65230e46d61b8885545321ea8734c024d483`

## Test durumu

- v2.5 mekanik validator / geometri / relocation / denge / PDF audit baseline: PASS.
- Güncel v2.6 kural kitabında kör Moderatör akışı ve çelişki kontrolü: PASS olarak çalışıldı; bu bir release kilidi değildir.
- Fiziksel yardımcı kart ekleri ana 118 kartın mekanik metnini değiştirmez.

## Kilit politikası

Kullanıcı açıkça “kilitle”, “stabil yap” veya eşdeğer bir onay vermeden v2.6 veya sonraki hiçbir taslak STABLE / LOCKED ilan edilmez.

## Kanonik kilitli artefakt

Library ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
