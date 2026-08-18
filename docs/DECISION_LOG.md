# Decision Log

## D-20260818-001 - v2.1'i değiştirilemez stabil temel olarak koru
- **Durum:** Kabul.
- **Karar:** `releases/v2.1/` yerinde değiştirilmez; yeni sürümler ayrı release olarak tutulur.

## D-20260818-002 - Kaptan kalıcı omurgadır ve ilk rotayı seçer
- **Durum:** Kabul.
- **Karar:** Kaptan rolü asla kaldırılmaz. İlk rotayı Kaptan tek başına, olay bilgisi olmadan seçer. Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferinde yeni Kaptan seçilir. Kaptan gece ayrıca uyanmaz ve makamı otomatik Ufuk bilgisi vermez.

## D-20260818-003 - Geçilmez Kayalık Liman yaklaşım hattına konulamaz
- **Durum:** Kabul.
- **Karar:** Geçilmez Kayalık son Liman/Ufuk hattına konulamaz; kurulum baştan çözümsüz olamaz.

## D-20260818-004 - Gövde bütün Haritalarda 2 kalır
- **Durum:** Kabul; 3 Gövde adayı reddedildi.
- **Karar:** Bütün Haritalarda başlangıç Gövdesi 2.

## D-20260818-005 - Geçilmez Kayalık her oyunda bulunur; çıkmazda geri dönüş açar
- **Durum:** Kabul.
- **Karar:** `5×5`, `5×6`, `6×5` için 1; `5×7`, `6×6`, `6×7` için 2 işaret. Normal geri hareket yasaktır; yalnız Kayalık kaynaklı tam çıkmazda bir önceki kareye bir tam hareket/gün harcayarak geri dönülebilir. Çözülmüş olay tekrar çalışmaz.
- **Test:** T-20260818-004 PASS.

## D-20260818-006 - Yeni sürüm v2.2 olarak adlandırılır
- **Durum:** Kabul.
- **Karar:** v2.1 sonrası kesinleşen değişiklikler v2.2 altında toplanır.

## D-20260818-007 - v2.2 stabil prototip olarak kilitlenir
- **Durum:** Kabul.
- **Karar:** İnsan kuralı, JSON/spec, doğrulayıcı, kural PDF'si, kart PDF'si ve Geçilmez Kayalık fiziksel işaret PDF'si çapraz doğrulamayı geçtikten sonra v2.2 `releases/v2.2/` altında değiştirilemez stabil prototip olarak kilitlenir.
- **Test:** T-20260818-005 PASS; T-20260818-006 PASS.
- **Sonuç:** Sonraki tasarım değişiklikleri v2.3+ olarak açılmalıdır.
