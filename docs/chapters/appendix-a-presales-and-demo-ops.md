<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Appendix A — Presales, Solution Architecture & DemoOps Integration

In high-growth enterprise software companies, one of the most severe sources of architectural friction occurs between Sales Engineering / Presales and Core Engineering.

Presales teams must move at commercial speed: configuring customer demonstrations, assembling rapid Proofs-of-Concept (PoCs), and building bespoke integration prototypes to win competitive deals. Core engineering, meanwhile, protects production stability, architectural integrity, and security boundaries.

When these disciplines clash, two failure modes occur:
1. **The Disposable Prototype Trap**: Presales hacks together a brittle, unversioned demo on a local laptop. The customer buys it, and the company discovers that turning the demo into production code requires a complete, nine-month rewrite.
2. **The Stifled Innovation Trap**: Presales requests a custom demo feature, and Core Engineering files it into the quarterly backlog, quoting a delivery date four months after the deal has already been lost.

This appendix adapts RDOM to create an agile, rigorous **DemoOps and Solution Architecture Pipeline**, establishing that showcases and demonstrations are first-class engineering deliverables and the empirical foundation for **User Acceptance Testing (UAT)**.

```
  Customer RFP / Enterprise Deal Opportunity / Feature UAT Gate
                             │
                             ▼
  Presales DAG Decomposition (Ehwaz PoC Waves)
                             │
                             ▼
  Demo Factory Composition (Project Factory ADR 002/003)
  (Declared Profile of Official SDKs & Production Substrates: DP-16)
                             │
                             ▼
  Isolated Ephemeral Worktree / Sandbox (DP-19, DP-21)
                             │
                             ▼
  Executable Showcase / Demonstration Deed (DP-11)
  * Validates Customer Value & Closes Enterprise Deal
  * Serves as Witnessed Artifact for RLOM UAT Sign-Off (P-6)
                             │
                             ▼
  PoC Promotion Evaluation (The Ráð Council)
         │                                       │
         ▼ (REJECT / TEARDOWN)                   ▼ (PROMOTE TO CORE)
  Clean Sandbox Teardown (DP-24)          DRY Hoisting Protocol (DP-13, DP-14)
                                          Six Sigma Defect Gating (DP-7)
                                          Merged into Core Sovereign Repo
```

### 1. The Demo Factory Composition Contract (ADR 002 & ADR 003)

In Project Factory (ADRs 002 and 003), Ravenhelm ratified that demos, PoCs, and showcases are **declared compositions of official platform SDKs and existing production surfaces**—never independent shadow runtimes, toy registries, or throwaway UI forks.

- **Compositions, Not Shadow Platforms**: A demo defines a composition profile linking existing library surfaces by ID, declaring its economic job, domain boundary, and external action surfaces.
- **No Synthetic Illusions**: Merely generating code or showing a trace does not prove an integration exists. Mutating operations (e.g., placing outbound calls, persisting records to CRM, dispatching webhooks) must use bounded SDK contracts that emit observable events and cryptographic receipts.
- **Scaffolding from Working Reality (DP-16)**: Demos are spun up in ephemeral sandboxes running the exact container digests and package versions compiled by RROM.

### 2. Showcases as the Empirical Engine of UAT (RLOM P-6)

In RDOM, a feature release is never complete when functional code simply compiles and passes unit tests. A feature release is only complete when it includes an executable **Showcase Demonstration Deed** (DP-11).

This showcase is the physical bridge to RLOM:
- **Witnessed UAT**: Product managers, sales engineers, and customer stakeholders conduct User Acceptance Testing by executing or observing the showcase against the live running system (DP-10).
- **Zero Ambiguity**: UAT is not a subjective conversation about whether a Jira ticket was interpreted correctly; it is an empirical inspection of the running showcase against the original acceptance criteria.
- **Customer Collateral**: The same showcase used for internal UAT becomes the verifiable demonstration artifact presented to prospective enterprise customers.

### 3. Ephemeral Demo Worktree Custody (DP-19, DP-21)

Every sales engineering integration prototype operates within an isolated git worktree branched from the canonical repository:
- **Zero Host Mutation**: Demos run inside containerized dev environments.
- **Isolated Namespaces**: Cloud resources and tenant contexts are strictly partitioned to prevent accidental cross-tenant data leaks during live customer calls.

### 4. The PoC-to-Production Promotion Gate

When an enterprise deal closes and a customer-validated PoC must become permanent product capability, the code is NOT merged directly into the core trunk. It undergoes the **Promotion Gate**:
1. **Hoisting Analysis (DP-13, DP-14)**: The Ráð inspects the prototype to identify reusable primitives versus customer-specific customizations.
2. **Refactoring to Invariants**: The code is refactored from prototype-grade to production-grade: adding exhaustive unit tests (DP-8), type safety (DP-9), and telemetry instrumentation.
3. **Six Sigma Gate Verification (DP-7)**: The promoted pull request must pass all standard CI linting, security scanning, and integration test suites before merging into `main`.

> **Augmentation Surface — Automated PoC Scaffolding**
>
> Where an agent layer transforms this practice: an agent consumes enterprise customer API specifications and sample datasets, automatically generating the OpenAPI contracts, mock endpoints, and tailored demo environments in minutes.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 840
  principle-citations: DP-7, DP-8, DP-9, DP-10, DP-11, DP-13, DP-14, DP-16, DP-19, DP-21, DP-24
  flagged-principle-gaps: none
-->
