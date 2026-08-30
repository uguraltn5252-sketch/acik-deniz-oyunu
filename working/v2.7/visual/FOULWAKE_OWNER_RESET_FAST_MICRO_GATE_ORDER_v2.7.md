# FOULWAKE v2.7 — Proje Sahibi Görsel Reset / Hızlı Mikro Kapı İş Emri

**Baş Editör kaynağı:** `v2.7-design@6e4f8f55d6f173d13293818f663e0fd6c0ae3d43`  
**Reddedilen exact pilot:** `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e`  
**Proje sahibi kanıtı:** `governance/PROJECT_OWNER_VISUAL_REJECTION_20260830.json`  
**Bağlayıcı KAPTAN referansı:** `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`  
**Durum:** `PROJECT_OWNER_REJECTED / ART_DIRECTION_RESET / VISUAL PRODUCTION PAUSED`

## 1. Son hüküm

Sanat Yönetiminin önceki `PILOT_ART_DIRECTION_PASS` kararı tarihsel inceleme kaydıdır; proje sahibinin estetik reddinden sonra üretim yetkisi vermez. Aktif candidate yoktur. Tam 121, final PDF, Simülasyon, release ve kilit kapalıdır.

## 2. KAPTAN kartı ve bağlayıcı sanat dili

`SET-KP-01` teknik kimliği/adet hesabı için korunur; görünen kart adı **KAPTAN**dır. Yüklenen kart KAPTAN ön yüzünün görsel kaynağı ve bütün deste için sanat dili anahtarıdır. Geminin, martının veya aynı sahnenin başka kartlarda tekrarı zorunlu değildir.

Bağlayıcı görsel dil:

- kalın, karakterli, elde çizilmiş siyah mürekkep konturu;
- yoğun gravür, çapraz tarama ve kirli baskı dokusu;
- sıcak yaşlı kâğıt;
- mat lacivert, oker, pas ve kirli krem;
- abartılı fakat tutarlı yüz/beden geometrisi;
- eski basım kart hissi;
- açık dijital boya, plastik AI parlaklığı, krom/specular deniz ve neon ışık yok.

KAPTAN kartında mevcut devredilebilir kaptanlık mekaniği korunur:

- Effect: **Kaptanlık açık bir makamdır; Sadakati kanıtlamaz. Kaptan değişebilir; makam oyundan kalkmaz.**
- Flavor: **Makam kalır. Şüphe de.**

## 3. Proje sahibinin arka-yüz dispozisyonu

- `BACK_SEA_ROCK`: **REWORK_REQUIRED** — deniz parlamayacak; tekrarlayan beyaz ışık pulları ve plastik/krom etki kaldırılacak.
- `BACK_ISLAND`: **REWORK_REQUIRED / FULL REDRAW** — ada arka yüzü bütünüyle yeniden kurulacak; sticker/karo/rozet hissi olmayacak.
- `BACK_LIGHTHOUSE`: **REWORK_REQUIRED** — fener büyüyebilir; uzun kayalık sırt zorunlu değildir. Kompakt kaya veya kıyı temeli kullanılabilir. Aile görünür, exact ön fener ve sonucu kör kalır.
- Diğer dört arka yüz: proje sahibi tarafından kabul edilmiş sayılmaz; şimdilik **HOLD**.

## 4. Kart metni kilidi

Görsel Tasarım kart adı, rol, effect, flavor, kimlik veya mekaniği yeniden yazamaz. Görsel üretim modeline kart metni çizdirilmez. İllüstrasyon ayrı üretilir; görünen metin yalnız kanonik UTF-8 kaynaktan şablonla yerleştirilir.

`exact: true` manifest beyanı kanıt değildir. Her final ön yüzde:

1. card-id → kanonik kayıt eşleşmesi,
2. başlık/effect/flavor alanlarının OCR veya doğrudan render-source çıkarımı,
3. normalize edilmiş exact karşılaştırma,
4. uyuşmazlıkta `BLOCKED_COPY_DRIFT`

zorunludur. Mevcut 12 ön yüz bu bağımsız denetim tamamlanana kadar KEEP değildir; **HOLD**dur.

## 5. Limit dostu yeni akış

### Aşama A — şu anda yetkili tek iş

Yalnız `FOULWAKE Sanat Yönetmeni`:

- KAPTAN referansını exact açar;
- en fazla **700 kelimelik tek bir sanat dili patchi** üretir;
- yalnız bir yeni dosya oluşturur:  
  `working/v2.7/visual/art_direction/FOULWAKE_KAPTAN_ART_LANGUAGE_PATCH_v2.7.md`;
- mevcut 121 manifesti, contact sheetleri, rasterları veya PDF'leri yeniden üretmez;
- Görsel Tasarıma üretim yetkisi vermez.

### Aşama B — patch proje sahibi tarafından kabul edilirse

Yalnız altı düşük çözünürlüklü thumbnail:

- 2 × `BACK_SEA_ROCK`
- 2 × `BACK_ISLAND`
- 2 × `BACK_LIGHTHOUSE`

Tek sheet olabilir. 300 dpi final, source-art paketi, provenance, SHA indeksi, altı layout, PDF ve 121 üretim yapılmaz.

### Aşama C — proje sahibi yönleri seçerse

Yalnız üç seçilmiş arka yüz finale alınır ve tek küçük masa örneğinde denenir. Bundan önce kanıt paketi şişirilmez.

## 6. Zorunlu kısa handoff

```
WORKSTREAM:
VISIBLE_CHAT_ACK: YES
SOURCE_BRANCH:
SOURCE_COMMIT:
SCOPE:
REFERENCE_OPENED: YES
FILES_CHANGED:
TOOLS_USED:
PLUGINS_USED:
NOT_USED_REASON:
RESULT:
TEMPORARY_SUBAGENTS: NONE
FULL_121_PRODUCTION_AUTHORIZED: NO
SIMULATION_AUTHORIZED: NO
LOCK_REQUESTED: NO
```
