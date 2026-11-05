---
title: "Supplementary Material S1 — Analysis details, robustness and outcome measurement"
subtitle: "No Best Model, Only Best Matches: Governance Configurations, Two Shocks, and the Asymmetry of Port Resilience"
---

All tables are generated from the replication package (codebook v2.9; `data/conditions_and_raw_outcomes_v4.csv`; scripts `src/ART41_R1_analysis.R`, `src/export_S1.R`, `src/july_variants.py`, `src/build_S1.py`). Notation: \~X denotes the absence of condition X and · denotes logical AND. Thresholds throughout: raw consistency ≥ 0.80, PRI ≥ 0.70, frequency ≥ 1; twelve condition cells at exactly 0.50 recoded to 0.501. Software: R 4.3.3, QCA 3.25, admisc 0.41; Python 3 (pandas).

# S1.1 Raw outcome metrics

Container vessel calls, year-over-year ratio to the same ISO week of the reference year (2019; 2022), four-week rolling mean. Windows: 1 Jan–30 Sep 2020 and 19 Nov 2023–18 Nov 2024 (codebook K22). Trough = Monday of the ISO week.

| Port | COVID depth % | COVID half-life (wk) | COVID trough | Red Sea depth % | Red Sea half-life (wk) | Red Sea trough | Pre-window ratio (Red Sea) |
|---|---|---|---|---|---|---|---|
| Rotterdam | 14.4 | 6 | 2020-06-08 | 14.4 | 3 | 2024-01-22 | 0.96 |
| Hamburg | 17.8 | 16 | 2020-04-06 | 19.4 | 3 | 2024-01-22 | 1.00 |
| Antwerp | 6.1 | 2 | 2020-02-24 | 12.5 | 3 | 2023-12-18 | 1.01 |
| Gdańsk | 29.5 | 3 | 2020-09-07 | 17.2 | 2 | 2024-01-08 | 0.93 |
| Valencia | 10.2 | 1 | 2020-04-06 | 0.2 | 1 | 2024-11-11 | 1.08 |
| Piraeus | 13.1 | 2 | 2020-09-14 | 15.7 | 2 | 2024-05-20 | 1.10 |
| Tanger Med | no decline | 0 | — | 2.2 | 1 | 2024-07-22 | 1.07 |
| Mersin | 2.0 | 2 | 2020-02-10 | 5.4 ᵃ | 1 | 2023-11-20 | 0.72 |
| Singapore | 11.2 | 10 | 2020-06-01 | 7.1 | 2 | 2024-06-24 | 1.07 |
| Shanghai | 9.6 | 3 | 2020-02-10 | 3.6 | 1 | 2024-11-11 | 1.06 |
| Busan | 11.7 | 2 | 2020-06-29 | 2.8 | 4 | 2024-11-18 | 1.13 |
| Port Klang | 62.7 | 4 | 2020-05-04 | 3.0 | 4 | 2024-11-18 | 1.10 |
| Colombo | 23.5 | 4 | 2020-06-08 | 0.0 ᵃ | 0 | 2023-11-20 | 0.68 |
| Jebel Ali | no decline | 0 | — | 5.3 | 2 | 2024-04-29 | 1.02 |
| Los Angeles | 13.8 | 2 | 2020-03-09 | 26.6 | 2 | 2024-03-18 | 0.97 |
| New York/NJ | 16.8 | 1 | 2020-06-22 | 13.7 | 1 | 2024-10-21 | 1.06 |
| Vancouver | 26.8 | 1 | 2020-03-09 | 50.3 | 2 | 2024-01-15 | 0.99 |
| Santos | 15.9 | 6 | 2020-09-28 | 3.5 | 1 | 2024-08-19 | 1.03 |
| Cartagena | 12.4 | 13 | 2020-08-03 | no decline | 0 | — | 1.23 |
| Durban | 14.7 | 1 | 2020-08-03 | 16.1 | 2 | 2024-01-08 | 2.74 |
| Lagos (Apapa) | 38.9 | 2 | 2020-06-15 | 32.4 | 1 | 2024-08-19 | 0.99 |
| Melbourne | 18.6 | 5 | 2020-03-30 | 15.1 | 1 | 2024-05-06 | 1.04 |

*ᵃ Pre-shock level rule (K24) applied; uncorrected values: Mersin 32.0 % / 6 wk; Colombo 4.4 % / 1 wk. Negative depths (no decline) enter the loss score as zero. Durban's pre-window ratio (2.74) reflects the October 2022 Transnet strike in the reference-year denominator; the rule does not apply because its trough falls in window week 7.*

**Calibration anchors.** Resilience-loss score = max(0, depth) × half-life; resilience calibrated by the direct method with descending anchors.

| Outcome | P90 (full non-membership) | P50 (crossover) | P10 (full membership) |
|---|---|---|---|
| Loss, COVID-19 | 156.28 | 28.20 | 4.62 |
| Loss, Red Sea | 52.20 | 13.95 | 0.40 |


**Calibrated memberships (after tie-break).**

| Port | C1 | C2 | C3 | C4 | C5 | Ycov | Yred | Ycov_B | Yred_B | E_C | E_R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Rotterdam | 0.950 | 0.950 | 0.950 | 0.330 | 0.400 | 0.208 | 0.095 | 0.269 | 0.073 | 0.477 | 0.700 |
| Hamburg | 0.700 | 0.950 | 0.700 | 0.220 | 0.700 | 0.003 | 0.032 | 0.013 | 0.036 | 0.518 | 0.700 |
| Antwerp | 0.700 | 0.950 | 0.700 | 0.330 | 0.700 | 0.881 | 0.140 | 0.904 | 0.094 | 0.499 | 0.700 |
| Gdańsk | 0.501 | 0.700 | 0.501 | 0.110 | 0.400 | 0.200 | 0.172 | 0.262 | 0.296 | 0.365 | 0.700 |
| Valencia | 0.300 | 0.950 | 0.700 | 0.220 | 0.950 | 0.904 | 0.952 | 0.915 | 0.951 | 0.756 | 0.700 |
| Piraeus | 0.700 | 0.300 | 0.300 | 0.440 | 0.400 | 0.562 | 0.207 | 0.720 | 0.345 | 0.709 | 0.950 |
| Tanger Med | 0.501 | 0.950 | 0.700 | 0.330 | 0.400 | 0.971 | 0.928 | 1.000 | 0.939 | 0.924 | 0.700 |
| Mersin | 0.050 | 0.700 | 0.050 | 0.330 | 0.050 | 0.954 | 0.865 | 0.953 | 0.914 | 0.651 | 0.950 |
| Singapore | 0.501 | 0.300 | 0.501 | 0.330 | 0.400 | 0.127 | 0.495 | 0.115 | 0.624 | 0.395 | 0.400 |
| Shanghai | 0.300 | 0.300 | 0.501 | 0.110 | 0.400 | 0.497 | 0.905 | 0.668 | 0.929 | 0.910 | 0.400 |
| Busan | 0.501 | 0.950 | 0.700 | 0.220 | 0.400 | 0.646 | 0.645 | 0.770 | 0.051 | 0.318 | 0.400 |
| Port Klang | 0.501 | 0.950 | 0.300 | 0.560 | 0.050 | 0.006 | 0.604 | 0.030 | 0.050 | 0.682 | 0.400 |
| Colombo | 0.300 | 0.700 | 0.300 | 0.220 | 0.050 | 0.181 | 0.954 | 0.276 | 0.990 | 0.323 | 0.400 |
| Jebel Ali | 0.950 | 0.300 | 0.300 | 0.000 | 0.050 | 0.971 | 0.674 | 0.999 | 0.672 | 0.474 | 0.400 |
| Los Angeles | 0.700 | 0.950 | 0.501 | 0.670 | 0.700 | 0.519 | 0.046 | 0.694 | 0.094 | 0.804 | 0.050 |
| New York/NJ | 0.700 | 0.950 | 0.501 | 0.440 | 0.400 | 0.806 | 0.514 | 0.761 | 0.799 | 0.804 | 0.400 |
| Vancouver | 0.700 | 0.950 | 0.501 | 0.330 | 0.700 | 0.544 | 0.001 | 0.440 | 0.003 | 0.762 | 0.050 |
| Santos | 0.300 | 0.950 | 0.501 | 0.330 | 0.400 | 0.176 | 0.906 | 0.251 | 0.930 | 0.821 | 0.050 |
| Cartagena | 0.300 | 0.700 | 0.300 | 0.220 | 0.050 | 0.045 | 0.954 | 0.045 | 0.995 | 0.940 | 0.050 |
| Durban | 0.050 | 0.300 | 0.300 | 0.890 | 0.950 | 0.844 | 0.197 | 0.824 | 0.331 | 0.702 | 0.050 |
| Lagos (Apapa) | 0.300 | 0.950 | 0.300 | 0.220 | 0.050 | 0.242 | 0.195 | 0.209 | 0.262 | 0.695 | 0.050 |
| Melbourne | 0.700 | 0.950 | 0.300 | 0.440 | 0.400 | 0.184 | 0.478 | 0.277 | 0.772 | 0.704 | 0.050 |


# S1.2 Truth tables

Observed rows only (twelve of thirty-two logically possible configurations; diversity ratio 0.375). OUT = 1 marks rows meeting both thresholds.


**Table S1.2-1. Outcome: resilience, COVID-19 window.**

| Row | C1 | C2 | C3 | C4 | C5 | OUT | n | Cons. | PRI | Cases |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0.873 | 0.655 | Durban |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0.686 | 0.047 | Shanghai |
| 9 | 0 | 1 | 0 | 0 | 0 | 0 | 4 | 0.575 | 0.269 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| 13 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0.685 | 0.324 | Santos |
| 14 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0.806 | 0.557 | Valencia |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0.747 | 0.466 | Piraeus, Jebel Ali |
| 21 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0.692 | 0.240 | Singapore |
| 25 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0.666 | 0.326 | Melbourne |
| 27 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.704 | 0.322 | Port Klang |
| 29 | 1 | 1 | 1 | 0 | 0 | 0 | 5 | 0.694 | 0.393 | Rotterdam, Gdańsk, Tanger Med, Busan, New York/NJ |
| 30 | 1 | 1 | 1 | 0 | 1 | 0 | 3 | 0.756 | 0.483 | Hamburg, Antwerp, Vancouver |
| 32 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0.826 | 0.519 | Los Angeles |


**Table S1.2-2. Outcome: resilience, Red Sea window.**

| Row | C1 | C2 | C3 | C4 | C5 | OUT | n | Cons. | PRI | Cases |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0.717 | 0.036 | Durban |
| 5 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0.902 | 0.756 | Shanghai |
| 9 | 0 | 1 | 0 | 0 | 0 | 0 | 4 | 0.753 | 0.589 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| 13 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0.755 | 0.529 | Santos |
| 14 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0.762 | 0.543 | Valencia |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0.843 | 0.647 | Piraeus, Jebel Ali |
| 21 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0.903 | 0.706 | Singapore |
| 25 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0.752 | 0.432 | Melbourne |
| 27 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.796 | 0.470 | Port Klang |
| 29 | 1 | 1 | 1 | 0 | 0 | 0 | 5 | 0.711 | 0.429 | Rotterdam, Gdańsk, Tanger Med, Busan, New York/NJ |
| 30 | 1 | 1 | 1 | 0 | 1 | 0 | 3 | 0.590 | 0.286 | Hamburg, Antwerp, Vancouver |
| 32 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0.676 | 0.307 | Los Angeles |


**Table S1.2-3. Outcome: fragility, COVID-19 window.**

| Row | C1 | C2 | C3 | C4 | C5 | OUT | n | Cons. | PRI | Cases |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0.758 | 0.345 | Durban |
| 5 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0.985 | 0.953 | Shanghai |
| 9 | 0 | 1 | 0 | 0 | 0 | 1 | 4 | 0.844 | 0.731 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| 13 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0.849 | 0.676 | Santos |
| 14 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0.756 | 0.443 | Valencia |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0.779 | 0.534 | Piraeus, Jebel Ali |
| 21 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0.903 | 0.760 | Singapore |
| 25 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0.839 | 0.674 | Melbourne |
| 27 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.860 | 0.678 | Port Klang |
| 29 | 1 | 1 | 1 | 0 | 0 | 0 | 5 | 0.801 | 0.607 | Rotterdam, Gdańsk, Tanger Med, Busan, New York/NJ |
| 30 | 1 | 1 | 1 | 0 | 1 | 0 | 3 | 0.772 | 0.517 | Hamburg, Antwerp, Vancouver |
| 32 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0.812 | 0.481 | Los Angeles |


**Table S1.2-4. Outcome: fragility, Red Sea window.**

| Row | C1 | C2 | C3 | C4 | C5 | OUT | n | Cons. | PRI | Cases |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0.990 | 0.964 | Durban |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0.695 | 0.244 | Shanghai |
| 9 | 0 | 1 | 0 | 0 | 0 | 0 | 4 | 0.646 | 0.411 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| 13 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0.725 | 0.471 | Santos |
| 14 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0.717 | 0.457 | Valencia |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0.706 | 0.338 | Piraeus, Jebel Ali |
| 21 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0.766 | 0.294 | Singapore |
| 25 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0.806 | 0.555 | Melbourne |
| 27 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.819 | 0.530 | Port Klang |
| 29 | 1 | 1 | 1 | 0 | 0 | 0 | 5 | 0.783 | 0.571 | Rotterdam, Gdańsk, Tanger Med, Busan, New York/NJ |
| 30 | 1 | 1 | 1 | 0 | 1 | 1 | 3 | 0.836 | 0.714 | Hamburg, Antwerp, Vancouver |
| 32 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0.857 | 0.693 | Los Angeles |


# S1.3 Solutions: conservative, parsimonious and intermediate

Intermediate solutions use the directional expectations of Table 4.x (resilience: C1, C2, C3, C5 present, C4 absent; fragility: the complements, codebook K19). Labels C1P*/M* identify alternative models where minimisation is ambiguous.


**Resilience, covid-19 window.**

| Solution | Model | Term | Cons. | PRI | Raw cov. | Cases (membership > 0.5) |
|---|---|---|---|---|---|---|
| conservative | - | none explained |  |  |  |  |
| parsimonious | - | none explained |  |  |  |  |
| intermediate | - | none explained |  |  |  |  |


**Resilience, red sea window.**

| Solution | Model | Term | Cons. | PRI | Raw cov. | Cases (membership > 0.5) |
|---|---|---|---|---|---|---|
| conservative | M1 | \~C2·C3·\~C4·\~C5 | 0.909 | 0.755 | 0.270 | Singapore, Shanghai |
| parsimonious | M1 | \~C2·C3 | 0.886 | 0.696 | 0.283 | Singapore, Shanghai |
| intermediate | C1P1 M1 | \~C2·C3·\~C4 | 0.910 | 0.755 | 0.275 | Singapore, Shanghai |


**Fragility, covid-19 window.**

| Solution | Model | Term | Cons. | PRI | Raw cov. | Cases (membership > 0.5) |
|---|---|---|---|---|---|---|
| conservative | M1 | \~C2·C3·\~C4·\~C5 | 0.909 | 0.761 | 0.256 | Singapore, Shanghai |
| conservative | M1 | \~C1·C2·\~C3·\~C4·\~C5 | 0.844 | 0.731 | 0.564 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| parsimonious | M1 | \~C2·C3 | 0.874 | 0.682 | 0.266 | Singapore, Shanghai |
| parsimonious | M1 | \~C1·C2·\~C3 | 0.809 | 0.678 | 0.582 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| parsimonious | M2 | \~C2·C3 | 0.874 | 0.682 | 0.266 | Singapore, Shanghai |
| parsimonious | M2 | \~C1·\~C3·\~C4 | 0.833 | 0.712 | 0.608 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| parsimonious | M3 | \~C2·C3 | 0.874 | 0.682 | 0.266 | Singapore, Shanghai |
| parsimonious | M3 | \~C1·\~C3·\~C5 | 0.824 | 0.705 | 0.604 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| intermediate | C1P1 M1 | \~C2·C3·\~C5 | 0.909 | 0.761 | 0.256 | Singapore, Shanghai |
| intermediate | C1P1 M1 | \~C1·C2·\~C3·\~C5 | 0.842 | 0.730 | 0.569 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| intermediate | C1P2 M1 | \~C2·C3·\~C5 | 0.909 | 0.761 | 0.256 | Singapore, Shanghai |
| intermediate | C1P2 M1 | \~C1·\~C3·\~C4·\~C5 | 0.852 | 0.743 | 0.599 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| intermediate | C1P3 M1 | \~C1·\~C3·\~C5 | 0.824 | 0.705 | 0.604 | Mersin, Colombo, Cartagena, Lagos (Apapa) |
| intermediate | C1P3 M1 | \~C2·C3·\~C5 | 0.909 | 0.761 | 0.256 | Singapore, Shanghai |


**Fragility, red sea window.**

| Solution | Model | Term | Cons. | PRI | Raw cov. | Cases (membership > 0.5) |
|---|---|---|---|---|---|---|
| conservative | M1 | C1·C2·C3·\~C4·C5 | 0.836 | 0.714 | 0.481 | Hamburg, Antwerp, Vancouver |
| conservative | M1 | \~C1·\~C2·\~C3·C4·C5 | 0.990 | 0.964 | 0.211 | Durban |
| parsimonious | M1 | \~C1·C4 | 0.768 | 0.535 | 0.424 | Durban |
| parsimonious | M1 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| parsimonious | M2 | \~C2·C4 | 0.828 | 0.604 | 0.231 | Durban |
| parsimonious | M2 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| parsimonious | M3 | \~C2·C5 | 0.897 | 0.740 | 0.248 | Durban |
| parsimonious | M3 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| parsimonious | M4 | \~C3·C5 | 0.827 | 0.677 | 0.475 | Durban |
| parsimonious | M4 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| parsimonious | M5 | \~C1·\~C2·\~C3 | 0.723 | 0.425 | 0.255 | Durban |
| parsimonious | M5 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| intermediate | C1P1 M1 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| intermediate | C1P1 M1 | \~C1·\~C2·\~C3·C4 | 0.820 | 0.557 | 0.218 | Durban |
| intermediate | C1P2 M1 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| intermediate | C1P2 M1 | \~C1·\~C2·\~C3·C4 | 0.820 | 0.557 | 0.218 | Durban |
| intermediate | C1P3 M1 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| intermediate | C1P3 M1 | \~C1·\~C2·\~C3·C4·C5 | 0.990 | 0.964 | 0.211 | Durban |
| intermediate | C1P4 M1 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| intermediate | C1P4 M1 | \~C1·\~C2·\~C3·C4·C5 | 0.990 | 0.964 | 0.211 | Durban |
| intermediate | C1P5 M1 | C1·\~C4·C5 | 0.847 | 0.734 | 0.523 | Hamburg, Antwerp, Vancouver |
| intermediate | C1P5 M1 | \~C1·\~C2·\~C3·C4 | 0.820 | 0.557 | 0.218 | Durban |


# S1.4 Necessity

**Single conditions.** No condition reaches 0.90; inclusion ≥ 0.80 with low RoN reflects skewed memberships (C2 > 0.5 in 77 % of cases, \~C4 in 86 %).

| Condition | resilience, COVID-19 window (inclN / RoN) | resilience, Red Sea window (inclN / RoN) | fragility, COVID-19 window (inclN / RoN) | fragility, Red Sea window (inclN / RoN) |
|---|---|---|---|---|
| C1 | 0.673 / 0.722 | 0.561 / 0.681 | 0.649 / 0.744 | 0.751 / 0.788 |
| C2 | 0.814 / 0.397 | 0.831 / 0.415 | 0.872 / 0.448 | 0.871 / 0.432 |
| C3 | 0.675 / 0.776 | 0.609 / 0.757 | 0.629 / 0.786 | 0.670 / 0.794 |
| C4 | 0.513 / 0.885 | 0.436 / 0.854 | 0.451 / 0.876 | 0.527 / 0.909 |
| C5 | 0.636 / 0.847 | 0.451 / 0.762 | 0.491 / 0.796 | 0.630 / 0.864 |
| \~C1 | 0.645 / 0.735 | 0.734 / 0.803 | 0.639 / 0.766 | 0.542 / 0.700 |
| \~C2 | 0.370 / 0.918 | 0.358 / 0.921 | 0.295 / 0.895 | 0.317 / 0.900 |
| \~C3 | 0.699 / 0.709 | 0.726 / 0.741 | 0.710 / 0.754 | 0.662 / 0.709 |
| \~C4 | 0.800 / 0.535 | 0.865 / 0.582 | 0.834 / 0.589 | 0.772 / 0.541 |
| \~C5 | 0.681 / 0.605 | 0.814 / 0.688 | 0.797 / 0.703 | 0.632 / 0.599 |


**Disjunctions with inclN ≥ 0.85 and coverage ≥ 0.50 (superSubset).**

| Outcome | Expression | inclN | RoN | covN |
|---|---|---|---|---|
| resilience, COVID-19 window | \~C1  +  C2 | 0.908 | 0.308 | 0.524 |
| resilience, COVID-19 window | C1  +  C2 | 0.901 | 0.326 | 0.527 |
| resilience, COVID-19 window | \~C1  +  \~C4 | 0.897 | 0.482 | 0.590 |
| resilience, COVID-19 window | C2  +  \~C3 | 0.958 | 0.293 | 0.542 |
| resilience, COVID-19 window | \~C2  +  \~C4 | 0.857 | 0.501 | 0.580 |
| resilience, COVID-19 window | C2  +  \~C4 | 0.922 | 0.249 | 0.510 |
| resilience, COVID-19 window | C2  +  C4 | 0.879 | 0.359 | 0.529 |
| resilience, COVID-19 window | C2  +  \~C5 | 0.944 | 0.252 | 0.521 |
| resilience, COVID-19 window | C2  +  C5 | 0.885 | 0.345 | 0.526 |
| resilience, COVID-19 window | \~C3  +  \~C4 | 0.900 | 0.454 | 0.578 |
| resilience, COVID-19 window | C3  +  \~C5 | 0.858 | 0.487 | 0.574 |
| resilience, COVID-19 window | \~C4  +  C5 | 0.903 | 0.466 | 0.585 |
| resilience, COVID-19 window | \~C1  +  \~C2  +  C3 | 0.876 | 0.565 | 0.622 |
| resilience, COVID-19 window | \~C1  +  \~C2  +  C5 | 0.859 | 0.581 | 0.622 |
| resilience, COVID-19 window | C1  +  \~C2  +  \~C5 | 0.859 | 0.434 | 0.550 |
| resilience, COVID-19 window | C1  +  \~C3  +  C4 | 0.854 | 0.556 | 0.606 |
| resilience, COVID-19 window | C1  +  C3  +  \~C4 | 0.856 | 0.451 | 0.556 |
| resilience, COVID-19 window | C1  +  C3  +  C4 | 0.866 | 0.650 | 0.667 |
| resilience, COVID-19 window | \~C1  +  \~C3  +  \~C5 | 0.857 | 0.511 | 0.585 |
| resilience, COVID-19 window | \~C1  +  \~C3  +  C5 | 0.868 | 0.554 | 0.612 |
| resilience, COVID-19 window | C1  +  \~C3  +  \~C5 | 0.859 | 0.450 | 0.557 |
| resilience, COVID-19 window | C1  +  \~C3  +  C5 | 0.912 | 0.526 | 0.618 |
| resilience, COVID-19 window | C1  +  C3  +  C5 | 0.858 | 0.649 | 0.663 |
| resilience, COVID-19 window | C1  +  \~C4  +  \~C5 | 0.862 | 0.374 | 0.526 |
| resilience, COVID-19 window | C1  +  C4  +  \~C5 | 0.873 | 0.440 | 0.559 |
| resilience, COVID-19 window | C1  +  \~C2  +  C4  +  C5 | 0.852 | 0.628 | 0.647 |
| resilience, COVID-19 window | \~C1  +  C3  +  C4  +  C5 | 0.852 | 0.555 | 0.605 |
| resilience, Red Sea window | \~C4 | 0.865 | 0.582 | 0.645 |
| resilience, Red Sea window | \~C1  +  C2 | 0.901 | 0.318 | 0.544 |
| resilience, Red Sea window | C1  +  C2 | 0.883 | 0.333 | 0.541 |
| resilience, Red Sea window | \~C1  +  \~C5 | 0.905 | 0.600 | 0.672 |
| resilience, Red Sea window | C2  +  \~C3 | 0.916 | 0.293 | 0.543 |
| resilience, Red Sea window | C2  +  C3 | 0.867 | 0.396 | 0.558 |
| resilience, Red Sea window | C2  +  \~C5 | 0.971 | 0.269 | 0.562 |
| resilience, Red Sea window | \~C3  +  \~C5 | 0.850 | 0.591 | 0.643 |
| resilience, Red Sea window | C3  +  \~C5 | 0.900 | 0.523 | 0.630 |
| resilience, Red Sea window | C1  +  \~C2  +  \~C5 | 0.859 | 0.449 | 0.576 |
| resilience, Red Sea window | \~C1  +  \~C3  +  C5 | 0.862 | 0.570 | 0.637 |
| resilience, Red Sea window | C1  +  C4  +  \~C5 | 0.850 | 0.446 | 0.570 |
| resilience, Red Sea window | \~C2  +  C4  +  \~C5 | 0.852 | 0.573 | 0.633 |
| resilience, Red Sea window | \~C1  +  \~C2  +  C3  +  C4 | 0.864 | 0.549 | 0.626 |
| resilience, Red Sea window | \~C1  +  \~C2  +  C3  +  C5 | 0.877 | 0.525 | 0.620 |
| resilience, Red Sea window | \~C1  +  C3  +  C4  +  C5 | 0.852 | 0.573 | 0.634 |
| fragility, COVID-19 window | C2 | 0.872 | 0.448 | 0.604 |
| fragility, COVID-19 window | C1  +  \~C4 | 0.875 | 0.512 | 0.634 |
| fragility, COVID-19 window | C1  +  \~C5 | 0.890 | 0.554 | 0.662 |
| fragility, COVID-19 window | \~C3  +  \~C4 | 0.885 | 0.484 | 0.627 |
| fragility, COVID-19 window | C3  +  \~C4 | 0.861 | 0.546 | 0.645 |
| fragility, COVID-19 window | C3  +  \~C5 | 0.891 | 0.541 | 0.656 |
| fragility, COVID-19 window | \~C4  +  \~C5 | 0.899 | 0.505 | 0.643 |
| fragility, COVID-19 window | \~C4  +  C5 | 0.851 | 0.480 | 0.607 |
| fragility, COVID-19 window | \~C1  +  \~C3  +  \~C5 | 0.857 | 0.549 | 0.644 |
| fragility, COVID-19 window | \~C2  +  \~C3  +  \~C5 | 0.857 | 0.602 | 0.672 |
| fragility, Red Sea window | C2 | 0.871 | 0.432 | 0.577 |
| fragility, Red Sea window | C1  +  \~C3 | 0.854 | 0.592 | 0.648 |
| fragility, Red Sea window | \~C3  +  \~C4 | 0.854 | 0.454 | 0.578 |
| fragility, Red Sea window | \~C4  +  C5 | 0.874 | 0.474 | 0.597 |
| fragility, Red Sea window | C1  +  \~C2  +  \~C4 | 0.898 | 0.454 | 0.600 |
| fragility, Red Sea window | C1  +  \~C2  +  \~C5 | 0.873 | 0.457 | 0.589 |
| fragility, Red Sea window | \~C1  +  C3  +  \~C4 | 0.874 | 0.451 | 0.588 |
| fragility, Red Sea window | C1  +  C3  +  \~C4 | 0.862 | 0.471 | 0.590 |
| fragility, Red Sea window | C1  +  C4  +  \~C5 | 0.882 | 0.462 | 0.596 |
| fragility, Red Sea window | \~C2  +  C3  +  \~C4 | 0.878 | 0.489 | 0.606 |
| fragility, Red Sea window | C3  +  C4  +  \~C5 | 0.852 | 0.444 | 0.573 |
| fragility, Red Sea window | \~C1  +  \~C2  +  C3  +  C5 | 0.853 | 0.516 | 0.607 |


# S1.5 Robustness (full table)

Each cell: consistency / PRI / raw coverage of the term, recomputed with the outcome recalibrated under the perturbation; solution = conservative minimisation.

| Perturbation | Pandemic 4-case path | Pandemic Shanghai–Singapore term | Pandemic solution | Red Sea Durban path | Red Sea Hamburg–Antwerp–Vancouver term | Red Sea solution |
|---|---|---|---|---|---|---|
| baseline | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.990 / 0.964 / 0.211 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| Durban C4 = 0.78 | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.990 / 0.964 / 0.211 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| Durban C4 = 0.67 | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.989 / 0.963 / 0.208 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| Cartagena C1 = 0.50 | 0.840 / 0.719 / 0.547 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.990 / 0.964 / 0.211 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| Cartagena C1 = 0.70 | 0.835 / 0.705 / 0.529 | 0.909 / 0.761 / 0.256 | C2·\~C3·\~C4·\~C5  +  \~C2·C3·\~C4·\~C5 | 0.990 / 0.964 / 0.211 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| tie-break 0.499 | 0.844 / 0.732 / 0.564 | 0.909 / 0.760 / 0.256 | \~C1·\~C3·\~C4·\~C5 | 0.990 / 0.964 / 0.211 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| outcome anchors P85/P50/P15 | 0.820 / 0.737 / 0.532 | 0.887 / 0.776 / 0.243 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.953 / 0.886 / 0.199 | 0.810 / 0.707 / 0.458 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| outcome anchors P75/P50/P25 | 0.792 / 0.719 / 0.517 | 0.860 / 0.751 / 0.237 | \~C2·C3·\~C4·\~C5 | 0.917 / 0.852 / 0.189 | 0.791 / 0.702 / 0.440 | \~C1·\~C2·\~C3·C4·C5 |
| calibration B (additive) | 0.828 / 0.691 / 0.602 | 0.834 / 0.584 / 0.256 | \~C1·\~C2·C3·\~C4·\~C5 | 0.933 / 0.717 / 0.202 | 0.779 / 0.662 / 0.456 | \~C1·\~C2·\~C3·C4·C5 |
| A1 without K24 (Mersin 32.0/6, Colombo 4.4/1) | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.964 / 0.881 / 0.200 | 0.810 / 0.674 / 0.453 | \~C1·\~C2·\~C3·C4·C5 |
| J0: de facto submitted windows, no K24 (= submitted Table 4.1) | 0.832 / 0.717 / 0.560 | 0.792 / 0.582 / 0.225 | C1·C2·\~C3·C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.980 / 0.930 / 0.215 | 0.748 / 0.609 / 0.444 | \~C1·\~C2·\~C3·C4·C5 |
| J0: de facto submitted windows, K24 | 0.739 / 0.536 / 0.602 | 0.751 / 0.353 / 0.258 | none explained | 0.982 / 0.942 / 0.222 | 0.758 / 0.631 / 0.464 | \~C1·\~C2·\~C3·C4·C5 |
| A2: A1 + ISO-week 51-53/1 masked | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.990 / 0.964 / 0.210 | 0.836 / 0.716 / 0.480 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |
| A4: Red Sea start 1 Dec 2023 | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.989 / 0.961 / 0.213 | 0.818 / 0.692 / 0.477 | \~C1·\~C2·\~C3·C4·C5 |
| A3: Red Sea start 15 Dec 2023 | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.915 / 0.791 / 0.222 | 0.771 / 0.524 / 0.506 | \~C1·\~C2·\~C3·C4·C5 |
| A5: Red Sea window 6 months (to 18 May 2024) | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.881 / 0.686 / 0.206 | 0.745 / 0.615 / 0.471 | none explained |
| F1: full windows (to 31 Dec 2021 / 1 Oct 2023-30 Jun 2025) | 0.659 / 0.451 / 0.505 | 0.786 / 0.565 / 0.254 | \~C1·\~C2·\~C3·C4·C5 | 0.735 / 0.164 / 0.181 | 0.746 / 0.452 / 0.496 | none explained |
| F2: F1 + holiday mask | 0.722 / 0.505 / 0.530 | 0.807 / 0.599 / 0.250 | \~C1·\~C2·C3·\~C4·\~C5  +  \~C1·\~C2·\~C3·C4·C5 | 0.735 / 0.217 / 0.177 | 0.754 / 0.496 / 0.490 | none explained |
| F3: F1 with Red Sea start 19 Nov 2023 | 0.659 / 0.451 / 0.505 | 0.786 / 0.565 / 0.254 | \~C1·\~C2·\~C3·C4·C5 | 0.900 / 0.680 / 0.192 | 0.869 / 0.765 / 0.500 | C1·C2·C3·C5 |
| V1: A1 + K24 on the Nov 2026 PortWatch re-pull | 0.844 / 0.731 / 0.564 | 0.909 / 0.761 / 0.256 | \~C2·C3·\~C4·\~C5  +  \~C1·C2·\~C3·\~C4·\~C5 | 0.990 / 0.964 / 0.211 | 0.836 / 0.714 / 0.481 | C1·C2·C3·\~C4·C5  +  \~C1·\~C2·\~C3·C4·C5 |


**Leave-one-out (outcome recalibrated on 21 cases).**

| Case removed | Pandemic 4-case path | Pandemic Shanghai–Singapore | Red Sea Durban path | Red Sea Hamburg–Antwerp–Vancouver |
|---|---|---|---|---|
| Rotterdam | 0.847 / 0.733 / 0.600 | 0.910 / 0.761 / 0.270 | 0.994 / 0.978 / 0.224 | 0.829 / 0.692 / 0.485 |
| Hamburg | 0.842 / 0.752 / 0.550 | 0.910 / 0.807 / 0.257 | 0.994 / 0.982 / 0.217 | 0.820 / 0.683 / 0.440 |
| Antwerp | 0.863 / 0.760 / 0.566 | 0.910 / 0.759 / 0.258 | 0.994 / 0.978 / 0.223 | 0.821 / 0.670 / 0.456 |
| Gdańsk | 0.837 / 0.714 / 0.559 | 0.902 / 0.741 / 0.247 | 0.993 / 0.978 / 0.217 | 0.829 / 0.699 / 0.481 |
| Valencia | 0.845 / 0.730 / 0.571 | 0.910 / 0.759 / 0.258 | 0.965 / 0.888 / 0.208 | 0.846 / 0.735 / 0.479 |
| Piraeus | 0.839 / 0.730 / 0.566 | 0.903 / 0.759 / 0.242 | 0.993 / 0.975 / 0.198 | 0.832 / 0.711 / 0.489 |
| Tanger Med | 0.852 / 0.746 / 0.574 | 0.900 / 0.738 / 0.262 | 0.993 / 0.975 / 0.210 | 0.880 / 0.783 / 0.481 |
| Mersin | 0.896 / 0.814 / 0.574 | 0.897 / 0.733 / 0.261 | 0.993 / 0.975 / 0.211 | 0.835 / 0.712 / 0.486 |
| Singapore | 0.842 / 0.723 / 0.581 | 0.895 / 0.657 / 0.230 | 0.993 / 0.978 / 0.190 | 0.832 / 0.718 / 0.476 |
| Shanghai | 0.842 / 0.733 / 0.562 | 0.895 / 0.760 / 0.222 | 0.998 / 0.994 / 0.206 | 0.862 / 0.755 / 0.480 |
| Busan | 0.839 / 0.730 / 0.562 | 0.910 / 0.759 / 0.263 | 0.993 / 0.975 / 0.215 | 0.834 / 0.723 / 0.468 |
| Port Klang | 0.838 / 0.744 / 0.538 | 0.910 / 0.807 / 0.257 | 0.993 / 0.975 / 0.216 | 0.835 / 0.712 / 0.498 |
| Colombo | 0.832 / 0.698 / 0.541 | 0.902 / 0.737 / 0.247 | 0.965 / 0.890 / 0.208 | 0.813 / 0.686 / 0.479 |
| Jebel Ali | 0.824 / 0.705 / 0.574 | 0.976 / 0.927 / 0.262 | 0.993 / 0.975 / 0.219 | 0.835 / 0.712 / 0.494 |
| Los Angeles | 0.839 / 0.730 / 0.568 | 0.910 / 0.759 / 0.266 | 0.994 / 0.982 / 0.217 | 0.831 / 0.717 / 0.475 |
| New York/NJ | 0.854 / 0.748 / 0.563 | 0.910 / 0.759 / 0.260 | 0.993 / 0.975 / 0.218 | 0.825 / 0.712 / 0.468 |
| Vancouver | 0.839 / 0.730 / 0.566 | 0.910 / 0.759 / 0.266 | 0.994 / 0.982 / 0.217 | 0.827 / 0.701 / 0.459 |
| Santos | 0.837 / 0.712 / 0.560 | 0.910 / 0.761 / 0.270 | 0.993 / 0.975 / 0.210 | 0.862 / 0.755 / 0.480 |
| Cartagena | 0.832 / 0.729 / 0.514 | 0.902 / 0.770 / 0.235 | 0.965 / 0.890 / 0.208 | 0.813 / 0.686 / 0.479 |
| Durban | 0.845 / 0.730 / 0.574 | 0.910 / 0.759 / 0.259 | 0.991 / 0.913 / 0.159 | 0.839 / 0.718 / 0.514 |
| Lagos (Apapa) | 0.832 / 0.703 / 0.538 | 0.910 / 0.761 / 0.269 | 0.994 / 0.978 / 0.222 | 0.839 / 0.718 / 0.514 |
| Melbourne | 0.842 / 0.726 / 0.578 | 0.910 / 0.761 / 0.270 | 0.994 / 0.978 / 0.216 | 0.832 / 0.718 / 0.477 |


# S1.6 Measurement windows: reconstruction and changed cells

The frozen July 2026 snapshots (44 series; SHA-256 identical to the July result register) were re-run under alternative windows. Only the de facto windows reproduce the submitted Table 4.1; they were recovered by a grid search over window bounds (`src/grid.py`).

| Windows | COVID cells reproducing submitted Table 4.1 | Red Sea cells reproducing submitted Table 4.1 |
|---|---|---|
| Stated in the submitted text (1 Jan 2020–31 Dec 2021; 1 Oct 2023–30 Jun 2025) | 5 / 22 | 10 / 22 |
| De facto, recovered (24 Feb–4 Oct 2020; 26 Nov 2023–26 Sep 2024) | 22 / 22 | 22 / 22 |
| Revision, acute phase (1 Jan–30 Sep 2020; 19 Nov 2023–18 Nov 2024) | 20 / 22 | 14 / 22 |


**Port–shock cells that change (10).** depth % / half-life (weeks).

| Port | Shock | Submitted (de facto windows) | Acute windows | Acute windows + K24 |
|---|---|---|---|---|
| Valencia | Red Sea | -0.5 / 0 | 0.2 / 1 | 0.2 / 1 |
| Mersin | COVID-19 | 0.1 / 1 | 2.0 / 2 | 2.0 / 2 |
| Mersin | Red Sea | 29.4 / 5 | 32.0 / 6 | 5.4 / 1 |
| Shanghai | COVID-19 | 5.5 / 1 | 9.6 / 3 | 9.6 / 3 |
| Shanghai | Red Sea | 1.8 / 1 | 3.6 / 1 | 3.6 / 1 |
| Busan | Red Sea | -5.1 / 0 | 2.8 / 4 | 2.8 / 4 |
| Port Klang | Red Sea | 2.0 / 2 | 3.0 / 4 | 3.0 / 4 |
| Colombo | Red Sea | 2.9 / 1 | 4.4 / 1 | 0.0 / 0 |
| New York/NJ | Red Sea | 6.9 / 1 | 13.7 / 1 | 13.7 / 1 |
| Cartagena | Red Sea | -19.8 / 0 | -6.0 / 0 | -6.0 / 0 |


# S1.7 Pre-shock level rule (K24)

Rule: if the mean ratio over the eight weeks before the window departs from unity by more than 0.15 **and** the trough falls in window weeks 0–3, depth and half-life are measured against the pre-window level. Red Sea window shown; the rule cannot be evaluated for the COVID window (no pre-window ratios for the 2019 base).

| Port | Pre-window ratio (8 wk) | |pre − 1| > 0.15 | Trough week in window | K24 applied |
|---|---|---|---|---|
| Rotterdam | 0.958 |  | 9 |  |
| Hamburg | 0.997 |  | 9 |  |
| Antwerp | 1.007 |  | 4 |  |
| Gdańsk | 0.926 |  | 7 |  |
| Valencia | 1.079 |  | 51 |  |
| Piraeus | 1.105 |  | 26 |  |
| Tanger Med | 1.075 |  | 35 |  |
| Mersin | 0.719 | yes | 0 | yes |
| Singapore | 1.075 |  | 31 |  |
| Shanghai | 1.056 |  | 51 |  |
| Busan | 1.127 |  | 52 |  |
| Port Klang | 1.105 |  | 52 |  |
| Colombo | 0.681 | yes | 0 | yes |
| Jebel Ali | 1.017 |  | 23 |  |
| Los Angeles | 0.971 |  | 17 |  |
| New York/NJ | 1.056 |  | 48 |  |
| Vancouver | 0.993 |  | 8 |  |
| Santos | 1.033 |  | 39 |  |
| Cartagena | 1.228 | yes | 51 |  |
| Durban | 2.736 | yes | 7 |  |
| Lagos (Apapa) | 0.988 |  | 39 |  |
| Melbourne | 1.045 |  | 24 |  |


**Mersin, weekly container calls and ratio to the same ISO week of 2022 (September 2023 – March 2024).** The window opens on 19 November 2023.

| Week (Monday) | Container calls | Ratio to 2022 | 4-week rolling mean |
|---|---|---|---|
| 2023-09-04 | 22 | 0.595 | 0.591 |
| 2023-09-11 | 15 | 0.484 | 0.580 |
| 2023-09-18 | 27 | 0.818 | 0.602 |
| 2023-09-25 | 22 | 0.667 | 0.641 |
| 2023-10-02 | 28 | 0.824 | 0.698 |
| 2023-10-09 | 29 | 0.763 | 0.768 |
| 2023-10-16 | 25 | 0.893 | 0.787 |
| 2023-10-23 | 21 | 0.618 | 0.774 |
| 2023-10-30 | 26 | 0.667 | 0.735 |
| 2023-11-06 | 23 | 0.639 | 0.704 |
| 2023-11-13 | 23 | 0.657 | 0.645 |
| 2023-11-20 | 25 | 0.758 | 0.680 |
| 2023-11-27 | 30 | 0.769 | 0.706 |
| 2023-12-04 | 23 | 0.639 | 0.706 |
| 2023-12-11 | 24 | 0.706 | 0.718 |
| 2023-12-18 | 25 | 0.962 | 0.769 |
| 2023-12-25 | 31 | 1.033 | 0.835 |
| 2024-01-01 | 22 | 0.759 | 0.865 |
| 2024-01-08 | 30 | 0.968 | 0.930 |
| 2024-01-15 | 25 | 0.862 | 0.905 |
| 2024-01-22 | 31 | 1.148 | 0.934 |
| 2024-01-29 | 25 | 0.962 | 0.985 |
| 2024-02-05 | 33 | 1.065 | 1.009 |
| 2024-02-12 | 29 | 1.115 | 1.072 |
| 2024-02-19 | 27 | 0.794 | 0.984 |
| 2024-02-26 | 27 | 0.931 | 0.976 |
| 2024-03-04 | 27 | 0.771 | 0.903 |
| 2024-03-11 | 36 | 1.200 | 0.924 |


**Mersin, mean daily container calls by quarter.**

| Quarter | Mean daily container calls |
|---|---|
| 2022Q1 | 4.2 |
| 2022Q2 | 4.1 |
| 2022Q3 | 4.6 |
| 2022Q4 | 4.9 |
| 2023Q1 | 3.7 |
| 2023Q2 | 2.7 |
| 2023Q3 | 2.8 |
| 2023Q4 | 3.6 |
| 2024Q1 | 4.1 |
| 2024Q2 | 4.1 |
| 2024Q3 | 4.2 |
| 2024Q4 | 3.8 |


# S1.8 Exposure (two-step) contexts

E_C: OxCGRT stringency, 2020 mean, calibrated on world-distribution anchors (75.67 / 60.49 / 41.48). E_R: rule-based lane-dependence and partner-trade index (codebook §C). Fragility = 1 − calibrated resilience.

| Port | E_C | Fragility, COVID | E_R | Fragility, Red Sea | Stringency context | Rerouting context |
|---|---|---|---|---|---|---|
| Rotterdam | 0.48 | 0.79 | 0.70 | 0.90 | low | exposed |
| Hamburg | 0.52 | 1.00 | 0.70 | 0.97 | high | exposed |
| Antwerp | 0.50 | 0.12 | 0.70 | 0.86 | low | exposed |
| Gdańsk | 0.36 | 0.80 | 0.70 | 0.83 | low | exposed |
| Valencia | 0.76 | 0.10 | 0.70 | 0.05 | high | exposed |
| Piraeus | 0.71 | 0.44 | 0.95 | 0.79 | high | exposed |
| Tanger Med | 0.92 | 0.03 | 0.70 | 0.07 | high | exposed |
| Mersin | 0.65 | 0.05 | 0.95 | 0.13 | high | exposed |
| Singapore | 0.40 | 0.87 | 0.40 | 0.50 | low | partial |
| Shanghai | 0.91 | 0.50 | 0.40 | 0.10 | high | partial |
| Busan | 0.32 | 0.35 | 0.40 | 0.35 | low | partial |
| Port Klang | 0.68 | 0.99 | 0.40 | 0.40 | high | partial |
| Colombo | 0.32 | 0.82 | 0.40 | 0.05 | low | partial |
| Jebel Ali | 0.47 | 0.03 | 0.40 | 0.33 | low | partial |
| Los Angeles | 0.80 | 0.48 | 0.05 | 0.95 | high | unexposed |
| New York/NJ | 0.80 | 0.19 | 0.40 | 0.49 | high | partial |
| Vancouver | 0.76 | 0.46 | 0.05 | 1.00 | high | unexposed |
| Santos | 0.82 | 0.82 | 0.05 | 0.09 | high | unexposed |
| Cartagena | 0.94 | 0.96 | 0.05 | 0.05 | high | unexposed |
| Durban | 0.70 | 0.16 | 0.05 | 0.80 | high | unexposed |
| Lagos (Apapa) | 0.70 | 0.76 | 0.05 | 0.81 | high | unexposed |
| Melbourne | 0.70 | 0.82 | 0.05 | 0.52 | high | unexposed |


*Step 1: E_C → \~Y consistency 0.617, PRI 0.455; necessity 0.762, RoN 0.588. E_R → \~Y consistency 0.672, PRI 0.497; necessity 0.563, RoN 0.808. Six-condition conservative solution for Red Sea-window fragility: \~C1·\~C2·\~C3·C4·C5·\~E_R. Within-context minimisations are not reported (case-to-condition benchmark; codebook K17d). New York–New Jersey E_R at 0.70 instead of 0.40: E_R → \~Y 0.660 / 0.480; no other change.*


# S1.9 Calibration B (additive composite)

Resilience B = 0.5 (1 − normalised depth) + 0.5 (1 − normalised half-life), calibrated at the 10th / 50th / 90th percentiles. Results are in the "calibration B (additive)" row of S1.5: the Durban path holds (0.933 / 0.717 / 0.202); the pandemic four-case path falls below PRI (0.828 / 0.691 / 0.602); the Hamburg–Antwerp–Vancouver term does not survive (0.779 / 0.662). The additive composite lets a deep but short trough offset a shallow but long one, which is why the product (resilience-triangle area) is the primary definition.


# S1.10 Data vintage

All 22 ports × 2 shocks were re-pulled from the PortWatch API on 3 November 2026 (engine v5.1, paginated). Of 60,566 overlapping port-days, three differ (Singapore 30 Oct 2024; Shanghai 3 Jan 2024 and 7 Feb 2025), none on a trough or half-life path. Under the acute windows with K24 the November data reproduce all 44 outcome cells (`data/window_variants/cond_NOV2026_A1_acute.csv`).
