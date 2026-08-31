# FOULWAKE Çalışma Hattı Görevleri

**Aktif visual candidate:** **YOK**  
**Yetki kaynağı:** `governance/CURRENT_STAGE.json`  
**Kapsam politikası:** `governance/WORKSTREAM_SCOPE_BASELINES.json`  
**Varsayılan:** Exact güncel yetki yoksa yazma yoktur.

## Güncel görev tablosu

| Hat | Görünür sohbet | Dal / reset baseline | Durum | Şu anda yapılabilecek iş |
|---|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` | `work/v2.7-story@e04eef7f...` | PAUSED | Hiçbir dosya değişikliği yok |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` | `work/v2.7-art-direction@11913681...` | REWORK_REQUIRED | Yalnız KAPTAN patch dosyasını ≤700 kelimeyle düzelt |
| Görsel | `FOULWAKE Görsel Tasarım 2` | `work/v2.7-visual@23c062f6...` | OWNER-REJECTED / PAUSED | Hiçbir görsel veya kanıt üretme |
| Simülasyon | `Simülasyon Testi` | Dal yok | NOT STARTED | Dal açma ve test başlatma |
| Baş Editör | Bu sohbet | `v2.7-design` | ACTIVE | Kaynak, governance, entegrasyon ve kapsam denetimi |

## Sanat Yönetimi — exact mevcut görev

Yalnız şu dosya değişebilir:

`working/v2.7/visual/art_direction/FOULWAKE_KAPTAN_ART_LANGUAGE_PATCH_v2.7.md`

Cumulative fark `119136812c2c749e14e675f1400640664fa044bc..HEAD` üzerinden
hesaplanır; en fazla 1 dosya, Markdown ve 700 kelime.

Patch:

- gönderilen KAPTAN kartını `SET-KP-01` için ana görsel kaynak olarak tanımlar;
- exact görünen copyyi
  `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` kaynağına bağlar;
- bütün ön/arka kartlar için bağımsız `FRAMING_PASS / REFRAME_REQUIRED`
  kapısını ekler;
- görsel üretim yetkisi vermez.

Raster, thumbnail, contact sheet, layout, manifest, PDF, kaynak paket, release
ve lock alanları kapsam dışıdır.

## Görsel — bekleme hükmü

`23c062f6...` pilotu proje sahibi tarafından reddedildi. Eski Sanat Yönetimi
PASS'i veya teknik manifestler üretim yetkisi değildir. KAPTAN görseli boş
sandalye/başka figürle değiştirilemez; görünen copy görsel modelce yazılamaz.
Yeni Görsel iş ancak düzeltilmiş patchin proje sahibi kabulünden sonra yeni
exact Baş Editör emriyle açılır.

## Simülasyon — bekleme hükmü

Aktif candidate ve `SRC-002` kararı yokken dal açılmaz. İleride yetki verilirse
Data Analytics kullanımı ve yeniden üretilebilir seed/komut/ham çıktı kanıtı
zorunludur. Game Studio yalnız oynanabilir tarayıcı prototipi açıkça
yetkilendirilirse gerekir.

## Baş Editör sorumlulukları

- `CURRENT_STAGE` ile görevleri tekil ve çelişkisiz tutmak.
- Specialist cumulative farklarını reset baseline üzerinden denetlemek.
- `releases/v2.6` exact tree SHA'sını korumak.
- KAPTAN copy, kadraj, provenance ve tool/plugin beyanlarını doğrulamak.
- `SRC-002` için proje sahibinin seçimini beklemek; tahminle kimlik değiştirmemek.
- Candidate, Simülasyon, release ve lock kapılarını ayrı tutmak.

## Handoff asgari alanları

`WORKSTREAM`, `VISIBLE_CHAT`, `VISIBLE_CHAT_ACK`, `SOURCE_BRANCH`,
`SOURCE_COMMIT`, `AUTHORIZATION_STAGE`, `SCOPE`, `CHANGED_FILES`,
`PROTECTED_FIELDS_CONFIRMED`, `TESTS_RUN`, `TOOLS_USED`, `PLUGINS_USED`,
`PLUGINS_AVAILABLE_BUT_NOT_USED`, `NOT_USED_REASON`, `RESULT`,
`OPEN_RISKS`, `NEXT_RECIPIENT`, `LOCK_REQUESTED`.
