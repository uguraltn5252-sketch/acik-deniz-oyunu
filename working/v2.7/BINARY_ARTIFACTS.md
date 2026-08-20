# v2.7 Draft Binary Artifacts

**Durum:** **DRAFT / NOT LOCKED**  
**Mekanik baseline:** v2.6 STABLE / LOCKED  
**v2.7 görünen metin kaynakları:** `FOULWAKE_CARD_TEXTS_v2.7.json` ve `FOULWAKE_RULEBOOK_STORY_v2.7.md`  
**Görsel yön onayı:** 20 Ağustos 2026

GitHub deposunda büyük binary dosyaların kendileri yerine kanonik yol, boyut ve SHA-256 kayıtları tutulur.

## Candidate sınırı

Bu dosyadaki mevcut kayıtlar sanat yönü örneklerini ve 29 sayfalık görsel rulebook
taslağını tanımlar; güncel dal için tam 121 kartlık release candidate manifesti
değildir. Temiz v2.7 sıfırlamasından önceki 121/121 üretim ve final preflight
kayıtları tarihsel kanıttır; güncel source commit, renderlar ve manifestlerle
yeniden bağlanmadan `ART-001` veya `SRC-001` engelini kapatmaz.

Candidate tesliminde kart/rulebook source → render → PDF izlenebilirliği,
121/121 front/back eşlemesi, SHA-256 manifestleri ve fiziksel prova kayıtları bu
dosyaya exact commit kimliğiyle eklenir.

## v2.7 görsel taslak çıktıları

- Kural kitabı görsel taslağı: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf`  
  SHA-256: `cc3b36fb317c6469a34e51ec9c4baa49f2d420e2cbffec400e9ff629f93f5690`  
  Boyut: `34244928` byte  
  Sayfa: `29` A4

- Onaylı sanat yönü baskı seti: `/Oyun-GitHub/v2.7/exports/FOULWAKE_v2.7_APPROVED_ART_DIRECTION_PRINT_SET.pdf`  
  SHA-256: `5d0aac67b5c746209c35662ebf2680f0819259e98ea3c5f4d629496c811cf5e2`  
  Boyut: `7937209` byte  
  Sayfa: `2` A4

- KAR-01 Uzakgören kart yüzü: `/Oyun-GitHub/v2.7/exports/KAR-01_Uzakgoren_front.png`  
  SHA-256: `b3605fb05e9baa77a60fa696d6851179501d57e1c6fa647ef54d3ff58c34e20d`  
  Boyut: `1641364` byte  
  Piksel: `898 × 1488`, 300 dpi, taşmalı çalışma ölçüsü `76 × 126 mm`

- GUC-24 Islak Çorap kart yüzü: `/Oyun-GitHub/v2.7/exports/GUC-24_Islak_Corap_front.png`  
  SHA-256: `a812249cda1f24cc64f4f5fe747d110f9b67ee3a24b285776be3f0e2e4c916a3`  
  Boyut: `1090499` byte  
  Piksel: `821 × 1121`, 300 dpi, taşmalı çalışma ölçüsü `69,5 × 94,9 mm`

- HAR-AD-09 Deryanın Göbek Deliği kart yüzü: `/Oyun-GitHub/v2.7/exports/HAR-AD-09_Deryanin_Gobek_Deligi_front.png`  
  SHA-256: `b5d0aff9c531f9079ed416726362644e00103ecf95cb2cc4991ea5c7330f52ea`  
  Boyut: `1091019` byte  
  Piksel: `898 × 898`, 300 dpi, taşmalı çalışma ölçüsü `76 × 76 mm`

- Deniz + Kayalık ortak arka yüz: `/Oyun-GitHub/v2.7/exports/BACK_SEA_ROCK.png`  
  SHA-256: `c3cf3399c294874bb12194f9bdf369a00110b7c78d2a234590c16be864e74c45`  
  Boyut: `2035243` byte  
  Piksel: `898 × 898`, 300 dpi, taşmalı çalışma ölçüsü `76 × 76 mm`

Bu dosyalar sanat yönü ve baskı hiyerarşisi için onaylanmış v2.7 taslaklarıdır; tam 121 kartlık görsel üretimin tamamlandığı veya v2.7'nin kilitlendiği anlamına gelmez.

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
