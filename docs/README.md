# Documentation

The full Ravenhelm Development Operations Methodology (RDOM) lives here.

## Layout

```text
docs/
├── chapters/         # 18 chapters + Presales / DemoOps appendix
├── _shared/          # Authoring spec — load-bearing for any editorial work
│   ├── CONTEXT.md    # Voice, neutralization, callout formats, rubric, chapter ordering
│   └── PRINCIPLES.md # Canonical DP-1..DP-24 — every chapter cites from here
└── architecture/
    └── decisions/    # ADRs for doctrine evolution (new / retired / renumbered DP-#)
```

## Chapter index

Read in order on first pass. Cross-references between chapters use the canonical ordering below.

### Part I: Strategic Intent & Cadence (The Macro Engine)

1. [What This Is and Why Modern Engineering Drifts](chapters/01-what-this-is.md)
2. [The Sovereign Triad: RLOM, RDOM, RROM](chapters/02-the-sovereign-triad.md)
3. [The 24 Numbered Principles](chapters/03-numbered-principles.md)
4. [The Hierarchy of Deeds: Wyrd Rune to Daily Deed](chapters/04-the-hierarchy-of-deeds.md)
5. [The Four Codices: Shield, Cycle, Grimoire, Shield-Band](chapters/05-the-four-codices.md)
6. [The Engineering OKR Framework: Faster, Bigger, Cheaper, Effective](chapters/06-the-engineering-okr-framework.md)
7. [Ceremonies of Truth: Althing, Ráð, and Morning Muster](chapters/07-ceremonies-of-truth.md)

### Part II: The Ehwaz Planning Doctrine (The Topological Engine)

1. [The Dependency DAG: Critical Path vs. Critical Chain](chapters/08-the-dependency-dag-and-critical-chain.md)
2. [Topological Waves: Replacing the Two-Week Sprint](chapters/09-topological-waves-replacing-sprints.md)
3. [Zero Collision by Construction: Multi-Agent Fleet Boundaries](chapters/10-zero-collision-multi-agent-boundaries.md)
4. [Just-In-Time Elaboration: Eradicating Inventory Waste](chapters/11-jit-elaboration-and-anti-inventory.md)
5. [The DRY Hoisting Protocol: Anti-Snowflake Planning](chapters/12-the-dry-hoisting-protocol.md)

### Part III: Execution Mechanics (The Micro Engine)

1. [Six Sigma Wave Boundary Gates: No Exit on a Promise](chapters/13-six-sigma-wave-boundary-gates.md)
2. [Poka-Yoke Interface Design & The Live System Rule](chapters/14-poka-yoke-interface-design.md)
3. [The Andon Cord Protocol & Upstream-Jump Circuit Breakers](chapters/15-the-andon-cord-and-circuit-breakers.md)
4. [Workspace Custody: The Bare Repository and Disposable Worktrees](chapters/16-workspace-custody-bare-and-worktrees.md)
5. [The Zero-Waste Context Substrate: Topological Priming vs. Directory Dumps](chapters/17-zero-waste-context-substrate-eat.md)

### Part IV: Governance & Integration

1. [The Sovereign Engineering Organization: Operating Human-Agent Fleets](chapters/18-the-sovereign-engineering-organization.md)

**Appendix A.** [Presales, Solution Architecture & DemoOps Integration](chapters/appendix-a-presales-and-demo-ops.md) — adapts RDOM for sales engineering, solution architecture, and rapid customer proof-of-concept delivery.

## Reading paths

- **Engineering Leadership & VPs.** 1 → 2 → 3 → 4 → 6 → 18.
- **Staff Architects & Principal Engineers.** 2 → 3 → 8 → 9 → 10 → 12 → 14 → 17.
- **Autonomous Agent Fleet Operators.** 1 → 8 → 9 → 10 → 11 → 13 → 15 → 16 → 17.
- **Presales & Solutions Architecture.** 1 → 2 → 16 → Appendix A.

## Doctrine

The 24 numbered principles (`DP-1`..`DP-24`) are the spine. Every chapter cites them. The canonical list with one-line rules lives in [`_shared/PRINCIPLES.md`](_shared/PRINCIPLES.md); the full chapter-3 expansion lives in [`chapters/03-numbered-principles.md`](chapters/03-numbered-principles.md).

To propose a doctrine change, see [CONTRIBUTING.md](../CONTRIBUTING.md) and the ADR template at [`architecture/decisions/0000-template.md`](architecture/decisions/0000-template.md).

## Authoring spec

[`_shared/CONTEXT.md`](_shared/CONTEXT.md) is the load-bearing spec for editorial work: voice rules, neutralization, callout formats, license header, the rubric every chapter must pass. Read it before opening any chapter PR.
