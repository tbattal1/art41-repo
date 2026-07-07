# ART-41 — PİLOT KONSOLİDE PAKET (Notion'a kopyalanacak)
**Tarih:** 07.07.2026 | **Faz:** Pilot TAMAMLANDI (4/4) → Codebook v2 KİLİT → Ağustos tam kodlamaya HAZIR
**Hedef:** RTBM VSI "Port Governance – Reloaded" | Deadline 01.12.2026 | Submit hedefi ≤25.11.2026

## Durum özeti (tek paragraf)
Dört pilot vaka (Rotterdam, Mersin, Durban, Melbourne) konfigürasyon uzayının dört ayrı köşesini doğruladı; codebook 13 revizyon notuyla stres testinden geçti, 10 HOCAM kararı işlendi ve v2 olarak kilitlendi. Tasarım hatası düzeltmesi: Melbourne kirası 50 yıl (99 değil). Bilinen tek açık tasarım kalemi: Ş2 "uyum performansı" outcome tanımı (Ağustos'un ilk işi). Bekleyen işler kural değiştirmeyen hücre teyitleri.

## Pilot matrisi (kararlar işlenmiş)
| Vaka | C1 | C2 | C3 | C4 | C5 | Profil |
|------|----|----|----|----|----|--------|
| Rotterdam | 0.95 | 0.95 | 0.95✅ | 0.33✅ | 0.40✅ | Özerk-koordineli landlord |
| Mersin | 0.05 | 0.70 | 0.05✅ | 0.33 | 0.05 | Otoritesiz tam-imtiyaz |
| Durban | 0.05 | 0.30 | 0.30✅ | 0.89 | 0.95✅ | Kilitli devlet-operatör |
| Melbourne | 0.70 | 0.95 | 0.30✅ | 0.44✅ | 0.40✅ | Finansallaşmış özel landlord |

## Pilotun ürettiği analitik sermaye (Discussion'a taşınacak)
1. **Üçlü kontrol tipolojisi (C1):** vesayet / kamu hissedar hakkı / bağımsız regülatör tavanı — "özerklik kimden bağımsızlık?" (Rotterdam–Melbourne–Mersin karşıtlığı)
2. **İki dallı finansal kilit (C4b):** imtiyaz vadesi (Dal-A) vs KİT mali kısıtı (Dal-B) — kilitlenmenin iki ekonomi-politiği (Melbourne vs Durban)
3. **Yasalaşmış-ama-uygulanmamış reform = en ağır katılık** (Durban, 2005 Kanunu, 16 yıl)
4. **De jure C5 × de facto C4c ayrışması:** kâğıt üstü sosyal entegrasyon ≠ saha meşruiyeti (Durban profili)
5. **Aynı bileşik, farklı kompozisyon:** Mersin C4=0.33 ≈ Rotterdam ~0.33 ama içerik tamamen farklı → bileşik + dekompozisyon birlikte raporlanır

## Karar günlüğü
K1:E | K2:E | K3:C4c=0 | K4:doküman turu→çözüldü | K5:zımnen onaylı | K6:E | K7:E | K8:0.30 | K9:E | K10:E | **K11:E** (evrensel yasal planlar C3.4'ü karşılamaz — Codebook v2.1)

## Açık doğrulama kuyruğu (Ağustos başı, kural değiştirmez)
- Rotterdam: C3.4 ✅, C5.3 ✅, C4b ✅ (RWG 25y kesin + APMT çıkarım, 0.33) çözüldü — kalan yalnız C5.1 (Havenbedrijf ana sözleşme amaç maddesi; C5=0.40→0.70 olabilir, düşük öncelik)
- Mersin: C3.3 ✅ ve C3.4 ✅ çözüldü (bkz. ART41_mersin_dogrulama.md; K11 onaylandı) — kalan: C5 sözleşme koşulları (Eurobond izahnamesi yolu)
- Durban: TAMAMLANDI ✅ — PCC, B-BBEE, PMAESA (09.04.2019 tarihli aktiflik) çözüldü; IAPH negatifi tarihli (üyelik 06.2023)
- Melbourne: TAMAMLANDI ✅ — SEMP birincil belgesiyle 5 hücre çözüldü, C4a aleyhte düzeltildi (bkz. ART41_melbourne_dogrulama.md)
- Ş1 outcome: KİLİT ✅ — Y = YoY aynı-hafta oranı (Rotterdam'da 4 tanım test edildi; yalnız YoY gerçek COVID dibini buldu). Ş2 referansı=2022, script v5, Codebook Bölüm B güncellendi. Snapshot disiplini devrede (SHA damgalı). Açık: fsQCA Y'si konteyner mi toplam mı (Ağustos, 2. vaka teyidi).

## Sonraki adımlar (sıralı)
1. **PortWatch Rotterdam Ş1 pilot outcome hesabı** — outcome protokolünün ilk gerçek-veri testi
2. Doğrulama kuyruğu (yukarıda)
3. Ağustos: kalan 18 vaka kodlaması (Codebook v2 ile, mekanik)
4. Eylül: kalibrasyon + fsQCA + robustness (C.1–C.5)

## Dosya haritası
- ART41_design_v2.md (tasarım, güncel)
- ART41_codebook_v2.md (KİLİT kural kitabı)
- ART41_pilot_{rotterdam,mersin,durban,melbourne}.md (kanıt sayfaları)
- ART41_karar_formu.md (arşiv)
