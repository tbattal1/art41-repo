# ART-41 — Codebook v2.8 (English edition of the locked codebook v2.6, with revision entries K17–K23)

## Preface to the English edition

Codebook v2.6 (Turkish, locked on 08.07.2026) was the version used for the coding of all 22 cases (July 2026). The present edition, v2.7, is (i) a faithful English translation of v2.6 and (ii) a set of revision entries (K17–K20, 03.11.2026) made in response to the first-round reviews. **No C1–C5 coding rule was altered at revision.** The only change to a recorded condition score is the correction logged as K18 (Gdańsk C5), which applies the existing rules; it is documented in the change log and in Section G.

Editorial conventions of this edition:

- Working-session apparatus of the Turkish original (progress flags, interlocutor names) has been removed. "Author decision, <date>" marks a rule or correction decided by the author; "coding assistant" denotes the AI coding assistant where the original named it.
- Section lettering: because the new remote-conditions section is inserted as Section C, the remaining sections of v2.6 are re-lettered (v2.6 C → D, D → E, E → F, F → G). Internal cross-references have been updated accordingly.
- Rule numbers (K1–K16, Note #1–#14), thresholds, score tables, example ports, dates and sources are reproduced unchanged.
- Symbol register (checked for overlap): A/B — calibration anchor sets; C1–C5 — governance conditions; D, Q, Z — indicators of E_R; E_C, E_R — remote conditions; N — number of cases; P90/P50/P10 — calibration percentiles; S1–S3 — supplementary files; Shock 1 / Shock 2 — the COVID-19 and Red Sea shocks (the Turkish original uses "Ş1/Ş2"; spelled out here to avoid collision with S1–S3). Y — outcome (resilience); ¬Y — fragility.

---

**Status (v2.6):** LOCKED — stress-tested with the 4-case pilot + Batch 1-2 (Hamburg/Antwerp/Gdańsk/Valencia/Piraeus/Tanger Med) + Batch 3 Asia (Singapore/Shanghai/Busan/Port Klang) + Batch 4 (Colombo/Jebel Ali); 16 author decisions (K1–K16) incorporated. The full coding round (August) is carried out with this version; any change is opened only as a new version with a documented rationale (change-log entry mandatory, see Section F).

**Documented-cell rule (absolute):** No code cell whose source is undocumented may enter the truth table. Every code = value + source + date + one-sentence rationale. A cell without evidence = MISSING; guessing is prohibited.

---

## SECTION A — CODING RULES

### General rules

1. **Source hierarchy:** (1) primary legal text (statute, law, concession agreement) > (2) official port-authority report > (3) World Bank Port Reform Toolkit 2025 / ESPO / ITF-OECD > (4) peer-reviewed literature > (5) trade press (only for confirming events, not for classification).
2. **Time window:** Conditions are coded as of end-2019 (pre-shock state → direction of causality). The reform-count window is FIXED: **2005–2019** (v2, Note #2). Major governance changes after 2019 are noted on the coding sheet and taken into account in the Shock-2 robustness coding.
3. **Conflicting sources:** The higher source in the hierarchy prevails; the conflict is noted on the coding sheet.
4. **Unknown ≠ 0.05:** A cell without evidence is MISSING; a case with a MISSING cell is replaced from the reserve list.
5. **Correction log:** When a coder (including the coding assistant) finds his or her own error, an explicit correction record is entered — precedents: Melbourne 99 → 50 years; Singapore C4 0.11 → 0.33.

### C1 — Regulatory Autonomy

**SUBJECT RULE (v2, Note #5 + #12, K1 + K9, author decision):** The subject of C1 = the actor that ACTUALLY performs the landlord/management function — public or private.
**Distinguishing test:** Does the actor lease/license to third-party operators?

- No (single-operator concessionaire, e.g. MIP) → subject = the public side (grantor/regulator); operator discretion is recorded under C2.
- Yes (e.g. PoM, Rotterdam N.V.) → subject = that actor.

**CONTROL TYPOLOGY (v2, Note #1 + #13, K10, author decision):** Three control types are treated separately:

| Type | Example | Effect |
|---|---|---|
| (i) Hierarchical tutelage (ministerial approval, general budget) | Mersin public side, TNPA/Transnet | Lowers autonomy |
| (ii) General-meeting rights of a public shareholder | Rotterdam (municipality 70 % + state 30 %) | Does NOT lower autonomy |
| (iii) Independent-regulator ceiling | Melbourne (ESC Pricing Order) | Only the AFFECTED decision domain is treated as outside autonomy |
| (iv) Sovereign-integrated fusion (K16) | Jebel Ali (PCFC = DP World, Dubai state) | Does NOT lower autonomy — no external central approval; the group self-governs |

**K16 — SOVEREIGN-INTEGRATED CONTROL (control type iv) (v2.6, 08.07.2026, author decision):** Where landlord/regulator + operator + owner are in a state of FUSION within the same sovereign state group (e.g. Dubai state → PCFC + DP World, same chairman; sovereign = owner), the K9 subject test degenerates (there is no counterpart to separate). Because no EXTERNAL central authority exists to approve decisions, the group self-governs all three decision domains (tariff/investment/concession) → NO tutelage → **C1 = 0.95** (Jebel Ali). **Critical distinction:** separation (Singapore: MPA ≠ PSA + external ministerial approval → tutelage → 0.50) versus fusion (Dubai: sovereign direction = self-government → 0.95). Note: C2 is still coded under K13 (corporatised state operator → public-dominant, Jebel Ali 0.30).

**K13 — CORPORATISED DOMESTIC-STATE OPERATOR DISTINCTION (v2.3, 08.07.2026, author decision):**
In the configuration "corporatised but 100 % (or majority) domestic-state-owned operator + separate statutory-board/administrative landlord-regulator" (e.g. PSA/Temasek + MPA; SIPG + municipal administration):

- **The C1 subject = the landlord/regulator authority** (K9 literally: the operator does not lease to third parties, it operates → single-operator branch → subject = public side).
- **The K10(ii) shareholder relief applies ONLY to a corporatised LANDLORD with shareholders** (Rotterdam N.V.). It does not apply to a statutory board (MPA — no shareholders) or to an operator that is NOT a landlord (PSA).
- Where state control is active hierarchical direction rather than a passive general-meeting right (SASAC appointments + party oversight, Shanghai), it is type (i) → lowers autonomy.
- **Rationale:** Corporatisation ≠ privatisation; the conceptual distinction between C1 (autonomy) and C2 (ownership hybridity) is preserved.

**Score table (three decision domains: tariff / investment / concession-leasing):**

| Evidence | Score |
|---|---|
| All three within the governing body; no tutelage | 0.95 |
| Two autonomous; one under tutelage or a regulator ceiling | 0.70 |
| Autonomous legal personality exists, but strategic decisions are subject to central approval | 0.50 |
| Legal personality exists, but even operational decisions sit within the national system | 0.30 |
| Deconcentrated government department / no corporatised authority | 0.05 |

### C2 — Ownership Hybridity

| Evidence | Score |
|---|---|
| >80 % of container capacity private/mixed AND ≥2 independent operators | 0.95 |
| >80 % private but a single dominant operator | 0.70 |
| ~40–60 % mixed | 0.50 |
| <20 % private participation (public-dominant in containers but private presence in other cargo types OR a formal landlord structure) | 0.30 |
| Fully public service port (no meaningful private participation in any segment) | 0.05 |

**v2 (Note #10, K8, author decision):** The primary metric is the container share; in diversified ports the private share in bulk/liquid cargo is kept on the coding sheet as a SEPARATE COLUMN (it does not change the score; raw material for the Discussion). Durban precedent: containers ~100 % public + private bulk + formal landlord → 0.30.
**Note:** A state-owned foreign operator (COSCO, DP World) counts as "private"; the operator type is marked in the column.
**K13 (v2.3, author decision):** Corporatised DOMESTIC-STATE ownership is NOT "private" — it counts as public-dominant (≤0.30 band). The COSCO/DP World note above concerns a FOREIGN operator winning a concession in a host port; it does not apply to a country's OWN national state operator (Temasek/PSA, SIPG). Where corporatisation + listing + minority JVs do not change public-dominant control, the score is 0.30 (Singapore/Shanghai precedent).

### C3 — Multi-Level Coordination Density

Four binary indicators, sum/4:

1. Institutionalised city–port body (joint committee, including a shareholder-municipality body) — **note:** in a city-state / single-municipality-ownership configuration, where there is no separate city–port body (integration is intra-state hierarchy), it does NOT count (Singapore/Shanghai precedent; symmetry with the C3.2 vertical-hierarchy exclusion).
2. Active participation in a national port strategy/coordination body — **v2:** vertical-hierarchy coordination (ministry → SOE → port) does NOT count (Mersin/Durban precedent); membership of a sector association (TÜRKLİM, Ports Australia) does NOT count. A horizontal multi-stakeholder framework (tripartite ITM, regional port integration) DOES count.
3. ACTIVE international network membership (documented activity within the last 3 years; passive membership does not count).
4. Written crisis / business-continuity coordination protocol — **v2.1 (Note #14, K11, author decision):** Facility-scale plans that are universal legal requirements (ISPS, Law No. 5312 emergency response plans, SEMP-type statutory plans) do NOT count — since every port in the jurisdiction has them, they carry no discriminating power. Bar: port-specific + multi-actor (municipality / other ports / hinterland) + institutionalisation beyond the legal minimum (precedents: Rotterdam FERM + CyberNautics + port-ISAC → 1; Mersin Law No. 5312 facility plan → 0; Melbourne SEMP → 0; a digital-sharing PCS on its own → 0).

**Score:** 4/4 = 0.95, 3/4 = 0.70, 2/4 = 0.50, 1/4 = 0.30, 0/4 = 0.05

### C4 — Compound Lock-In (three sub-dimensions, unweighted mean)

**(a) Regulatory rigidity (window 2005–2019):**

| Situation | Score |
|---|---|
| ≥2 meaningful reforms | 0 |
| 1 reform | 0.33 |
| 1 reform + a documented failed/stalled subsequent framework reform (Mersin: Ports Law [Limancılık Kanunu] — K2, author decision) | 0.67 |
| 0 reforms (with or without failed attempts) | 1 |
| **Enacted-but-unimplemented core reform** (Durban: the 2005 Act's corporatisation mandate, 16 years — K6, author decision) | 1 |

**Note (definition of reform):** "Meaningful reform" = a structural GOVERNANCE/ownership reform (corporatisation, transition to the landlord model, restructuring of the concession model). Infrastructure/digital/spatial consolidation (Singapore Tuas, digitalPORT@SG) does NOT count; a concession EXTENSION is continuity, not reform (Port Klang 2010/2013 precedent).

**(b) Financial lock — TWO BRANCHES (v2, Note #10b, K7, author decision):**

- **Branch A (concessioned/leased ports):** Capacity-weighted remaining concession term (2019): <10 years = 0, 10–25 = 0.33, 25–40 = 0.67, >40 = 1. (Melbourne: 47 years → 1; Port Klang: ~32 years → 0.67.)
- **Branch B (state-operator ports):** SOE financial constraint — three indicators: documented investment gap / debt-service pressure / equipment age–renewal gap. 0 indicators = 0, 1 = 0.33, 2 = 0.67, 3 = 1. (Durban: 3/3 → 1; PSA/SIPG: 0/3 → 0.)
- The choice of branch is justified on the coding sheet; in mixed structures the dominant structure governs.
- **K15 — RENEWABLE / AREA-BASED LEASE SYSTEM (v2.5, 08.07.2026, author decision):** Where a landlord port has a renewable/area-based lease system INSTEAD OF fixed long concessions (e.g. Busan: fixed rent by berth area, active restructuring, competitive re-tendering) and the exact lease term cannot be sourced, C4b is coded on **evidence of financial flexibility** rather than remaining term. Balance between sunk terminal capital (lock-in direction) and renewable/renegotiable leases (flexibility direction). Busan precedent: sunk capex + renewable lease → 0.33. An estimated term figure does NOT enter the truth table (documented-cell rule).

**K21 — PRIVATE-USE TERMINALS (TUP) UNDER BRANCH A (v2.7, 03.11.2026, author decision):** Where a container terminal operates under a public authorization rather than a lease or concession (Brazilian *terminal de uso privado*, TUP; ANTAQ *contrato de adesão*), its remaining term for the capacity-weighted Branch A computation is the remaining term of the authorization as fixed in the adhesion contract (Lei 12.815/2013, Art. 8 §2: 25 years, renewable), counted from the contract date. Terminals not operating at the coding date (end-2019) are excluded from the weights. Alternatives (TUP excluded; TUP treated as >40 years) are reported as sensitivity in the coding sheet. First application: Santos (DP World Santos, Contrato de Adesão nº 17/2014-ANTAQ → 09.09.2039).

**(c) Social-legitimacy gap (window 2015–2019):**
Documented **operationally effective** conflict CLUSTERS: 0 = 0, 1 = 0.33, 2 = 0.67, ≥3 = 1.
**Cluster definition (v2, Note #3):** Same parties + same demand + <12 months = 1 event.
**v2.2 (K12, author decision — operational rule):** C4c measures ONLY acute conflict that has produced or could produce an operational interruption (strike, blockade, protest halting throughput, dispute leading to concession termination). Ongoing environmental/legal litigation (Hamburg Elbe dredging, dig-out port objections) does NOT enter C4c unless it turned into an operational interruption; it is noted on the coding sheet in a SEPARATE COLUMN as "structural conflict (non-operational)". Durban precedent: SDCEA opposition delayed the dig-out + strike threat → operationally effective, counts. (Note: financial insolvency/collapse — Hanjin 2016 — is not a conflict and does not enter C4c.)
**Time note (v2, Note #7):** Fixed at 2019 in the main analysis; in the robustness analysis for Shock 2 it is re-coded with a 2019–2023 window (C4c only).

**Direction note:** C4 measures lock-in; the hypothesised direction is left open — consistent with the asymmetric logic of fsQCA; framed as an open question in the Introduction. (Finding: Singapore/Port Klang high C4a + zero C4b/C4c = "stability-because-optimised" ≠ "locked-because-blocked" — the lock-in ↔ dysfunction divergence, a Discussion axis.) *Revision note (03.11.2026):* for the fragility outcome, directional expectations were fixed at revision (K19); this is an analysis setting, not a coding rule.

### C5 — Social Value Integration

Three binary indicators, sum/3:

1. BINDING environmental/community mandate in the statute/founding law (obligation language; including a statutory public-duty definition — Durban precedent; Spanish TRLPEMM environmental duty + mandatory *memoria de sostenibilidad* → 1)
2. Regularly convened stakeholder representation body in governance (including statutory PCC-type committees — with confirmation of actual functioning; Spanish *Consejo de Navegación y Puerto*, TRLPEMM Art. 34 → 1)
3. Social-green conditions in concession/licence terms (local employment, B-BBEE, emission threshold, shore power)

**Score:** 3/3 = 0.95, 2/3 = 0.70, 1/3 = 0.40, 0/3 = 0.05
**v2 (Note #8):** Voluntary CSR/green programmes — however comprehensive — do NOT count as structural integration (Mersin; Singapore MSGI; Malaysia voluntary green-port policy precedent).
**v2 (Note #11, analytical):** C5 measures de jure institutionalisation, C4c measures de facto legitimacy; their divergence (the Durban profile) is not a contradiction but a FINDING — candidate backbone of the Discussion.
**K14 — UNIVERSAL BINDING GREEN MANDATE (v2.4, 08.07.2026, author decision):** For C5.3, a universal/national **binding** green mandate (mandatory shore power; ECA/SECA emission threshold; EU at-berth sulphur mandate from 2010; China DECA; Korea Port Air Quality Act) COUNTS. Rationale: C5 measures institutionalisation (not discriminating power) — K11's discriminating-power bar was for C3.4/C3.1; the C5 indicators do not require it. **Known consequence (accepted):** the EU at-berth mandate (binding from 2010) makes C5.3 = 1 in all EU ports → C5.3 becomes uniform in the EU sub-sample (approaching an EU/ECA-port proxy); since C5 is composite (C5.1/C5.2 discriminate), fsQCA is preserved, but this is reported transparently in the Discussion. **Retroactive:** C5.3 was re-checked in the coded EU cases (see Section G).

---

## SECTION B — OUTCOME DERIVATION PROTOCOL (LOCKED — 07.07.2026, with the Rotterdam Shock-1 pilot)

**DECISION:** Y = **year-on-year same-ISO-week ratio** (seasonally adjusted), 4-week rolling mean. Rationale: on the real Rotterdam data, LEVEL-raw was fooled by the Christmas artefact and LEVEL-mask/seasonal by the early-2020 winter trough; only YoY found the true COVID trough (8 June 2020). The decision was tested against data.

1. **Data:** IMF PortWatch port-level daily → ISO-weekly (complete weeks only). Snapshot discipline: raw data are pulled once, frozen in `art41_snapshots/`, SHA-256 stamped; all analyses run from the frozen file.
2. **YoY ratio:** ratio_t = value(year, ISO week) / value(reference year, same ISO week). Reference: **Shock 1 → 2019; Shock 2 → 2022**. The W53 → W52 mapping is logged.
3. **Metrics:** trough ratio (1 − trough = depth of decline, %) → trough week → return to the 95 % threshold (first touch + sustained for 4 weeks) → half-life.
4. **Two metric columns:** total portcalls and portcalls_container are reported separately. Primary fsQCA Y: portcalls_container (decision recorded in the design log after the Rotterdam pilot and confirmed in the full coding round, July 2026; see manuscript §3.4 — the total series understated and mistimed the pandemic trough).
5. **Fate of LEVEL:** NOT the primary definition; "definition sensitivity" in the robustness appendix.
6. **Reproducibility chain:** Every metric cell is documented with snapshot file name + SHA + script version (v5.2 at revision; v5 at submission) → GitHub.

**Known weaknesses:** reference-year sensitivity test (robustness); the Shock-2 reference-year conflict was resolved with 2022.

### B.7 Measurement windows (K22, v2.8, 04.11.2026, author decision)

**Rule.** The trough is searched, and the half-life counted, within an **acute-phase window** per shock:

| Shock | Window | Rationale |
|---|---|---|
| Shock 1 (COVID-19) | 1 Jan 2020 – 30 Sep 2020 | Demand-collapse phase. From Q4-2020 the container system entered a congestion regime (record volumes, schedule reliability collapse) that is a different mechanism from the one the outcome is meant to capture; a window extended to end-2021 would mix the two. |
| Shock 2 (Red Sea) | 19 Nov 2023 – 18 Nov 2024 | Twelve months from the Galaxy Leader hijack (19 Nov 2023), i.e. from the first rerouting decisions to the point where the rerouted network had become the new routine. |

The series used for the YoY ratio and the rolling mean are unchanged (Shock 1: 2019-01-01 → 2022-01-09; Shock 2: 2021-01-01 → 2025-07-06); the window only bounds the trough search. The half-life is counted from the trough forward without an upper bound (right-censoring is flagged where it occurs; none in the 22 × 2 cells).

**Disclosure.** The submitted manuscript stated the windows as Jan 2020 – Dec 2021 and Oct 2023 – Jun 2025. Re-running the frozen July 2026 snapshots (44/44 SHA-256 matches with the July result register) with those windows does **not** reproduce Table 4.1; a grid search over window bounds (`src/grid.py`) reproduces all 44 cells exactly with COVID 24 Feb 2020 – 4 Oct 2020 and Red Sea 26 Nov 2023 – 26 Sep 2024 (ISO weeks W09–W40 2020 and W48 2023 – W38 2024). These are therefore the windows **de facto used** in the submitted version. The July engine code that produced them is not in the repository and the mechanism is not recoverable; the author takes responsibility for the misstatement. The de facto windows are retained as a robustness row ("J0"), and the rule above replaces them with windows that are defined ex ante and justified by the shock mechanisms rather than recovered ex post.

**Consequences for Table 4.1 (July snapshots, A1 windows vs de facto windows).** Eight cells change: Shanghai COVID depth 5.5 → 9.6 %, half-life 1 → 3 wk; Mersin COVID 0.1 → 2.0 %, 1 → 2 wk; Mersin Red Sea 29.4 → 32.0 %, 5 → 6 wk; Valencia Red Sea −0.5 → 0.2 %, 0 → 1 wk; Busan Red Sea −5.1 → 2.8 %, 0 → 4 wk; Port Klang Red Sea 2.0 → 3.0 %, 2 → 4 wk; Colombo Red Sea 2.9 → 4.4 %; NY/NJ Red Sea 6.9 → 13.7 %; Shanghai Red Sea 1.8 → 3.6 %; Cartagena Red Sea −19.8 → −6.0 % (no decline in either case). All other cells are identical.

### B.8 Data-anomaly mask for full-window robustness (K23, v2.8, 04.11.2026, author decision)

**Rule.** In robustness runs that extend the window beyond the acute phase (F-variants), weeks in which **all** PortWatch vessel-type series of a port fall simultaneously by more than 40 % against the same ISO week of the reference year are treated as a data-coverage anomaly (AIS gap) and masked before the trough search. The rule is not applied in the primary analysis because no such week falls inside the A1 windows. Documented instance: Colombo, 11 Sep – 29 Oct 2023 (all vessel types ≈ −50 %, present in the July 2026 and November 2026 snapshots alike); it falls outside the A1 Red Sea window but dominates the trough when the window starts on 1 Oct 2023. The holiday mask (ISO weeks 51–53 and 1) is a separate, pre-existing sensitivity variant (A2/F2) and has no effect under A1.

---

## SECTION C — REMOTE CONDITIONS (added at revision, 03.11.2026)

### C.0 Purpose and status within the design

Two *remote* conditions are added to the design in response to Reviewer 3: exposure to the COVID-19 demand shock (E_C) and exposure to the Red Sea rerouting shock (E_R). They are **not governance conditions** and are not added to the five-condition governance model. Following Schneider and Wagemann's (2006) two-step procedure, they enter a separate first step that identifies the exposure *contexts* in which fragility occurs; the governance conditions C1–C5 are then examined within those contexts (step two; descriptive only, see C.3 and K17d). The published five-condition results of the submitted version are unchanged by this addition; the two-step analysis is reported as a new Section 4.6 and informs the Discussion.

Both remote conditions are measured from sources that are (i) external to the port and its governance, (ii) public and free, (iii) available for all 22 cases, and (iv) fixed before the shock's outcome is examined. Rules, thresholds and fallbacks were fixed before any data were retrieved (change-log entry K17); the two amendments made after retrieval but before any outcome comparison are logged as K17a–K17d.

### C.1 E_C — Exposure to the COVID-19 demand shock

**Concept.** The intensity of domestic non-pharmaceutical restrictions in the port's country during the year of the demand collapse. Domestic restrictions suppress import demand, hinterland activity and port labour availability simultaneously; they are the component of pandemic exposure that is external to port governance and comparably measured worldwide.

**Source.** Oxford COVID-19 Government Response Tracker (OxCGRT), *StringencyIndex_Average*, national level, daily (Hale et al., 2021; DOI 10.1038/s41562-021-01079-8). Data file: the OxCGRT final national-level CSV (version and download date recorded in the coding sheet; SHA-256 stored with the data snapshot).

**Measure.** E_C(raw) = arithmetic mean of the daily national StringencyIndex_Average from **1 March 2020 to 31 December 2020** (inclusive). Window = 2020 only (author decision). Rationale: the COVID outcome window is 2020Q1–2021Q4, but the demand collapse that the resilience-loss score measures formed in 2020; 2021 stringency reflects vaccination and variant dynamics that overlap with recovery and would blur exposure with response.

**Calibration (K17a).** Direct method. Anchors are the **world-distribution percentiles of the 2020 national means** (same measure, same window, all 185 OxCGRT countries): full membership (0.95) at ≥ **75.7** (P90); crossover (0.50) at **60.5** (P50); full non-membership (0.05) at ≤ **41.5** (P10). The anchors are therefore external to the 22-case sample (they are not sample percentiles) and avoid the outlier sensitivity flagged for the outcome calibration. The nominal scale points of the pre-registered v1 rules (70/55/40) were replaced before any outcome comparison because they placed all 22 cases above the crossover, which would have made E_C non-discriminating by construction (K17a). If more than 80 % of cases fall on one side of the crossover under the percentile anchors, the skew is reported (Section 4.6) and the condition is retained; anchors are **not** moved post hoc.

**Sub-national robustness (pre-committed).** OxCGRT publishes sub-national indices for Australia, Brazil, Canada, China and the United States. As a robustness check only, E_C is recomputed for Melbourne (Victoria), Santos (São Paulo), Vancouver (British Columbia), Shanghai (Shanghai) and Los Angeles / New York–New Jersey (California / New York) using the sub-national series, and the two-step analysis is re-run. The national series remains primary for comparability across the 22 cases.

**Known limitation to be stated.** National stringency does not capture trading-partner lockdowns (the external-demand component). This is accepted because partner-weighted stringency would require port-level trade-partner shares that are not publicly available for all 22 ports.

### C.2 E_R — Exposure to the Red Sea rerouting shock

**Concept.** The degree to which a port's deep-sea container connectivity depended, immediately before the crisis (2023Q4), on services transiting the Suez Canal / Bab el-Mandeb, and the degree to which the port stood to lose calls rather than merely suffer delays when those services were diverted around the Cape of Good Hope.

Three indicators, each coded from public sources with the rule below, are combined into an ordinal four-level membership.

#### C.2.1 Indicator D — lane dependence (binary)

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

*Source.* UNCTAD *Review of Maritime Transport 2024*, Red Sea crisis section (list of affected trade lanes); where RMT 2024 does not list lanes explicitly, the public 2023Q4 alliance network maps (2M, Ocean Alliance, THE Alliance) are used and cited instead. Each D = 1 port is corroborated by at least one named 2023Q4 service that called at the port and transited Suez.

#### C.2.2 Indicator Q — partner-region trade quotient (continuous, country level)

Q = (value of the port country's 2023 merchandise trade with partner countries on the *far side of Suez* relative to the port) ÷ (value of the port country's 2023 merchandise trade with all partners *outside its own region*).

- "Merchandise trade" = imports + exports, HS chapters 01–24 and 28–99 (i.e., excluding HS 25–27: mineral products, ores and fuels, which move predominantly in bulk and tanker tonnage). This is the containerisable-trade proxy.
- **Partner sets (K17b).** Partner groups are defined on UN M49 regions/sub-regions with the ISO-3 country additions listed below; the exhaustive partner lists are kept in the coding sheet (`exposure_coding.md`).
  - *Atlantic-side reporters* (European, Mediterranean, Black Sea and North African port countries: Netherlands, Germany, Belgium, Poland, Spain, Greece, Morocco, Türkiye):
    - **Own region** = the **Euro-Mediterranean block** = all M49 *Europe* + M49 *Northern Africa* + {TUR, CYP, SYR, LBN, ISR, PSE, JOR, GEO, ARM, AZE}. Trade within this block is predominantly land-borne or short-sea and does not use the Suez mainlines; it is excluded from the denominator.
    - **Far side of Suez** = M49 *Eastern Asia* + *South-eastern Asia* + *Southern Asia* + the **Gulf-plus** set {SAU, ARE, QAT, KWT, BHR, OMN, IRQ, IRN, YEM} + M49 *Eastern Africa* + M49 *Oceania*.
  - *Asian and Gulf reporters* (China, Republic of Korea, Singapore, Malaysia, Sri Lanka, United Arab Emirates):
    - **Own region** = the reporter's M49 sub-region(s): *Eastern Asia* + *South-eastern Asia* for China, Korea, Singapore and Malaysia; *Southern Asia* for Sri Lanka; *Western Asia* for the UAE.
    - **Far side of Suez** = M49 *Europe* **excluding RUS and BLR** + M49 *Northern Africa* + the Levant/Türkiye/Caucasus set {TUR, CYP, SYR, LBN, ISR, PSE, JOR, GEO, ARM, AZE}.
  - The Comtrade partner "Other Asia, nes" (code 490, Taiwan Province of China; S19 in the standard-area nomenclature) is mapped to *Eastern Asia*.
- United States: Q is computed from US Census Bureau foreign-trade statistics by customs district (New York district), since the two US cases differ in lane exposure. Los Angeles has D = 0 and needs no Q.
- Q is computed only for D = 1 ports (15 cases). Source: UN Comtrade (or the WITS front end), reference year 2023, reporter = port country; download date, query parameters and file checksum recorded.

**Threshold.** Q is "high" if Q ≥ **0.40** — i.e., at least two-fifths of the country's inter-regional containerisable trade crosses Suez (author decision). This is a conventional cut and is declared as such; sensitivity at **0.30** and **0.50** is pre-committed.

#### C.2.3 Indicator Z — Mediterranean / Red Sea adjacency (binary) (K17c)

Z = 1 if the port lies in the **Eastern or Central Mediterranean, the Black Sea or the Red Sea**. Rationale: these ports are intermediate calls on the Asia–Europe mainline *reachable only through Suez*; when services were diverted via the Cape they were bypassed (direct Asia–North Europe routing with Mediterranean cargo relayed or omitted), so their exposure mechanism is loss of calls rather than delay. Z = 0 for all other ports, **including the Western Mediterranean** (Valencia, Tanger Med) and the Gulf (reached from Asia without Bab el-Mandeb). *Evidence for the Eastern/Central restriction:* Drewry 1Q24 port-capacity commentary — Eastern and Central Mediterranean hubs lost vessel-call capacity after the diversion, whereas Western Mediterranean ports gained it (K17c). *Source.* UNCTAD RMT 2024 and the documented 2024 Mediterranean call omissions (Drewry 1Q24; port-authority 2024 annual reports where cited on the coding sheet).

#### C.2.4 Combination rule and membership scores

| Profile | E_R |
|---|---|
| D = 0 | 0.05 |
| D = 1, Q low, Z = 0 | 0.40 |
| D = 1, and exactly one of {Q high, Z = 1} | 0.70 |
| D = 1, Q high, Z = 1 | 0.95 |

No case can sit at the 0.50 crossover by construction. Pre-registered expected placement (written in the v1 rules before computation, so that computed values can be checked against them, not adjusted toward them): Mersin, Valencia, Piraeus, Tanger Med ≥ 0.70; Northern European and East Asian ports 0.40 or 0.70 depending on Q; Durban, Lagos, Santos, Cartagena, Los Angeles, Vancouver, Melbourne = 0.05. *Note:* under K17c, Valencia and Tanger Med carry Z = 0, so their placement at ≥ 0.70 depends on Q alone; any departure from the pre-registered expectation is reported, not corrected.

**Pre-committed fallback.** If Q shows little discriminating power among D = 1 ports (inter-quartile range < 0.10), Q is dropped, E_R reduces to the three-level {D, Z} scheme (0.05 / 0.40 / 0.95), and this is reported.

### C.3 Use in the analysis (K17d)

*Step 1 — remote conditions.* For each shock, truth table and minimisation of the outcome "fragility" (¬Y) on the remote condition alone: E_C for COVID; E_R for the Red Sea. With one remote condition per shock, step 1 reduces to a necessity/sufficiency test of exposure for fragility (consistency, PRI, coverage reported; benchmarks 0.80 / 0.75 as in the main analysis).

*Step 2 — proximate conditions within context (descriptive).* The governance conditions C1–C5 are examined within the high-exposure (E ≥ 0.70) and low-exposure (E ≤ 0.40) contexts for each shock. **Within-context minimisations are not reported** (K17d): with 22 cases split across contexts, the case-to-condition ratio falls below the Marx and Duşa (2011) specification benchmark. Step 2 therefore reports, descriptively, whether the cases on the published fragility paths sit in the high- or low-exposure context, and whether Mersin's switch across shocks is reproduced by its E_C / E_R placement.

*Limitation to be stated.* Country-level measurement weakens E_R for transhipment hubs whose traffic is loosely tied to national trade (Piraeus, Colombo, Tanger Med, Singapore, Port Klang); Q therefore understates their exposure. This is stated in Section 5.7, and the D/Z indicators carry the hub cases.

*Coding sheet and snapshots.* `exposure_coding.md`: per-port rows for D (service named), Q (numerator, denominator, source query), Z, E_R; and E_C (raw mean, window, file version). Data snapshots: OxCGRT CSV, the 185-country 2020 national-mean file used for the anchors, and Comtrade extracts, each with SHA-256; R script section `# 7. TWO-STEP (R3)`.

*References for this section.* Hale et al. (2021) *Nature Human Behaviour* 5(4), 529–538, doi:10.1038/s41562-021-01079-8; Marx & Duşa (2011) *Methodological Innovations Online* 6(2), 103–148, doi:10.4256/mio.2010.0037; Schneider & Wagemann (2006) *European Journal of Political Research* 45(5), 751–786, doi:10.1111/j.1475-6765.2006.00635.x; UNCTAD (2024) *Review of Maritime Transport 2024*, Geneva.

---

## SECTION D — TEST AND ROBUSTNESS PACKAGE

(unchanged from v1)

- D.1 Test–retest (5 cases, ≥14 days apart, target ≥80 %) + transparent coding sheet
- D.2 Calibration anchor shifting (±1 step; P90/P50/P10 → P85/P50/P15)
- D.3 Consistency 0.75/0.80/0.85; PRI ≥0.70; leave-one-out; skewness >80 %; simultaneous subset relations
- D.4 Y_COVID vs Y_RedSea as separate runs — overlap report
- D.5 Within-case: 2 typical + 1 deviant (optional)
- Reference: Oana & Schneider protocol, R `QCA` + `SetMethods`

## SECTION E — PILOT + BATCH RESULT RECORD

- Pilot 4/4 (Rotterdam, Mersin, Durban, Melbourne) — 07.07.2026
- Batch 1-2 (Hamburg, Antwerp, Gdańsk, Valencia, Piraeus, Tanger Med) — 08.07.2026
- **Batch 3 Asia (Singapore, Shanghai, Busan, Port Klang) — 08.07.2026 → K13/K14/K15 produced**
- **Batch 4 (Colombo, Jebel Ali) — 08.07.2026 → 16/22 coded, K16 produced**
- Remaining at the v2.6 lock: Batch 5-6 (LA, NY/NJ, Vancouver, Santos, Cartagena, Lagos) — completed under v2.6 in July 2026 (see Preface)

## SECTION F — CHANGE LOG

| Version | Date | Change | Rationale | Decision |
|---|---|---|---|---|
| v1 | 07.07.2026 | First version | — | — |
| v2 | 07.07.2026 | 13 pilot revision notes (subject, control typology, C4a steps, C4b two branches, cluster definition, CSR exclusion) | 4-case pilot | K1–K10 |
| v2.1 | 07.07.2026 | C3.4: universal statutory facility plans do not count | Discriminating power; symmetry with Note #8 | K11 |
| v2.2 | 08.07.2026 | C4c only operationally effective acute conflict | Outcome is operational → the legitimacy gap is operational too (Schneider & Wagemann condition specification) | K12 |
| v2.3 | 08.07.2026 | K13: corporatised domestic-state operator → C1 subject = landlord/regulator; K10(ii) only for landlords with shareholders; in C2 domestic state = public-dominant | Corporatisation ≠ privatisation; C1/C2 conceptual distinction preserved (Singapore/Shanghai) | K13 |
| v2.4 | 08.07.2026 | K14: universal binding green mandate enters C5.3 (shore power, ECA/SECA threshold, EU at-berth mandate, DECA) | C5 measures institutionalisation, not discriminating power; the K11 bar was for C3 (Shanghai DECA) | K14 |
| v2.5 | 08.07.2026 | K15: landlord + renewable/area-based lease system → C4b on evidence of financial flexibility (not remaining term) | Codebook Branch A assumes fixed concessions; Busan's renewable leases are a structural gap; estimated terms prohibited | K15 |
| v2.6 | 08.07.2026 | K16: sovereign-integrated control type (iv) → no external tutelage under fusion → C1 = 0.95 (Jebel Ali) | The K10 typology did not cover the Gulf fusion model; separation ↔ fusion distinction | K16 |
| v2.7 | 03.11.2026 | K17: Remote conditions E_C, E_R added at revision in response to Reviewer 3; rules fixed before data retrieval. | Reviewer 3 (two-step remote/proximate design, Schneider & Wagemann 2006) | K17 |
| v2.7 | 03.11.2026 | K17a: E_C anchors moved from nominal scale points (70/55/40; all 22 cases above crossover) to world-distribution percentiles (75.7/60.5/41.5) before any outcome comparison. | Nominal anchors non-discriminating by construction; external (world-distribution) anchors avoid sample-outlier sensitivity | K17a |
| v2.7 | 03.11.2026 | K17b: Q partner-set definitions as in Section C.2.2 (Euro-Mediterranean block as own region for Atlantic-side reporters; far side = Eastern/South-eastern/Southern Asia, Gulf-plus, Eastern Africa, Oceania; for Asian/Gulf reporters far side = Europe excl. RUS/BLR + Northern Africa + Levant/Türkiye/Caucasus set; own region = M49 sub-region(s)); Taiwan (Comtrade 490/S19) mapped to Eastern Asia. | Exhaustive, reproducible partner lists on M49 basis; land-borne/short-sea trade excluded from the denominator | K17b |
| v2.7 | 03.11.2026 | K17c: Z restricted to Eastern/Central Mediterranean, Black Sea, Red Sea (Drewry 1Q24 evidence: East/Central Med hubs lost vessel-call capacity, West Med gained). | Bypass mechanism (loss of calls) documented for East/Central Med hubs only; West Med gained | K17c |
| v2.7 | 03.11.2026 | K17d: Within-context minimisations not reported (case-to-condition ratio, Marx & Duşa 2011); Step 2 descriptive. | Specification benchmark not met within exposure contexts | K17d |
| v2.7 | 03.11.2026 | K18: Gdańsk C5 0.70 → 0.40: July 2026 retroactive K14 uplift withdrawn (K14 concerns C5.3, already 1); Act on Sea Ports and Harbours (1996) Art. 7 lists no environmental/community mandate. Valencia C5 = 0.95 confirmed (TRLPEMM Art. 34, C5.2 rule). Piraeus C5 = 0.40 confirmed (K14; EU at-berth 0.10 % sulphur limit, Directive (EU) 2016/802 Art. 7, binding since 1 Jan 2010). | Pending confirmation of Section G resolved against the primary legal texts; existing C5 rules applied, no rule change | K18 |
| v2.7 | 03.11.2026 | K19: Directional expectations for fragility outcomes set to the complements of the resilience expectations (C1 = 0, C2 = 0, C3 = 0, C4 = 1, C5 = 0); conservative solution reported as headline. | Analysis setting for the fragility (¬Y) minimisation; not a coding rule | K19 |
| v2.7 | 03.11.2026 | K20: Interpretive: the Durban path is reported as lock-in fragility in a port unexposed to the Red Sea rerouting (E_R = 0.05). | Fragility in a low-exposure context cannot be attributed to exposure; strengthens the governance (C4) reading | K20 |
| v2.7 | 03.11.2026 | K21: Branch A rule for private-use terminals (TUP): remaining ANTAQ authorization term (25 yr from adhesion contract); non-operating terminals excluded; sensitivity reported. | Santos C4b recomputation after a source check found Tecon Santos' lease extended to 2047 in 2015; value 0.33 confirmed | K21 |
| v2.8 | 04.11.2026 | K22: Acute-phase measurement windows fixed (COVID 1 Jan – 30 Sep 2020; Red Sea 19 Nov 2023 – 18 Nov 2024); disclosure that the submitted version de facto used 24 Feb – 4 Oct 2020 and 26 Nov 2023 – 26 Sep 2024 (recovered empirically from the frozen snapshots), while the text stated Jan 2020 – Dec 2021 and Oct 2023 – Jun 2025. Engine v5.2. | Windows must be defined ex ante by the shock mechanism; the stated windows mix the demand collapse with the 2021 congestion regime and the 2025 normalisation and do not reproduce Table 4.1 | K22 |
| v2.8 | 04.11.2026 | K23: Data-anomaly mask (simultaneous >40 % fall in all vessel-type series vs reference week) for full-window robustness runs only; documented instance Colombo 11 Sep – 29 Oct 2023. | AIS coverage gaps must not be read as shock troughs; no instance inside the A1 windows | K23 |

**Retroactive effect (v2.1):** Mersin C3.4 0 → confirmed; Melbourne C3.4 1 (flagged) → 0; Durban C3.4 (flagged) → 0.
**Retroactive effect (v2.4/K14):** see Section G.
**Retroactive effect (v2.7/K18):** Gdańsk C5 0.70 → 0.40; Valencia 0.95 and Piraeus 0.40 confirmed (see Section G).
**Retroactive effect (v2.8/K22):** outcome cells recomputed on the frozen July 2026 snapshots (`data/conditions_and_raw_outcomes_v3.csv`); eight cells change (Section B.7).

## SECTION G — K14 RETROACTIVE RECORD (EU at-berth mandate, 08.07.2026)

EU sulphur directive, 0.1 % at berth (binding from 2010) → C5.3 = 1 in all EU ports. Effect:

| Port | Recorded C5 | After K14 | Change | Confidence |
|---|---|---|---|---|
| Rotterdam | 0.40 | 0.40 | — (C5.3 already 1: shore power/ESI/green concession) | High |
| Hamburg | 0.70 | 0.70 | — (C5.3 already 1) | High |
| Antwerp | 0.70 | 0.70 | — (C5.3 already 1) | High |
| Valencia | 0.70 | 0.95 | ↑ (C5.1 + C5.2 already 1; C5.3 added) | Medium* |
| Gdańsk | 0.40 | 0.70 | ↑ (C5.3 added) | Medium* |
| Piraeus | 0.05 | 0.40 | ↑ (from 0/3; mathematically certain) | High |

\*Valencia/Gdańsk: awaiting confirmation against the C5 breakdown in the original case file (if C5.3 was already 1, no change).

**Resolution at revision (03.11.2026, K18):** The pending confirmations were resolved against the primary legal texts. Gdańsk: C5.3 was already 1 in the July coding, so the K14 uplift was unwarranted; the Act on Sea Ports and Harbours (1996) Art. 7 lists no environmental/community mandate (C5.1 = 0) → C5 reverts to **0.40**. Valencia: C5.1 (TRLPEMM environmental duty) and C5.2 (Consejo de Navegación y Puerto, TRLPEMM Art. 34) = 1, C5.3 = 1 → **0.95 confirmed**. Piraeus: C5.3 = 1 under K14 (EU at-berth 0.10 % sulphur limit, Directive (EU) 2016/802 Art. 7, binding since 1 January 2010) → **0.40 confirmed**.
