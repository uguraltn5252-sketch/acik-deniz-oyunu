# v2.7 Draft Binary Artifacts

**Durum:** **DRAFT / NOT LOCKED**  
**Metin ve mekanik kaynağı:** v2.6 STABLE / LOCKED  
**Görsel yön onayı:** 20 Ağustos 2026

GitHub deposunda büyük binary dosyaların kendileri yerine kanonik yol, boyut ve SHA-256 kayıtları tutulur.

## v2.7 görsel taslak çıktıları

- Tarihsel kural kitabı görsel taslağı: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf`  
  SHA-256: `cc3b36fb317c6469a34e51ec9c4baa49f2d420e2cbffec400e9ff629f93f5690`  
  Boyut: `34244928` byte  
  Sayfa: `29` A4  
  Kanıt durumu: `NOT_CURRENT_V2_7_STORY_INTEGRATION_EVIDENCE`; v2.6 iç sayfalarını yeniden stilleyen bu dosya güncel v2.7 anlatı yerleşiminin source -> render -> PDF kanıtı değildir.

- Kural kitabı temsilî doğrulama provası: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_RULEBOOK_REPRESENTATIVE_PROOF.pdf`  
  SHA-256: `ec3946ca413b862721320e35c2c1561c6f1d068b43132a56322173e49c026bf7`  
  Boyut: `2409487` byte  
  Sayfa: `2` A4  
  Kaynak: `FOULWAKE_RULEBOOK_STORY_v2.7.md` blob `f1e0eb75434540a85e8b21484acd99ca0abc66cf`; bölümler `3.3`, `3.4`, `3.6`

- Onaylı sanat yönü baskı seti: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_APPROVED_ART_DIRECTION_PRINT_SET.pdf`  
  SHA-256: `271dca14330e95d76501232d4a14bab9e692aed01cb4dd9a43a267d625d8dba6`  
  Boyut: `7749855` byte  
  Sayfa: `2` A4

- KAR-01 Uzakgören kart yüzü: `/Oyun-GitHub/v2.7/exports/KAR-01_Uzakgoren_front.png`  
  SHA-256: `2798de04b8d7660ac98a842944c9b8b67acd377505de16ca9f7e7cbe40b3a14b`  
  Boyut: `1642513` byte  
  Piksel: `898 × 1488`, 300 dpi, taşmalı çalışma ölçüsü `76 × 126 mm`

- GUC-24 Islak Çorap kart yüzü: `/Oyun-GitHub/v2.7/exports/GUC-24_Islak_Corap_front.png`  
  SHA-256: `308771d8aeb5e8b3bf452db036f3983e0e6990f6c441e52bf61733945fb421df`  
  Boyut: `1019620` byte  
  Piksel: `821 × 1121`, 300 dpi, taşmalı çalışma ölçüsü `69,5 × 94,9 mm`  
  Metin kaynağı: Card Texts blob `38a03b71cd3232fd844db8d80d8e53662510b6a3`; eski flavor metni exact kaynağa düzeltilmiştir.

- HAR-AD-09 Deryanın Göbek Deliği kart yüzü: `/Oyun-GitHub/v2.7/exports/HAR-AD-09_Deryanin_Gobek_Deligi_front.png`  
  SHA-256: `cf3b0d7847ee115eb353c73b575a62524d2dce9c629a4745290fce675af8420c`  
  Boyut: `1030232` byte  
  Piksel: `898 × 898`, 300 dpi, taşmalı çalışma ölçüsü `76 × 76 mm`

- Deniz + Kayalık ortak arka yüz: `/Oyun-GitHub/v2.7/exports/BACK_SEA_ROCK.png`  
  SHA-256: `c3cf3399c294874bb12194f9bdf369a00110b7c78d2a234590c16be864e74c45`  
  Boyut: `2035243` byte  
  Piksel: `898 × 898`, 300 dpi, taşmalı çalışma ölçüsü `76 × 76 mm`

Bu dosyalar sanat yönü ve baskı hiyerarşisi için temsilî v2.7 taslaklarıdır; tam 121 kartlık görsel üretimin tamamlandığı veya v2.7'nin kilitlendiği anlamına gelmez.

## İlk aşama izlenebilirlik kayıtları

- `working/v2.7/visual/manifests/FOULWAKE_CARD_INVENTORY_v2.7.json`: 121 kartın kimlik, kaynak, ölçü ve arka yüz eşleme envanteri.
- `working/v2.7/visual/manifests/FOULWAKE_SOURCE_RENDER_PDF_PROVENANCE_v2.7.json`: kaynak blobu -> render SHA-256 -> PDF sayfası zinciri.
- `working/v2.7/visual/FOULWAKE_VISUAL_REVALIDATION_v2.7.md`: temsilî okunabilirlik, tutarlılık ve risk raporu.

Tam 121 kartlık candidate, tam 29 sayfalık v2.7 kural kitabı entegrasyonu, fiziksel baskı/kesim/duplex/ışık testi ve kör dönüş-yön sızıntı testi henüz tamamlanmamıştır.

## Kilitli v2.6 kaynakları

- Kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf`  
  SHA-256: `192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a`  
  Boyut: `1104041` byte  
  Sayfa: `29` A4

- Tam Kart PDF: `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6.pdf`  
  SHA-256: `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298`  
  Boyut: `1768745` byte  
  Sayfa: `34` A4

- Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`  
  SHA-256: `ffc9c17c725e6093c62a3ebddc5f19c36fb0647f6a51a3e7014852fe0623d534`  
  Boyut: `4360296` byte

Kilitli `releases/v2.6/` ağacı ve v2.6 binary kaynakları değiştirilmemiştir.
