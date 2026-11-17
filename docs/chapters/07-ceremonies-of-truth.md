<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 7 — Ceremonies of Truth (Althing, Ráð, and Morning Muster)

Agile ceremonies in most engineering teams have deteriorated into performative rituals: twenty-minute daily standups where developers recite status reports to a disengaged manager, biweekly sprint retrospectives where identical complaints are rehashed on digital sticky notes, and sprint planning sessions that resemble poker games rather than engineering design reviews.

RDOM replaces ritual theater with **Ceremonies of Truth**. Every ceremony in RDOM has a single objective: the uncompromising reconciliation of declared intent with observed reality.

```
  +-----------------------------------------------------------------------+
  |                        CEREMONIES OF TRUTH                            |
  +-----------------------------------------------------------------------+
      |
      +---> [ THE ALTHING ]           Quarterly Council: Ratifies Saga's Vow & OKRs
      |
      +---> [ THE RÁÐ ]               Wave Architecture Council: Hoisting & DAG Approval
      |
      +---> [ THE MORNING MUSTER ]    Daily Sync: Blocker, Worktree & Andon Review
      |
      +---> [ THE DOOM VERIFICATION ] Wave Gate: Witnessed Deed Acceptance & Promotion
```

### The Four Ceremonies

#### 1. The Althing (Quarterly Strategic Council)

The assembly of engineering leads, architects, and product operators to review the preceding quarter's execution and ratify the next Saga's Vow.
- **Cadence**: Once per quarter.
- **Inputs**: Valknut OKR scorecard (Faster, Bigger, Cheaper, Effective), preceding wave defect post-mortems, and incoming RLOM initiatives.
- **Outputs**: Ratified Saga's Vow with concrete OKRs, high-level architecture initiatives, and allocated capacity buffers.
- **Truth Criterion**: No initiative is accepted without topological feasibility proof and an assigned principal owner.

#### 2. The Ráð (Wave Architecture & Hoisting Council)

The technical council held before any new topological wave is authorized for execution.
- **Cadence**: At the boundary of each topological wave.
- **Inputs**: Candidate wave DAG, component specifications, proposed interface schemas.
- **Outputs**: Validated wave DAG, ratified DRY hoisting allocations (DP-13, DP-14), and assigned disjoint blast radii for parallel slices (DP-3).
- **Truth Criterion**: If two parallel slices require the same database schema, shared library, or API endpoint, the Ráð halts execution until the shared dependency is hoisted into Wave $N-1$.

#### 3. The Morning Muster (Daily Alignment & Blocker Inspection)

The daily synchronization between human engineers, team leads, and agent coordinators.
- **Cadence**: Daily, 15 minutes maximum (or fully asynchronous via structured summaries).
- **Format**: Three strict questions only:
  1. *What verified deeds were merged into the trunk in the last 24 hours?* (DP-11)
  2. *What isolated worktree slice is currently checked out and what is its blast radius?* (DP-19)
  3. *Is any Andon cord currently pulled or upstream dependency broken?* (DP-5, DP-12)
- **Truth Criterion**: Discussion of unverified work or speculative progress is disallowed. Status is proven by merged PRs and green CI runs.

#### 4. The Doom Verification (Wave Gate Acceptance)

The formal inspection conducted when all tasks in a topological wave claim completion.
- **Cadence**: Upon completion of all nodes in Wave $N$.
- **Inputs**: Aggregated test execution logs, integration test suites, end-to-end smoke test runs, and performance benchmark proofs.
- **Outputs**: Wave certification authorization, unmounting of completed worktrees (DP-24), and unlocking of Wave $N+1$.
- **Truth Criterion**: 100% green test execution. No wave is closed on a promise. If a single verification fails, the wave remains open and the Andon cord is pulled.

> **Augmentation Surface — Automated Muster & Gate Verification**
>
> Where an agent layer transforms this practice: an automated agent aggregates git commit logs, worktree states, and CI statuses into a structured daily muster brief before engineers begin their day, and independently runs the comprehensive Doom verification suite when a wave boundary is reached.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 720
  principle-citations: DP-3, DP-5, DP-11, DP-12, DP-13, DP-14, DP-19, DP-24
  flagged-principle-gaps: none
-->
