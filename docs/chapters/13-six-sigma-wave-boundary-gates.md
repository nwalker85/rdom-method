<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 13 — Six Sigma Wave Boundary Gates (No Exit on a Promise)

In conventional software development, quality assurance is an after-the-fact inspection process. Code is written, merged into a feature branch, and thrown over to QA or staging. If bugs are found, tickets are logged, and developers attempt to recall context they lost two weeks ago. In manufacturing, this is the equivalent of building an automobile with loose bolts, shipping it to the end of the assembly line, and hoping an inspector catches the defect before the customer drives it off the lot.

Six Sigma revolutionized manufacturing by proving that **quality cannot be inspected into a product; it must be built into every process step**. The cost of fixing a defect rises by an order of magnitude at every progressive stage of assembly.

RDOM applies Six Sigma quality control to software engineering through **Wave Boundary Gates** (DP-7) and the **Triad of Proof** (DP-11). No code, branch, or wave is permitted to exit on a promise.

```
  Manufacturing Scrap Model (Late Inspection):
  [ Dev Writes Code ] ──> [ Merges Branch ] ──> [ QA Tests ] ──> [ Production Defect ]
  Cost: $1x                     Cost: $10x          Cost: $100x         Cost: $1,000x

  RDOM Six Sigma Wave Boundary Gate (The Triad of Proof):
  ┌────────────────────────────────────────────────────────────────────────┐
  │ 1. FUNCTIONAL SILICON (Automated Green Tests)                          │
  │    * 0 Linter Warnings (Merge-Base Diffing)                            │
  │    * 0 Type Errors                                                     │
  │    * 100% Passing Unit, Contract & Integration Tests                   │
  ├────────────────────────────────────────────────────────────────────────┤
  │ 2. LIVING DOCUMENTATION (Authoritative Surface)                        │
  │    * AGENTS.md & .agents/ working library updated                      │
  │    * Architecture Decision Records (ADRs) ratified                     │
  │    * Operational runbooks & API/CLI references published               │
  ├────────────────────────────────────────────────────────────────────────┤
  │ 3. THE SHOWCASE / DEMO DEED (Empirical Basis for UAT)                  │
  │    * Executable demonstration walkthrough / interactive sandbox        │
  │    * Witnessed against live running system (DP-10)                     │
  │    * Submitted to RLOM Validation Gate for User Acceptance Testing     │
  └────────────────────────────────────────────────────────────────────────┘
                                     │
                        (PASS)       │       (FAIL)
              ┌──────────────────────┴──────────────────────┐
              ▼                                             ▼
       [ Merged to Trunk ]                       [ ANDON CORD PULLED ]
       [ Wave Advanced ]                         [ Wave Blocked ]
```

### The Invariants of the Wave Boundary Gate

1. **The Triad of Proof Requirement (DP-11)**:
   A feature release or wave completion is never granted on passing code alone. Every feature release must produce:
   - **Functional Code**: Verified green across all test layers.
   - **Living Documentation**: Updated user guides, architecture records, and operational runbooks.
   - **The Showcase / Demonstration Deed**: A recorded or executable demonstration proving the capability operating in a live or staging environment. This showcase is the physical artifact submitted to RLOM for User Acceptance Testing (UAT).
2. **Zero Defect Escape Tolerance (DP-7)**:
   Zero broken contracts, failing tests, or unhandled compiler warnings are allowed to cross from Wave $N$ into Wave $N+1$. A wave does not close when 95% of tasks are finished; it closes only when 100% of tasks have verified green status.
3. **Red-Green-Refactor Proof (DP-8)**:
   Every functional change must demonstrate that its corresponding test suite failed before the implementation was introduced, and passes deterministically afterward.
4. **Witnessed Deed Attachment**:
   Every merged pull request must link to an immutable artifact containing the complete execution trace of the test suite, lint passes, documentation diffs, and showcase artifacts.

### CI Workflow Hygiene: Real Gates vs. The Illusion of Green

In Project Factory (RAV-2037), analysis revealed three critical failure modes that create hollow CI pipelines that appear green while providing zero protection:

#### 1. Merge-Base Diffs, Not No-Ref Diffs

A whitespace, lint, or format check written as a bare `git diff --check` with no revision argument compares the working tree to the index after checkout—which are identical. The check always exits with code 0, silently passing on the very commit that introduced broken formatting. CI lint gates must explicitly diff against the pull request merge base:

```bash
git diff --check "$(git merge-base origin/main HEAD)"...HEAD
```

#### 2. Action Pinning by Commit SHA

Third-party CI Actions must be pinned to full, immutable 40-character commit SHAs, never floating semantic tags (e.g., `@v4`). Floating tags allow external upstream changes to silently alter CI behavior or inject security vulnerabilities without repository changes.

#### 3. Real Runner Scheduler Onboarding

A repository's CI pipeline only protects the estate once it is actively onboarded to automated runner scheduler capacity. Workflows that sit queued indefinitely or run on unmonitored local setups provide zero quality assurance. Onboarding to runner capacity is an explicit gate requirement before repository promotion.

### The Cost of Defect Leakage

When a defect leaks past a wave boundary:
- Downstream workers build on top of broken assumptions.
- Subsequent tasks must be rolled back or patched mid-flight.
- Fleet concurrency collapses as multiple agents fail simultaneously.

By enforcing the Triad of Proof and rigorous CI hygiene at every wave boundary, RDOM guarantees that downstream workers and customer stakeholders build on a verified foundation.

> **Augmentation Surface — Automated Gatekeeper Verification**
>
> Where an agent layer transforms this practice: an automated gatekeeper inspects all pull requests submitted within a wave, verifies merge-base lint cleanliness, validates documentation completeness, executes the automated showcase script, and cryptographically signs the wave completion certificate for UAT review.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 910
  principle-citations: DP-7, DP-8, DP-10, DP-11
  flagged-principle-gaps: none
-->
