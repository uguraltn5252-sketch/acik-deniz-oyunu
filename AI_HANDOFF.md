# FOULWAKE AI Handoff

Bu dosya yeni oturumun başlangıç noktasıdır. Güncel görev ve yazma yetkisi için
tek makine-okunur kaynak `governance/CURRENT_STAGE.json` dosyasıdır. Tarihsel
handoff, PASS, iş emri veya specialist branch çıktısı kendi başına yeni iş
yetkisi vermez.

## Güncel durum — 30 Ağustos 2026

- Son kilitli sürüm: **v2.6 STABLE / LOCKED**; exact kaynak `releases/v2.6/`.
- Aktif çalışma: **v2.7 DRAFT / NOT LOCKED / RELEASE BLOCKED**.
- Entegrasyon dalı: `v2.7-design`.
- Aktif görsel candidate: **YOK**.
- `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e`:
  proje sahibi tarafından reddedilmiş tarihsel kanıt.
- Tam 121, PDF, Simülasyon, release ve kilit: **YETKİSİZ**.
- Varsayılan uzman yazma politikası: **DENY**.

## Şu anda yetkili tek iş

`FOULWAKE Sanat Yönetmeni`, `work/v2.7-art-direction` dalında yalnız
`working/v2.7/visual/art_direction/FOULWAKE_KAPTAN_ART_LANGUAGE_PATCH_v2.7.md`
dosyasını düzeltebilir. Başlangıç commiti
`119136812c2c749e14e675f1400640664fa044bc`; toplam fark en fazla bir Markdown
dosyası ve 700 kelimedir.

Patch şu dört noktayı açıkça bağlamalıdır:

1. Yüklenen KAPTAN kartı yalnız stil örneği değil, `SET-KP-01` kartının
   bağlayıcı görsel kaynağıdır.
2. Görünen copy yalnız
   `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` kaynağından gelir.
3. Bütün ön/arka kartlar için bağımsız Sanat Yönetimi kadraj kapısı vardır.
4. Raster, thumbnail, contact sheet, layout, manifest, PDF veya tam üretim yoktur.

Diğer bütün hatlar yazmaya kapalıdır. Yeni aşama ancak düzeltilmiş patchin proje
sahibi tarafından kabulü ve yeni exact Baş Editör emriyle açılır.

## KAPTAN exact sözleşmesi

- Teknik kimlik: `SET-KP-01`.
- Görünen başlık: **KAPTAN**.
- Bölüm etiketi: **ÖZEL YETENEK**.
- Etki: **Oylamada eşitlik olursa, senin tarafın geçerli olur.**
- Flavor: **Lidere et. Gemi senin emrinde.**
- Görsel kaynak:
  `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`.
- Kaynak, KAPTAN figürü ve kart kompozisyonu için bağlayıcıdır; küçük
  crop/ölçek/renk/arka-plan temizliği yapılabilir. Boş sandalye veya başka özneyle
  değiştirilemez.
- Gemi, martı ve sahne diğer kartlar için zorunlu motif değildir; bağlayıcı
  deste dili mürekkep, yoğun gravür taraması, sıcak kirli kâğıt, mat
  lacivert–oker–pas paleti ve eski basım kart hissidir.
- Görsel model okunabilir kart metni üretmez. Copy kanonik UTF-8 kaynaktan
  şablonla yerleştirilir; OCR veya render-source exact karşılaştırması gerekir.
  Sapma: `BLOCKED_COPY_DRIFT`.

## Kadraj kapısı

Sanat Yönetmeni bütün ön ve arka kart illüstrasyonlarında kart oranı, 3 mm
taşma, 4–5 mm güvenli alan, ana figür/nesne ölçeği, odak, istemsiz yüz/el/nesne
kesimi, metin alanı çakışması, thumbnail ve masa-mesafesi okunurluğu ile
kadraj çeşitliliğini inceler. Görsel Tasarım kendi kadrajına PASS veremez.
Yalnız `FRAMING_PASS` veya `REFRAME_REQUIRED` kullanılabilir; sapma
`BLOCKED_FRAMING_DRIFT`tir.

## Arka yüz owner dispozisyonu

| Varlık | Güncel hüküm |
|---|---|
| `BACK_SEA_ROCK` | `REWORK_REQUIRED` — mat deniz; beyaz parlama, krom/specular veya plastik AI cilası yok |
| `BACK_ISLAND` | `REWORK_REQUIRED / FULL_REDRAW` — eski ada türetilmez; sticker/rozet/karo hissi yok |
| `BACK_LIGHTHOUSE` | `REWORK_REQUIRED` — fener daha büyük; uzun kayalık sırt zorunlu değil |
| Diğer dört arka | `HOLD` — proje sahibi kabulü yok |

## Zorunlu okuma sırası

1. `AI_HANDOFF.md`
2. `governance/CURRENT_STAGE.json`
3. `PROJECT_STATE.md`
4. `governance/DECISION_REGISTER.md`
5. `governance/ACTIVE_WORKSTREAMS.json`
6. `governance/WORKSTREAM_ASSIGNMENTS.md`
7. `governance/WORKSTREAM_PROTOCOL.md`
8. `governance/SUPERSESSION_MAP.json`
9. İlgili exact iş emri ve kaynak dosyaları

## Kaynak önceliği

1. Proje sahibinin en yeni açık kararı ve ona bağlı düzeltme kaydı.
2. Değişmeyen içerik/mekanik için v2.6 STABLE / LOCKED.
3. `governance/CURRENT_STAGE.json` içindeki aktif yetki.
4. `governance/DECISION_REGISTER.md` ve
   `working/v2.7/SOURCE_HIERARCHY_v2.7.json`.
5. Tarihsel üretim ve inceleme kanıtları.

Çelişkide otomatik seçim yapılmaz. İş durur ve exact dosya/alan/commit ile Baş
Editöre dönülür.

## Açık kritik çelişki

`SRC-002` exact karşılaştırması
`governance/SRC_002_COMPARISON_20260830.json` içindedir. v2.6
`GUC-22 = Bayat Peksimet` derken v2.7, `GUC-22 = Kaptanın Çatlak Kupası` ve
`GUC-23 = Bayat Peksimet` diyor. Proje sahibi karar vermeden kimlikler
düzeltilemez ve final 121/candidate/simülasyon baselineı kurulamaz.

## Kalıcı güvenlik kuralları

- `releases/v2.6/` yerinde değişmez.
- GitHub'a yazılmış olmak PASS, candidate, release veya lock değildir.
- Specialist dalı yalnız `CURRENT_STAGE` ve
  `WORKSTREAM_SCOPE_BASELINES.json` içinde exact yetkilendirilmiş dosyayı
  değiştirebilir.
- Handoff `TOOLS_USED`, `PLUGINS_USED`,
  `PLUGINS_AVAILABLE_BUT_NOT_USED` ve `NOT_USED_REASON` alanlarını içerir.
- Kilit sürecini yalnız proje sahibinin açık `kilitle/stable/release` talimatı
  başlatır; açık blocker varken uygulanmaz.

## Güncel devam komutu

> `governance/CURRENT_STAGE.json` içindeki tek dosyalık Sanat Yönetimi patch
> düzeltmesini bekle. Bunun dışında üretim başlatma.
