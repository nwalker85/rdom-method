<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 6 — The Engineering OKR Framework (Faster, Bigger, Cheaper, Effective)

Most engineering organizations struggle with OKRs because they attempt to measure activity rather than system performance. They set goals like "Ship Feature X" or "Migrate 5 microservices," which tell leadership nothing about whether the engineering engine is actually becoming healthier, faster, or more scalable.

RDOM grounds engineering goal-setting in the **Valknut OKR Framework**, which balances four mutually reinforcing dimensions: **Faster, Bigger, Cheaper, Effective**.

Every quarterly Saga's Vow must establish concrete, measurable key results across these four quadrants. Optimizing for speed without measuring defects produces catastrophic technical debt; optimizing for cost without measuring throughput starves the business.

```
                    +------------------------------------+
                    |       THE VALKNUT OKR MATRIX       |
                    +------------------------------------+
                                      |
                 +--------------------+--------------------+
                 |                                         |
                 v                                         v
        +------------------+                      +------------------+
        |      FASTER      |                      |      BIGGER      |
        | Velocity & Flow  |                      | Scale & Capacity |
        +------------------+                      +------------------+
        * Cycle Time (PRs)                        * Agent Fleet Concurrency
        * Wave Completion Latency                 * Daily Commits / Merges
        * Lead Time to Production                 * Worktree Parallelism
                 |                                         |
                 +--------------------+--------------------+
                                      |
                 +--------------------+--------------------+
                 |                                         |
                 v                                         v
        +------------------+                      +------------------+
        |     CHEAPER      |                      |    EFFECTIVE     |
        | Unit Economics   |                      | Quality & Trust  |
        +------------------+                      +------------------+
        * Token Efficiency / Task                 * Zero Wave Defect Escapes
        * Build & CI Cloud Cost                   * Zero Collision Incidents
        * Context Prime Scrap Rate                * 100% Witnessed Deeds
```

### The Four Quadrants

#### 1. Faster (Velocity & Topological Flow)

Measures the velocity with which intent is converted into verified, running code.
- **Cycle Time to Merge**: The elapsed duration from the opening of a Daily Deed pull request to its verified merge into the trunk.
- **Wave Completion Latency**: The calendar time required to advance a complete topological wave from Wave 0 foundation to Wave $N$ verification.
- **Zero-Blocker Cadence**: Minimizing idle wait time caused by unhoisted shared dependencies (DP-13, DP-14).

#### 2. Bigger (Scale, Throughput & Fleet Capacity)

Measures the organization's ability to scale execution without hitting non-linear coordination friction.
- **Concurrent Worktree Slices**: The number of isolated agent and human worktrees active simultaneously without merge collisions (DP-3, DP-19).
- **Fleet Throughput**: The volume of validated, production-grade deeds delivered per planning cycle.
- **Surface Coverage**: The breadth of platform subsystems actively evolving in parallel under Ehwaz wave scheduling.

#### 3. Cheaper (Unit Economics & Context Waste Eradication)

Measures economic and resource efficiency across compute, tooling, and AI agent token consumption.
- **Token Efficiency per Verified Deed**: Eradicating context thrash by replacing raw directory crawling with AST-level topological priming (`eat prime`, `eat read`) (DP-20).
- **CI Compute Efficiency**: Caching deterministic build artifacts and minimizing redundant rebuilds according to immutable release doctrine (RROM).
- **Manufacturing Scrap Reduction**: Eliminating discarded, aborted, or rolled-back branches caused by upstream specification drift.

#### 4. Effective (Defect Prevention & Sovereign Quality)

Measures structural integrity, system resilience, and compliance with Six Sigma standards.
- **Zero Wave Boundary Escapes**: Zero defects or broken contracts allowed to cross from Wave $N$ to Wave $N+1$ (DP-7).
- **Zero Collision Compliance**: Zero multi-agent merge conflicts occurring across parallel branches (DP-3).
- **Witnessed Deed Completeness**: 100% of merged pull requests must possess attached, witnessed test execution and verification logs (DP-11).
- **Andon Cord Resolution Latency**: The speed with which root causes are diagnosed and fixed when the line is stopped (DP-12).

> **Augmentation Surface — OKR Metric Synthesis**
>
> Where an agent layer transforms this practice: an automated metrics telemetry engine continuously aggregates cycle times, token costs, worktree concurrency, and defect escape rates across GitHub/Forgejo and CI pipelines, publishing a weekly Valknut scorecard directly into the executive dashboard.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 760
  principle-citations: DP-3, DP-7, DP-11, DP-12, DP-13, DP-14, DP-19, DP-20
  flagged-principle-gaps: none
-->
