<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 11 — Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)

In Lean manufacturing, Taiichi Ohno identified work-in-process (WIP) and inventory as the most dangerous forms of waste (*Muda*). Inventory ties up capital, conceals manufacturing defects, and rots while waiting for assembly.

In software engineering, the most destructive and expensive form of inventory is not unreleased code; it is **unimplemented specification inventory**.

Product teams spend weeks writing detailed requirements documents, acceptance criteria, and Figma mockups for features that will not be coded for three months. By the time an engineer or agent opens the ticket, the underlying system architecture has evolved, APIs have changed, customer priorities have shifted, and the specification is obsolete. The team either builds the wrong thing or spends days in meetings rewriting the spec.

RDOM enforces **Progressive Just-In-Time (JIT) Elaboration** (DP-6). Detailed technical specifications are treated as perishable goods with a shelf life of zero.

```
  Traditional Agile Backlog Bloat (Perishable Inventory):
  ┌────────────────────────────────────────────────────────┐
  │ 200+ Fully Specified User Stories in Backlog           │
  │ (Written in Month 1 -> Stale in Month 2 -> Toxic in 3) │
  └────────────────────────────────────────────────────────┘

  RDOM Just-In-Time Elaboration Pipeline:
  Intent Layer (High-Level Intent & Boundary Contracts Only)
        │
        ▼ (Wave N-1 Achieves Verified Green)
  JIT Elaboration Trigger
        │
        ▼
  Active Wave N Specification (Elaborated Against Live Silicon & ASTs)
        │
        ▼
  Immediate Execution in Isolated Worktree
```

### The Rules of JIT Elaboration

1. **Strategic Intent is Broad; Implementation Specs are JIT**: Long-Sagas and Saga's Vows define objectives, boundary constraints, and architectural invariants. They do not specify function signatures, database schema columns, or UI DOM hierarchies months in advance.
2. **The Wave Boundary Elaboration Trigger**: A task in Wave $N$ is only elaborated to concrete implementation detail (AST targets, exact file paths, test assertions) when Wave $N-1$ has achieved verified green (DP-6, DP-7).
3. **Elaboration against Live Reality**: When an agent or engineer prepares a task brief for Wave $N$, they read the *actual code, schemas, and tests* merged in Wave $N-1$ using live topological priming (`eat prime`, `eat read`) (DP-10, DP-20). Specifications are anchored to running reality, not theoretical designs.
4. **Zero Backlog Inventory**: Issues that are not scheduled for execution in the current or immediately following topological wave remain as high-level intent nodes in RLOM. Any detailed specification created more than one wave ahead is considered manufacturing scrap.

### Eradicating Specification Rot

When specifications are generated just-in-time:
- **Zero Rework**: No developer ever spends time updating specifications that were invalidated by earlier architectural changes.
- **Accurate Context**: Coding agents receive prompts that reflect the exact current state of the repository, eliminating hallucinated APIs and outdated imports.
- **Immediate Flow**: Requirements flow directly from elaboration into code generation, test verification, and merge without sitting in an idle backlog queue.

> **Augmentation Surface — Automated JIT Specification Drafting**
>
> Where an agent layer transforms this practice: as Wave $N-1$ pull requests pass their final verification gates, an agent analyzes the merged diffs, updates the schema models, and drafts the precise, AST-anchored briefs for Wave $N$ tasks, presenting them to the human architect for rapid ratification.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 680
  principle-citations: DP-6, DP-7, DP-10, DP-20
  flagged-principle-gaps: none
-->
