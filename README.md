# Açık Deniz Sosyal Çıkarım Oyunu

Bu repository oyunun kalıcı ve denetlenebilir kaynak kaydıdır. Amaç, ChatGPT oturumları veya model sürümleri değişse bile kuralları, testleri ve sürüm geçmişini kaybetmemektir.

## Kanonik durum

- Son kilitli/stabil prototip: **v2.2**
- Kanonik release: `releases/v2.2/`
- Önceki stabil geri dönüş: `releases/v2.1/`
- `releases/v2.1/` ve `releases/v2.2/` yerinde değiştirilmez.
- Yeni tasarım değişiklikleri v2.3+ çalışma hattında ayrı branch/PR ile yapılır.

## Her yeni ChatGPT oturumunda

1. `AI_HANDOFF.md` okunur.
2. `PROJECT_STATE.md` okunur.
3. `releases/v2.2/README_RELEASE_v2.2.md` ve `releases/v2.2/V22_RELEASE_VALIDATION.md` okunur.
4. `python releases/v2.2/oyun_simulasyon_v2_2.py --validate-only --geometry-audit` çalıştırılır.
5. Son commit/PR/issue durumu kontrol edilir.
6. Yeni değişiklikler doğrudan `releases/v2.2/` üzerine yazılmaz.

## v2.2 kaynak hiyerarşisi

1. `releases/v2.2/OYUN_TAM_KURALLAR_v2.2.md`
2. `releases/v2.2/OYUN_Kural_Kitabi_v2.2.pdf`
3. `releases/v2.2/OYUN_SIMULASYON_SPEC_v2.2.json`
4. `releases/v2.2/oyun_simulasyon_v2_2.py`

Uyuşmazlık bulunursa sessiz varsayım yapılmaz; karar kaydı açılır ve kullanıcı kararı kaynak kabul edilir.
