# Project State

**Son güncelleme:** 2026-08-18  
**Stabil temel:** v2.1  
**Durum:** GitHub geçişi tamamlanıyor.

## Kesin olarak korunmuş durum

`releases/v2.1/` içindeki paket mevcut stabil referanstır. Paket kendi doğrulayıcısı ile temiz geçmektedir.

- Oyuncu aralığı: 6–15
- 118 kart kimliği doğrulanır.
- Harita başlangıç geometrisi ve Ufuk yasallığı doğrulanır.
- Manifest SHA-256 kontrolleri doğrulanır.
- Kural PDF'si ve kart PDF'si bütünlük kontrollerinden geçer.

## Önemli uyarı

v2.1 üretildikten sonra sohbetlerde yeni tasarım kararları konuşulmuş olabilir. Bunlar henüz bu repository'ye resmî olarak taşınmış sayılmaz.

Bu nedenle gelecekteki bir ChatGPT/model sürümü:

1. v2.1'i **stabil geri dönüş noktası** olarak kabul etmeli,
2. sohbetten veya kullanıcıdan gelen daha yeni kararları doğrudan v2.1'in üstüne yazmamalı,
3. önce yeni bir değişiklik kaydı/branch oluşturmalı,
4. çelişki varsa kullanıcı kararını kaynak kabul etmelidir.

## Sıradaki geliştirme hedefi

`develop` çalışma hattını kurmak ve v2.1 sonrası konuşulmuş kararları tek tek karşılaştırarak resmî geliştirme durumuna geçirmek.

## Değişiklik tamamlanmış sayılma ölçütü

Bir değişiklik ancak aşağıdakilerin hepsi tamamlandığında resmîdir:

- İnsan kural metni güncel.
- Makine JSON kaynağı güncel.
- İlgili kod/test güncel.
- Statik doğrulama geçiyor.
- Baskı dosyası etkileniyorsa yeniden üretilmiş ve görsel kontrolden geçmiş.
- `docs/DECISION_LOG.md` güncel.
- `docs/TEST_LOG.md` güncel.
