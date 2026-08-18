# Açık Deniz Sosyal Çıkarım Oyunu

Bu repository oyunun kalıcı kaynak kaydıdır. Amaç, ChatGPT oturumlarına veya model sürümlerine bağımlı olmadan kuralları, makine verisini, testleri ve sürüm geçmişini tek yerde tutmaktır.

## Kanonik durum

- Son kilitli/stabil paket: **v2.1**
- Stabil kaynak: `releases/v2.1/`
- v2.1 klasörü **değiştirilemez arşiv** kabul edilir.
- Yeni tasarım değişiklikleri önce ayrı bir branch/PR üzerinde yapılır.
- v2.1'den sonra yalnız sohbet içinde konuşulmuş fakat dosyalara işlenmemiş kararlar olabilir; bu nedenle yeni çalışmaya başlamadan önce `PROJECT_STATE.md` okunmalıdır.

## Her yeni ChatGPT oturumunda

1. `AI_HANDOFF.md` okunur.
2. `PROJECT_STATE.md` okunur.
3. Son commit, PR ve issue durumu kontrol edilir.
4. Stabil v2.1 geri dönüş noktası olarak korunur.
5. Yeni değişiklikler doğrudan v2.1'in üstüne yazılmaz.

## Çalışma düzeni

1. Sorun veya tasarım amacı tanımlanır.
2. Ayrı branch/PR açılır.
3. İnsan kuralı, makine JSON'u, kod ve ilgili testler birlikte güncellenir.
4. Kararın gerekçesi `docs/DECISION_LOG.md` dosyasına işlenir.
5. Test sonucu `docs/TEST_LOG.md` dosyasına işlenir.
6. Onaylanan değişiklik ana hatta alınır.

## Kaynak hiyerarşisi

v2.1 paketinin kendi tanımına göre:

1. Ayrıntılı insan kuralları: `OYUN_TAM_KURALLAR_v2.1.md`
2. Masa kural kitabı: `OYUN_Kural_Kitabi_v2.1.pdf`
3. Makine kaynağı: `OYUN_SIMULASYON_SPEC_v2.1.json`

Uyuşmazlık bulunursa sessizce varsayım yapılmaz; issue açılır ve kullanıcı kararı beklenir.

## Not: baskı çıktıları

PDF baskı çıktılarının doğrulanmış v2.1 kopyaları ayrıca kalıcı proje yedeğinde tutulur. Repository içindeki kaynak dosyaları oyunun sürekliliği için birincil çalışma malzemesidir; baskı artefaktlarının SHA-256 kayıtları `releases/v2.1/ARTIFACTS.md` içinde tutulur.
