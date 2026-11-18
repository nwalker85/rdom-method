# Canonical Principles of RDOM

The **Ravenhelm Development Operations Methodology (RDOM)** is anchored in twenty-four shop-floor principles organized across four operational pillars.

---

## Pillar I: The Dependency Wavefront (The Ehwaz Doctrine & Concurrency)

- **DP-1: The Graph Precedes the Plan.** Every implementation begins with an explicit dependency DAG ($G = (V, E)$). A numbered task list without edges is an unverified hypothesis.
- **DP-2: Topological Wave Partitioning.** Work is partitioned into discrete waves ($W_0, W_1, \dots, W_N$). A wave consists exclusively of tasks whose inbound dependencies have all resolved.
- **DP-3: Zero Collision by Construction.** Concurrent agent slices and human engineers are only dispatched across tasks in the same topological wave with disjoint write surfaces and isolated test schemas. Cross-wave concurrency is forbidden.
- **DP-4: The Critical Chain Floor.** The longest dependent path through the graph is identified before execution begins. It sets the floor on total delivery time and receives primary resource focus; non-critical paths are managed as buffered slack.
- **DP-5: Upstream-Jump Circuit Breaker.** No worker may branch outward to implement, stub, or mock against an unfinished upstream dependency. If an upstream block occurs, the worker halts and pulls the Andon cord.
- **DP-6: Progressive JIT Elaboration.** Only the currently active wave ($W_k$) receives granular, bite-sized TDD implementation specifications. Specifying code steps for Wave $W_{k+2}$ is inventory waste (*Muda*) that rots before execution.

---

## Pillar II: Six Sigma Defect Prevention & TDD Gates

- **DP-7: Verified Green Precedes Promotion.** Wave $W_{k+1}$ cannot open on a verbal assurance or a mock pass. It opens strictly when all exit criteria of Wave $W_k$ pass mechanical verification against the live running system using checks that prove they can fail.
- **DP-8: Red-Green-Refactor as State Transitions.** A task does not begin with an implementation edit. It begins with a failing test asserting expected behavior, followed by minimal passing code, followed by refactoring.
- **DP-9: Poka-Yoke Interface Design.** Public APIs, component models, CLI flags, and tool permission profiles must make invalid states unrepresentable and keep the safe verification path cheaper than guessing.
- **DP-10: Live Running System as Truth.** Hypotheses and fixes are confirmed against the live running kernel, container, or network state and the production entrypoint call graph; never against stale documentation, memory, or isolated mocks.
- **DP-11: Witnessed Deliverable Attachment (The Triad of Proof).** A feature release or wave completion is never done on passing code alone. It requires the complete Triad of Proof: deterministic automated test verification with caller parity, updated documentation/runbooks, and an executable showcase that serves as the factual basis for RLOM User Acceptance Testing (UAT).
- **DP-12: The Andon Cord Protocol.** When an unresolvable defect, broken upstream invariant, or silent data corruption is detected, halt downstream dispatch immediately and inspect uncommitted worktree diffs before discarding any lane.

---

## Pillar III: DRY Architecture & Anti-Snowflake Hoisting

- **DP-13: Planning-Time DRY Refactoring.** Before a plan is ratified, scan the graph for duplicate capability across slices. Refactor the graph to prevent snowflakes before code is written.
- **DP-14: The Hoist-vs-Defer Rule.** If an interface is *known* (from diagnosed defects or established standards), hoist it upstream into an earlier wave as a shared crate/library. If *guessed*, allow the first consumer to build it inline and schedule an explicit extraction task.
- **DP-15: Zero Unacknowledged Duplication (Consumption Contract).** A repo or slice may decline to use an established estate surface, but it may not do so silently. Every identified repeat must either be hoisted or bound to a scheduled extraction issue or explicit `consumes_exemption`.
- **DP-16: Scaffolding from Working Reality.** Never build abstract frameworks in a vacuum. Scaffolds, SDKs, and base classes are extracted only from working, production-proven reference implementations.
- **DP-17: Shared Substrate Invariance.** Platform-wide substrates (gateway, observability, secrets and elevation, OCI registry) are invariant across repositories; never re-implemented per service.
- **DP-18: Locality Invariance (`AGENTS.md` Authority).** Every repository, platform, and product carries an authoritative `AGENTS.md` at its root that travels with code in pull requests.

---

## Pillar IV: Workspace Custody & Multi-Agent Ergonomics

- **DP-19: Dedicated Worktree Custody.** Every task slice operates in an isolated, disposable git worktree projected from a single canonical `.bare/` repository with an explicit fetch refspec, adhering to the Checkout Custody Standard.
- **DP-20: Anti-Thrash Context Priming.** Agents must never crawl directories blindly or dump whole files into context. Orientation uses `<800`-token topological digests (`eat prime`) and `<10ms` AST byte-range reads (`eat read`) to preserve context budgets.
- **DP-21: Zero Ambient Mutation on Production Hosts.** Development work never directly edits live configurations or files on server hosts via SSH. All mutations pass through source repos, PRs, and RROM deployment rails.
- **DP-22: WIP Commit Checkpointing.** Never use `git stash` across branch switches. Session momentum is preserved via WIP commits and quicksave snapshots before risky operations.
- **DP-23: The Pull Request Boundary & Supervisor Merge Gate.** Direct pushes to `main` or `develop` are physically barred. Workers open pull requests with the Triad of Proof; only the supervisor who received explicit human approval executes the squash merge and triggers deployment.
- **DP-24: Custody-Gated Worktree Disposal.** A worktree is disposable once its PR is merged and validated. Deletion requires custody proof that no unpushed commits or uncommitted edits remain.
