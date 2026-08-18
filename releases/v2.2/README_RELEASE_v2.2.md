# OYUN v2.2 - Stabil Prototip Release

Bu klasör v2.2'nin kilitli kaynak ve baskı paketidir.

## Kaynak önceliği
1. `OYUN_TAM_KURALLAR_v2.2.md`
2. `OYUN_Kural_Kitabi_v2.2.pdf`
3. `OYUN_SIMULASYON_SPEC_v2.2.json`
4. `oyun_simulasyon_v2_2.py`

## Fiziksel çıktı
- `OYUN_Kartlar_A4_Prototip_v2.2.pdf`
- `OYUN_Gecilmez_Kayalik_Isaretleri_v2.2.pdf`

## Doğrulama
`python oyun_simulasyon_v2_2.py --validate-only --geometry-audit`

Ayrıntılı release kontrolü: `V22_RELEASE_VALIDATION.md`.

Bu klasör yerinde değiştirilmez. Sonraki tasarım değişiklikleri v2.3+ geliştirme hattında yapılır.

## Binary artifact storage
Baskı PDF'lerinin ve tam ZIP paketinin kalıcı Library konumları `BINARY_ARTIFACTS.md` dosyasında kayıtlıdır. `V22_RELEASE_MANIFEST.json` içindeki SHA-256 değerleri kanonik doğrulama değerleridir.
