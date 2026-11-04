---
title: "ART-41 R1 — Exposure Conditions: Pre-registered Coding Rules (draft v1, for approval before any data are pulled)"
---

**Hocam için özet (TR).** Bu belge, hesaplama yapılmadan *önce* sabitlenecek kuralları içeriyor. Onayından sonra tek bir harfi değiştirmeden veriyi çekeceğim; değişiklik gerekirse codebook değişiklik günlüğüne gerekçeli yazılacak. Karar noktaları **[KARAR]** ile işaretli; geri kalanı önerilen metin. Semboller: E_C (COVID maruziyeti), E_R (Kızıldeniz maruziyeti), D (hat bağımlılığı), Q (partner-bölge ticaret oranı), Z (Akdeniz/Kızıldeniz bitişikliği). A/B (kalibrasyon), C1–C5, N, P90/P50/P10, S1–S3 (ek dosyalar) ile çakışmadığı kontrol edildi.

---

# 1. Purpose and status within the design

Two *remote* conditions are added to the design in response to Reviewer 3: exposure to the COVID-19 demand shock (E_C) and exposure to the Red Sea rerouting shock (E_R). They are **not governance conditions** and are not added to the five-condition governance model. Following Schneider and Wagemann's (2006) two-step procedure, they enter a separate first step that identifies the exposure *contexts* in which fragility occurs; the governance conditions C1–C5 are then minimised within those contexts (step two). The published five-condition results of the submitted version are unchanged by this addition; the two-step analysis is reported as a new Section 4.6 and informs the Discussion.

Both remote conditions are measured from sources that are (i) external to the port and its governance, (ii) public and free, (iii) available for all 22 cases, and (iv) fixed before the shock's outcome is examined. Rules, thresholds and fallbacks are fixed in this document before any data are retrieved (codebook change log entry K17).

# 2. E_C — Exposure to the COVID-19 demand shock

**Concept.** The intensity of domestic non-pharmaceutical restrictions in the port's country during the year of the demand collapse. Domestic restrictions suppress import demand, hinterland activity and port labour availability simultaneously; they are the component of pandemic exposure that is external to port governance and comparably measured worldwide.

**Source.** Oxford COVID-19 Government Response Tracker (OxCGRT), *StringencyIndex_Average*, national level, daily (Hale et al., 2021; DOI 10.1038/s41562-021-01079-8). Data file: the OxCGRT final national-level CSV (version and download date recorded in the coding sheet; SHA-256 stored with the data snapshot).

**Measure.** E_C(raw) = arithmetic mean of the daily national StringencyIndex_Average from **1 March 2020 to 31 December 2020** (inclusive). Rationale for the window: the COVID outcome window is 2020Q1–2021Q4, but the demand collapse that the resilience-loss score measures formed in 2020; 2021 stringency reflects vaccination and variant dynamics that overlap with recovery and would blur exposure with response. **[KARAR 1: window = 2020 only (proposed) vs full 2020–2021 outcome window.]**

**Calibration.** Direct method with scale-anchored thresholds on the 0–100 index: full membership (0.95) at ≥ 70; crossover (0.50) at 55; full non-membership (0.05) at ≤ 40. Anchors are set on the index's own scale rather than on sample percentiles, in line with Reviewer 3's preference and to avoid the outlier sensitivity flagged for the outcome calibration. If, after computation, more than 80 % of cases fall on one side of the crossover, the skew is reported (Section 4.6) and the condition is retained; anchors are **not** moved post hoc. **[KARAR 2: anchors 70/55/40 — alternatives 75/60/45 or 65/50/35.]**

**Sub-national robustness (pre-committed).** OxCGRT publishes sub-national indices for Australia, Brazil, Canada, China and the United States. As a robustness check only, E_C is recomputed for Melbourne (Victoria), Santos (São Paulo), Vancouver (British Columbia), Shanghai (Shanghai) and Los Angeles / New York–New Jersey (California / New York) using the sub-national series, and the two-step analysis is re-run. The national series remains primary for comparability across the 22 cases.

**Known limitation to be stated.** National stringency does not capture trading-partner lockdowns (the external-demand component). This is accepted because partner-weighted stringency would require port-level trade-partner shares that are not publicly available for all 22 ports.

# 3. E_R — Exposure to the Red Sea rerouting shock

**Concept.** The degree to which a port's deep-sea container connectivity depended, immediately before the crisis (2023Q4), on services transiting the Suez Canal / Bab el-Mandeb, and the degree to which the port stood to lose calls rather than merely suffer delays when those services were diverted around the Cape of Good Hope.

Three indicators, each coded from public sources with the rule below, are combined into an ordinal four-level membership.

## 3.1 Indicator D — lane dependence (binary)

D = 1 if at least one of the port's *principal* deep-sea container lanes in 2023Q4 transited Suez/Bab el-Mandeb: Asia–North Europe, Asia–Mediterranean (incl. Black Sea and Türkiye), Asia–US East Coast via Suez (services from South and South-East Asia), Europe–Gulf/Indian subcontinent, Europe–East Africa via the Red Sea. D = 0 otherwise.

*Operational rule by port region* (applied mechanically; exceptions must be documented against a service schedule):

| D = 1 | D = 0 |
|---|---|
| Mediterranean, Black Sea, Türkiye (Valencia, Piraeus, Tanger Med, Mersin) | Pacific North America (Los Angeles, Vancouver) |
| Northern Europe (Rotterdam, Hamburg, Antwerp-Bruges, Gdańsk) | South America (Santos, Cartagena — Asia services via Pacific/Panama; Europe services across the Atlantic) |
| East and South-East Asia as the origin end of Asia–Europe lanes (Shanghai, Busan, Singapore, Port Klang) | Sub-Saharan Africa outside the Red Sea (Durban, Lagos — Asia and Europe services route via the Indian Ocean / Cape and West Africa, not Suez) |
| South Asia hub (Colombo) | Australia (Melbourne — Asia–Australia direct; Europe–Australia marginal) |
| Gulf hub with Europe–Gulf lane (Jebel Ali) | |
| US East Coast with Suez-routed services from South/South-East Asia (New York–New Jersey) | |

*Source.* UNCTAD *Review of Maritime Transport 2024*, Red Sea crisis section (list of affected trade lanes) **[to be verified at retrieval — if RMT 2024 does not list lanes explicitly, the public 2023Q4 alliance network maps (2M, Ocean Alliance, THE Alliance) are used and cited instead]**, corroborated for each D = 1 port by at least one named 2023Q4 service that called at the port and transited Suez.

## 3.2 Indicator Q — partner-region trade quotient (continuous, country level)

Q = (value of the port country's 2023 merchandise trade with partner countries on the *far side of Suez* relative to the port) ÷ (value of the port country's 2023 merchandise trade with all partners *outside its own macro-region*).

- "Merchandise trade" = imports + exports, HS chapters 01–24 and 28–99 (i.e., excluding HS 25–27: mineral products, ores and fuels, which move predominantly in bulk and tanker tonnage). This is the containerisable-trade proxy.
- "Far side of Suez": for European, Mediterranean, Black Sea and North African countries → partners in East Asia, South-East Asia, South Asia, the Gulf (GCC), East Africa (Red Sea–Indian Ocean littoral) and Oceania. For East/South-East/South Asian and Gulf countries → partners in Europe (EU-27, UK, Norway, Switzerland, Western Balkans), Türkiye, the Mediterranean and Black Sea littoral and North Africa. Partner groups are defined by UN M49 regions and listed exhaustively in the coding sheet.
- "Own macro-region" (excluded from the denominator because that trade is predominantly land-borne or short-sea and does not use the Suez mainlines): UN M49 region of the port country (e.g., *Europe* for the Netherlands; *Eastern Asia* + *South-Eastern Asia* for China, Korea, Singapore, Malaysia; *Southern Asia* for Sri Lanka; *Western Asia* for the UAE).
- United States: Q is computed from US Census Bureau foreign-trade statistics by customs district (New York district), since the two US cases differ in lane exposure. Los Angeles has D = 0 and needs no Q.
- Q is computed only for D = 1 ports (15 cases). Source: UN Comtrade (or WITS front end), reference year 2023, reporter = port country; download date, query parameters and file checksum recorded.

Threshold: Q is "high" if Q ≥ 0.40 — i.e., at least two-fifths of the country's inter-regional containerisable trade crosses Suez. **[KARAR 3: 0.40 proposed; it is a conventional cut and is declared as such; sensitivity at 0.30 and 0.50 is pre-committed.]**

## 3.3 Indicator Z — Mediterranean / Red Sea adjacency (binary)

Z = 1 if the port lies in the Mediterranean, Black Sea or Red Sea. Rationale: these ports are intermediate calls on the Asia–Europe mainline *reachable only through Suez*; when services were diverted via the Cape they were bypassed (direct Asia–North Europe routing with Mediterranean cargo relayed or omitted), so their exposure mechanism is loss of calls rather than delay. Z = 0 for all other ports, including the Gulf (reached from Asia without Bab el-Mandeb). *Source.* UNCTAD RMT 2024 and the documented 2024 Mediterranean call omissions **[specific public source to be fixed at retrieval; candidates: UNCTAD RMT 2024, Drewry/Alphaliner public commentary, port authority 2024 annual reports]**.

## 3.4 Combination rule and membership scores

| Profile | E_R |
|---|---|
| D = 0 | 0.05 |
| D = 1, Q low, Z = 0 | 0.40 |
| D = 1, and exactly one of {Q high, Z = 1} | 0.70 |
| D = 1, Q high, Z = 1 | 0.95 |

No case can sit at the 0.50 crossover by construction. Expected (not yet computed) placement: Mersin, Valencia, Piraeus, Tanger Med ≥ 0.70; Northern European and East Asian ports 0.40 or 0.70 depending on Q; Durban, Lagos, Santos, Cartagena, Los Angeles, Vancouver, Melbourne = 0.05. **These expectations are written down now so that the computed values can be checked against them, not adjusted toward them.**

**Pre-committed fallback.** If Q shows little discriminating power among D = 1 ports (inter-quartile range < 0.10), Q is dropped, E_R reduces to the three-level {D, Z} scheme (0.05 / 0.40 / 0.95), and this is reported.

# 4. Two-step analysis plan (Section 4.6, new)

*Step 1 — remote conditions.* For each shock, truth table and minimisation of the outcome "fragility" (¬Y) on the remote condition(s) alone: E_C for COVID; E_R for the Red Sea. With one remote condition per shock, step 1 reduces to a necessity/sufficiency test of exposure for fragility: is high exposure sufficient for fragility? necessary? (Consistency, PRI, coverage reported; benchmark 0.80 / 0.75 as in the main analysis.)

*Step 2 — proximate conditions within context.* The governance minimisation (C1–C5) is re-run separately within the high-exposure and low-exposure contexts for each shock (cases with E ≥ 0.70 vs E ≤ 0.40; no case at 0.50). Because each sub-analysis has ≤ 5 conditions, the Marx and Duşa (2011) specification benchmark is respected in every minimisation. Reported: whether the published fragility paths (¬C1·C2·¬C3·¬C4 for COVID; ¬C1·¬C2·¬C3·C4·C5 for the Red Sea) hold within the context in which their cases sit, and whether Mersin's switch across shocks is reproduced by its E_C / E_R placement.

*Expected interpretive gains (hypotheses, stated before computation).* (H-a) Mersin: low E_C, high E_R — the exposure-contingency reading of Section 5.3 becomes a measured claim. (H-b) Durban: E_R = 0.05 yet the most fragile Red Sea case — fragility in a low-exposure context cannot be attributed to exposure, which strengthens the governance (C4) reading. (H-c) Port Klang: high E_C, consistent with the MCO-driven collapse. If any hypothesis fails, the text reports the failure and revises the interpretation, not the measure.

*Limitations to be written.* Country-level measurement weakens E_R for transhipment hubs whose traffic is loosely tied to national trade (Piraeus, Colombo, Tanger Med, Singapore, Port Klang); Q therefore understates their exposure. This is stated in Section 5.7 and the D/Z indicators carry the hub cases.

# 5. Codebook and repository entries

- Codebook v2.7: new section "Remote conditions E_C, E_R" containing Sections 2–3 above verbatim; change-log entry K17 (dated, "added in response to R3; rules fixed before data retrieval").
- Coding sheet `exposure_coding.md`: per-port rows for D (service named), Q (numerator, denominator, source query), Z, E_R; and E_C (raw mean, window, file version).
- Data snapshots: OxCGRT CSV and Comtrade extracts with SHA-256; R script section `# 7. TWO-STEP (R3)`.

# 6. References (verified against Crossref)

Hale, T., Angrist, N., Goldszmidt, R., Kira, B., Petherick, A., Phillips, T., Webster, S., Cameron-Blake, E., Hallas, L., Majumdar, S., & Tatlow, H. (2021). A global panel database of pandemic policies (Oxford COVID-19 Government Response Tracker). *Nature Human Behaviour, 5*(4), 529–538. https://doi.org/10.1038/s41562-021-01079-8

Marx, A., & Duşa, A. (2011). Crisp-set Qualitative Comparative Analysis (csQCA), contradictions and consistency benchmarks for model specification. *Methodological Innovations Online, 6*(2), 103–148. https://doi.org/10.4256/mio.2010.0037

Schneider, C. Q., & Wagemann, C. (2006). Reducing complexity in Qualitative Comparative Analysis (QCA): Remote and proximate factors and the consolidation of democracy. *European Journal of Political Research, 45*(5), 751–786. https://doi.org/10.1111/j.1475-6765.2006.00635.x

UNCTAD (2024). *Review of Maritime Transport 2024*. Geneva: United Nations. **[exact chapter/page to be fixed at retrieval]**
