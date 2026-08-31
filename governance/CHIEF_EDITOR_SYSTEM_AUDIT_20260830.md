# FOULWAKE Baş Editör Sistem Denetimi — 30 Ağustos 2026

**Denetlenen branch:** `v2.7-design`  
**Başlangıç head:** `bd2be30f59458752561ae30bf43bcfeff59a2f10`  
**Kapsam:** Repository kaynakları, görev/yetki modeli, specialist dalları,
workflow/CI, art briefleri, copy, kadraj, release/lock ve gelecekteki hata riski  
**Sonuç:** Kritik aktif çelişkiler düzeltildi; `SRC-002` ve `GOV-001` dış
bağımlılık/proje sahibi kararı nedeniyle açık

## 1. Envanter ve doğrulama

- 151 Git tree girdisi; 132 blob.
- 131 text kaynağı ve bir KAPTAN JPEG referansı.
- 70 Markdown, 39 JSON, 9 Python, 1 workflow YAML, 2 CSV, 9 TXT, 1 JPEG.
- 39/39 JSON parse edildi.
- 121/121 art-brief kaydı; kimlikler benzersiz; indeksler 1–121.
- Front aileleri: 20 Karakter, 30 Güç, 1 Çürümüş, 15 Sadakat, 30 Açık Deniz,
  12 Kayalık, 6 Ada, 4 Deniz Feneri, 3 Yardımcı.
- Back eşlemesi: 20/31/15/42/6/4/3 = 121.
- `releases/v2.6` bütün branchlerde exact aynı tree:
  `efb41c46f06174c42dcdab2859b7c0ba517f86f0`.
- Branch resetleri:
  - story `e04eef7f1fef6ea407feaaf26558551297c44b37`
  - art direction `119136812c2c749e14e675f1400640664fa044bc`
  - visual `23c062f6de06c32eab224b3440c8474725d4fe9e`
  - simulation: yok

## 2. Kritik bulgular ve düzeltmeler

| Önem | Bulgu | Gelecek riski | Uygulanan düzeltme |
|---|---|---|---|
| CRITICAL | AI_HANDOFF, PROJECT_STATE, ACTIVE_WORKSTREAMS ve SOURCE_HIERARCHY eski pilot PASS/12+7 KEEP durumunu aktif gibi taşıyordu | Yeni uzman reddedilmiş paketten tam üretime başlayabilirdi | Tek `CURRENT_STAGE.json`; no candidate; diğer durum kaynakları aynı hükme çekildi |
| CRITICAL | `SET-KP-01` manifest ve pilot briefi yüklenen KAPTANı yasaklayıp boş sandalye, farklı ad ve farklı iç copy üretiyordu | Owner kartı yeniden kaybolur; copy/mekanik drift oluşur | Owner correction evidence, exact copy override, manifest ve pilot brief tam düzeltildi |
| CRITICAL | Görsel model için gerçek source→render copy karşılaştırması yoktu; self-declared `exact:true` yeterli sayılıyordu | Başlık/effect/flavor sessizce değişebilirdi | Template-only copy, OCR/render-source exact compare ve `BLOCKED_COPY_DRIFT` |
| CRITICAL | Kadraj bağımsız kabul kapısı değildi | Yüz/el/nesne kesimi, kötü ölçek ve metin çakışması teknik PASS içinde kaçabilirdi | Bütün front/back için Art Direction `FRAMING_PASS/REFRAME_REQUIRED`; Visual self-PASS yasak |
| HIGH | Workflow specialist direct pushlarda çalışmıyordu | PR açmadan scope dışı dosya push edilebilirdi | Bütün `work/**` pushları ve cumulative scope validator |
| HIGH | Visual regex bütün `working/v2.7/visual/**` alanına izin veriyordu | Görsel, art-direction briefi/referans/Chief order değiştirebilirdi | Exact path allowlist; aktif yetki yoksa default-deny |
| HIGH | Art Direction normalde bütün art_direction ağacına yazabiliyordu | Tek patch emriyle çok dosya veya binary üretilebilirdi | Reset baseline + exact bir path + 1 file + ≤700 word + text only |
| HIGH | Locked v2.6 diff tabanlı kontrol root/zero-before durumunda zayıftı | Eksik diff veya geçmiş baz seçiminde drift kaçabilirdi | Her eventte exact Git subtree SHA doğrulaması |
| HIGH | Eski work order ve PASS belgeleri aktif kaynaklarla aynı öncelikteydi | Tarihsel görev yeniden çalıştırılabilirdi | `SUPERSESSION_MAP.json` ve active/historical source ayrımı |
| HIGH | BACK_LIGHTHOUSE briefi küçük kuleyi uzun iki yönlü kaya sırtına zorluyordu | Owner kararı yine ihlal edilebilirdi | Lighthouse briefi kompakt temel ve daha büyük kuleyle yeniden yazıldı |
| HIGH | BACK_ISLAND briefi eski varlıktan türetmeyi açıkça yasaklamıyordu | Reddedilmiş ada paint-over/crop olarak dönebilirdi | `FULL REDRAW`; crop/trace/recolor/paint-over yasağı |
| HIGH | BACK_SEA_ROCK owner eleştirisi tek aktif hedef değildi | Parlak beyaz pullar/krom deniz geri gelebilirdi | “Mat ve ışıldamayan”; specular/bloom/plastik AI yasağı |
| MEDIUM | Simülasyon gate verdictleri serbest stringdi | Belirsiz verdict release kontrolünü geçebilirdi | Kapalı PASS/PASS_WITH_MINOR_ISSUES/FAIL/BLOCKER enumları |
| MEDIUM | Lock schema exact tree/candidate/evidence bağlarını yeterince zorlamıyordu | Yanlış candidate veya açık blocker ile lock oluşabilirdi | Exact tree, attestation hash, fiziksel kanıt, sıfır blocker ve owner command |
| MEDIUM | PR/handoff araç ve eklenti kullanımını kaydetmiyordu | Canva/Data Analytics/Game Studio kullanımı denetlenemezdi | TOOLS/PLUGINS/AVAILABLE_BUT_NOT_USED/REASON alanları |
| MEDIUM | Görünür Visual sohbet adı eskiydi | Handoff yanlış sohbete mal edilebilirdi | `FOULWAKE Görsel Tasarım 2` tek güncel isim |
| MEDIUM | checkout v4 Node20 deprecation uyarısı üretiyordu | Gelecekte runner uyumsuzluğu | Official checkout v7.0.1 exact commit pin |
| MEDIUM | `SRC-002` exact iki seçenek olarak kayıtlı değildi | Uzman kimliği tahminle değiştirebilirdi | Exact karşılaştırma ve iki owner-choice kaydı |

## 3. KAPTAN exact düzeltmesi

Kaynak JPEG:

- Path:
  `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`
- Git blob: `6e3dc9eb5ac00758bc5dd307bc5bd646435ec5f4`
- SHA-256:
  `a3224299f1b868ec71b6f637e3cb4bdd48dd5ba978178a0a64bef3e052193a2a`
- Boyut: 896×1536; oran 7:12.

Exact visible copy: `KAPTAN` / `ÖZEL YETENEK` /
`Oylamada eşitlik olursa, senin tarafın geçerli olur.` /
`Lidere et. Gemi senin emrinde.`

Bu v2.7 owner overrideıdır; locked v2.6 yerinde değiştirilmemiştir.

## 4. CI ve görev güvenliği

`validate_workstream_scope.py` her specialist branchi kendi reset commitinden
HEAD'e kadar kümülatif denetler. Bu yöntem Visual dalındaki eski, tarihsel
story dosyalarını yeni ihlal sanmaz; yalnız reset sonrasındaki yeni işi ölçer.

- Yetki yoksa changed file sayısı sıfır olmalıdır.
- Yetki varsa exact paths, dosya sayısı, extension, binary ve kelime sınırı
  birlikte doğrulanır.
- Protected Chief Editor alanları her durumda yasaktır.
- Simulation branch güncel aşamada oluşursa CI BLOCKER verir.
- Policy specialist branchin eski kopyasından değil
  `origin/v2.7-design` kaynağından yüklenir.
- Pull request denetimi merge ref yerine exact PR head SHA'yı kullanır.

## 5. Bilerek korunmuş tarih

Eski handoff, Sanat Yönetimi PASS ve rework kanıtları silinmedi veya yeniden
yazılmadı. Bunlar denetim izi olarak tutulur; üretim yetkisi
`SUPERSESSION_MAP.json` ile kaldırılmıştır. Specialist branchler değiştirilmedi.

## 6. Açık kalan konular

### SRC-002 — proje sahibi kararı gerekir

v2.6 `GUC-22 = Bayat Peksimet`; v2.7 `GUC-22 = Kaptanın Çatlak Kupası` ve
`GUC-23 = Bayat Peksimet`. Hangisinin amaçlı olduğu repositoryden kanıtlanamaz.
Baş Editör bunu tahminle düzeltemez. Seçenekler:
`governance/SRC_002_COMPARISON_20260830.json`.

### GOV-001 — GitHub platform sınırı

`main` ve `v2.7-design` branch protection `protected:false`. Rulesets uç noktası
private repository/current plan için 403 döndürür. Workflow direct pushu
sonradan FAIL eder fakat server-side pushu önceden reddedemez. Repository
public yapılırsa veya GitHub Pro/ruleset yetkisi sağlanırsa required status
check ve force-push/deletion yasağı ayrıca etkinleştirilmelidir.

### Fiziksel kanıt

Baskı, kesim, duplex, opaklık, gerçek ışık ve masa-mesafesi kanıtı yapılmadı.
Dijital test bunu ikame etmez.

## 7. Güncel tek sonraki adım

Sanat Yönetmeni `119136812...` baselineından yalnız mevcut KAPTAN patch
dosyasını düzeltir. Patch, KAPTANın SET-KP-01 ana görsel kaynağı olduğunu,
exact copy kaynağını ve bağımsız kadraj kapısını açıkça taşımalıdır. Proje
sahibi kabulü ve yeni exact Chief Editor order olmadan görsel üretim başlamaz.
