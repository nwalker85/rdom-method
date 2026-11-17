# Ravenhelm Development Operations Methodology (RDOM)

> A tiered, sovereign operating methodology for software development, agentic concurrency, and engineering cadence — installable across engineering teams, grounded in twenty-four numbered principles, and bridging executive OKRs to high-concurrency autonomous agent execution.

Authored by **[Nathan Walker](https://nwalker.cc)** · Published by **[Ravenhelm LLC](https://ravenhelm.co)**  
Current Release: **v1.0.0** · [PDF (Light)](RDOM-v1.0.0.pdf) · [PDF (Dark)](RDOM-v1.0.0-dark.pdf) · [Changelog](CHANGELOG.md) · [Principles](docs/_shared/PRINCIPLES.md) · [Start Reading →](docs/chapters/01-what-this-is.md)

---

## What Problem This Solves

You opened your repository or issue tracker this morning. Your engineering organization—human engineers and autonomous AI agent swarms alike—is moving furiously, but the results are chaotic:

- **The Sprint Delusion**: Work is arbitrarily batched into 2-week sprints designed for human calendar coordination. Agents either sit idle waiting for retro ceremonies or blaze ahead unguided, producing speculative code that drifts from the quarterly mandate.
- **The Prompting Fallacy**: Agents are unleashed with flat prompt checklists. They edit overlapping files simultaneously, generate git merge collisions, and hallucinate snowflake implementations across slices rather than hoisting reusable libraries.
- **Inventory Waste (*Muda*)**: Agents spend tens of thousands of tokens elaborating detailed code for tasks three steps ahead of an unverified upstream dependency, only to throw it away when the producer interface changes.
- **Defect Escapes**: Tasks are declared "Done" on a promise or an isolated unit mock, poisoning `main` and breaking staging environments.
- **OKR Disconnect**: Executive OKRs live in decorative quarterly slides, entirely divorced from the actual commits, PRs, and PRDs flowing through the engineering pipeline.

The **Ravenhelm Development Operations Methodology (RDOM)** permanently resolves this breakdown. It forms the central pillar of the **Ravenhelm Sovereign Methodology Triad**:

```
                       THE SOVEREIGN METHODOLOGY TRIAD

   ┌────────────────────────────────────────────────────────────────────────┐
   │ 1. RLOM — Ravenhelm Linear Operating Method                            │
   │    Governs: The Work Graph, Demand Intake, Validation Gates, Reporting │
   │    Axiom: "If it isn't witnessed by a deed, it didn't happen."         │
   │    Status: v1.0.3 · 29 Principles (P-1..P-29)                          │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼ (Issues dispatched to engineering)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ 2. RDOM — Ravenhelm Development Operations Methodology                 │
   │    Governs: Planning, Concurrency, Agent Slices, TDD, Anti-Thrash      │
   │    Axiom: "Wave N+1 never opens on a promise; only on verified green." │
   │    Foundation: Ehwaz Doctrine (ᛖ), Valknut Cadence, Six Sigma, JIT     │
   │    Status: v1.0.0 · 24 Principles (DP-1..DP-24)                        │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼ (Merged code ready for compilation)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ 3. RROM — Ravenhelm Release Operations Methodology                     │
   │    Governs: Build Once, Artifact Custody, Multi-Surface Rails, GitOps  │
   │    Axiom: "Builds are the unit; releases are names."                   │
   │    Status: v1.0.0 · 18 Principles (RP-1..RP-18)                        │
   └────────────────────────────────────────────────────────────────────────┘
```

---

## The Core Axiom

> ### **Concurrency is earned through topological proof; quality is gated by verified green.**
>
> *A plan is a directed acyclic graph, not a task list. Execution proceeds in topological waves where parallel work carries zero collision risk by construction. Detail is elaborated just-in-time, shared capability is hoisted before snowflakes form, and no downstream wave opens on an exit promise.*

```
Wave 0 (No unmet deps) ──► [Six Sigma Gate: Verified Green] ──► Wave 1 ──► [Six Sigma Gate] ──► Wave 2
  ├── Agent Slice A                                              ├── Agent Slice C
  └── Agent Slice B (Concurrent)                                  └── Agent Slice D
```

---

## The 24 Numbered Principles

RDOM is governed by twenty-four inviolable principles across four operational pillars:

| ID | Principle | Core Rule |
|---|---|---|
| **DP-1** | **The Graph Precedes the Plan** | Every implementation begins with an explicit dependency DAG ($G = (V, E)$); flat task lists are unverified hypotheses. |
| **DP-2** | **Topological Wave Partitioning** | Work is partitioned into discrete waves ($W_0, W_1, \dots, W_N$) consisting only of tasks whose dependencies have resolved. |
| **DP-3** | **Zero Collision by Construction** | Concurrent agent slices are dispatched only within the same topological wave; cross-wave concurrency is barred. |
| **DP-4** | **The Critical Chain Floor** | The longest dependent path sets the schedule floor and receives primary focus; non-critical paths are managed as buffered slack. |
| **DP-5** | **Upstream-Jump Circuit Breaker** | Workers cannot branch outward to build against unfinished dependencies; blocked workers stop and sound the Andon cord. |
| **DP-6** | **Progressive JIT Elaboration** | Only the active wave ($W_k$) receives granular TDD specs; detailing downstream waves is toxic inventory waste (*Muda*). |
| **DP-7** | **Verified Green Precedes Promotion** | Wave $W_{k+1}$ opens only when all exit criteria of Wave $W_k$ pass mechanical verification against the live running system with active runner capacity. |
| **DP-8** | **Red-Green-Refactor State Transitions** | Work begins with a failing test asserting behavior, followed by minimal passing code, followed by refactoring. |
| **DP-9** | **Poka-Yoke Interface Design** | Public APIs, schemas, and CLI flags must make invalid states unrepresentable; errors must be structural types. |
| **DP-10** | **Live Running System as Truth** | Hypotheses and fixes are confirmed against the live running kernel/system state—never stale documentation or memory. |
| **DP-11** | **Witnessed Deed Attachment (Code, Docs, Showcase)** | Every feature release requires the Triad of Proof: verified automated tests, living documentation/runbooks, and an executable showcase serving as the empirical basis for RLOM User Acceptance Testing (UAT). |
| **DP-12** | **The Andon Cord Protocol** | On circular dependencies or silent corruption, the worker halts immediately, flags the blocker, and yields. |
| **DP-13** | **Planning-Time DRY Refactoring** | Before execution, scan the DAG for duplicate capability and refactor the graph to prevent snowflakes before code is written. |
| **DP-14** | **The Hoist-vs-Defer Rule** | Known interfaces are hoisted upstream into early waves; guessed interfaces are built inline with scheduled deferred extractions. |
| **DP-15** | **Zero Unacknowledged Duplication (Consumption Contract)** | A repo or slice may decline to use an established estate surface, but it may not do so silently; bypassing a platform library requires an explicit `consumes_exemption`. |
| **DP-16** | **Scaffolding from Working Reality** | Frameworks, SDKs, and base classes are extracted only from working, tested implementations—never imagined in a vacuum. |
| **DP-17** | **Shared Substrate Invariance** | Shared memory buffers, IPC wire protocols, and cancellation barriers belong to Layer 0 substrate crates, never re-rolled. |
| **DP-18** | **Locality Invariance** | Subsystems must expose identical interfaces whether running in-process, across POSIX shared memory, or over remote QUIC. |
| **DP-19** | **Dedicated Worktree Custody** | Every task slice operates in an isolated, disposable git worktree projected from a canonical `.bare/` repository, adhering to the Repo Agent Bootstrap Standard (`AGENTS.md` + `.agents/`). |
| **DP-20** | **Anti-Thrash Context Priming** | Agents must never crawl directories blindly; ingestion uses topological EAT digests (`eat prime`, `eat read`) to protect context. |
| **DP-21** | **Zero Ambient Mutation on Hosts** | Development never edits live configs on server hosts via SSH; all mutations pass through repos, PRs, and GitOps pipelines. |
| **DP-22** | **WIP Commit Checkpointing** | Never use `git stash` across branch switches; session momentum is preserved via WIP commits and Gamer-style Quicksaves. |
| **DP-23** | **The PR Boundary** | Direct pushes to `main` or `develop` are physically barred; all code lands via PRs gated by CI and advisory review. |
| **DP-24** | **Clean Worktree Disposal** | A worktree is disposable once its PR is merged and validated; deletion is gated by proof that no unpushed work remains. |

---

## Start Reading

The book is organized into **18 chapters plus Appendix A**:

| Part | Chapters | Focus |
|---|---|---|
| **Part I: Strategic Intent & Cadence** | [01](docs/chapters/01-what-this-is.md) – [07](docs/chapters/07-ceremonies-of-truth.md) | Valknut Hierarchy of Deeds, The Four Codices, Faster/Bigger/Cheaper/Effective OKRs, Ceremonies of Truth |
| **Part II: The Ehwaz Planning Doctrine** | [08](docs/chapters/08-the-dependency-dag-and-critical-chain.md) – [12](docs/chapters/12-the-dry-hoisting-protocol.md) | Dependency DAGs, Topological Waves, Multi-Agent Concurrency, JIT Elaboration, DRY Hoisting |
| **Part III: Execution Mechanics** | [13](docs/chapters/13-six-sigma-wave-boundary-gates.md) – [17](docs/chapters/17-zero-waste-context-substrate-eat.md) | Six Sigma Gates, Poka-Yoke Interfaces, Andon Cord, Bare Worktrees, EAT Zero-Waste Substrate |
| **Part IV: Governance & Integration** | [18](docs/chapters/18-the-sovereign-engineering-organization.md) | Operating Sovereign Human-Agent Fleets & End-to-End Method Integration |
| **Appendix A** | [App. A](docs/chapters/appendix-a-presales-and-demo-ops.md) | Presales, Solution Architecture & DemoOps Integration |

---

## Publications & Artifacts

The manuscript is typeset using **Typst** in two publication-grade editions conforming to Ravenhelm's brand standards (Source Serif 4 + IBM Plex Mono):

- **[Download PDF (Dark Edition)](RDOM-v1.0.0-dark.pdf)** — Obsidian background (`#0B0C0E`), Bone ink (`#EDE8DC`), Garnet accents (`#A3222F`).
- **[Download PDF (Print Edition)](RDOM-v1.0.0.pdf)** — Bone paper (`#EDE8DC`), Obsidian ink (`#0B0C0E`), designed for formal print and digest reading.

To recompile the publication PDFs locally:

```bash
python3 scripts/build-pdf.py
```

---

## License & Commercial Inquiries

RDOM is published under the **Apache License, Version 2.0**. Commercial training, third-party certification, and enterprise fleet advisory rights are reserved by **Ravenhelm LLC**.

For enterprise advisory, autonomous agent fleet architectures, or software delivery audits, contact:

**Nathan Walker** · **Ravenhelm LLC**  
Email: [nate@ravenhelm.co](mailto:nate@ravenhelm.co) · Web: [https://ravenhelm.co](https://ravenhelm.co)
