<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 13 — Six Sigma Wave Boundary Gates (No Exit on a Promise)

In conventional software development, quality assurance is an after-the-fact inspection process. Code is written, merged into a feature branch, and thrown over to QA or staging. If bugs are found, tickets are logged, and developers attempt to recall context they lost two weeks ago. In manufacturing, this is the equivalent of building an automobile with loose bolts, shipping it to the end of the assembly line, and hoping an inspector catches the defect before the customer drives it off the lot.

Six Sigma revolutionized manufacturing by proving that **quality cannot be inspected into a product; it must be built into every process step**. The cost of fixing a defect rises by an order of magnitude at every progressive stage of assembly.

RDOM applies Six Sigma quality control to software engineering through **Wave Boundary Gates** (DP-7). No code, branch, or wave is permitted to exit on a promise.

```
  Manufacturing Scrap Model (Late Inspection):
  [ Dev Writes Code ] ──> [ Merges Branch ] ──> [ QA Tests ] ──> [ Production Defect ]
  Cost: $1x                     Cost: $10x          Cost: $100x         Cost: $1,000x

  RDOM Six Sigma Gate Model (Defect Prevention at the Source):
  ┌────────────────────────────────────────────────────────────────────────┐
  │ ATOMIC WORKTREE SLICE                                                  │
  │ [ Red Test ] ──> [ Minimal Green Code ] ──> [ Structural Refactor ]   │
  └────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ WAVE BOUNDARY DEFECT GATE (DP-7)                                       │
  │ [ Static Analysis / Linters ] : 0 Warnings                             │
  │ [ Strict Type Checking ]      : 0 Errors                               │
  │ [ Unit & Contract Test Suite ]: 100% Pass                              │
  │ [ Integration Smoke Tests ]   : 100% Pass                              │
  │ [ Witnessed Deed Attached ]   : CI Log Digest (DP-11)                  │
  └────────────────────────────────────────────────────────────────────────┘
                                     │
                        (PASS)       │       (FAIL)
              ┌──────────────────────┴──────────────────────┐
              ▼                                             ▼
       [ Merged to Trunk ]                       [ ANDON CORD PULLED ]
       [ Wave Advanced ]                         [ Wave Blocked ]
```

### The Invariants of the Wave Boundary Gate

1. **Zero Defect Escape Tolerance**: Zero broken contracts, failing tests, or unhandled compiler warnings are allowed to cross from Wave $N$ into Wave $N+1$. A wave does not close when 95% of tasks are finished; it closes only when 100% of tasks have verified green status (DP-7).
2. **Red-Green-Refactor Proof (DP-8)**: Every functional change must demonstrate that its corresponding test suite failed before the implementation was introduced, and passes deterministically afterward. For autonomous coding agents, the agent's log must record the execution of the failing test as proof of test validity.
3. **Deterministic CI Verification**: Local execution logs ("it works on my machine") are not accepted as truth. Verification must occur within a clean, containerized CI runner that mirrors production runtime invariants.
4. **Witnessed Deed Attachment (DP-11)**: Every merged pull request must link to an immutable artifact containing the complete execution trace of the test suite and static analysis passes.

### The Cost of Defect Leakage

When a defect leaks past a wave boundary:
- Downstream workers build on top of broken assumptions.
- Subsequent tasks must be rolled back or patched mid-flight.
- Fleet concurrency collapses as multiple agents fail simultaneously.

By enforcing an absolute quality gate at the wave boundary, RDOM ensures that downstream workers always build upon an unshakable, verified foundation.

> **Augmentation Surface — Automated Gatekeeper Verification**
>
> Where an agent layer transforms this practice: an automated gatekeeper inspects all pull requests submitted within a wave, runs comprehensive test suites in parallel ephemeral containers, and cryptographically signs the wave completion certificate only when all quality criteria are met.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 710
  principle-citations: DP-7, DP-8, DP-11
  flagged-principle-gaps: none
-->
