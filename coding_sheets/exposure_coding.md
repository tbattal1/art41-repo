# ART-41 — Coding sheet: remote conditions E_C (pandemic exposure) and E_R (Red Sea rerouting exposure)

Rules: codebook v2.8 §C (entries K17–K17d). Rules were fixed on 2026-11-03 before data retrieval (`docs/exposure_rules_v1.md`); the two amendments (K17a anchors; K17c Z definition) are logged with reasons. Computation scripts: `src/e_covid.py`, `src/fetch_comtrade.py`, `src/compute_Q.py`. Derived tables: `data/exposure/`.

## E_C — pandemic exposure (national stringency, 1 Mar–31 Dec 2020)

Source: OxCGRT `OxCGRT_compact_national_v1.csv` (downloaded 2026-11-03 from github.com/OxCGRT/covid-policy-dataset; SHA-256 fa5c95fa…0fe79, full hash in `data/exposure/OxCGRT_SNAPSHOT.txt`), `StringencyIndex_Average`, `Jurisdiction = NAT_TOTAL`. Anchors: world distribution of 2020 national means, 185 countries with ≥250 daily observations — P90 75.67, P50 60.49, P10 41.48 (K17a).

| Port | Country | Mean 2020 | E_C | Note |
|---|---|---|---|---|
| Rotterdam | NLD | 59.90 | 0.48 | near crossover |
| Hamburg | DEU | 60.86 | 0.52 | near crossover |
| Antwerp-Bruges | BEL | 60.49 | 0.50 | 0.4998 — knife-edge; treated as below crossover, sensitivity run with 0.501 |
| Gdańsk | POL | 56.99 | 0.37 | |
| Valencia | ESP | 66.22 | 0.76 | |
| Piraeus | GRC | 64.99 | 0.71 | |
| Tanger Med | MAR | 73.15 | 0.92 | |
| Mersin | TUR | 63.65 | 0.65 | |
| Singapore | SGP | 57.80 | 0.40 | |
| Shanghai | CHN | 72.18 | 0.91 | national series; sub-national robustness available |
| Busan | KOR | 55.65 | 0.32 | |
| Port Klang | MYS | 64.35 | 0.68 | |
| Colombo | LKA | 55.81 | 0.32 | |
| Jebel Ali | ARE | 59.84 | 0.47 | near crossover |
| Los Angeles | USA | 67.63 | 0.80 | national series |
| New York–New Jersey | USA | 67.63 | 0.80 | national series |
| Vancouver | CAN | 66.38 | 0.76 | |
| Santos | BRA | 68.20 | 0.82 | |
| Cartagena | COL | 74.42 | 0.94 | |
| Durban | ZAF | 64.83 | 0.70 | |
| Lagos | NGA | 64.66 | 0.70 | |
| Melbourne | AUS | 64.87 | 0.70 | national series; Victoria sub-national robustness available |

Partner-weighted stringency (2019 trade weights, UN Comtrade; `E_C_partner_weighted.csv`): range 61.4–68.0 across the 22 countries — flat; not used (documented in §3.6).

## E_R — Red Sea rerouting exposure (2023Q4)

### D — lane dependence (binary; rule K17 §3.1)

| D = 1 | Basis |
|---|---|
| Rotterdam, Hamburg, Antwerp-Bruges, Gdańsk | Northern European ends of the Asia–North Europe lane (UNCTAD RMT 2024, Ch. II, pp. 33–34: Asia–Europe rerouting; Suez carries 22 % of world container trade) |
| Valencia, Piraeus, Tanger Med, Mersin | Mediterranean / Eastern Mediterranean calls of Asia–Mediterranean and Asia–North Europe lanes; Drewry 1Q24 capacity data confirm Suez-dependence for East/Central Med hubs |
| Shanghai, Busan, Singapore, Port Klang | Asian origin/hub ends of the Asia–Europe lane |
| Colombo | South Asian hub on Asia–Europe and Europe–Indian-subcontinent lanes |
| Jebel Ali | Europe–Gulf lane transits Suez and the Red Sea |
| New York–New Jersey | Suez-routed services from South and South-East Asia to the US East Coast |

| D = 0 | Basis |
|---|---|
| Los Angeles, Vancouver | Pacific lanes |
| Santos, Cartagena | Asia services via Pacific/Panama; Europe services across the Atlantic |
| Durban, Lagos | Asia and Europe services via the Indian Ocean / Cape and West Africa; no Suez transit |
| Melbourne | Asia–Australia direct |

*Documented uncertainty:* service-level corroboration (a named 2023Q4 Suez-transit service per D = 1 port from carrier/alliance schedules) is listed as the corroboration step in the rules; the region-level rule was applied here and the service-level check is **pending** — to be completed before resubmission or the limitation stated.

### Q — partner-region trade quotient (country level, 2023; rule K17 §3.2 + K17b)

Source: UN Comtrade public preview API, reporter imports and exports 2023, HS TOTAL minus HS 25, 26, 27; 154 queries archived in `data/exposure/comtrade_raw/` with SHA-256 and URL in each file's `_meta`. Region mapping: UN M49 via `country_converter`; Comtrade partner 490 "Other Asia, nes" (S19) treated as Eastern Asia (Taiwan); other "nes" aggregates negligible (< 0.05 bn USD).

| Reporter | Far-side trade (bn USD) | Other inter-regional (bn USD) | Q | Q ≥ 0.40 |
|---|---|---|---|---|
| NLD | 195.1 | 123.1 | 0.613 | high |
| DEU | 595.5 | 396.6 | 0.600 | high |
| BEL | 80.9 | 84.1 | 0.490 | high (near threshold) |
| POL | 107.1 | 46.8 | 0.696 | high |
| ESP | 114.9 | 87.7 | 0.567 | high |
| GRC | 14.1 | 8.6 | 0.621 | high |
| MAR | 17.5 | 12.8 | 0.578 | high |
| TUR | 144.8 | 63.3 | 0.696 | high |
| SGP | 104.5 | 165.4 | 0.387 | low (near threshold) |
| CHN | 1063.3 | 1949.7 | 0.353 | low |
| KOR | 169.6 | 302.2 | 0.360 | low |
| MYS | 56.2 | 112.5 | 0.333 | low |
| LKA | 6.6 | 12.6 | 0.342 | low |
| ARE | 113.1 | 474.1 | 0.193 | low |
| USA (New York district) | — | — | pending (US Census customs-district data; API key required) | results identical at 0.40 and 0.70 |

Sensitivity: at a 0.30 threshold SGP, CHN, KOR, MYS, LKA become "high"; at 0.50 BEL becomes "low". IQR among D = 1 reporters > 0.10 → Q retained (fallback not triggered).

### Z — Eastern/Central Mediterranean, Black Sea, Red Sea adjacency (K17c)

Z = 1: Piraeus, Mersin. Z = 0: all others, including Valencia and Tanger Med (Western Mediterranean / Gibraltar — remained on the Cape-diverted routing; Drewry data via Hellenic Shipping News, March 2024: Piraeus weekly vessel capacity −31 %, Gioia Tauro −18 % in 1Q24; Valencia and Barcelona +11 %, Algeciras −1.4 % in January 2024).

### E_R membership

| E_R | Ports |
|---|---|
| 0.95 | Piraeus, Mersin |
| 0.70 | Rotterdam, Hamburg, Antwerp-Bruges, Gdańsk, Valencia, Tanger Med |
| 0.40 | Shanghai, Busan, Singapore, Port Klang, Colombo, Jebel Ali, New York–New Jersey (provisional) |
| 0.05 | Los Angeles, Vancouver, Santos, Cartagena, Durban, Lagos, Melbourne |

## Change record
- 2026-11-03: rules fixed (K17); data retrieved; K17a (anchors), K17b (partner sets, Taiwan), K17c (Z) applied before any outcome comparison; table locked. Pending: NY–NJ Q; service-level corroboration of D.
