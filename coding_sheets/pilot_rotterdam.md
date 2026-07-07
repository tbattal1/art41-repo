# ART-41 — Pilot Kodlama Sayfası: ROTTERDAM (Vaka #1)
**Kodlama tarihi:** 07.07.2026 | **Kodlama penceresi:** 2019 sonu itibarıyla (şok öncesi durum)
**Statü:** PİLOT — v2 codebook kilitlenmeden truth table'a girmez
**Bayrak lejantı:** ✅ birincil/güçlü kaynak | ⚠️ ikincil kaynak, birincil teyit gerekli | ⛔ MISSING-pending

---

## C1 — Regulatory Autonomy → **0.95** ✅ (bir nüans notuyla)

| Alt kanıt | Bulgu | Kaynak |
|---|---|---|
| Tüzel yapı | Havenbedrijf Rotterdam N.V. — 2004'te belediye dairesinden korporatize şirkete dönüşüm; borsa dışı kamu limited şirketi | ScienceDirect (van der Lugt vd.), portofrotterdam.com |
| Tarife özerkliği | Liman ücretleri (port dues) otoritenin kendi gelir kalemi; kendi belirliyor | portofrotterdam.com (About) |
| Arazi/imtiyaz özerkliği | Uzun vadeli kiralamaları üçüncü taraflara doğrudan sözleşmeleyebiliyor; ulusal mevzuatın ÜZERİNE ek çevre düzenlemesi çıkarabiliyor (ESPO kriterleri karşılanıyor) | Aussenwirtschaft NL raporu (ESPO dashboard kriterleri) |
| Hissedar kontrolü | İki kamu hissedarı: Rotterdam Belediyesi ~%70, Hollanda Devleti ~%30. Yılda 2 resmi genel kurul + çeyreklik gayriresmî toplantı; büyük kararlar genel kurul yetkisinde | Springer GeoJournal (2023), portofrotterdam.com |

**Gerekçe:** Tarife + imtiyaz + operasyonel yatırım kararları otoritede; hissedar yetkisi bakanlık vesayeti değil, korporatif genel kurul hakkı. Codebook'un 0.95 tanımını karşılıyor.
**⚠️ CODEBOOK REVİZYON NOTU #1:** Kural tablosu "bakanlık onayı"nı ölçüyor ama Rotterdam tipi vakada kontrol hiyerarşik vesayet değil, HİSSEDARLIK hakkı üzerinden işliyor. v2'ye eklenecek ayrım: "hiyerarşik devlet onayı (vesayet)" ≠ "kamu hissedarının korporatif genel kurul yetkisi". İkincisi özerkliği 0.95'ten düşürmez; birincisi düşürür. (Bu ayrım Singapur/PSA ve Busan kodlamasında da kritik olacak.)

---

## C2 — Ownership Hybridity → **0.95** ✅

| Alt kanıt | Bulgu (2019 itibarıyla) | Kaynak |
|---|---|---|
| Operatör çoğulluğu | ≥3 bağımsız grup: ECT Delta + Euromax (Hutchison Ports), APM Terminals (2 terminal, Maersk grubu), RWG (DP World %30 + CMA CGM %10 + 3 taşıyıcı %20'şer konsorsiyum) | thefreighthero.nl terminal envanteri, Terminal49 |
| Kamu operasyon payı | Otorite landlord — konteyner elleçlemede kamu operasyonu yok | portofrotterdam.com (gelir modeli: kira + liman ücreti) |

**Gerekçe:** Konteyner kapasitesinin fiilen tamamı özel/karma operatörde VE çoklu bağımsız operatör → 0.95.
**Not (analiz dışı, Discussion hammaddesi):** 2024'te yapı değişti — Hutchison ECT'yi TiL+IFM'e sattı, DP World Amaliahaven imtiyazını sonlandırdı (Kas 2024). Kodlama penceresi 2019 olduğu için skoru etkilemez; ama Ş2 outcome yorumunda "şok sırasında sahiplik türbülansı" notu düşülecek.

---

## C3 — Multi-Level Coordination Density → **0.95 provizyonel** (3✅ + 1⚠️)

| Gösterge | Bulgu | Kaynak | Bayrak |
|---|---|---|---|
| 1. Kent–liman organı | Belediye %70 hissedar + resmi genel kurul mekanizması; kent-liman koordinasyonu hissedarlık yapısına gömülü | Springer GeoJournal | ✅ |
| 2. Ulusal koordinasyon | Devlet %30 hissedar (Maliye Bakanlığı temsilcisi genel kurulda); (Devlet) Liman Başkanı kamu görevleri devlet + 4 belediye adına ifa ediliyor; ulusal mainport politikası çerçevesi | portofrotterdam.com (org yapısı), Springer | ✅ |
| 3. Uluslararası ağ (aktif) | ESPO Port Performance Dashboard kriterlerini karşılıyor; ESPO/IAPH aktif üyelik | Aussenwirtschaft raporu | ✅ |
| 4. Yazılı kriz protokolü | Liman Başkanlığı bölümünün resmi görev tanımında "incident control" var; FERM siber dayanıklılık ortaklığı [birincil teyit gerekli] | portofrotterdam.com | ⚠️ |

**Gerekçe:** 3/4 kesin + 1/4 güçlü aday → provizyonel 0.95; FERM/kriz protokolü birincil dokümanla teyit edilirse kesinleşir, edilemezse 0.70'e düşer.

---

## C4 — Compound Lock-In → **provizyonel ~0.33** (bir alt boyut ⛔)

**(a) Düzenleyici katılık → 0.33** ✅
2004 korporatizasyon reformu 15 yıllık pencerenin (2004–2019) tam sınırında; 2014 esas sözleşme güncellemesi ikincil düzenleme. Başarısız reform girişimi kaydı yok.
**⚠️ CODEBOOK REVİZYON NOTU #2:** "Son 15 yıl" penceresi sınır vakası üretti (2004 reformu 2019 kodlamasında tam sınırda). v2 kuralı: reform yılı pencere başlangıç yılına eşitse DAHİL sayılır; ayrıca pencere "15 yıl" yerine "2005–2019 sabit pencere" olarak tüm vakalara aynı takvimle uygulanır (vakalar arası karşılaştırılabilirlik).

**(b) Finansal kilit → ⛔ MISSING-pending**
MV2 imtiyazları (RWG, APMT MVII) 2008 civarı imzalandı; sektör normu ~25 yıl AMA sözleşme süreleri arama sonuçlarında doğrulanamadı. ECT'nin eski Delta arazi kiralamalarının vadesi de belirsiz. **Kural gereği tahmin YOK.** Aksiyon: PoR yıllık raporu (2019) imtiyaz/kira vade dipnotları + RWG/APMT basın arşivi birincil taraması. Kapasite-ağırlıklı ortalama oradan hesaplanacak.

**(c) Sosyal meşruiyet açığı → 0.33** ✅
2015–2019 penceresinde 1 büyük belgelenmiş ihtilaf kümesi: Ocak 2016 tam otomasyona karşı 24 saatlik grev — 13 yılın ilk grevi, ~3.000 katılımcı, ITF/ETF destekli; Temmuz 2016'da iş güvencesi anlaşmasıyla çözüldü (FNV Havens, 800 işin risk altında olduğu iddiasıyla). Tek küme = 0.33.
Kaynaklar: Equal Times (11.01.2016), Offshore Energy (12/2015, 01/2016), Vice/Motherboard, JOC (06.07.2016).
**⚠️ CODEBOOK REVİZYON NOTU #3:** "Olay sayısı" kuralı belirsizlik üretti: Aralık 2015 ültimatom + Ocak 2016 grev + müteakip tehditler TEK ihtilaf kümesi mi, üç olay mı? v2 kuralı: aynı uyuşmazlık konusuna bağlı olaylar TEK KÜME sayılır (küme tanımı: aynı taraflar + aynı talep + <12 ay aralık).

**C4 bileşik:** (0.33 + [pending] + 0.33)/3 → (b) tamamlanmadan hesaplanmaz.

---

## C5 — Social Value Integration → **provizyonel 0.40** (1✅ + 1 sınır + 1 kesin 0)

| Gösterge | Bulgu | Kaynak | Skor |
|---|---|---|---|
| 1. Tüzükte bağlayıcı çevre/topluluk mandatı | Esas sözleşme amaçları: geliştirme + güvenli/etkin gemi trafiği. Ek çevre düzenlemesi ÇIKARMA yetkisi var ama tüzükte bağlayıcı topluluk/çevre YÜKÜMLÜLÜĞÜ dili doğrulanamadı | portofrotterdam.com, Aussenwirtschaft | Sınır (0/1) ⚠️ |
| 2. Paydaş temsil organı | İki katmanlı yapı (Yönetim + Bağımsız Denetim Kurulu); topluluk/emek/çevre temsilcili daimi organ kaydı YOK (Deltalinqs sektör örgütü, governance organı değil) | Springer, portofrotterdam.com | 0 ✅ |
| 3. İmtiyazda sosyal/yeşil koşullar | MV2 imtiyazlarında çevresel koşullar (temiz ekipman, modal split yükümlülükleri) sektörde bilinen örnek — AMA birincil şartname teyidi gerekli | genel literatür bilgisi | 1 ⚠️ |

**Provizyonel:** 1/3 → 0.40. Gösterge 1 ve 3'ün birincil teyidiyle 0.40 ↔ 0.70 arasında kesinleşecek.
**Aksiyon:** PoR 2019 yıllık raporu + MV2 imtiyaz kamu özetleri + esas sözleşme (articles of association, 2014 versiyonu Springer makalesinde refere ediliyor).

---

## ÖZET SATIR (provizyonel, truth table'a GİRMEZ)
| C1 | C2 | C3 | C4 | C5 |
|----|----|----|----|----|
| 0.95 ✅ | 0.95 ✅ | 0.95 (⚠️×1) | ~0.33 (⛔×1) | 0.40 (⚠️×2) |

## PİLOTUN ÜRETTİĞİ CODEBOOK v2 MADDELERİ
1. Vesayet onayı ≠ kamu hissedar genel kurul yetkisi ayrımı (C1)
2. Sabit takvim penceresi 2005–2019 (C4a)
3. İhtilaf "küme" tanımı: aynı taraflar + aynı talep + <12 ay (C4c)
4. Yeni bayrak disiplini işledi: 3 hücre birincil teyide yönlendirildi, 1 hücre MISSING-pending — hiçbir hücre tahminle dolmadı ✅

## SONRAKİ ADIMLAR (Rotterdam kapanışı için)
- [ ] PoR Annual Report 2019 → imtiyaz vade dipnotları (C4b) + esas sözleşme mandat dili (C5.1)
- [ ] MV2 imtiyaz çevresel koşul birincil teyidi (C5.3)
- [ ] FERM/kriz protokolü birincil teyidi (C3.4)
- [ ] Outcome tarafı: PortWatch Rotterdam serisi çekilip Ş1 metrikleri pilot hesap
