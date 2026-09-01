# FOULWAKE KAPTAN Sanat Dili ve Kadraj Patchi v2.7

**Güncel Baş Editör kaynağı:** `v2.7-design@0d7731a59f3ff689174a34bbfe5491e908c64dd3`  
**Yaratıcı düzeltme kaynağı:** `v2.7-design@bd2be30f59458752561ae30bf43bcfeff59a2f10`  
**Proje sahibi kararı:** `f9a8d14684cf09677cc4e2468033bd276c15b99d`  
**Baseline:** `work/v2.7-art-direction@119136812c2c749e14e675f1400640664fa044bc`  
**Bağlayıcı emir:** `working/v2.7/visual/FOULWAKE_OWNER_RESET_FAST_MICRO_GATE_ORDER_v2.7.md`  
**Bağlayıcı referans:** `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`  
**Aşama:** ART_DIRECTION_MICRO_PATCH / VISUAL_PRODUCTION_PAUSED

## 1. KAPTAN kaynağı ve bağlayıcı deste dili

Yüklenen KAPTAN kartındaki ana kaptan figürü ve ana kart kompozisyonu, teknik kimliği `SET-KP-01` ve görünen adı **KAPTAN** olan kartın bağlayıcı ana görsel kaynağıdır; kaynak yalnız `STYLE_ONLY` değildir. KAPTAN tamamen yeni bir kaptan konsepti, boş sandalye veya farklı ana özneyle değiştirilemez. Yalnız kart şablonuna uyum için gerekli küçük crop, ölçek, renk dengesi ve arka-plan/kenar temizliği yapılabilir; figürün kimliği ve kompozisyonun ana ilişkisi korunur.

Gemi, martı ve sahnenin birebir tekrarı diğer kartlarda zorunlu değildir. Deste genelinde bağlayıcı olan, KAPTAN kaynağından türetilen şu sanat dilidir:

- Kalın, karakterli, elde çekilmiş mürekkep konturu; hacimde yönlü gravür, yoğun çapraz tarama ve çizgi birikimi.
- Sıcak kirli kâğıt üzerinde mat lacivert, donuk oker, pas kahvesi, kirli krem ve katran siyahıyla sınırlı palet.
- Yüz, beden, nesne ve coğrafyada grotesk fakat kendi içinde tutarlı oranlar; bilinçli abartı kabul edilir, rastgele deformasyon edilmez.
- Aşınmış kenar, mürekkep birikimi ve hafif baskı kusuruyla eski basım kart hissi; yüzeye yapıştırılmış genel grunge filtresi kullanılmaz.
- Airbrush, plastik dijital boya, krom/specular parlama, neon beyaz, lens bloom, pürüzsüz AI cilası ve yapay ışıldama yasaktır.

Bu dil asgari teknik checklist değildir: her görselde maddi inandırıcılık, yaratıcı özgüllük ve deste içi akrabalık aranır; yalınlaştırma sanat değerlendirmesinin derinliğini veya yaratıcı kalite standardını düşüremez.

## 2. KAPTAN exact copy kilidi

Görünen metin yalnız `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` kanonik kaynağından exact alınır:

- Başlık: `KAPTAN`
- Bölüm etiketi: `ÖZEL YETENEK`
- Etki: `Oylamada eşitlik olursa, senin tarafın geçerli olur.`
- Flavor: `Lidere et. Gemi senin emrinde.`

Görsel üretim modeli bu metni üretmez, yeniden yazmaz veya resme gömmez. Final uygulamada copy kanonik UTF-8 kaynaktan şablonla yerleştirilir. OCR/render-source exact karşılaştırmasındaki uyuşmazlık `BLOCKED_COPY_DRIFT`tir.

## 3. Üç yeniden çizim hedefi

### BACK_SEA_ROCK — REWORK_REQUIRED

Parlaklık, beyaz ışıldama, düzenli beyaz ışık pulları ve cilalı/krom deniz etkisi kaldırılır. Deniz mat lacivert–siyah mürekkep kütleleri, kırık yönlü tarama ve seyrek düşük-kontrast köpükle kurulur; derin ve hareketli fakat ışıldamayan FOULWAKE denizi okunur.

### BACK_ISLAND — REWORK_REQUIRED / FULL_REDRAW

Tamamen yeniden çizilir; mevcut ada kompozisyonu türetilmez. Kara doğal, düzensiz, denizde fiziksel ağırlığı olan bir kıyı kütlesidir. Ortalanmış oval, çevresel halo, temiz grafik boşluk, kalın etiket konturu, sticker, ikon, rozet ve bağımsız karo etkisi yasaktır. Ada ailesi görünür; exact ön ada, yerleşim veya sonuç gizli kalır.

### BACK_LIGHTHOUSE — REWORK_REQUIRED

Fener, kart, thumbnail ve normal masa mesafesinde ilk bakışta seçilecek kadar büyütülür. Uzun kayalık sırt zorunlu değildir; kompakt kaya, kısa burun veya sade kıyı temeli kullanılabilir. Yığma taş kule ve sade üst seyir/ateş yapısı dönemsel, anonim ve mürekkepli okunur. Merkez ikon, ışın, glow, halo, modern beacon, Fresnel/Argand optiği, hedef veya madalyon yoktur; exact ön fener ve sonuç gizli kalır.

## 4. Bağımsız kadraj kapısı

Sanat Yönetimi, bütün ön ve arka kart illüstrasyonlarının kadrajını her görsel kapıda bağımsız değerlendirir. Görsel Tasarım kendi kadrajına nihai PASS veremez. Kontrol en az şunları kapsar:

- exact kart oranı, illüstrasyon penceresi, 3 mm bleed ve 4–5 mm safe area;
- ana figür/nesne ölçeği, odak, görsel hiyerarşi ve denge;
- yüz, el veya gerekli ana nesnelerde istemsiz/anlamsız kesim;
- başlık, effect, flavor ve card-id alanlarıyla çakışma;
- çizgi ve siluet düzeyinde thumbnail ve normal masa-mesafesi okunurluğu;
- kartlar arasında aynı plan, model, poz veya benzer kadraj tekrarlarının aşırılaşması;
- deste genelindeki kompozisyon ve kadraj ritmi.

Her görsele yalnız `FRAMING_PASS` veya `REFRAME_REQUIRED` verilir. `FRAMING_PASS` olmadan ilgili görsel KEEP, final veya tam üretime geçemez; sapma `BLOCKED_FRAMING_DRIFT`tir.

## 5. Üretim kilidi

Bu patch governance mimarisini değiştirmez ve görsel üretim yetkisi vermez. Bu aşamada raster, thumbnail, final görsel, contact sheet, layout, manifest, PDF, release artefaktı veya 121 kart üretilmez/değiştirilmez. Yeni Görsel Tasarım üretimi ancak proje sahibi kabulü ve yeni exact Baş Editör emriyle açılabilir.

**RESULT:** ART_LANGUAGE_PATCH_CORRECTED / PENDING_PROJECT_OWNER_ACCEPTANCE  
**TEMPORARY_SUBAGENTS:** NONE  
**FULL_121_PRODUCTION_AUTHORIZED:** NO  
**SIMULATION_AUTHORIZED:** NO  
**LOCK_REQUESTED:** NO
