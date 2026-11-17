<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 4 — The Hierarchy of Deeds (Wyrd Rune to Daily Deed)

When strategic vision fails to translate into working software, the breakdown rarely happens at the level of individual lines of code. It happens because there is a broken chain of custody between an organization's high-level objectives and the daily commits pushed by engineers and agents.

In traditional agile shops, this breakdown is masked by arbitrary "Epics" and "User Stories" floating in Jira without formal hierarchy or dependency linkages. A company objective is announced in January; by March, developers are working on tickets whose connection to that objective is purely coincidental.

The **Hierarchy of Deeds** establishes a rigorous, unbroken chain of custody from the sovereign strategic intent down to the atomic commit.

```
       [ WYRD RUNE ]           Unchanging Sovereign North Star (Multi-Year)
             │
             ▼
       [ LONG-SAGA ]           Annual Strategic Objective / Architectural Initiative
             │
             ▼
      [ SAGA'S VOW ]           Quarterly Commitment / Milestone / Engineering OKR
             │
             ▼
     [ TOPOLOGICAL WAVE ]      Coherent Dependency Wavefront (Ehwaz Wave 0..N)
             │
             ▼
       [ DAILY DEED ]          Atomic, TDD-Gated Task / Scoped Pull Request
```

### The Five Levels of Deed Custody

#### 1. The Wyrd Rune (Sovereign North Star)

The highest tier of intent. The Wyrd Rune represents the multi-year existential purpose and competitive moat of the platform. It rarely changes and defines the boundary of what the organization will and will not build.

#### 2. The Long-Saga (Annual Strategic Initiative)

The multi-quarter architectural and product themes that advance the Wyrd Rune. Examples include: *Transition to Autonomous Fleet Operations*, *Multi-Region Active-Active Data Mesh*, or *Unified Developer Substrate*. Each Long-Saga has clear business justification, an assigned principal owner, and measurable annual goals.

#### 3. The Saga's Vow (Quarterly Commitment / Engineering OKRs)

The binding quarterly contract between leadership and engineering. In the Valknut cadence, this replaces the bloated "Program Increment" (PI) with four concrete engineering OKR dimensions: **Faster, Bigger, Cheaper, Effective** (detailed in Chapter 6). A Saga's Vow is not a wish list; it is a scoped set of deliverables backed by topological feasibility analysis.

#### 4. The Topological Wave (Ehwaz Execution Wavefront)

Within each Saga's Vow, execution does not occur in arbitrary two-week sprints. It is decomposed into a Directed Acyclic Graph (DAG) executed across topological waves (Wave 0 through Wave $N$). A wave represents a set of independent tasks whose prerequisites have all been verified green in prior waves (DP-1, DP-2).

#### 5. The Daily Deed (Atomic Deliverable Slice)

The terminal unit of execution. A Daily Deed is an atomic, test-driven change implemented in an isolated worktree (DP-19). It represents a single, reviewable pull request that moves the repository from one verified state to another. A deed is never marked complete without an attached, witnessed artifact: test logs, terminal recordings, or CI build digests (DP-11).

### The Invariants of Deed Custody

1. **Every commit must trace to a Deed.** Unanchored work is manufacturing waste. If an engineer or agent is writing code that does not fulfill an active Deed, that work is stopped immediately.
2. **Every Deed must trace to a Wave.** Independent tasks cannot exist outside the topological dependency graph. If a task has no predecessors or successors, it is either an unhoisted platform utility or unaligned work.
3. **Every Wave must trace to a Saga's Vow.** Technical efforts must produce measurable progress against an explicit quarterly commitment.
4. **No promotion without witnessed deeds.** Work is verified at every boundary. If a deed has no passing test evidence, it does not exist (DP-7, DP-11).

> **Augmentation Surface — Lineage Traceability**
>
> Where an agent layer transforms this practice: an automated governance agent evaluates every incoming PR, verifying that its branch metadata links to an active Daily Deed, that the deed belongs to the currently active Topological Wave, and that all upstream dependencies have achieved green verification.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 730
  principle-citations: DP-1, DP-2, DP-7, DP-11, DP-19
  flagged-principle-gaps: none
-->
