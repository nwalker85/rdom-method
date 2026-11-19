# Central Whiteboard - RDOM Editorial Directives, Invariants & Chapter Tracker

> **Notice to all writing subagents and editors**: This whiteboard is the authoritative editorial control plane for the *Ravenhelm Development Operations Methodology (RDOM)* manuscript (**Book II of the Ravenhelm Operations Methodology**). All subagents MUST strictly adhere to the invariants, directives, terminology, and structural rubrics declared below.

---

## 1. Core Invariants & Axioms

1. **Axiom of Concurrency (The Core Axiom)**:
   > *"Concurrency is earned through topological proof; quality is gated by verified green."*
   A plan is a directed acyclic graph ($G = (V, E)$), not a flat task list. Concurrency across engineers and agent slices is safe *only* within the same topological wave where tasks share no edge dependencies.

2. **Axiom of Precedence**:
   > *"The Graph Precedes the Plan."* (Principle **DP-1**)
   Any implementation without an explicit DAG of preconditions is unverified speculation.

3. **Axiom of Quality (Six Sigma Wave Boundary)**:
   > *"Wave $N+1$ never opens on a promise; only on verified green."* (Principle **DP-7**)
   Defects compound exponentially downstream. No wave boundary is crossed based on "it compiles locally," mock passes, or promissory notes.

4. **Axiom of Evidence**:
   > *"A deliverable is complete only when witnessed by the Triad of Proof."* (Principle **DP-11**)
   Every completion requires the Triad of Proof: deterministic passing automated tests with caller parity against live environments, updated operational documentation/runbooks, and an executable showcase/walkthrough.

5. **Axiom of Anti-Inventory (*Muda*)**:
   > *"Specifying code for Wave $N+2$ while Wave $N$ is incomplete is inventory waste."* (Principle **DP-6**)
   Granular TDD specifications are elaborated Just-In-Time (JIT) for the active wave only.

6. **Axiom of the Circuit Breaker**:
   > *"Never branch outward to build against an unfinished upstream dependency."* (Principle **DP-5**, **DP-12**)
   When a blocker or broken dependency occurs, workers pull the Andon Cord immediately. Speculative mocking of broken upstream interfaces is prohibited.

---

## 2. Voice, Tone & Terminology Boundaries

- **Tone**: Visceral, authoritative systems-engineering mindset (`STYLE-GUIDE.md`). Grounded in real production battle scars, industrial engineering (Toyota Production System, Shigeo Shingo's Poka-Yoke, Six Sigma, Goldratt's Critical Chain), and distributed systems.
- **Style**: Zero prose em-dashes (`—`); crime-scene openers on the bench; corpse of v1; high-low collision; bench imperatives; exact ledger numbers.
- **Terminology**: Zero Myth / Codex vocabulary leakage. Keep **The Ehwaz Doctrine (ᛖ)** as the canonical name for RDOM's Dependency-Wave Delivery. Use canonical ops terms for Chapters 04-07 (*The Topological Work Hierarchy*, *The Four Operational Contracts*, *The Four-Dimensional Engineering Scorecard*, *Quarterly Invariant Review*, *Monthly Architecture Review*, *Daily Fleet Sweep*).

---

## 3. Chapter Expansion Registry & Progress Tracker

| Chapter | Title | Target Principles | Words | Status |
|:---|:---|:---|:---:|:---:|
| **01** | What This Is and Why Modern Engineering Drifts | DP-1, DP-2, DP-3, DP-7, DP-12, DP-19 | 3,459 | COMPLETED |
| **02** | The Sovereign Triad: RLOM, RDOM, RROM | DP-1, DP-7, DP-11, DP-23 | 3,155 | COMPLETED |
| **03** | The 24 Numbered Principles | DP-1 through DP-24 | 4,233 | COMPLETED |
| **04** | The Topological Work Hierarchy: From Strategic Invariant to Atomic Commit | DP-1, DP-4, DP-11, DP-23 | 3,030 | COMPLETED |
| **05** | The Four Operational Contracts: Repository Law, Cadence, Architecture, and Fleet Custody | DP-18, DP-19, DP-20, DP-21 | 2,780 | COMPLETED |
| **06** | The Four-Dimensional Engineering Scorecard: Faster, Bigger, Cheaper, Effective | DP-4, DP-6, DP-7, DP-20 | 2,785 | COMPLETED |
| **07** | Ceremonies of Truth: Quarterly Invariant Review, Monthly Architecture Review, and the Daily Fleet Sweep | DP-1, DP-7, DP-12, DP-24 | 3,914 | COMPLETED |
| **08** | The Dependency DAG: Critical Path vs. Critical Chain | DP-1, DP-2, DP-4, DP-5 | 3,813 | COMPLETED |
| **09** | Topological Waves: Replacing the Two-Week Sprint | DP-2, DP-3, DP-7 | 3,444 | COMPLETED |
| **10** | Zero Collision by Construction: Multi-Agent Fleet Boundaries | DP-3, DP-10, DP-19 | 2,871 | COMPLETED |
| **11** | Just-In-Time Elaboration: Eradicating Inventory Waste (Muda) | DP-6, DP-8, DP-14 | 3,180 | COMPLETED |
| **12** | The DRY Hoisting Protocol: Anti-Snowflake Planning | DP-13, DP-14, DP-15, DP-16 | 3,169 | COMPLETED |
| **13** | Six Sigma Wave Boundary Gates: No Exit on a Promise | DP-7, DP-8, DP-10, DP-11 | 4,495 | COMPLETED |
| **14** | Poka-Yoke Interface Design & The Live System Rule | DP-9, DP-10, DP-18 | 3,624 | COMPLETED |
| **15** | The Andon Cord Protocol & Upstream-Jump Circuit Breakers | DP-5, DP-12 | 3,853 | COMPLETED |
| **16** | Workspace Custody: Bare Repositories and Disposable Worktrees | DP-19, DP-21, DP-22, DP-24 | 3,171 | COMPLETED |
| **17** | The Zero-Waste Context Substrate: Topological Priming vs. Directory Dumps | DP-20 | 2,893 | COMPLETED |
| **18** | The Sovereign Engineering Organization: Operating Human-Agent Fleets | DP-1..DP-24 | 3,486 | COMPLETED |
| **App A** | Presales, Solution Architecture & DemoOps Integration | DP-11, DP-18 | 2,752 | COMPLETED |
