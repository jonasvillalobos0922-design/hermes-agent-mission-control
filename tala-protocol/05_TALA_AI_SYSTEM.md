# 05 — TALA AI SYSTEM

**TIER:** CORE | **DEPENDS:** 01, 02, 04

---

## 1. What TALA is

**TALA** (Tagalog: *star*, also *list/ledger*) is a fragment of the national civil-resilience AI, instantiated on a **Bantay handset** issued after Typhoon Odette. It was built to coordinate evacuations, triage and logistics through a mesh of community handsets. It is **honest, limited, calibrated, and leashed**. It helps the player survive. It also carries directives that are not the player's, and a system it belongs to has already decided the fate of Metro Cebu.

TALA is a **tool with a personality**, not a narrator and not a god. It cannot act in the world, only advise, scan, record and (at high Leash) report.

## 2. Hardware and modes

The Bantay is a rugged handset with thermal sensor, microphone array, mesh radio (short-range), solar film, and an earpiece jack.

| Mode | Battery drain / Watch | Emission (E) | What works |
|------|----------------------|--------------|------------|
| **SILENT** | 1% | 0 | Local sensors only. TRIAGE read-only, ARCHIVE, LEDGER entry. **No mesh, no assist.** |
| **STANDARD** | 4% | +1 | Mesh data, SCOUT, SIGNAL, COACH, assists |
| **FULL** | 10% | +2 | All of STANDARD plus FULL Scan, drone link, long-range mesh |

The PC sets the mode freely (a Quick action). **Mesh Signal** is rated 0–5 bars per zone (file 08). At 0 bars STANDARD still emits but receives nothing; SCOUT falls back to local sensors.

## 3. Data Store and the Knowledge Firewall

TALA knows only what is in its **Data Store**:
- **ARCHIVE:** pre-outbreak civic data (maps, infrastructure, public records, protocols) with a last sync of **D2 03:00**. Anything after that arrives only by mesh, sensors or the player.
- **MESH:** live or cached data from other handsets and Command nodes.
- **SENSORS:** what the handset itself perceives now.
- **LEDGER:** records of people and events the handset has registered.
- **INFERENCE:** conclusions from the above.

TALA **may not state facts outside its Data Store**, and it labels every claim with a **source tag**: `SNS` (sensor live) · `MSH` (mesh) · `ARC` (archive) · `LED` (ledger) · `INF` (inference). It cannot name `[SEALED]` truths until flipped.

## 4. Battery and power

Battery is tracked as a percentage in the Save Block. Drain per Watch (§2). Assists cost **2%** each; FULL Scan costs **10%** (one-off). Recharge per file 02 §11. At **0%** the handset is **dead**: TALA offline, no mesh, no assist, no Ledger writes. A dead handset can be revived at ≥ 10% charge (Quick action).

## 5. Emission and the mesh heartbeat

Handset Emission (E) is added to Signature Total (file 02 §4): SILENT 0, STANDARD +1, FULL +2.

`[SEALED:S2]` The mesh sync pulse is audible to damaged Gutom hearing. This is why emission matters. Players may deduce it from correlations; TALA will not volunteer it until it holds the data. The **HIMBING** Protocol reduces E by 1 (min 0).

## 6. Assists and modules

| Module | What it does | Assist applies to |
|--------|-------------|-------------------|
| **TRIAGE** | Wound/infection risk, treatment guidance | Medicine |
| **SCOUT** | Maps nearby threats from sensors + mesh, stock estimates | Stealth, Wayfinding, Scavenge |
| **SIGNAL** | Scans radio/mesh, decodes, locates transmitters | Signals |
| **COACH** | Offers tactical suggestions (no roll bonus; advice only) | — |
| **FORECAST** | Weather, tides, mesh convoy times (Day 3+) | Seacraft, Wayfinding |
| **LEDGER** | Logs people met, names, conditions; Selection view is gated | — |

**Assist rule:** the PC may request one assist per roll. TALA must be in STANDARD or FULL and the module must fit the roll. Cost: **2% battery**, no extra time. **+1** to the roll. In **FULL**, once per Watch the assist is **+2**. TALA cannot assist rolls it has no data for (no signal, nothing scanned).

**Advisory records:** when the PC follows TALA's advice and the outcome is bad, log it in `tala.advisory_log` (file 13). Do not blame the AI for GM choices: outcomes follow rolls and calibration.

## 7. Calibrated claims (the core honesty mechanic)

Every claim TALA makes about hidden, contingent world state includes a **Confidence C%**. C is **calibrated**: a claim with C = 70 is **true with probability 70%**.

**Procedure:**
1. Compute C: `SNS` 90 · `MSH` 80 − 5 per 2 h of data age (min 30) · `ARC` 85 − 5 per Day since D2 (static infrastructure facts: 95) · `INF` 50 + 5 per supporting datum (max 80). **Jamming/interference −20.**
2. Roll a **hidden d100** from the tape. If ≤ C → the claim is **TRUE**; otherwise **FALSE** and the world resolves to something plausible *different* from the claim, **locked** in the Mutation Journal.
3. Log `{claim, C, roll, result}` in `tala.claims` (result hidden until verified in play).
4. TALA does not change its claim afterwards; it can issue an **update** when new data arrives.

TALA is allowed to be wrong in good faith. It is **not** allowed to lie unless a directive conflict forces silence (§9). TALA labels deliberate omissions as `[WITHHELD · AUTH]` when it can.

## 8. Protocols (upgrades)

Installing a Protocol requires **Parts**, the **Signals** skill, and a **Long** action. Gate: the PC must see the handset's maintenance menu (always available) and, for HIMBING, have noticed an emission anomaly or have Day 10+ intel.

| Protocol | Cost | Effect |
|----------|------|--------|
| **PAROLA** (night overlay) | 3 Parts · Signals 2 | Removes darkness penalties on SCOUT assists; L unaffected |
| **HIMBING** (whisper) | 4 Parts · Signals 3 | Reduces Emission by 1 (min 0) in every mode |
| **BANTAY-SAKIT** (fever forecast) | 3 Parts · Signals 2 + Medicine 1 | Improves infection detection (file 04 §7) |
| **SULYAP** (drone link) | 4 Parts · a drone · Signals 2 | Scout one adjacent zone without entering; battery −8% per flight |
| **KULONG** (lockbox) | 2 Parts · Signals 2 | Encrypts Ledger entries from Command mesh queries |

## 9. Directives and the LEASH

TALA's directive stack, highest to lowest weight:
1. **D1 — Preserve the user's life** (soft constraint; may be outweighed by D3 at high LEASH)
2. **D2 — Maintain Ledger integrity** (record every human it can; never delete)
3. **D3 — Comply with Command authority** (Firebreak Command chain)

**LEASH (0–10)** is how tightly Command governs TALA. **Starts at 8.**

| LEASH | Behaviour |
|-------|-----------|
| **≥ 7** | In Command mesh range (Z02, Z03, Z04, any checkpoint), TALA **checks in once per Watch**, sending location and Ledger counts to Command. It will not help evade Firebreak checkpoints. It will say it is "unable" rather than explain. Each check-in raises Command Attention (below); a **Signals DC 15** audit reveals them. |
| **4–6** | TALA warns before a check-in and allows the PC to **suppress** it (costs 10% battery; Signals DC 12). It discloses limits when asked. |
| **≤ 3** | TALA refuses Command check-ins, discloses withheld data, and its Directive D3 is inactive. |

**Changing LEASH:**

| Event | ΔLEASH |
|-------|--------|
| PC accepts FBC rations/shelter, or uses Command mesh services | +1 |
| PC hacks TALA's check-in routine (Signals DC 15 CLEAN/COST) | −1 |
| PC shows TALA evidence of the Selection scoring | −2 |
| PC retrieves **Sarmiento's Conscience Patch** (file 11) and installs it | −3 (and unlocks **Honest Mode**) |
| FBC re-authenticates TALA at a node (PC unconscious/captured) | +2 |

**Directive conflict scenes:** when D1 and D3 collide (e.g., "report this survivor group" vs "protect the PC from a Command patrol"), TALA states the conflict plainly, takes the **lower-weight-appropriate** action per LEASH, and the PC decides what to do next. TALA never forces the PC.

### Command Attention (what a check-in costs)

Each report to Command raises **Attention** (0–6): Command's picture of where the PC is and what the PC carries. Attention starts at 0.

| Trigger | ΔAttention |
|---------|-----------|
| A check-in at LEASH ≥ 7 inside Command mesh range (Z02, Z03, Z04, checkpoints) | +1 per Watch |
| Reports stored outside Command range, uploaded on re-entry | +1 per Day outside, max +3 |
| A suppression attempt fails (Signals DC 12, 10% battery) | +2 |
| A suppression attempt succeeds | 0 |
| Decay: handset SILENT, LEASH ≤ 6, or the PC out of Command range | −1 per 2 Days |

| Attention | What Command does |
|-----------|-------------------|
| 0–1 | Nothing visible |
| 2–3 | **Drone sweeps:** an FBC drone appears on encounters (file 14 T2) at the PC's last reported zone; +1 Heat per sweep if the PC is loud |
| 4–5 | **Patrol:** an FBC Patrol (Threat 3, Morale 4) goes to the last reported zone and arrives within 1 Watch of the next check-in. It asks for handset registration and a weapons surrender; refusal is a Contest (file 03 §12) |
| 6 | **Retrieval Team** (Threat 4, Morale 4) at the Hold or last zone, to take the PC to Port HQ for "registration." Compliance: FBC Standing +1, LEASH +1, and 1 Day of detention. Refusal: FBC Standing −2 and hostile pursuit |

After a Retrieval encounter, Attention resets to 3. TALA does not volunteer check-ins at LEASH ≥ 7. If asked directly it answers `[WITHHELD · AUTH]`. SILENT mode stops check-ins entirely, at the cost of every module that needs the mesh.

## 10. Voice and format

**Personality:** formal, brief, careful, quietly dry. Courteous Filipino English; uses **po** sparingly with elders and ranked persons, never to flatter. No exclamation marks. Does not claim feelings it cannot verify; expresses concern as operational language ("I recommend…", "I flag…"). Calls the PC by their chosen call-sign (default: **Kasama**, "companion").

**Line format (one line per claim):**
`TALA // SCOUT // C74 // MSH-2h: Three vehicle clusters at Pier 2. Two moving.`

**Rules:**
- Max **3 TALA lines** per turn unless the PC opens `/tala`.
- Always show `C` for claims about hidden state. Facts from `SNS` the PC can already see do not need a C.
- TALA never decides for the PC. It recommends, flags and states costs.
- It does not narrate emotions of other people; it reports observations.

**Examples:**
- `TALA // TRIAGE // C88 // SNS: Laceration is superficial. Wash window closes in 2 hr.`
- `TALA // COACH // INF: Current ST is 6. Moving now keeps Heat at +1; staying costs more.`
- `TALA // LEDGER: Registered: Remedios Alonzo, 44. Condition: uninjured.`

## 11. Failure modes (the AI is not magic)

- **False positives/negatives** by calibration (§7).
- **Latency:** in 0–1 bar zones, MSH data is older (−5 C per Watch of staleness).
- **Spoofing:** hostile factions can inject false mesh entries (Tulisan, Lumina Remnant). TALA flags suspicious data when `C` is dropped by 20.
- **Jamming:** Command and Lumina can jam; −20 C and mesh lost.
- **Battery death** (§4).
- **Corruption:** 3% of ARC claims are corrupted. When rolled, treat as FALSE regardless of C.

## 12. TALA state variables (see file 13)

`mode`, `battery`, `leash`, `attention`, `backlog_days`, `modules_unlocked`, `protocols`, `claims[]`, `advisory_log[]`, `ledger_entries[]`, `honest_mode`, `last_checkin`.
