<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 5 — The Four Codices (Shield, Cycle, Grimoire, Shield-Band)

In the Valknut doctrine, an engineering organization cannot function on informal rules, Slack folklore, or transient memory. Governance must be tangible, written, and enforceable by both human engineers and automated agents.

RDOM organizes engineering institutional memory into **The Four Codices**. Each codex governs a distinct aspect of organizational reality, providing immutable guardrails for execution.

```
                  +-----------------------------------+
                  |       THE FOUR CODICES            |
                  +-----------------------------------+
                   /          |             |        \
                  /           |             |         \
                 v            v             v          v
          +------------+ +------------+ +------------+ +------------+
          |  SKJÖLDR   | |VERÐRHRINGR | |GALDRARITAR | | SKULDALIÐ  |
          | The Shield | | The Cycle  | |The Grimoire| | Shield-Band|
          +------------+ +------------+ +------------+ +------------+
          Boundaries,    OKRs, Cadence  Daily Runbooks Peer Review,
          Contracts,     & Topological  & Engineering  Witnessing,
          Architecture   Wave Windows   Standards      Defect Gates
```

### 1. Skjöldr (The Shield — Boundaries & Architecture)

The Skjöldr codex defines the boundaries of the system. It governs architecture, service interfaces, API contracts, and decision records.
- **Contents**: Architecture Decision Records (ADRs), interface schemas (OpenAPI, Protobuf), system topology diagrams, and security boundaries.
- **Rule**: No service boundary may be altered, and no cross-cutting dependency may be introduced, without a formal update to Skjöldr.
- **Principle Binding**: Governs Poka-Yoke Interface Design (DP-9) and Planning-Time DRY Refactoring (DP-13).

### 2. Verðrhringr (The Cycle — Cadence & OKRs)

The Verðrhringr codex governs time, cadence, and objective delivery. It tracks the progress of the active Saga's Vow and the sequencing of topological waves.
- **Contents**: Quarterly engineering OKR scorecards (Faster, Bigger, Cheaper, Effective), wave dependency DAGs, capacity buffers, and milestone schedules.
- **Rule**: Verðrhringr replaces timeboxed sprint backlogs. It dictates when waves open and close based on verifiable topological progression.
- **Principle Binding**: Governs Topological Wave Execution (DP-2) and The Critical Chain Floor (DP-4).

### 3. Galdraritar (The Grimoire — Daily Practice & Runbooks)

The Galdraritar codex is the operational repository of engineering recipes, standard operating procedures (SOPs), and runbooks.
- **Contents**: Repository onboarding guides, local development setup, debugging playbooks, production deployment runbooks, and disaster recovery procedures.
- **Rule**: If a procedure must be executed more than once, it must be codified in Galdraritar. Ambient, unrecorded execution folklore is strictly forbidden.
- **Principle Binding**: Governs Scaffolding from Working Reality (DP-16) and Shared Substrate Invariance (DP-17).

### 4. Skuldalið (The Shield-Band — Witnessing & Defect Gates)

The Skuldalið codex defines the circle of verification and mutual accountability. It governs code review standards, test coverage thresholds, and deployment sign-offs.
- **Contents**: Pull request review guidelines, automated CI gate definitions, static analysis rules, security scan thresholds, and verification rubrics.
- **Rule**: Code is never merged without an unbroken chain of custody witnessed by the Shield-Band. Neither human engineers nor AI agents may bypass the verification criteria recorded in Skuldalið.
- **Principle Binding**: Governs Verified Green Precedes Promotion (DP-7) and The PR Boundary (DP-23).

> **Augmentation Surface — Codex Invariant Auditing**
>
> Where an agent layer transforms this practice: automated linters and semantic inspectors continuously evaluate incoming pull requests against the Four Codices, ensuring that interface changes obey Skjöldr, milestone milestones match Verðrhringr, tooling follows Galdraritar, and test evidence satisfies Skuldalið.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 670
  principle-citations: DP-2, DP-4, DP-7, DP-9, DP-13, DP-16, DP-17, DP-23
  flagged-principle-gaps: none
-->
