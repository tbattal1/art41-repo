# ART-41 — Vaka Kodlama: CARTAGENA (#19)
**Tarih:** 08.07.2026 | **Codebook:** v2.6 (K1–K16) | ✅ KİLİTLİ — 5/5 kaynaklı, sıfır MISSING
**Desen:** Kolombiya landlord modeli — devlet grantor + özel sociedades portuarias (konsesyoner-operatör).

## YAPISAL ÖZET
- **Model:** Ley 1ª/1991 (Estatuto de Puertos Marítimos) → landlord; konsesyoner yalnız işletme hakkı alır, mülkiyet Devlette. Superintendencia (bugün Supertransporte) + ANI grantor-regülatör.
- **Operatör:** SPRC (Sociedad Portuaria Regional de Cartagena, konsesyon 007/1993, 20→40 yıla uzatıldı → 2033) + Contecar (003/2008) = **Grupo Puerto de Cartagena** (özel, konteyner dominant). Bayda ayrıca Compas/Central Cartagena (dökme/genel, küçük).

## C1 = **0.30**
Özne = devlet grantor (Superintendencia/ANI). SPRC/Contecar konsesyoner-operatör (serbestisi C2'ye). Grantor ulusal hükümet yapısı: konsesyon modifikasyonları/uzatmaları hükümet-onaylı (dava kaydı: Ministerio de Transporte, Consejo Asesor, büyük genişleme Decreto gerektirir) → tüzel yapı ama kararlar ulusal sistem içinde → 0.30. **Kaynak:** Consejo de Estado davası (Superintendencia yetkisi, hükümet onayı); revistas.upr (Ley 1ª/1991 landlord).

## C2 = **0.70** (vaka-vaka kalibrasyon, HOCAM onaylı)
Konteyner >%80 özel AMA tek dominant grup (SPRC+Contecar = Grupo Puerto de Cartagena; ayrı konsesyon, aynı ekonomik grup). Bayda diğer societies konteyner-dışı. → ">%80 özel, tek dominant operatör" → 0.70 (Mersin emsali). **Kaynak:** puertocartagena.com (Grupo); D&B (SPRC private).

## C3 = **0.30** (1/4)
C3.3=1 (Karayip hub, Caribbean Shipping Association "Best Port" 10×, global hatlar); C3.1/3.2=0 (ulusal sistem dikey; ayrı kent-liman organı yok); C3.4=0. **Kaynak:** puertocartagena.com (Caribbean rankings).

## C4 = **0.22**
- C4a=0.33: Contecar konsesyonu (003/2008) = pencere-içi yapısal genişleme/reform.
- C4b=0.33 [Dal-A, KAYNAKLI]: Kalan konsesyon süresi (2019): SPRC→2033 (~14yr), Contecar/Muelle Nueve→2030 (~11yr) → ağırlıklı ~12-14yr → 10-25 bandı.
- C4c=0: 2015-2019 operasyonel-etkili ihtilaf yok (verimli/istikrarlı, ödüllü liman).
- mean(0.33, 0.33, 0) = **0.22**. **Kaynak:** Supertransporte ficha (2033/2030); colombiacompra (konsesyonlar).

## C5 = **0.05** (0/3)
C5.1=0 (SPRC özel şirket, kuruluşta bağlayıcı çevre mandatı yok); C5.2=0; C5.3=0 (Kolombiya 2019'da ECA dışı; bağlayıcı shore-power/emisyon mandatı yok; konsesyon çevre-uyumu baseline, ayırt-edici sosyal-yeşil değil). **Kaynak:** IMO ECA kapsamı; Ley 1ª/1991.

## OUTCOME (Y) — BEKLEYEN (YoY, Bölüm B).
## DEĞİŞİKLİK: 08.07.2026 C2=0.70 (vaka-vaka kalibrasyon, HOCAM); C4b kaynaklı. Kilit.
