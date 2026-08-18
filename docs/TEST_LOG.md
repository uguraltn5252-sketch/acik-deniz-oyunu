# Test Log

## T-20260818-001 — v2.1 stabil paket doğrulaması

- **Komut:** `python releases/v2.1/oyun_simulasyon_v2_1.py --validate-only`
- **Sonuç:** PASS
- **Kontrol edilenler:** oyuncu/Hain/Gövde tabloları, 118 kart kimliği, kanonik kart metni karması, harita başlangıcı, Ufuk yasallığı, her Liman sütununda kurulum, manifest SHA-256, PDF bütünlüğü.
- **Not:** Bu test denge simülasyonu veya kazanma oranı üretmez.
