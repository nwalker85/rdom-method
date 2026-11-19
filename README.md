# Ravenhelm Development Operations Methodology (RDOM)

> **Book II of the Ravenhelm Operations Methodology** (*The Sovereign Engineering Trilogy: RLOM · RDOM · RROM*) - A tiered, sovereign operating methodology for software development, agentic concurrency, and engineering cadence; installable across engineering teams, grounded in twenty-four numbered principles, and bridging Strategic Invariants to high-concurrency autonomous agent execution.

Authored by **[Nathan Walker](https://nwalker.cc)** · Published by **[Ravenhelm LLC](https://ravenhelm.co)**  
Current Release: **v1.0.0** · [PDF (Light)](RDOM-v1.0.0.pdf) · [PDF (Dark)](RDOM-v1.0.0-dark.pdf) · [Changelog](CHANGELOG.md) · [Principles](docs/_shared/PRINCIPLES.md) · [Start Reading ->](docs/chapters/01-what-this-is.md)

---

## What Problem This Solves

On 2026-09-11, the Mimir grammar compiled cleanly across two runtimes while a custody sweep the same night uncovered 81 dangling tips and 15 unpushed branches stranded in `git reflog` across five repositories. When human engineers and autonomous AI agent slices share a factory floor, the control structures of human floor management transfer; the social layer does not. Humans self-heal from vague instructions and ask when confused. Agents fail literal, brittle, and silent:

- **The Sprint Delusion**: Work is batched into two-week calendar sprints built for human meetings. Agent slices either finish a task in 18 minutes and sit idle or wedge for 47 minutes while downstream slices code against unfinished interfaces.
- **The Prompting Fallacy**: Agents are unleashed with flat prompt checklists. They edit overlapping files simultaneously, trample shared test databases (`pytest -n auto` on a default database), and generate snowflake implementations across slices rather than hoisting shared crates.
- **Inventory Waste (*Muda*)**: Teams spend thousands of tokens writing step-by-step code three waves ahead of an unverified upstream producer, only to throw it away when the producer struct changes during Wave 0.
- **Checks That Cannot Fail**: Tasks are declared "Done" when test scripts pipe `unittest` into `tail -5` (masking non-zero exit codes), 3-argument `git merge-tree` reports `0 conflicts` on two real conflicts, or 10 features merge with 73 passing unit tests and zero callers from `main()`.
- **Altitude Drift**: Strategic Invariants live in decorative quarterly slides, divorced from the actual commits, pull requests (`RAV-<id>`), and worktrees executing on the bench.

The **Ravenhelm Development Operations Methodology (RDOM)** is the second *dōmbōc* ("what is laid down; the judgment") of the **Ravenhelm Operations Methodology**:

```text
                  THE RAVENHELM OPERATIONS METHODOLOGY
             (The Sovereign Engineering Trilogy: RLOM · RDOM · RROM)

   ┌────────────────────────────────────────────────────────────────────────┐
   │ Book I: RLOM - Ravenhelm Linear Operating Method (The Work Graph)      │
   │    Governs: The Work Graph, Demand Intake, Validation Gates, Reporting │
   │    Axiom: "Merged != Built != Running; evidence beats assertion."      │
   │    Status: v1.0.3 · 29 Principles (P-1..P-29)                          │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼ (Issues dispatched to engineering)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Book II: RDOM - Ravenhelm Development Operations Methodology           │
   │    Governs: Topological Waves, Concurrency, Agent Slices, TDD, EAT     │
   │    Axiom: "Wave N+1 never opens on a promise; only on verified green." │
   │    Foundation: The Ehwaz Doctrine (ᛖ), Critical Chain, Six Sigma, JIT  │
   │    Status: v1.0.0 · 24 Principles (DP-1..DP-24)                        │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼ (Merged code ready for compilation)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Book III: RROM - Ravenhelm Release Operations Methodology              │
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

```text
Wave 0 (No unmet deps) ──► [Six Sigma Gate: Verified Green] ──► Wave 1 ──► [Six Sigma Gate] ──► Wave 2
  ├── Agent Slice A                                              ├── Agent Slice C
  └── Agent Slice B (Concurrent)                                  └── Agent Slice D
```

---

## The 24 Numbered Principles

RDOM is governed by twenty-four shop-floor principles across four operational pillars:

| ID | Principle | Core Rule |
|---|---|---|
| **DP-1** | **The Graph Precedes the Plan** | Every implementation begins with an explicit dependency DAG ($G = (V, E)$); flat task lists are unverified hypotheses. |
| **DP-2** | **Topological Wave Partitioning** | Work is partitioned into discrete waves ($W_0, W_1, \dots, W_N$) consisting only of tasks whose dependencies have resolved. |
| **DP-3** | **Zero Collision by Construction** | Concurrent agent slices are dispatched only within the same topological wave across disjoint write surfaces and test schemas. |
| **DP-4** | **The Critical Chain Floor** | The longest dependent path sets the schedule floor and receives primary focus; non-critical paths are managed as buffered slack. |
| **DP-5** | **Upstream-Jump Circuit Breaker** | Workers cannot branch outward to build against unfinished dependencies; blocked workers stop and pull the Andon cord. |
| **DP-6** | **Progressive JIT Elaboration** | Only the active wave ($W_k$) receives granular TDD specs; detailing downstream waves is toxic inventory waste (*Muda*). |
| **DP-7** | **Verified Green Precedes Promotion** | Wave $W_{k+1}$ opens only when all exit criteria of Wave $W_k$ pass mechanical verification using checks that prove they can fail. |
| **DP-8** | **Red-Green-Refactor State Transitions** | Work begins with a failing test asserting behavior, followed by minimal passing code, followed by refactoring. |
| **DP-9** | **Poka-Yoke Interface Design** | Public APIs, schemas, and permission profiles must make invalid states unrepresentable and keep the safe verification path cheaper than guessing. |
| **DP-10** | **Live Running System as Truth** | Hypotheses and fixes are confirmed against the live running system and entrypoint call graph; never stale docs or isolated mocks. |
| **DP-11** | **Witnessed Deliverable Attachment (Triad of Proof)** | Every deliverable requires the Triad of Proof: passing tests with caller parity, living docs/runbooks, and an executable showcase. |
| **DP-12** | **The Andon Cord Protocol** | On broken invariants or wedged lanes, halt downstream dispatch immediately and inspect uncommitted diffs before discarding work. |
| **DP-13** | **Planning-Time DRY Refactoring** | Before execution, scan the DAG for duplicate capability and refactor the graph to prevent snowflakes before code is written. |
| **DP-14** | **The Hoist-vs-Defer Rule** | Known interfaces are hoisted upstream into early waves; guessed interfaces are built inline with scheduled deferred extractions. |
| **DP-15** | **Zero Unacknowledged Duplication** | Every identified repeat in the planning scan must be either hoisted upstream or bound to a scheduled extraction issue. |
| **DP-16** | **Scaffolding from Working Reality** | Frameworks, SDKs, and project scaffolds are extracted only from working, production-proven reference implementations. |
| **DP-17** | **Shared Substrate Invariance** | Estate-wide substrates (gateway, observability, secrets, registry) are invariant across repos; never re-rolled per service. |
| **DP-18** | **Locality Invariance (`AGENTS.md` Authority)** | Every repository carries an authoritative root `AGENTS.md` that travels with code in pull requests. |
| **DP-19** | **Dedicated Worktree Custody** | Every task slice operates in an isolated, disposable git worktree projected from a canonical `.bare/` repository with an explicit fetch refspec. |
| **DP-20** | **Anti-Thrash Context Priming** | Agents never crawl directories blindly; orientation uses `<800`-token topological digests (`eat prime`) and `<10ms` AST byte reads (`eat read`). |
| **DP-21** | **Zero Ambient Mutation on Hosts** | Development never edits live configs on server hosts via SSH; all mutations pass through repos, PRs, and RROM deployment rails. |
| **DP-22** | **WIP Commit Checkpointing** | Never use `git stash` across branch switches; session momentum is preserved via WIP commits and quicksaves. |
| **DP-23** | **The Pull Request Boundary & Supervisor Merge Gate** | Direct pushes to `main` are barred; workers open PRs, and only the supervisor who received human approval merges and triggers deploy. |
| **DP-24** | **Custody-Gated Worktree Disposal** | A worktree is disposable once its PR is merged and validated; deletion requires custody proof that zero unpushed or uncommitted work remains. |

---

## Start Reading

The book is organized into **18 chapters plus Appendix A** (~64,100 words):

| # | Chapter | Part & Focus | Words |
|---|---|---|---|
| 01 | [What This Is and Why Modern Engineering Drifts](docs/chapters/01-what-this-is.md) | Part I: The Ehwaz Doctrine & Why the Social Layer Does Not Transfer | 3,459 |
| 02 | [The Sovereign Triad: RLOM, RDOM, RROM](docs/chapters/02-the-sovereign-triad.md) | Part I: The Three *Dōmbócs* (Intent, Execution, Custody) | 3,155 |
| 03 | [The 24 Numbered Principles](docs/chapters/03-numbered-principles.md) | Part I: The Shop-Floor Canon (`DP-1`..`DP-24`) & Estate Receipts | 4,233 |
| 04 | [The Topological Work Hierarchy: From Strategic Invariant to Atomic Commit](docs/chapters/04-the-hierarchy-of-deeds.md) | Part I: Strategic Invariants, Quarterly Contracts, Deliverables, Commits | 3,030 |
| 05 | [The Four Operational Contracts: Repository Law, Cadence, Architecture, and Fleet Custody](docs/chapters/05-the-four-codices.md) | Part I: `AGENTS.md`, Cadence Ledger, ADRs/Runbooks, Fleet Routing | 2,780 |
| 06 | [The Four-Dimensional Engineering Scorecard: Faster, Bigger, Cheaper, Effective](docs/chapters/06-the-engineering-okr-framework.md) | Part I: Balanced Engineering Control Matrix & Quota Physics | 2,785 |
| 07 | [Ceremonies of Truth: Quarterly Invariant Review, Monthly Architecture Review, and the Daily Fleet Sweep](docs/chapters/07-ceremonies-of-truth.md) | Part I: Reconciling the Docket, Flushing Court Cards, Sweeping Panes | 3,914 |
| 08 | [The Dependency DAG: Critical Path vs. Critical Chain](docs/chapters/08-the-dependency-dag-and-critical-chain.md) | Part II: The Ehwaz Doctrine Part I (CPM & Goldratt's Critical Chain) | 3,813 |
| 09 | [Topological Waves: Replacing the Two-Week Sprint](docs/chapters/09-topological-waves-replacing-sprints.md) | Part II: The Ehwaz Doctrine Part II (Wave Generation & Dispatch) | 3,444 |
| 10 | [Zero Collision by Construction: Multi-Agent Fleet Boundaries](docs/chapters/10-zero-collision-multi-agent-boundaries.md) | Part II: Disjoint Write Surfaces, `git merge-tree --write-tree`, DB Schemas | 2,871 |
| 11 | [Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)](docs/chapters/11-jit-elaboration-and-anti-inventory.md) | Part II: Open-Wave TDD Detailing vs. Future-Wave Interface Contracts | 3,180 |
| 12 | [The DRY Hoisting Protocol: Anti-Snowflake Planning](docs/chapters/12-the-dry-hoisting-protocol.md) | Part II: Planning-Time DRY Scan & The Hoist-vs-Defer Rule | 3,169 |
| 13 | [Six Sigma Wave Boundary Gates: No Exit on a Promise](docs/chapters/13-six-sigma-wave-boundary-gates.md) | Part III: Checks That Can Fail, Caller Reachability, Triad of Proof | 4,495 |
| 14 | [Poka-Yoke Interface Design & The Live System Rule](docs/chapters/14-poka-yoke-interface-design.md) | Part III: Pricing Verification Below Guessing (`Granularity::Exact`) | 3,624 |
| 15 | [The Andon Cord Protocol & Upstream-Jump Circuit Breakers](docs/chapters/15-the-andon-cord-and-circuit-breakers.md) | Part III: Stopping the Line & Rescuing Uncommitted Diffs (`doom momentum`) | 3,853 |
| 16 | [Workspace Custody: Bare Repositories and Disposable Worktrees](docs/chapters/16-workspace-custody-bare-and-worktrees.md) | Part III: Checkout Custody Standard (`.bare/`, Fetch Refspecs, One-per-PR) | 3,171 |
| 17 | [The Zero-Waste Context Substrate: Topological Priming vs. Directory Dumps](docs/chapters/17-zero-waste-context-substrate-eat.md) | Part III: Anti-Thrash Orientation (`eat prime` <800 Tokens, `eat read` <10ms) | 2,893 |
| 18 | [The Sovereign Engineering Organization: Operating Human-Agent Fleets](docs/chapters/18-the-sovereign-engineering-organization.md) | Part IV: Declarative Cores, Dumb Edges, Supervisor-Worker Topology | 3,486 |
| App. A | [Appendix A: Presales, Solution Architecture & DemoOps Integration](docs/chapters/appendix-a-presales-and-demo-ops.md) | Appendix: Commercial Proof, Ephemeral Demo Sandboxes, Hoisting | 2,752 |

---

## Publications & Artifacts

The manuscript is typeset using **Typst** in two publication-grade editions conforming to Ravenhelm's brand standards (Source Serif 4 + IBM Plex Mono):

- **[Download PDF (Dark Edition)](RDOM-v1.0.0-dark.pdf)** - Obsidian background (`#0B0C0E`), Bone ink (`#EDE8DC`), Garnet accents (`#A3222F`).
- **[Download PDF (Print Edition)](RDOM-v1.0.0.pdf)** - Bone paper (`#EDE8DC`), Obsidian ink (`#0B0C0E`), designed for formal print and digest reading.

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
