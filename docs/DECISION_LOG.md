# Decision Log

Tasarım kararlarının gerekçesi burada tutulur. Sohbet içinde alınmış bir karar, buraya ve ilgili kaynak dosyalara işlenmeden resmî sürüm kararı sayılmaz.

## Şablon

### D-YYYYMMDD-001 — Karar başlığı

- **Durum:** Öneri / Testte / Kabul / Reddedildi / Geri alındı
- **Sorun:**
- **Karar:**
- **Gerekçe:**
- **Etkilenen dosyalar:**
- **Test:**
- **Sonuç:**
- **İlgili issue/PR:**

---

### D-20260818-001 — v2.1'i değiştirilemez stabil temel olarak koru

- **Durum:** Kabul
- **Sorun:** Sohbet/model sürümleri değiştiğinde hangi dosyanın doğru sürüm olduğunun karışma riski.
- **Karar:** `releases/v2.1/` değiştirilemez stabil referans olacak; yeni değişiklikler ayrı branch/PR ile yapılacak.
- **Gerekçe:** Geri dönüş noktası ve izlenebilirlik sağlamak.
- **Etkilenen dosyalar:** Repository çalışma düzeni.
- **Test:** v2.1 `--validate-only` temiz geçti.
