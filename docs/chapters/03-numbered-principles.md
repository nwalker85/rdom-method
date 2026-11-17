<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- ALL RIGHTS RESERVED. ORG: ravenhelm.dev -->

## Chapter 3 — The 24 Numbered Principles

Software engineering organizations love slogans. Poster boards, desktop wallpapers, and corporate decks proclaim platitudes: "Move Fast and Break Things," "Customer Obsession," and "Keep It Simple." Within weeks, these slogans rot into corporate wallpaper. They offer zero mechanical guidance when an automated agent fleet triggers forty merge conflicts across three repositories, or when coordinating schema migrations across five interdependent services. Slogans fail because they lack state equations, topological invariants, and physical enforcement mechanisms. They appeal to human sentiment rather than manufacturing reality.

In industrial manufacturing, principles are not motivational aspirations; they are thermodynamic and mechanical laws. If a foundry engineer violates thermal dissipation tolerances, the engine block shatters on the test bench. If an aerospace machinist ignores tooling deflection, the turbine rotor shears its shaft. Physical laws do not negotiate with sprint deadlines, burn-down optimism, or executive hopes.

The Ravenhelm Development Operations Methodology (RDOM) approaches software construction with identical industrial and mathematical rigor. The twenty-four numbered principles (**DP-1** through **DP-24**) form an interconnected lattice of structural invariants. They are mechanical laws governing both autonomous AI agent swarms and human engineering teams: decomposing work into directed acyclic graphs, harvesting concurrency without spatial collision, sealing defect boundaries with Six Sigma gates, hoisting architectural duplication at planning time, and maintaining verifiable workspace custody.

In RDOM, a principle is not an opinion; it is an enforceable gate. If an implementation violates a principle, CI breaks, the Andon cord trips, the wavefront halts, and promotion is physically barred.

### Architecture of the Four Pillars

The twenty-four principles are organized into four mutually reinforcing structural pillars spanning the delivery lifecycle from topological intent down to silicon custody:

```mermaid
graph TD
    subgraph Pillar1["Pillar I: Dependency Wavefront (Ehwaz)"]
        DP1["DP-1: Graph Precedes Plan"]
        DP2["DP-2: Topological Waves"]
        DP3["DP-3: Zero Collision"]
        DP4["DP-4: Critical Chain Floor"]
        DP5["DP-5: Upstream Circuit Breaker"]
        DP6["DP-6: Progressive JIT Elaboration"]
    end

    subgraph Pillar2["Pillar II: Six Sigma Defect Prevention"]
        DP7["DP-7: Verified Green Promotion"]
        DP8["DP-8: Red-Green-Refactor FSM"]
        DP9["DP-9: Poka-Yoke Interface Design"]
        DP10["DP-10: Live Running System Truth"]
        DP11["DP-11: Witnessed Deed Triad"]
        DP12["DP-12: Andon Cord Protocol"]
    end

    subgraph Pillar3["Pillar III: DRY Architecture & Hoisting"]
        DP13["DP-13: Planning-Time DRY"]
        DP14["DP-14: Hoist-vs-Defer Rule"]
        DP15["DP-15: Zero Unacknowledged Duplication"]
        DP16["DP-16: Scaffolding from Reality"]
        DP17["DP-17: Shared Substrate Invariance"]
        DP18["DP-18: Locality Invariance"]
    end

    subgraph Pillar4["Pillar IV: Workspace Custody & Ergonomics"]
        DP19["DP-19: Dedicated Worktree Custody"]
        DP20["DP-20: Anti-Thrash Context Priming"]
        DP21["DP-21: Zero Ambient Mutation"]
        DP22["DP-22: WIP Commit Checkpointing"]
        DP23["DP-23: PR Review Boundary"]
        DP24["DP-24: Clean Worktree Disposal"]
    end

    DP1 -->|DAG Precedence| DP2
    DP2 -->|Wavefront Partition| DP3
    DP13 -->|Extract Shared Nodes| DP1
    DP14 -->|Hoist Shared Crates| DP2
    DP3 -->|Disjoint Blast Radii| DP19
    DP19 -->|Isolated Sandbox| DP8
    DP8 -->|Test State Transitions| DP7
    DP7 -->|Verification Proof| DP2
    DP5 -->|Halt on Contract Drift| DP12
    DP12 -->|Trip Wave Circuit Breaker| DP2
    DP10 -->|Validate Live State| DP7
    DP7 -->|Feeds Proof Triad| DP11
    DP20 -->|Surgical AST Priming| DP19
    DP22 -->|Crash-Safe Commits| DP23
    DP23 -->|Witnessed PR Merge| DP24
    DP17 -->|Substrate Rigidity| DP9
    DP18 -->|Root Authority Contract| DP16
```

---

### Pillar I: The Dependency Wavefront (Ehwaz Doctrine & Concurrency)

Pillar I governs the mathematical scheduling of concurrent execution across agent fleets and engineering teams.

#### DP-1: The Graph Precedes the Plan

- **Canonical Axiom**: Work is formally a Directed Acyclic Graph $G = (V, E)$; any plan lacking an explicit edge set $E$ is an unverified hypothesis.
- **Operational Mechanism**: Intake compilers ingest work definitions into machine-validated DAGs with declared dependencies. Automated linters reject cyclic graphs and floating nodes prior to branch provisioning.
- **The Failure Mode**: The "Sprint Bag." Teams schedule unlinked tickets, discovering mid-sprint that unbuilt prerequisites block delivery, creating compounding carryover debt.

#### DP-2: Topological Wave Partitioning

- **Canonical Axiom**: Given DAG $G = (V, E)$, work partitions into ordered waves $W_0, \dots, W_K$ where $(u, v) \in E \implies k(u) < k(v)$. Wave $W_{k+1}$ opens only upon verified green completion of $W_k$.
- **Operational Mechanism**: CI orchestrators enforce wave barriers. Worktree leases for $W_{k+1}$ remain locked until signed attestations prove all $W_k$ tasks satisfy deterministic verification gates.
- **The Failure Mode**: Premature integration thrash. Workers code consumers against mutating Wave 1 schemas, triggering continuous rebasing, broken contracts, and phantom defects.

#### DP-3: Zero Collision by Construction

- **Canonical Axiom**: Concurrent tasks $u, v \in W_k$ must maintain disjoint spatial blast radii: $\mathcal{B}(u) \cap \mathcal{B}(v) = \emptyset$. Concurrent mutation of identical files across branches is an architectural defect.
- **Operational Mechanism**: DAG validation computes touched resource footprints. Spatial overlaps force planners to hoist shared boundaries to $W_{k-1}$ or serialize tasks into sequential execution tiers.
- **The Failure Mode**: Git merge massacres. Parallel agents edit `routes.rs` or `schema.sql` simultaneously, discarding critical logic during conflicting, unverified rebase resolutions.

#### DP-4: The Critical Chain Floor

- **Canonical Axiom**: Let $d(v)$ be task duration. Critical path duration $D = \max_P \sum_{v \in P} d(v)$, plus feeder and project buffers under finite capacity, sets the physical delivery floor.
- **Operational Mechanism**: Schedulers map worker capacity against the DAG. Non-critical tasks are managed as slack; workers cannot consume review bandwidth on auxiliary tasks while critical nodes starve.
- **The Failure Mode**: Subsystem starvation. Teams merge dozens of low-priority PRs while the core database transaction engine on the critical path sits unreviewed, delaying releases.

#### DP-5: Upstream-Jump Circuit Breaker

- **Canonical Axiom**: A task $v \in W_k$ shall never jump upstream to modify the interface or behavior of $u \in W_j$ ($j < k$) without tripping an immediate replanning circuit breaker.
- **Operational Mechanism**: Pre-commit hooks detect diffs outside the bounded task scope. Modifying upstream crates halts execution, revokes active work leases, and triggers graph re-evaluation.
- **The Failure Mode**: Uncontrolled scope creep. A worker implementing a frontend widget modifies the foundational authentication service, silently breaking five unrelated downstream services.

#### DP-6: Progressive JIT Elaboration

- **Canonical Axiom**: A task $v \in W_k$ shall be elaborated to concrete implementation specifications if and only if $W_k$ is the active wave or $W_{k-1}$ has achieved verified green.
- **Operational Mechanism**: Issue trackers enforce state transitions. Detailed prompts and file manifests are generated Just-In-Time from verified upstream outputs, preventing stale context drift.
- **The Failure Mode**: Premature specification rot. Architects write detailed implementation plans for Wave 4 based on speculative Wave 1 designs, discarding weeks of labor when contracts evolve.

---

### Pillar II: Six Sigma Defect Prevention & TDD Gates

Pillar II establishes defect prevention at each state transition, eliminating downstream triage through deterministic verification.

#### DP-7: Verified Green Precedes Promotion

- **Canonical Axiom**: Code does not exist for promotion until deterministic verification passes: $\operatorname{Status}(v) = \operatorname{Promoted} \implies \operatorname{Verify}(v) = \operatorname{Pass}$.
- **Operational Mechanism**: CI gatekeepers reject human and agent merge requests lacking cryptographically signed test attestations. Green test suites are mandatory preconditions for promotion.
- **The Failure Mode**: "Ship now, fix later." Defective code merges into develop, breaking main, poisoning the development stream, and halting all dependent concurrent work.

#### DP-8: Red-Green-Refactor as State Transitions

- **Canonical Axiom**: Development is an unambiguous Finite State Machine: $\text{Red} \xrightarrow{\Delta \text{code}} \text{Green} \xrightarrow{\Delta \text{clean}} \text{Refactor}$. Implementation commits without preceding failing tests violate protocol.
- **Operational Mechanism**: Orchestrators inspect commit history for failing test executions before admitting implementation diffs. Passing suites prior to modification result in task rejection.
- **The Failure Mode**: Retrospective testing theatre. Developers write tautological assertions after writing code, validating existing implementation bugs rather than functional requirements.

#### DP-9: Poka-Yoke Interface Design

- **Canonical Axiom**: An interface must be physically impossible to consume incorrectly: $\forall c \in \operatorname{Invocations}, \operatorname{Malformed}(c) \implies \operatorname{CompileError}(c)$.
- **Operational Mechanism**: APIs employ parse-don't-validate idioms, newtypes, exhaustive sum types, and strict builder contracts, rejecting invalid state combinations at compile time.
- **The Failure Mode**: Runtime catastrophe. Primitive obsession permits unvalidated strings to flow into SQL statements or authorization checks, causing silent data corruption and breaches.

#### DP-10: Live Running System as Truth

- **Canonical Axiom**: Verification requires empirical proof from active running instances; documentation, test mocks, and memory are unverified hypotheses.
- **Operational Mechanism**: Health checks query live endpoints, inspecting actual database schemas and network listeners via testcontainers rather than synthetic mocks.
- **The Failure Mode**: The mock delusion. Test suites report 100% green coverage against outdated in-memory stubs, while production crashes instantly upon deploying against live PostgreSQL engines.

#### DP-11: Witnessed Deed Attachment (Code, Docs, Showcase)

- **Canonical Axiom**: A deed $v$ is complete if and only if the Triad of Proof is satisfied: $\operatorname{Complete}(v) \iff \operatorname{Code}(v) \land \operatorname{Docs}(v) \land \operatorname{Showcase}(v)$.
- **Operational Mechanism**: Promotion linters verify implementation code, corresponding documentation updates, and recorded automated showcases demonstrating live functionality.
- **The Failure Mode**: Dark deliverables. Features merge without documentation or operational runbooks; months later, no engineer understands how the subsystem functions.

#### DP-12: The Andon Cord Protocol

- **Canonical Axiom**: Any failure of an upstream invariant halts the active wave immediately: $\exists e \in \text{Failures} \implies \operatorname{Halt}(W_k)$.
- **Operational Mechanism**: Automated agent harnesses stop dispatching tasks upon detecting contract violations, notifying the supervisory channel and locking dependent tasks.
- **The Failure Mode**: Cascading failure swamps. Flaky tests or contract drifts are ignored; twenty agents compound the error across subsequent branches, requiring massive rollbacks.

---

### Pillar III: DRY Architecture & Anti-Snowflake Hoisting

Pillar III enforces structural reuse, preventing architectural fragmentation and bespoke code duplication.

#### DP-13: Planning-Time DRY Refactoring

- **Canonical Axiom**: Deduplication occurs during DAG compilation, not post-implementation: $\forall u, v \in V, \operatorname{Similarity}(u, v) > \theta \implies \exists w \in W_0 \text{ extracted}$.
- **Operational Mechanism**: Intake analyzers run semantic clustering across proposed deeds, identifying common utilities and hoisting them to foundation waves before parallel work begins.
- **The Failure Mode**: Parallel reinvention. Multiple agents building separate service adapters implement incompatible HTTP client wrappers, each with distinct retry bugs.

#### DP-14: The Hoist-vs-Defer Rule

- **Canonical Axiom**: If a component is required by $\ge 2$ consumers across distinct subgraphs, hoist immediately to shared libraries; if required by 1, defer to domain locality.
- **Operational Mechanism**: Workspace architecture linters flag cross-boundary imports. Shared types require registration in shared workspace crates; single-consumer abstractions are denied hoisting.
- **The Failure Mode**: Premature over-generalization or siloed duplication. Infrastructure code either chokes on speculative abstractions or drowns in copy-pasted boilerplate.

#### DP-15: Zero Unacknowledged Duplication (Consumption Contract)

- **Canonical Axiom**: Copying code requires an explicit consumption contract citing the source, mechanical justification, and an automated sync test.
- **Operational Mechanism**: AST scanners scan pull requests for structural similarity against existing codebases. Unreferenced duplicate logic triggers automated review rejections.
- **The Failure Mode**: Orphaned drift. Critical security patches applied to a core cryptographic routine fail to propagate to unacknowledged copy-pasted implementations.

#### DP-16: Scaffolding from Working Reality

- **Canonical Axiom**: New services, modules, and configurations must scaffold from proven, production-verified implementations rather than clean-slate theoretical templates.
- **Operational Mechanism**: Code generators ingest vetted production reference implementations, stamping out new services with battle-tested logging, telemetry, and error handling.
- **The Failure Mode**: Second-system syndrome. Engineers design abstract greenfield templates that omit critical edge cases, rediscovering production bugs already solved years prior.

#### DP-17: Shared Substrate Invariance

- **Canonical Axiom**: Foundational estate-wide substrates (logging, telemetry, database drivers) are immutable across service boundaries: $\forall s \in \text{Services}, \operatorname{Substrate}(s) \equiv \mathcal{S}_{\text{canonical}}$.
- **Operational Mechanism**: Build systems pull locked workspace dependencies from internal registries. Custom logging libraries or alternative database drivers fail build gates.
- **The Failure Mode**: Substrate balkanization. Every microservice utilizes different metrics collectors and log formats, blinding central observability and thwarting incident response.

#### DP-18: Locality Invariance

- **Canonical Axiom**: Logic resides in the tightest scope possible while respecting architectural boundaries. Repository-level `AGENTS.md` is authoritative for local context.
- **Operational Mechanism**: Linters enforce repository-root authority rules. Global configs cannot override domain boundaries, ensuring local repositories remain self-contained and auditable.
- **The Failure Mode**: Distributed spaghetti. Business rules bleed into ambient configuration scripts, making local component behavior impossible to reason about in isolation.

---

### Pillar IV: Workspace Custody & Multi-Agent Ergonomics

Pillar IV governs physical workspace isolation, state persistence, and operational ergonomics for agents and engineers.

#### DP-19: Dedicated Worktree Custody

- **Canonical Axiom**: Every concurrent task executes in an isolated git worktree: $\forall v_i, v_j \in W_k, \operatorname{Path}(v_i) \cap \operatorname{Path}(v_j) = \emptyset$. Bare repositories provide the single source of truth.
- **Operational Mechanism**: Tooling allocates ephemeral worktrees linked to a centralized `.bare/` repository. Direct modifications on shared checkouts are blocked by pre-commit hooks.
- **The Failure Mode**: Dirty stash collisions. Developers switch branches mid-task, polluting staging areas with half-finished edits and accidentally committing debug statements.

#### DP-20: Anti-Thrash Context Priming

- **Canonical Axiom**: Agent priming must consume $<800$ tokens of topological digest (`eat prime`); blind directory crawls and raw full-file dumping are prohibited.
- **Operational Mechanism**: Agents use surgical AST byte-range retrieval (`eat read`) and hyperedge traversal (`eat connections`), eliminating wasteful whole-file reads and context blowouts.
- **The Failure Mode**: Context collapse. An agent reads twenty full source files, exhaustively burning its context window, tripping loop breakers, and hallucinating invalid syntax.

#### DP-21: Zero Ambient Mutation on Production Hosts

- **Canonical Axiom**: Production infrastructure is immutable: $\Delta \operatorname{State}(\text{Host}) \neq \emptyset \implies \text{DeployViaGitOps}$. Direct SSH file modifications are strictly forbidden.
- **Operational Mechanism**: Production hosts disable remote write access outside automated GitOps pipelines. Configuration drifts are automatically reconciled against repository truth.
- **The Failure Mode**: The snowflake server. An engineer hotfixes a config file on production via SSH without committing; the next deployment wipes the fix, causing severe downtime.

#### DP-22: WIP Commit Checkpointing

- **Canonical Axiom**: State persistence is continuous and cheap: session progress must checkpoint via atomic WIP commits before risky operations, tool switches, or context boundaries.
- **Operational Mechanism**: Automated hooks create structured checkpoint commits at regular turn intervals, preserving dirty tree states without disrupting branch history.
- **The Failure Mode**: The lost afternoon. An agent crash, power failure, or shell timeout obliterates uncommitted work, forcing complete task re-implementation.

#### DP-23: The PR Boundary

- **Canonical Axiom**: Main and develop branches are append-only targets gated by witnessed pull request reviews. Direct pushes are structurally prohibited: $\operatorname{Push}(\text{main}) = \bot$.
- **Operational Mechanism**: Forgejo and GitHub repository protections block direct branch updates, requiring passed CI checks and explicit architectural approvals prior to merge.
- **The Failure Mode**: Cowboy commits. A developer pushes untested commits directly to main, triggering deployment of broken artifacts and bringing down production clusters.

#### DP-24: Clean Worktree Disposal

- **Canonical Axiom**: Worktree deletion is strictly gated by custody proof: a worktree may be deleted if and only if its commits are merged to main or archived in signed bundles.
- **Operational Mechanism**: Worktree management tools verify upstream merge status before pruning worktrees. Unmerged branches require explicit custody transfer before disposal.
- **The Failure Mode**: Accidental work destruction. Cleanup scripts blindly delete local directories, destroying days of experimental code and uncommitted verification artifacts.

---

### Cross-Cutting Invariance & Compounding Stability

The twenty-four principles form an interlocking algebraic system. Violating a single principle in one pillar inevitably triggers compounding failures across the other three. Conversely, adhering to upstream principles creates compounding stability downstream.

| Primary Principle | Reinforcing Principle | Compound Mechanism | Consequence of Severing Link |
|:---|:---|:---|:---|
| **DP-1** (Graph Precedes Plan) | **DP-2** (Topological Waves) | Explicit DAG edges drive deterministic wave partitioning. | Unlinked backlogs; impossible wave scheduling. |
| **DP-2** (Topological Waves) | **DP-3** (Zero Collision) | Wave barriers bound concurrency to disjoint file sets. | Cross-wave concurrency and continuous rebase thrash. |
| **DP-3** (Zero Collision) | **DP-19** (Worktree Custody) | Disjoint blast radii permit isolated worktrees without lock contention. | Shared checkouts, stash collisions, and lost edits. |
| **DP-13** (Planning-Time DRY) | **DP-1** (Graph Precedes Plan) | Deduplication hoists shared nodes before execution. | Slices reinvent identical utilities in parallel. |
| **DP-14** (Hoist vs. Defer) | **DP-2** (Topological Waves) | Shared primitives populate Wave 0 with verified contracts. | Downstream tasks build on unverified dependencies. |
| **DP-5** (Upstream Breaker) | **DP-12** (Andon Cord Protocol) | Upstream contract violations trip immediate halts. | Mocks hide defects until production deployment. |
| **DP-8** (Red-Green-Refactor) | **DP-7** (Verified Green) | Deterministic state transitions generate cryptographic gate proof. | Code promotes unverified, leaking defects downstream. |
| **DP-7** (Verified Green) | **DP-11** (Witnessed Deed Triad) | Automated CI verification fulfills the code leg of the Triad. | Undocumented, unverified features enter production. |
| **DP-20** (Anti-Thrash Context) | **DP-19** (Worktree Custody) | Surgical AST indexing primes worktrees without context waste. | Agents burn context crawling files, hallucinating APIs. |
| **DP-22** (WIP Checkpoints) | **DP-23** (PR Boundary) | Atomic WIP commits preserve crash-safe history for review. | Uncommitted work is lost on agent or shell timeout. |
| **DP-23** (PR Boundary) | **DP-24** (Clean Disposal) | Witnessed PR merges verify custody proof before disposal. | Stale worktrees accumulate or active work is purged. |

---

### Upstream and Downstream Integration

The twenty-four principles govern the operational interfaces of the Sovereign Triad:

- **Upstream Connection to RLOM**: RLOM governs strategic demand intake and value stream mapping. The RLOM-to-RDOM transition is governed by **DP-1** (compiling initiatives into DAGs of deeds), **DP-6** (delaying granular specifications until JIT wave opening), and **DP-11** (requiring the Triad of Proof, where executable showcases furnish empirical validation for RLOM acceptance).
- **Downstream Connection to RROM**: RROM governs immutable build artifacts, Harbor digest pinning, and GitOps cutovers on production clusters. RDOM feeds RROM through **DP-7** (verified green CI attestations), **DP-17** (shared substrate immutability), **DP-21** (zero ambient host mutation), and **DP-23** (the strict PR boundary). Builds are the unit and releases are names: a merge through **DP-23** triggers a single immutable build that RROM promotes across environments without recompilation.

> **Augmentation Surface — Automated Compliance & Governance**
>
> Where an agent layer transforms this practice: In traditional organizations, enforcing twenty-four engineering principles requires manual managers and reviewers, creating bureaucratic bottlenecks. In RDOM, an automated orchestration engine enforces these principles mechanically: compiling DAGs (**DP-1**), scheduling waves (**DP-2**), auditing blast radii (**DP-3**), provisioning bare worktrees (**DP-19**), priming agent context via topological AST indexing (**DP-20**), and enforcing Red-Green-Refactor transitions (**DP-8**). Compliance is passive, instant, and deterministic.
>
> What the human architect keeps: Sovereign control over strategic intent (RLOM demand), ratifying architectural hoist boundaries (**DP-13**, **DP-14**), adjudicating exemptions (**DP-15**), resolving Andon escalations (**DP-12**), and providing explicit witnessed approval for PR merges (**DP-23**) and production deployment cutovers.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 3078
  principle-citations: DP-1, DP-2, DP-3, DP-4, DP-5, DP-6, DP-7, DP-8, DP-9, DP-10, DP-11, DP-12, DP-13, DP-14, DP-15, DP-16, DP-17, DP-18, DP-19, DP-20, DP-21, DP-22, DP-23, DP-24
  flagged-principle-gaps: none
-->
