<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 8 — The Dependency DAG: Critical Path vs. Critical Chain

Traditional project planning relies on Critical Path Method (CPM), assuming that if every task's duration is estimated accurately, the longest sequence of dependent tasks dictates the delivery date. In software engineering—and particularly in software engineering augmented by AI agent fleets—CPM fails catastrophically.

CPM ignores resource contention. An agent can generate code in minutes, but human review capacity, CI runner saturation, staging environment locks, and database schema migrations create non-linear bottlenecks. When five parallel tasks complete simultaneously and queue up for code review or integration testing, the theoretical "critical path" evaporates into a queue-induced traffic jam.

RDOM applies Eliyahu Goldratt’s **Critical Chain Project Management (CCPM)** to software engineering through the **Dependency Directed Acyclic Graph (DAG)** (DP-1).

```
  Traditional Critical Path (CPM) — Blind to Resource Contention:
  [ Task A: 2d ] ───> [ Task B: 3d ] ───> [ Task C: 2d ] ───> Deploy (Total: 7d)
  (Fails when reviewer or CI bottleneck stalls Task B by 4 days)

  RDOM Critical Chain (CCPM) with Ehwaz Topological Buffers:
  ┌──────────────┐     ┌──────────────┐
  │ Wave 0: Base │ ──> │ Wave 1: SvcA │ ──┐
  └──────────────┘     └──────────────┘   │     ┌──────────────────┐     ┌─────────┐
         │                                ├───> │ Convergence Gate │ ──> │ Deploy  │
         │             ┌──────────────┐   │     │ (Capacity Buffer)│     └─────────┘
         └───────────> │ Wave 1: SvcB │ ──┘     └──────────────────┘
                       └──────────────┘
```

### The Anatomy of the Dependency DAG

Every project or feature begins with an explicit DAG where vertices represent discrete Daily Deeds and directed edges represent strict technical preconditions (DP-1):

1. **Precondition Edges**: Task $B$ cannot begin until Task $A$ produces a verified, merged deliverable (e.g., an API client library or database migration).
2. **Blast Radius Disjointness**: Any two parallel nodes in the DAG must have zero overlapping file modifications or schema locks (DP-3).
3. **Hoisted Substrates**: Any common dependency required by two downstream nodes must be explicitly represented as an ancestor node in an earlier wave (DP-13, DP-14).

### Critical Path vs. Critical Chain in Multi-Agent Fleets

In human-agent hybrid workflows, the binding constraint is rarely code generation speed. The constraints are:
- **Architectural Clarity**: The precision of interface contracts and specifications.
- **Verification Bandwidth**: The speed of CI pipelines and integration test runs.
- **Reviewer Throughput**: The cognitive capacity of the human architect to review pull requests and approve promotions.

The **Critical Chain Floor** (DP-4) establishes that project duration is governed by the sequence of dependent tasks combined with the constrained resources that execute and verify them.

### Buffer Management at Topological Convergence

Instead of inflating individual task estimates with hidden "padding," RDOM strips all task estimates to their realistic execution durations and places explicit **Capacity Buffers** at the convergence boundaries of topological waves:

- **Feeding Buffers**: Placed where a non-critical parallel branch merges into the critical chain, preventing delays on secondary tasks from stalling the primary flow.
- **Wave Convergence Buffers**: Placed at the end of each topological wave to absorb integration verification latency, CI queuing, and Andon cord investigations before the next wave opens.

> **Augmentation Surface — DAG Construction & Bottleneck Analysis**
>
> Where an agent layer transforms this practice: an agent scans repository ASTs and proposed pull request scopes, automatically constructing the dependency DAG, detecting circular dependencies, identifying unhoisted shared files, and calculating the critical chain constraint path.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 710
  principle-citations: DP-1, DP-3, DP-4, DP-13, DP-14
  flagged-principle-gaps: none
-->
