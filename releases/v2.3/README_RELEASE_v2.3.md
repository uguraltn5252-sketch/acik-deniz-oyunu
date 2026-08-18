# OYUN v2.3 — Stabil Prototip Release

**Kilit tarihi:** 18 Ağustos 2026  
**Durum:** **STABLE / LOCKED**

## Kanonik kaynak sırası

1. `OYUN_TAM_KURALLAR_v2.3.md`
2. `OYUN_Kural_Kitabi_v2.3.pdf` (Library binary; SHA-256 BINARY_ARTIFACTS.md içinde)
3. `OYUN_SIMULASYON_SPEC_v2.3.json`
4. `oyun_simulasyon_v2_3.py` ve test kanıtları

## v2.3 omurgası

- Kaptan kalıcıdır; ilk rotayı tek başına ve olay bilgisi olmadan seçer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferinde yeni Kaptan seçilir.
- Bütün Haritalarda başlangıç Gövdesi 2'dir.
- Toplam Harita 52, Kayalık 12, toplam kart kimliği 118'dir.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalıktır; kapalıyken normal Kayalıktan ayırt edilemez.
- Küçük Haritalar 1, büyük Haritalar 2 Geçilmez içerir; bunlar mevcut Kayalık kotasının içindedir.
- Geçilmez açıldığında Gemi kareye girmez, mevcut konumunda kalır ve normal rota günüyse hareket harcanır; kart açık kalıcı engel olur.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmezlerin tam ileri çıkmazında uygulanır.

## Doğrulama

- 7.200 kart çifti karşılaştırması
- 6.000 temsilî davranış oyunu
- 9.000 tam 6–15 oyuncu/süre duyarlılığı
- 51.204 geometri taraması / 51.102 yasal / 102 kurulum reddi
- kabul edilen kurulumlarda kalıcı rota kilidi: 0
- validator: PASS
- kural PDF: 32 sayfa / kart PDF: 32 sayfa / preflight ve görsel tarama: PASS

İnsan masa testi oyunun sosyal deneyimini iyileştirmek için hâlâ önerilir; ancak bu release kilidinin ön koşulu değildir. Sonraki tasarım değişiklikleri **v2.4+** olarak açılmalıdır.
