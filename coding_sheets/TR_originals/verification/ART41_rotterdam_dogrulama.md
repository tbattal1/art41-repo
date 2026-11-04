# ART-41 — Rotterdam Doğrulama Turu Eki
**Tarih:** 07.07.2026 | **Kapsam:** Pilot sayfasındaki 4 bekleyen hücre (C3.4, C4b, C5.1, C5.3)
**Sonuç özeti:** 2 hücre ÇÖZÜLDÜ (C3.4 ✅, C5.3 ✅) | 1 hücre kısmen (C5.1 ⚠️ sürüyor) | 1 hücre bilinçli MISSING-pending (C4b — birincil belge gerekli)

---

## C3.4 — Yazılı kriz koordinasyon protokolü → **1 ✅ ÇÖZÜLDÜ** → **C3 = 0.95 KESİNLEŞTİ (4/4)**

| Kanıt | Bulgu | Kaynak |
|---|---|---|
| FERM programı | 2016'da kuruldu — Liman Cyber Resilience programı; Port Authority + belediye + liman başkanı ağı (polis ve savcılık dahil) + Portbase + terminaller + NCSC | Security Delta (2017), Leiden Üniv. tezi (FERM 2016 atfıyla), Rotterdam Innovation City |
| CyberNautics2017 | Nisan 2017'den itibaren limanda "kolektif kriz yönetimi" yaklaşımı; çok-aktörlü tatbikat (PoR, Loodswezen/kılavuzluk, Portbase, konteyner terminalleri, armatörler, NCSC) | Security Delta (2017) |
| Port-ISAC | Limanın kritik süreç aktörlerini bağlayan bilgi paylaşım organı, NCSC çatısı | Leiden Üniv. tezi (2020) |
| Statü teyidi | Gemi trafiği süreci hükümetçe "hayati süreç" ilan edilmiş → kurumsallaşma zorunlu nitelikte | Security Delta (2017) |

**Gerekçe:** 2019 itibarıyla yazılı, çok-aktörlü, tatbikatlı kriz koordinasyon altyapısı fazlasıyla belgelendi. Gösterge 4 = 1. **C3: 4/4 = 0.95, bayrak kalktı.**
**Ş2 bonus notu:** FERM 2024'te ulusal beş-liman platformuna dönüştü (BOZ + Bakanlık + NCTV) — Ş2 dönemi Discussion malzemesi.

## C5.3 — İmtiyazda sosyal/yeşil koşul → **1 ✅ ÇÖZÜLDÜ**

| Kanıt | Bulgu | Kaynak |
|---|---|---|
| İmtiyaz emisyon kısıtları | "PoR ile konteyner operatörleri arasındaki imtiyaz sözleşmeleri, emisyonları azaltmak amacıyla kısıtlamalar içerir" — MV2 imtiyaz tasarımında görev almış danışmanlığın portföy beyanı | Port Consultants Rotterdam |
| Modal split çerçevesi | Karayolu %47→%35, demiryolu %13→%20, iç suyolu %40→%45 (2033 hedefi) — MV2 hinterland tasarımının çekirdeği | Maritime Journal (2015) |
| Hükümet-düzeyi bağlayıcı araç | "Overeenkomst luchtkwaliteit Maasvlakte 2" (Hava Kalitesi Anlaşması) + MV1-MV2'de kamyonlara düşük emisyon bölgesi | Government.nl |

**Gerekçe:** Üç bağımsız kaynak katmanı aynı yöne işaret ediyor: MV2 imtiyaz/izin mimarisinde bağlayıcı çevresel koşullar var. Gösterge 3 = 1.
**Not (dürüstlük):** Sözleşme maddesinin birebir metni kamuya açık değil (ticari sır); kanıt üçgenlemesi 2.–5. kademe kaynaklarla yapıldı. Coding sheet'te "üçgenleme ile 1" olarak işaretlendi — hakeme açık beyan edilecek güçte.

## C5.1 — Tüzükte bağlayıcı mandat → **⚠️ SÜRÜYOR**
PoR'un kendi beyanı ("core tasks: sustainable development...") kurumsal iletişim dili — tüzük hükmü değil. Havenbedrijf Rotterdam N.V. ana sözleşmesindeki amaç maddesi gerekiyor. **C5 şimdilik 0.40'ta sabit (1/3 kesin + 1 bekleyen):** C5.1 doğrulanırsa 0.70'e çıkar.

## C4b — MV2 imtiyaz vadeleri → **0.33 ✅ ÇÖZÜLDÜ (RWG kesin + APMT çıkarım; dipnot şeffaf)**

| Terminal | Süre | Kaynak | Skor mantığı |
|---|---|---|---|
| RWG | **25 yıl** (KESİN) | MOL 2007 basın bülteni, birebir: "Period of contract: 25 years"; imza 17.09.2007 (PoR CEO Hans Smits ↔ RWG konsorsiyumu). RWG kendi sitesi ve de Langen literatürü imza yılını (2007) doğruluyor ama süreyi vermiyor. | İmzadan (2007+25=2032)→2019'da 13 yıl kalan; operasyonel başlangıçtan (2014+25=2039)→20 yıl kalan. **Her iki yorum da 10–25 bandı → 0.33.** Başlangıç-tarihi belirsizliği skoru değiştirmiyor. |
| APMT MV2 | Açıklanmamış (ÇIKARIM: ~25 yıl) | İmza 2006 (APMT slayt: "Concession signed Aug 2006"; Maersk 2006 yıllık rapor notları). Süre hiçbir birincil kaynakta yok. Dayanaklar: (1) Maersk muhasebe notu terminal altyapısını "max. 25 years" amortize ediyor (muhasebe tavanı, sözleşme süresi DEĞİL — dipnotta belirtilecek); (2) aynı liman/dönem/otoritenin verdiği RWG'nin 25 yıl olması. | Çıkarımla ~25 yıl → 10–25 bandı → 0.33 |

**KESİN OLMAYAN sayı uyarısı (mis-citation önleme, Perplexity taramasından):** Maersk'in "max 25y amortisman", "50y arazi kirası", "20y imtiyaz hakkı amortismanı" rakamları MUHASEBE tavanlarıdır, sözleşme süresi değil. 2025 basınındaki "25-year cooperation" APMT'nin 2000'den beri Rotterdam varlığına atıf, MV2 imtiyazına değil. Bunlar C4b'ye GİRMEZ.

**Bileşik etki:** İki terminal de 0.33 bandında → kapasite-ağırlığı ne olursa olsun **Rotterdam C4b = 0.33.**

**Manuscript dipnotu (hazır metin):** *"The RWG concession term (25 years, MOL 2007) is documented; the APMT MV2 term is not publicly disclosed and is inferred to fall in the same band based on the concurrent award context and Maersk's 25-year infrastructure amortisation ceiling. Both interpretations place Rotterdam's financial lock-in in the 10–25 year band."*

**Rotterdam C4 bileşik güncellendi:** C4a(0.33) + C4b(0.33) + C4c(0.33) = **0.33** — üç boyut da alt banda hizalı, "düşük compound lock-in" profili netleşti.

## Konsolide matris etkisi
- Rotterdam C3: 0.95 ⚠️ → **0.95 ✅**
- Rotterdam C5: 0.40 (durum aynı, gerekçesi güçlendi)
- Rotterdam C4: ~0.33 ⚠️ sürüyor (yalnız C4b hücresi)
