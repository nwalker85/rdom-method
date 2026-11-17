<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 3 — The 24 Numbered Principles

RDOM is governed by 24 authoritative principles organized into four structural pillars. These principles are not aspirational recommendations; they are enforceable engineering invariants. Every workflow, pull request, and agent orchestration script must satisfy these constraints.

### Pillar I: Topological Concurrency & The Ehwaz Doctrine

- **DP-1: The Graph Precedes the Plan.** Every project, feature, or refactor must be expressed as a Directed Acyclic Graph (DAG) of dependency-linked units of work before execution begins. No implementation work is authorized without a validated DAG.
- **DP-2: Topological Wave Execution.** Work progresses in discrete topological waves: Wave 0 (shared substrates/foundations), Wave 1 (independent core services/components), Wave 2 (composite consumers/integrations), Wave 3 (end-to-end verification, documentation, and showcase). No Wave $N+1$ task may begin implementation until all Wave $N$ prerequisites are verified green.
- **DP-3: Zero Collision by Construction.** Parallel workstreams—whether manned by humans, AI coding agents, or hybrid pairs—must have disjoint blast radii. Shared files, interfaces, or tables must be resolved in an earlier wave or owned by a single slice. Concurrent editing of the same file across branches is an architectural defect.
- **DP-4: The Critical Chain Floor.** Resource contention across agent fleets and human reviewers dictates velocity, not optimistic critical paths. Capacity buffers must be placed at the convergence points of topological waves.
- **DP-5: The Upstream-Jump Circuit Breaker.** If an implementation task in Wave $N$ discovers that an upstream interface, schema, or assumption from Wave $<N$ is broken, work on that task halts immediately. Downstream work is paused until the upstream defect is repaired, tested, and reverified.
- **DP-6: Progressive Just-In-Time Elaboration.** Do not detail tasks in Wave 3 while Wave 0 is still in flight. Tasks are elaborated to exact implementation specifications just before their wave opens, incorporating live learnings from earlier waves.

### Pillar II: Six Sigma Defect Prevention & TDD

- **DP-7: Verified Green Precedes Promotion.** No pull request, wave boundary, or deliverable is accepted on the promise of "it compiles locally." Every transition requires deterministic, automated proof: unit tests, integration tests, type checks, and linting must pass cleanly in CI backed by active runner capacity.
- **DP-8: Red-Green-Refactor Transitions.** Every functional change must begin with an observable failing test (Red), proceed to the minimal implementation required to pass (Green), and conclude with structural optimization without altering behavior (Refactor). Agent fleets must demonstrate test failure prior to passing implementation.
- **DP-9: Poka-Yoke Interface Design.** Interfaces, CLI parameters, and API endpoints must be designed so that incorrect usage is impossible by construction. Strong typing, exhaustive enums, schema validation, and fail-fast invariants prevent defects from entering the execution pipeline.
- **DP-10: The Live Running System as Truth.** Hypotheses, debugging theories, and architecture decisions must be verified against the live running system, not stale documentation, cached memory, or local assumptions.
- **DP-11: Witnessed Deed Attachment (Code, Docs, Showcase).** A feature release is never complete on passing code alone. Every deliverable requires the complete Triad of Proof: verified automated tests, living user documentation and runbooks, and an executable showcase or walkthrough that serves as the factual basis for RLOM User Acceptance Testing (UAT).
- **DP-12: The Andon Cord Protocol.** Any engineer, reviewer, or automated agent has the authority and obligation to pull the Andon cord and halt wave execution upon detecting a failing test, an architecture drift, a broken contract, or an unverified dependency.

### Pillar III: DRY Architecture & Hoisting

- **DP-13: Planning-Time DRY Refactoring.** Duplication is an architectural defect that must be eliminated during DAG design, not during post-hoc code review. Common utilities, client libraries, data models, and configurations must be identified and extracted before parallel execution begins.
- **DP-14: The Hoist-vs-Defer Rule.** If a capability, schema, or abstraction is needed by two or more parallel nodes in Wave $N$, it MUST be hoisted into Wave $N-1$ as a shared primitive. It may never be implemented twice under the excuse of expediency.
- **DP-15: Zero Unacknowledged Duplication (The Consumption Contract).** A repo or slice may decline to use an established estate surface, but it may not do so silently. Every identified duplicate must be hoisted, and bypassing an existing platform library requires an explicit `consumes_exemption` recorded in the pull request.
- **DP-16: Scaffolding from Working Reality.** New components, services, and agent harnesses must be scaffolded from proven, working implementations within the estate, never synthesized from generic LLM training priors.
- **DP-17: Shared Substrate Invariance.** Platform foundations—logging frameworks, telemetry collectors, database connection pools, authentication middleware—must remain invariant across all application services. Applications adapt to the substrate; the substrate does not fork for applications.
- **DP-18: Locality Invariance.** Every repository, subsystem, or platform tier must maintain its own authoritative governance and documentation (`AGENTS.md`) at its root. Cross-cutting knowledge is hoisted; local implementation detail remains strictly local.

### Pillar IV: Workspace Custody & Ergonomics

- **DP-19: Dedicated Worktree Custody.** Every task, branch, and agent execution must operate within an isolated git worktree projected from a canonical bare repository (`.bare/`). Direct modification of the primary working tree is forbidden. Every repository implements the Repo Agent Bootstrap Standard (`AGENTS.md` + `.agents/` working library).
- **DP-20: Anti-Thrash Context Priming.** Agents and engineers must prime context via surgical topological indexing and AST slice retrieval (`eat prime`, `eat read`) rather than brute-force directory traversals or whole-file dumping. Context waste is considered manufacturing scrap.
- **DP-21: Zero Ambient Mutation on Hosts.** Development and testing must never mutate host configuration, ambient system packages, or global states directly. All mutations must occur within containers, ephemeral worktrees, or isolated sandboxes.
- **DP-22: WIP Commit Checkpointing.** State persistence is cheap and mandatory. Engineers and agents must snapshot dirty working state with frequent, structured WIP commits rather than fragile, non-portable git stashes.
- **DP-23: The PR Boundary.** No code enters `main` or `develop` without passing through a formal Pull Request / Merge Request. Merging requires explicit, witnessed human approval and automated verification gates.
- **DP-24: Clean Worktree Disposal.** Once a branch is merged and deployed, its corresponding worktree must be safely unmounted and purged after verifying that all custody records, commits, and artifacts have been reconciled.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 1040
  principle-citations: DP-1, DP-2, DP-3, DP-4, DP-5, DP-6, DP-7, DP-8, DP-9, DP-10, DP-11, DP-12, DP-13, DP-14, DP-15, DP-16, DP-17, DP-18, DP-19, DP-20, DP-21, DP-22, DP-23, DP-24
  flagged-principle-gaps: none
-->
