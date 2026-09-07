# FOULWAKE — 7 Eylül görsel çalışma pilotu

Somut inceleme ve oynama dosyaları `pdf/` içindedir: 30 sayfalık kural kitabı, 48 sayfalık 121 kart prototipi, 16 sayfalık görsel inceleme ve yedi tek sayfalık arka master.

Ön pilot kimlikleri: KAR-01, KAR-06, KAR-19, GUC-06, GUC-27, ERZ-01, SAD-H-03, HAR-AD-08, HAR-KY-06, HAR-AA-06, HAR-FN-04, SET-KP-01. Sonuncu, kabul edilmiş KAPTAN JPG'sinden yerleştirilir. Diğer 11 ön ve yedi arka özgün üretilmiş PNG'dir. Kalan 109 kimlik metin prototipidir.

`prompts.json` seçilen üretim ve yeniden işleme nedenlerini; `../../qa/recheck_visual/render_manifest.json` kimlik/ön-arka eşlemesi ve PDF hashlerini; `print_checks.json` kaynak, metin ve geometri kanıtını taşır. PNG kaynaklar değiştirilmeden saklanır. Baskı PDF'sinde piksel sayısı korunarak JPEG quality 80 / 4:4:4 kodlaması yapılır; fontlar vektördür.

Dış araçlar: image_gen.imagegen özgün çizim ve gerekli düzeltmeler; ReportLab tipografi ve PDF yerleşimi; PyMuPDF metin/geometri kontrolü ve render; Pillow yalnız PDF kodlaması ve teknik inceleme sayfa panoları. Üretici görüntü modelinin sürümü araç çıktısında bildirilmez. Ayrı geçici ajan veya bağımsız ikinci inceleyici kullanılmadı.

%100 A4 baskı; kart yaprakları 3. sayfadan başlayarak ön/arka çifttir. Uzun kenardan çevirme için arka sütunlar eşlenmiştir. Renkli taşma kesilir; tek arka master opak kılıf/kartonla kullanılmalıdır. 3 mm taşmalı arka master PDF'leri kesim dahil ölçüdedir; kaynak PNG ile baskı masterı aynı aşama değildir.

Aynı operatörün çalışma pilotudur; proje sahibinin estetik kabulü, matbaa PDF/X/CMYK kabulü, fiziksel renk/duplex/opaklık provası ve insan masası testi ayrıca beklenir. Ayrıntılı değerlendirme `../../qa/recheck_visual/visual_review.md` içindedir.
