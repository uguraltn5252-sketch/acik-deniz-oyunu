# Test Log

## T-20260818-001 - v2.1 stabil paket doğrulaması
- Sonuç: PASS.
- 118 kart kimliği, başlangıç geometrisi, Ufuk yasallığı, manifest ve PDF bütünlüğü doğrulandı.

## T-20260818-002 - Dinamik başlangıç + tek Geçilmez Kayalık erişilebilirliği
- Sonuç: PASS / kritik geometri bulundu.
- `6×5` karşı-uç başlangıç/Liman geometrisinde son satır dışındaki zorunlu çapraz kareler kilit üretebildi; bu yüzden kurulum erişilebilirlik kontrolü zorunlu hale geldi.

## T-20260818-003 - 2/3 Gövde duyarlılığı
- Sonuç: 3 Gövde adayı reddedildi.
- Kanonik karar: bütün Haritalarda 2 Gövde.

## T-20260818-004 - 1/2 Geçilmez Kayalık + acil geri dönüş
- Sonuç: PASS / teknik kabul.
- 51.204 geometri yerleşimi; 51.102 yasal; 102 baştan reddedilecek.
- 15.000 yeni-kural davranışsal oyun + 6.000 kontrol.
- Kalıcı route lock: 0; kurulum hatası: 0.
- Temsilî Tayfa: %54,8; acil geri dönüş yaklaşık %4,2 oyun.

## T-20260818-005 - v2.2 çekirdek kaynak sözleşmesi
- Komut: `python oyun_simulasyon_v2_2.py --validate-only --geometry-audit`
- Sonuç: PASS.
- 2 Gövde, dinamik başlangıç, Kaptan omurgası, 1/2 Geçilmez Kayalık ve acil geri dönüş makine spec'iyle doğrulandı.

## T-20260818-006 - v2.2 baskı/release çapraz doğrulaması
- Sonuç: **PASS**.
- Kural kitabı: 32 sayfa; tüm sayfalar render edilip görsel tarandı.
- Kart PDF: 32 sayfa; tüm sayfalar render edildi; sayfa 2-32 baseline kart PDF ile metin ve sayfa ölçüsü bakımından eşleşiyor.
- Geçilmez Kayalık işaret PDF: 1 sayfa / 12 işaret; Türkçe glif ve kesim çizgileri kontrol edildi.
- Release PDF'lerinde görünür `v2.1` ibaresi yok.
- Kural PDF'sinde Kaptan kalıcılığı, kör ilk rota, başarılı İsyan/ölümde değişim, 2 Gövde, dinamik başlangıç, Geçilmez Kayalık ve acil geri dönüş hükümleri metinsel olarak doğrulandı.
- `V22_RELEASE_VALIDATION.md`: PASS.
- Hüküm: v2.2 stabil prototip olarak `releases/v2.2/` altında kilitlenebilir.
