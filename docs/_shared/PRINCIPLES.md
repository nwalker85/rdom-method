# Canonical Principles of RDOM

The **Ravenhelm Development Operations Methodology (RDOM)** is anchored in twenty-four inviolable principles organized across four operational pillars.

---

## Pillar I: The Dependency Wavefront (Ehwaz Doctrine & Concurrency)

- **DP-1: The Graph Precedes the Plan.** Every implementation begins with an explicit dependency DAG ($G = (V, E)$). A numbered task list without edges is an unverified hypothesis.
- **DP-2: Topological Wave Partitioning.** Work is partitioned into discrete waves ($W_0, W_1, \dots, W_N$). A wave consists exclusively of tasks whose inbound dependencies have all resolved.
- **DP-3: Zero Collision by Construction.** Concurrent agent slices and human engineers are only dispatched across tasks in the same topological wave. Cross-wave concurrency is forbidden.
- **DP-4: The Critical Chain Floor.** The longest dependent path through the graph is identified before execution begins. It sets the floor on total delivery time and receives primary resource focus; non-critical paths are managed as buffered slack.
- **DP-5: Upstream-Jump Circuit Breaker.** No worker may branch outward to implement, stub, or mock against an unfinished upstream dependency. If an upstream block occurs, the worker halts and sounds the Andon cord.
- **DP-6: Progressive JIT Elaboration.** Only the currently active wave ($W_k$) receives granular, bite-sized TDD implementation specifications. Specifying code steps for Wave $W_{k+2}$ is inventory waste (*Muda*) that rots before execution.

---

## Pillar II: Six Sigma Defect Prevention & TDD Gates

- **DP-7: Verified Green Precedes Promotion.** Wave $W_{k+1}$ cannot open on a verbal assurance or a mock pass. It opens strictly when all exit criteria of Wave $W_k$ pass mechanical verification against the live running system with real runner capacity.
- **DP-8: Red-Green-Refactor as State Transitions.** A task does not begin with an implementation edit. It begins with a failing test asserting expected behavior, followed by minimal passing code, followed by refactoring.
- **DP-9: Poka-Yoke Interface Design.** Public APIs, component models, and CLI flags must make invalid states unrepresentable. Error paths must be structural types, never ambient panics or silent empty returns.
- **DP-10: Live Running System as Truth.** Hypotheses and fixes are confirmed against the live running kernel, container, or network state—never against stale documentation, memory, or optimism.
- **DP-11: Witnessed Deed Attachment (Code, Docs, Showcase).** A feature release or wave completion is never done on passing code alone. It requires the complete Triad of Proof: deterministic automated test verification, updated user documentation/runbooks, and an executable showcase or walkthrough that serves as the factual basis for RLOM User Acceptance Testing (UAT).
- **DP-12: The Andon Cord Protocol.** When an unresolvable defect, circular dependency, or silent data corruption is detected, the agent slice stops immediately, flags the blocker, and yields.

---

## Pillar III: DRY Architecture & Anti-Snowflake Hoisting

- **DP-13: Planning-Time DRY Refactoring.** Before a plan is ratified, scan the graph for duplicate capability across slices. Refactor the graph to prevent snowflakes before code is written.
- **DP-14: The Hoist-vs-Defer Rule.** If an interface is *known* (from diagnosed defects or established standards), hoist it upstream into an earlier wave as a shared crate/library. If *guessed*, allow the first consumer to build it inline and schedule an explicit extraction task.
- **DP-15: Zero Unacknowledged Duplication (Consumption Contract).** A repo or slice may decline to use an established estate surface, but it may not do so silently. Every identified repeat must either be hoisted or assigned an explicit `consumes_exemption` with a recorded justification.
- **DP-16: Scaffolding from Working Reality.** Never build abstract frameworks in a vacuum. Scaffolds, SDKs, and base classes are extracted only from working, tested implementations.
- **DP-17: Shared Substrate Invariance.** Platform-wide concerns (shared memory buffers, IPC wire protocols, cancellation barriers) belong to Layer 0 substrate crates, never reimplemented per tool.
- **DP-18: Locality Invariance.** A tool or subsystem must expose the identical interface regardless of whether execution is in-process, across POSIX shared memory, or routed over QUIC to a remote worker.

---

## Pillar IV: Workspace Custody & Multi-Agent Ergonomics

- **DP-19: Dedicated Worktree Custody.** Every task slice operates in an isolated, disposable git worktree projected from a single canonical `.bare/` repository, adhering to the Repo Agent Bootstrap Standard (`AGENTS.md` + `.agents/` working library).
- **DP-20: Anti-Thrash Context Priming.** Agents must never crawl directories blindly or dump whole files into context. Ingestion uses topological EAT digests (`eat prime`, `eat read`) to strictly preserve context budgets.
- **DP-21: Zero Ambient Mutation on Production Hosts.** Development work never directly edits live configurations or files on server hosts via SSH. All mutations pass through source repos, PRs, and GitOps pipelines.
- **DP-22: WIP Commit Checkpointing.** Never use `git stash` across branch switches. Session momentum is preserved via WIP commits and Gamer-style Quicksaves before risky operations.
- **DP-23: The PR Boundary.** Direct pushes to `main` or `develop` are physically barred. All code lands via pull requests gated by CI, branch protection, and advisory review.
- **DP-24: Clean Worktree Disposal.** A worktree is disposable once its PR is merged and validated. Deletion requires custody proof that no unpushed commits or uncommitted edits remain.
