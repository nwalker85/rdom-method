<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 9 — Topological Waves: Replacing the Two-Week Sprint

The two-week sprint is the most pervasive anti-pattern in modern software development. Invented as a crude timeboxing mechanism to force predictability onto unpredictable work, sprints create artificial deadlines that incentivize engineers to cut corners, defer testing, and ship half-baked code to "make sprint cutoff."

Even worse, sprints treat all backlog items as if they exist on a flat plane. A database migration ticket, a frontend UI ticket, and a billing integration ticket are all scheduled into the same two-week window. The frontend engineer waits five days for the database migration to land, rushes the integration in thirty-six hours, and pushes an unverified commit on Friday afternoon. On Monday, the team starts the next sprint while the previous sprint's work generates bug tickets that pollute the backlog for the next six weeks.

RDOM completely eliminates the calendar sprint. In its place, it installs **Topological Wave Execution** (DP-2).

```
  Traditional Two-Week Sprint (Temporal Blindness):
  ┌────────────────────────────────────────────────────────┐
  │ Sprint 14 (Calendar Days 1-14)                         │
  │ [DB Schema]  [API Endpoint]  [UI Screen]  [Worker Job] │ <-- Simultaneous thrash,
  └────────────────────────────────────────────────────────┘     hidden dependencies

  RDOM Topological Wave Structure (Structural Progression):
  ┌────────────────────────┐
  │ Wave 0: Foundations    │  DB Migrations, Shared Schemas, Client SDKs
  └────────────────────────┘
              │  (Verified Green Gate: DP-7)
              ▼
  ┌────────────────────────┐
  │ Wave 1: Core Services  │  Service A Worker, Service B API (Disjoint Blast Radii)
  └────────────────────────┘
              │  (Verified Green Gate: DP-7)
              ▼
  ┌────────────────────────┐
  │ Wave 2: Composite Flow │  Integration Layer, Cross-Service Telemetry, UI Flow
  └────────────────────────┘
              │  (Verified Green Gate: DP-7)
              ▼
  ┌────────────────────────┐
  │ Wave 3: E2E & Gate     │  End-to-End Synthetic Tests, Performance Verification
  └────────────────────────┘
```

### The Wave Progression Model

A topological wave is not a timebox; it is an event-driven execution wavefront governed by structural dependencies:

#### Wave 0: Substrates and Foundations

- **Scope**: Database migrations, protocol buffer schemas, OpenAPI specifications, shared core libraries, configuration contracts, and mock test servers.
- **Exit Gate**: All migrations tested against local instances, schema packages published and versioned, mock interfaces accessible to downstream consumers.

#### Wave 1: Independent Core Components

- **Scope**: Autonomous services, workers, handlers, and models that consume Wave 0 foundations but have completely disjoint blast radii from one another (DP-3).
- **Execution**: Multiple engineers or autonomous coding agents work in parallel worktrees with zero collision risk.
- **Exit Gate**: 100% unit test coverage, green contract validation tests against Wave 0 schemas.

#### Wave 2: Composite Integrations and Consumers

- **Scope**: Orchestration pipelines, gateway routing, user interface workflows, and cross-service event handlers that compose Wave 1 components.
- **Exit Gate**: Successful integration test suites verifying data flow across multiple services.

#### Wave 3: End-to-End System Verification

- **Scope**: Synthetic transaction tests, performance benchmarks, chaos drills, and deployment artifact validation.
- **Exit Gate**: Wave Doom verification passes cleanly with zero defects (DP-7, DP-11).

### The Invariants of Wave Progression

1. **No Leapfrogging**: No task in Wave $N+1$ may begin until all prerequisite nodes in Wave $N$ have merged into trunk and passed CI verification (DP-2, DP-7).
2. **Variable Duration**: A wave lasts as long as required to achieve verified green—whether four hours or four days. There is no calendar cutoff.
3. **Zero Rollover**: Tasks do not "roll over" into the next wave. If a task fails or stalls, the wave remains open and the Andon cord is pulled (DP-12).
4. **Instant Advancement**: The moment the final gate of Wave $N$ turns green, Wave $N+1$ worktrees are authorized immediately without waiting for a planning meeting.

> **Augmentation Surface — Automated Wave Gate Orchestration**
>
> Where an agent layer transforms this practice: the orchestration system continuously listens to CI completion webhooks. As soon as all Wave $N$ pull requests are merged and verified, the orchestrator automatically provisions the isolated worktrees and briefs for all Wave $N+1$ tasks.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 740
  principle-citations: DP-2, DP-3, DP-7, DP-11, DP-12
  flagged-principle-gaps: none
-->
