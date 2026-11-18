# Authoring Context & Style Guide - RDOM

This specification defines the voice, conventions, and quality criteria for all chapters of the **Ravenhelm Development Operations Methodology (RDOM)**, **Book II of the Ravenhelm Operations Methodology** (*The Sovereign Engineering Trilogy: RLOM · RDOM · RROM*).

---

## 1. Voice, Posture, and Mechanics

Every chapter follows the unified Ravenhelm style register (`STYLE-GUIDE.md`):

- **Zero prose em-dashes (`—`).** Replace every prose em-dash with `;` (when joining two weighted clauses) or ` - ` (spaced hyphen for parentheticals/asides).
- **Start at the crime scene on the bench, never in the lecture hall.** Kill throat-clearing openers (*"In modern software engineering..."*, *"For decades, organizations have..."*). Open with the broken artifact on the workbench, the exact date, the exact metric, the command that lied, or the production scar.
- **Show the corpse of v1 ("the wrong one we built first").** Never present a principle as if it fell from the sky whole. Show the naive v1 built first, the failure mode that killed it under load, and the physical constraint that forced the real design.
- **High-low collision (cathedral math + shop-floor nouns).** Collide exact technical primitives (`git merge-tree --write-tree`, `concurrencyPolicy: Forbid`, `sha256`, `DAG topological sort`, `Granularity::Exact`) with blunt physical nouns (`corpse`, `hinge`, `wreckage`, `receipt`, `anvil`, `blindfold`).
- **Bench imperatives over brochure descriptions.** Write second-person shop-floor recipes and direct cause-and-effect, never third-person brochure prose.
- **Rhythm: long-build verse -> short-knife breakdown.** Accumulate evidence in multi-clause paragraphs, then land the verdict in a knife sentence of 5 words or fewer inside the paragraph.
- **Repetition must carry a receipt.** Never repeat a phrase for rhetorical rhythm alone; the second occurrence must escalate the paperwork.
- **Exact numbers always.** Cite exact ledger figures (`287,838 of 287,879 webhooks`, `215 of 217 repos`, `9 minutes 23 seconds`, `81 dangling tips and 15 unpushed branches`), never vague approximations.
- **Terminology boundaries.** Personal codex / myth terms (*Wyrd Rune*, *Saga's Vow*, *Althing*, *Ráð*, *Four Codices*, *Codex of the Shield/Cycle/Grimoire/Band*, *Valknut OKR*, *Jarl*, *Thegn*, *Skald*, *Berserkr*) never leak into ops docs. Keep **The Ehwaz Doctrine (ᛖ)** as the canonical name for RDOM's Dependency-Wave Delivery. Real running estate systems (`Bifrost`, `Heimdall`, `Vitki`, `Ullr`/`Yager`, `Idunn`, `Doom`/`Doomcourt`, `EAT`, `Snotra`, `Harbor`, `OpenBao`, `Valkyrie`, `Norns`) are valid architectural receipts when introduced with their functional role.

---

## 2. Structure of Each Chapter

Each chapter markdown file in `docs/chapters/` follows this structure:

1. **License Header Block**:

   ```markdown
   <!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
   <!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->
   ```

2. **Opening Crime Scene**: The concrete engineering failure mode on the bench that occurs when this discipline is missing, including the corpse of v1.
3. **The Theoretical & Mechanical Foundation**: Formal mechanics, mathematical formulations, and architectural diagrams (Mermaid or ASCII).
4. **Operational Mechanics & Step-by-Step Protocols**: Concrete implementation recipes, algorithms, state machines, policy gates, and tabular rules.
5. **Concrete Anti-Patterns & Defect Escapes**: How teams and agent fleets fail in practice.
6. **Upstream & Downstream Integration (The Sovereign Triad)**: Explicit interface contracts connecting upstream to Book I (RLOM) and downstream to Book III (RROM).
7. **Augmentation Surface Callout & `<!-- RUBRIC_CHECK -->` Block**: Validating chapter completeness, word count, and principle citations (`DP-1`..`DP-24`).

---

## 3. Chapter Index

The book comprises 18 core chapters grouped into four parts, plus Appendix A:

### Part I: Strategic Intent & Cadence (The Macro Engine)

- **Chapter 01**: What This Is and Why Modern Engineering Drifts
- **Chapter 02**: The Sovereign Triad (RLOM, RDOM, RROM)
- **Chapter 03**: The 24 Numbered Principles
- **Chapter 04**: The Topological Work Hierarchy: From Strategic Invariant to Atomic Commit
- **Chapter 05**: The Four Operational Contracts: Repository Law, Cadence, Architecture, and Fleet Custody
- **Chapter 06**: The Four-Dimensional Engineering Scorecard: Faster, Bigger, Cheaper, Effective
- **Chapter 07**: Ceremonies of Truth: Quarterly Invariant Review, Monthly Architecture Review, and the Daily Fleet Sweep

### Part II: The Ehwaz Planning Doctrine (The Topological Engine)

- **Chapter 08**: The Dependency DAG: Critical Path vs. Critical Chain
- **Chapter 09**: Topological Waves: Replacing the Two-Week Sprint
- **Chapter 10**: Zero Collision by Construction: Multi-Agent Fleet Boundaries
- **Chapter 11**: Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)
- **Chapter 12**: The DRY Hoisting Protocol: Anti-Snowflake Planning

### Part III: Execution Mechanics (The Micro Engine)

- **Chapter 13**: Six Sigma Wave Boundary Gates: No Exit on a Promise
- **Chapter 14**: Poka-Yoke Interface Design & The Live System Rule
- **Chapter 15**: The Andon Cord Protocol & Upstream-Jump Circuit Breakers
- **Chapter 16**: Workspace Custody: Bare Repositories and Disposable Worktrees
- **Chapter 17**: The Zero-Waste Context Substrate: Topological Priming vs. Directory Dumps

### Part IV: Governance & Integration

- **Chapter 18**: The Sovereign Engineering Organization: Operating Human-Agent Fleets
- **Appendix A**: Presales, Solution Architecture & DemoOps Integration
