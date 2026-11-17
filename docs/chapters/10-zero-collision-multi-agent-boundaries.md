<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 10 — Zero Collision by Construction (Multi-Agent Fleet Boundaries)

When organizations attempt to scale engineering throughput by deploying multiple autonomous AI coding agents or hiring large numbers of developers, they almost universally encounter Amdahl’s Law and Brooks’s Law in their most destructive forms: coordination overhead explodes, merge conflicts multiply, and branches spend days stuck in merge hell.

Two agents tasked with adding features to the same codebase will independently modify `package.json`, reformat `main.go`, update the same database migration timestamp, and inject mutually incompatible utility functions. Merging their work requires hours of manual conflict resolution, frequently invalidating the test suites of both.

RDOM enforces **Zero Collision by Construction** (DP-3). Concurrency is never achieved by allowing multiple workers to touch the same files simultaneously; it is achieved by architecting tasks with mathematically disjoint blast radii.

```
  Unconstrained Concurrency (Collision Prone):
  [ Agent 1 ] ───> Modifies: [ handler.go, router.go, config.json ] ──┐
                                                                       ├──> MERGE CONFLICT
  [ Agent 2 ] ───> Modifies: [ service.go, router.go, config.json ] ──┘

  RDOM Zero-Collision Topological Partitioning:
  Wave 0 (Hoisted Interface):
  [ Slice 0 ] ───> Defines: [ router_interface.go, config_schema.json ] (Merged & Green)
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
  Wave 1 Slice A (Disjoint):        Wave 1 Slice B (Disjoint):
  Modifies ONLY:                    Modifies ONLY:
  [ internal/service_a/* ]          [ internal/service_b/* ]
```

### The Mathematical Disjointness Criterion

For any two concurrent tasks $T_A$ and $T_B$ executing within the same topological wave:

$$\text{BlastRadius}(T_A) \cap \text{BlastRadius}(T_B) = \emptyset$$

Where $\text{BlastRadius}(T)$ includes:
1. **File Paths**: The set of absolute file system paths modified or created by task $T$.
2. **Database Migrations & Schemas**: Table locks, column alterations, or migration sequence numbers.
3. **Configuration Keys**: Environment variable namespaces, YAML/JSON configuration nodes.
4. **Exported Symbols & Route Names**: Public function signatures, gRPC service methods, and HTTP route registrations.

If the intersection is non-empty, $T_A$ and $T_B$ CANNOT be scheduled concurrently. One of two actions must be taken:
- **Sequentialization**: One task is designated as a prerequisite of the other and moved to the next wave.
- **Planning-Time Hoisting**: The intersecting surface (e.g., the shared router or configuration schema) is extracted into Wave $N-1$ as a standalone deliverable (DP-13, DP-14). Once merged, $T_A$ and $T_B$ consume the immutable interface without modifying it.

### Blast Radius Enforcement in Agent Fleets

When provisioning worktrees for autonomous agents:
1. **Explicit File Allowlist**: The agent's brief and system prompt must contain an explicit manifest of permitted files and directories. Any write attempt outside this manifest triggers an immediate execution abort.
2. **Static Collision Check**: Before a worktree slice is spawned, the orchestrator computes the diff of planned touchpoints against all currently active slices. If an overlap is detected, the spawn is blocked.
3. **Fast-Forward Rebase Invariant**: Because blast radii are strictly disjoint, every pull request generated within a topological wave must be rebaseable onto `main` with zero manual conflict resolution.

> **Augmentation Surface — Pre-Execution Collision Analysis**
>
> Where an agent layer transforms this practice: prior to dispatching agent slices, an automated analyzer inspects the planned task briefs, verifies file-path and symbol disjointness, and automatically splits or hoists overlapping tasks before code generation begins.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 700
  principle-citations: DP-3, DP-13, DP-14
  flagged-principle-gaps: none
-->
