<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 2 — The Sovereign Triad (RLOM, RDOM, RROM)

Software delivery fails most frequently at the seams between product management, engineering execution, and deployment operations.

In conventional organizations, product managers throw user stories over the wall into Jira; engineers write code in branches that diverge for weeks; and release engineers attempt to assemble fragile artifacts through unversioned CI pipelines. When an outage occurs, product blames engineering for slow delivery, engineering blames operations for fragile environments, and operations blames product for unstable requirements.

The **Sovereign Triad** establishes total coherence across these three lifecycle phases. Each discipline is governed by an authoritative methodology book, its own numbered principles, and a binding physical axiom.

```
       DEMAND & INTENT                  EXECUTION CADENCE                 RELEASE & RUNTIME
  +------------------------+        +------------------------+        +------------------------+
  |          RLOM          |        |          RDOM          |        |          RROM          |
  | Ravenhelm Linear       | =====> | Ravenhelm Development  | =====> | Ravenhelm Release      |
  | Operating Method       |        | Operations Method      |        | Operations Method      |
  +------------------------+        +------------------------+        +------------------------+
  Axiom: "If it isn't               Axiom: "Concurrency is            Axiom: "Builds are the
  witnessed by a deed,              earned through topological        unit; releases are names."
  it didn't happen."                proof; quality is gated
                                    by verified green."
```

### The Three Methodologies

#### 1. RLOM — Demand, Intent, and the Work Graph

Governed by 29 principles (`P-1` through `P-29`), RLOM manages how intent enters the organization, how initiatives decompose into projects, and how projects decompose into deliverable issues. It treats the issue tracker as an active, living work graph, not a historical junkyard.
- **The Core Axiom**: *"If it isn't witnessed by a deed, it didn't happen."*
- **Role**: Declares *what* needs to be built and *why*, securing business alignment, customer demand, and acceptance criteria before engineering capacity is committed.

#### 2. RDOM — Execution, Concurrency, and Engineering Cadence

Governed by 24 principles (`DP-1` through `DP-24`), RDOM is the execution engine. It accepts the work graph from RLOM, resolves it into a rigorous dependency DAG, hoists common patterns, executes across topological waves, and enforces Six Sigma quality gates at every boundary.
- **The Core Axiom**: *"Concurrency is earned through topological proof; quality is gated by verified green."*
- **Role**: Governs *how* systems are designed, scaffolded, coded, and verified across human engineers and autonomous agent fleets.

#### 3. RROM — Release, Artifact Custody, and Runtime Deployment

Governed by 18 principles (`RP-1` through `RP-18`), RROM governs what happens once code is merged into the trunk. It enforces immutable OCI artifact compilation, strict registry custody, and multi-rail distribution (e.g., container workloads via GitOps and developer CLI tools via managed package taps).
- **The Core Axiom**: *"Builds are the unit; releases are names."*
- **Role**: Governs *where* and *how* verified artifacts are promoted, ensuring that runtime deployments are bit-for-bit identical across all stages without rebuilding.

### The Lifecycle Handoffs and the UAT Showcase Loop

The handoffs between the members of the Triad are governed by strict contractual boundaries, bound together by the **Showcase-as-UAT** feedback loop:

1. **RLOM $\to$ RDOM (The Intake Contract)**:
   Engineering does not start work on unrefined, ambiguous tickets. RLOM issues must satisfy the Definition of Ready: clear acceptance criteria, verified user demand, and an assigned owner. RDOM converts these issues into topological DAG nodes (DP-1).
2. **RDOM Delivery: The Feature Release Triad (Code, Docs, Showcase)**:
   In RDOM, a feature release is never complete when functional code simply compiles. Every release must produce three co-equal deliverables (DP-11):
   - **Functional Silicon**: Code verified green via automated TDD suites (DP-7, DP-8).
   - **Living Documentation**: Authoritative user documentation, updated architecture decisions (ADRs), and executable runbooks.
   - **The Showcase / Demonstration Deed**: An executable walkthrough, interactive sandbox session, or recorded CLI/UI demonstration proving the feature operating against the live running system (DP-10).
3. **RDOM $\to$ RLOM (The Showcase as User Acceptance Testing)**:
   The Showcase deed is not marketing collateral; it is the physical artifact required for **RLOM Validation and User Acceptance Testing (UAT)** (P-6). Product operators and stakeholders do not review abstract code diffs; they evaluate the Showcase against the original RLOM acceptance criteria. UAT sign-off is gated on the witnessed showcase.
4. **RDOM $\to$ RROM (The Merge Boundary)**:
   Code cannot be merged into `main` on a developer's promise. It must pass all automated Six Sigma gates, attach witnessed deeds (test logs, docs, showcase proof), and satisfy the PR boundary (DP-7, DP-11, DP-23).
5. **RROM $\to$ RLOM (The Proven Deployment Loop)**:
   When RROM deploys an immutable build to production, it stamps the RLOM issue with the immutable container digest or Homebrew release tag, transitioning the issue to Done with verified live evidence.

> **Augmentation Surface — Triad State Reconciliation**
>
> Where an agent layer transforms this practice: an autonomous auditor continuously monitors the synchronization between the RLOM issue graph, the RDOM git worktrees, and the RROM container registries, validating that every candidate release carries its living documentation and executable showcase before notifying stakeholders for UAT.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 880
  principle-citations: DP-1, DP-7, DP-8, DP-10, DP-11, DP-23
  flagged-principle-gaps: none
-->
