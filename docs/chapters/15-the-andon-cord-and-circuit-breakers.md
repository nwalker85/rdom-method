<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 15 — The Andon Cord Protocol & Upstream-Jump Circuit Breakers

In the Toyota Production System, every workstation along the assembly line is equipped with a cord or button called the *Andon*. If any worker—regardless of seniority—notices a defective part, a misalignment, or a safety hazard, they are authorized and expected to pull the cord. The entire production line halts immediately until the root cause is diagnosed and corrected.

In software engineering, the opposite behavior prevails. When a developer working on a Wave 2 integration discovers that an upstream Wave 0 database migration has an invalid constraint or a missing index, they almost never stop the line. Instead, they write an ad-hoc workaround: an in-memory fallback, a monkey patch, or an awkward conditional check. The root defect remains in the upstream code, silently corrupting every other component that touches it.

RDOM institutes **The Andon Cord Protocol** (DP-12) and **The Upstream-Jump Circuit Breaker** (DP-5) to halt defect propagation at the point of origin.

```
  Downstream Monkey-Patching Anti-Pattern:
  [ Upstream Wave 0 DB Defect ] ──> [ Wave 1 Worker A writes patch ]
                                ──> [ Wave 1 Worker B writes different patch ]
                                ──> [ Wave 2 Integration crashes in production ]

  RDOM Andon Cord & Circuit Breaker Protocol:
  [ Wave 1 Task detects Upstream Defect ]
                   │
                   ▼ (ANDON CORD PULLED: DP-12)
  [ EXECUTION HALTED FOR CURRENT SLICE ]
                   │
                   ▼ (CIRCUIT BREAKER ENGAGED: DP-5)
  [ All downstream tasks referencing upstream component are paused ]
                   │
                   ▼
  [ Root Cause Repaired at Upstream Source ]
                   │
                   ▼
  [ Upstream Tests Verified Green (DP-7) ]
                   │
                   ▼
  [ Downstream Worktrees Rebased & Execution Resumed ]
```

### The Upstream-Jump Circuit Breaker (DP-5)

When an engineer or autonomous coding agent in Wave $N$ discovers that an interface, schema, model, or assumption from an earlier wave ($<N$) is flawed:

1. **Immediate Execution Halt**:
   The worker must immediately cease writing code on the downstream task. Continuing to build on a cracked foundation is considered manufacturing sabotage.
2. **Never Patch Downstream**:
   Writing local adapter code, suppressing errors, or working around an upstream structural flaw is strictly forbidden.
3. **Escalate to Root Source**:
   The worker or orchestrator logs an Andon alert, documenting the exact failure mode with observable evidence (DP-10).
4. **Upstream Repair Deed**:
   A targeted repair deed is opened against the upstream component. The upstream test suite is updated to reproduce the failure (Red), the repair is implemented (Green), and the upstream component is verified and merged (DP-8, DP-7).
5. **Clean Rebase & Resume**:
   The downstream worktree is rebased onto the updated upstream commit, verifying that the workaround-free implementation now passes cleanly.

### The Invariants of the Andon Protocol

- **Authority to Halt**: Any human engineer, pull request reviewer, or autonomous agent has the explicit authority to pull the Andon cord. No manager approval is required to halt execution.
- **Blameless Root Cause Analysis**: Pulling the Andon cord is celebrated as an act of defect prevention, not penalized as a delay.
- **Resumption Invariant**: The production line may only be restarted when the root defect has been verified fixed with an automated test.

> **Augmentation Surface — Automated Andon Cord Triggers**
>
> Where an agent layer transforms this practice: an automated supervisor monitors active agent runs and test execution streams. If an agent encounters a broken upstream contract or repeated interface errors, the supervisor automatically pulls the Andon cord, halts dependent worker agents, and notifies the lead architect.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 720
  principle-citations: DP-5, DP-7, DP-8, DP-10, DP-12
  flagged-principle-gaps: none
-->
