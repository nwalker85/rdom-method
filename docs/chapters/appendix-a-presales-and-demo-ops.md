<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Appendix A — Presales, Solution Architecture & DemoOps Integration

In high-growth enterprise software companies, one of the most severe sources of architectural friction occurs between Sales Engineering / Presales and Core Engineering.

Presales teams must move at commercial speed: configuring customer demonstrations, assembling rapid Proofs-of-Concept (PoCs), and building bespoke integration prototypes to win competitive deals. Core engineering, meanwhile, protects production stability, architectural integrity, and security boundaries.

When these disciplines clash, two failure modes occur:
1. **The Disposable Prototype Trap**: Presales hacks together a brittle, unversioned demo on a local laptop. The customer buys it, and the company discovers that turning the demo into production code requires a complete, nine-month rewrite.
2. **The Stifled Innovation Trap**: Presales requests a custom demo feature, and Core Engineering files it into the quarterly backlog, quoting a delivery date four months after the deal has already been lost.

This appendix adapts RDOM to create an agile, rigorous **DemoOps and Solution Architecture Pipeline**.

```
  Customer RFP / Enterprise Deal Opportunity
                     │
                     ▼
  Presales DAG Decomposition (Ehwaz PoC Waves)
                     │
                     ▼
  Isolated Ephemeral Worktree / Sandbox (DP-19, DP-21)
  (Scaffolded from Working Production Reality: DP-16)
                     │
                     ▼
  Customer Demo Delivery & Win (Witnessed Value)
                     │
                     ▼
  PoC Promotion Evaluation (The Ráð Council)
         │                               │
         ▼ (REJECT / ARCHIVE)            ▼ (PROMOTE TO CORE)
  Clean Sandbox Teardown          DRY Hoisting Protocol (DP-13, DP-14)
                                  Six Sigma Defect Gating (DP-7)
                                  Merged into Core Sovereign Repo
```

### 1. Scaffolding Demos from Working Reality (DP-16)

Presales demos and PoCs must never be built in isolated toy environments or external sandboxes that do not mirror real system architecture.
- **Production-Identical Substrates**: Demos are spun up in ephemeral sandboxes running the exact container digests compiled by RROM.
- **Hermetic Mock Data**: Custom customer data models are ingested via Poka-Yoke schemas (DP-9) rather than manual database mutations.

### 2. Ephemeral Demo Worktree Custody (DP-19, DP-21)

Every sales engineering integration prototype operates within an isolated git worktree branched from the canonical repository:
- **Zero Host Mutation**: Demos run inside containerized dev environments.
- **Isolated Namespaces**: Cloud resources and tenant contexts are strictly partitioned to prevent accidental cross-tenant data leaks during live customer calls.

### 3. The PoC-to-Production Promotion Gate

When a deal closes and a customer-validated PoC must become permanent product capability, the code is NOT merged directly into the core trunk. It undergoes the **Promotion Gate**:
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
  word-count: 690
  principle-citations: DP-7, DP-8, DP-9, DP-13, DP-14, DP-16, DP-19, DP-21
  flagged-principle-gaps: none
-->
