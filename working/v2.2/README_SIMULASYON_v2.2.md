# OYUN v2.2 - Geliştirme Kaynağı

Bu klasör v2.2'nin gerçek çalışma kaynaklarını içerir. `releases/v2.1/` stabil geri dönüş temelidir ve değiştirilmez.

## Kaynak önceliği

1. `OYUN_TAM_KURALLAR_v2.2.md` - ayrıntılı insan kuralı
2. `OYUN_SIMULASYON_SPEC_v2.2.json` - makine okunur kural/spec
3. `oyun_simulasyon_v2_2.py` - statik/geometri doğrulayıcı
4. `OYUN_DEGISIKLIK_KAYDI_v2.2.md` - v2.1 -> v2.2 farkları

## Doğrulama

```bash
python oyun_simulasyon_v2_2.py --validate-only
```

Araç tam sosyal denge simülatörü değildir. Kart adedi/metin karması, dinamik başlangıç, Liman erişimi, 1/2 Geçilmez Kayalık, Ufuk yasallığı, Kaptan omurgası ve acil geri dönüş sözleşmesini doğrular.

## Stabil sayılma koşulu

v2.2 şu anda **development** statüsündedir. İnsan kuralı + JSON + doğrulayıcı temiz geçtikten sonra kural kitabı/PDF bileşenleri üretilip görsel kontrol edilir ve son regresyon tamamlanır. Ondan sonra `releases/v2.2/` altında kilitlenir.
