# FOULWAKE KAPTAN Sanat Dili Patchi v2.7

**Baş Editör kaynağı:** `v2.7-design@7ce0b8c00f275e5b135201c54d4adf6aad45ac43`  
**Proje sahibi kararı:** `f9a8d14684cf09677cc4e2468033bd276c15b99d`  
**Bağlayıcı emir:** `working/v2.7/visual/FOULWAKE_OWNER_RESET_FAST_MICRO_GATE_ORDER_v2.7.md`  
**Reddedilen görsel girdi:** `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e`  
**Bağlayıcı referans:** `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`  
**Aşama:** ART_DIRECTION_MICRO_PATCH / VISUAL_PRODUCTION_PAUSED

## 1. Bağlayıcı sanat dili

KAPTAN kartındaki gemi, martı veya sahne düzeni deste genelinde kopyalanmaz. Bağlayıcı olan görsel dildir:

- Birincil siluetlerde kalın, karakterli, elde çekilmiş siyah mürekkep; ikincil biçimlerde daha ince fakat aynı el basıncını taşıyan kontur.
- Hacmi boya gradyanı yerine yönlü gravür, çapraz tarama, çizgi yoğunluğu ve sıcak kâğıt rezerviyle kurma.
- Sıcak kirli kâğıt üzerinde mat lacivert, donuk oker, pas kahvesi, kirli krem ve katran siyahıyla sınırlı palet.
- Yüz, beden, nesne ve coğrafyada grotesk fakat kendi içinde tutarlı oranlar: bilinçli abartı kabul edilir; rastgele deformasyon kabul edilmez.
- Aşınmış kenar, hafif baskı kusuru ve mürekkep birikimiyle eski basım kart hissi; doku genel “grunge” filtresi gibi yüzeye yapıştırılmaz.
- Airbrush, plastik dijital boya, krom/specular parlama, neon beyaz, lens bloom, pürüzsüz AI cilası ve yapay ışıldama yasaktır.

## 2. Üç yeniden çizim hedefi

### BACK_SEA_ROCK — REWORK_REQUIRED

Mevcut parlaklık, tekrarlayan beyaz ışık pulları ve cilalı/krom deniz etkisi kaldırılır. Deniz; mat lacivert ve siyah mürekkep kütleleri, kırık yönlü tarama ve yalnız gerekli yerlerde kirli kâğıt rezerviyle kurulur. Köpük seyrek, kesintili ve düşük kontrastlıdır; düzenli beyaz şerit, glow veya parlak dalga tepesi oluşturmaz. Sonuç derin ve hareketli, fakat ışıldamayan bir FOULWAKE denizi olmalıdır.

### BACK_ISLAND — REWORK_REQUIRED / FULL REDRAW

Mevcut ada kompozisyonu türetilmez; sıfırdan çizilir. Kara doğal, düzensiz ve denizin içinde fiziksel ağırlığı olan bir kıyı kütlesidir. Ortalanmış oval, çevresel halo, temiz grafik boşluk, kalın etiket konturu, rozet, ikon ve bağımsız karo/sticker etkisi yasaktır. Kıyı kırıkları, taş, toprak ve az bitki aynı mürekkep–tarama diliyle birleşir. Ada ailesi anlaşılır; belirli ön ada, yerleşim, ürün, kişi veya sonuç okunmaz.

### BACK_LIGHTHOUSE — REWORK_REQUIRED

Fener, normal kart ve thumbnail mesafesinde ilk bakışta seçilecek kadar büyütülür. Uzun çapraz kayalık sırt bağlayıcı değildir; kompakt kaya, kısa burun veya sade kıyı temeli kullanılabilir. Kule yığma taş, dönemsel ve anonimdir; küçük bir üst seyir/ateş yapısıyla okunur. Fener suya yapıştırılmış merkez ikonu gibi durmaz. Işın, glow, halo, modern beacon, Fresnel/Argand optiği, hedef veya madalyon yoktur. Aile görünür; exact ön fener ve sonuç kör kalır.

## 3. Görünen metin ve üretim kilidi

Görünen kart adı **KAPTAN**dır; `SET-KP-01` yalnız teknik kimliktir. Kart adı, rol, effect, flavor, kimlik ve mekanik yeniden yazılamaz. Görsel model hiçbir görünen kart yazısı üretmez. İllüstrasyon metinsiz hazırlanır; final metin yalnız kanonik UTF-8 kaynaktan şablonla yerleştirilir. OCR/render-source karşılaştırmasındaki her uyuşmazlık `BLOCKED_COPY_DRIFT` sonucudur.

Bu patch görsel üretim izni değildir. Thumbnail, final raster, contact sheet, layout, manifest, PDF ve 121 kart üretimi yapılmaz.

**RESULT:** ART_LANGUAGE_PATCH_DELIVERED / PENDING_PROJECT_OWNER_ACCEPTANCE  
**TEMPORARY_SUBAGENTS:** NONE  
**FULL_121_PRODUCTION_AUTHORIZED:** NO  
**SIMULATION_AUTHORIZED:** NO  
**LOCK_REQUESTED:** NO
