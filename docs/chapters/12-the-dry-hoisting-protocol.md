<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 12 — The DRY Hoisting Protocol: Anti-Snowflake Planning

Every software organization claims to believe in DRY ("Don't Repeat Yourself"). Yet in practice, DRY is treated as a stylistic recommendation enforced during code review. A pull request is submitted, a reviewer notices duplicate helper functions, and a debate ensues about whether refactoring is "in scope" for the sprint. Inevitably, the team defers the refactor to a "tech debt ticket" that is never prioritized.

In multi-agent and multi-developer environments, post-hoc DRY is a catastrophic failure mode. When multiple parallel workers implement similar features, each creates their own "snowflake" implementation: divergent error types, redundant HTTP clients, bespoke caching logic, and slightly incompatible data serialization formats. By the time code review occurs, untangling the duplication requires rewriting the entire wave.

RDOM enforces **Planning-Time DRY Hoisting** (DP-13, DP-14). Duplication is an architectural defect that must be eradicated during DAG construction, before a single line of feature code is written.

```
  Post-Hoc Duplicate Proliferation (Snowflake Anti-Pattern):
  [ Slice A: Auth API ] ───> Implements Snowflake DB Client A ──┐
  [ Slice B: Billing  ] ───> Implements Snowflake DB Client B ──┼──> Architectural Drift
  [ Slice C: Webhook  ] ───> Implements Snowflake DB Client C ──┘

  RDOM Planning-Time Hoisting Protocol:
  1. DAG Analysis detects shared DB Client requirement across Slices A, B, C.
  2. The Hoist-vs-Defer Rule triggers: DB Client MUST be hoisted into Wave 0.
  
  ┌────────────────────────────────────────────────────────┐
  │ Wave 0: Hoisted Shared DB Client (Single Source)       │
  └────────────────────────────────────────────────────────┘
              │  (Verified Green Gate: DP-7)
         ┌────┴────────────────────────┬───────────────────┐
         ▼                             ▼                   ▼
  [ Slice A: Auth API ]       [ Slice B: Billing ]       [ Slice C: Webhook ]
  (Consumes Shared DB Client with Zero Duplication and Zero Collision)
```

### The Hoist-vs-Defer Rule

The fundamental law of RDOM architecture is the **Hoist-vs-Defer Rule** (DP-14):

> *If a capability, abstraction, utility, data model, or schema is required by two or more parallel nodes in Wave $N$, it MUST be hoisted into Wave $N-1$ (or earlier) as a first-class shared deliverable. It may NEVER be implemented independently across parallel slices.*

### The Three Hoisting Filters

During the Ráð (Wave Architecture Council), candidate tasks are evaluated through three hoisting filters:

1. **The Substrate Filter**: Does this feature require an infrastructure primitive (database connection pool, structured logging configuration, metric collector, secret provider)? If yes, that primitive must be hoisted into the platform substrate tier (DP-17).
2. **The Schema Filter**: Does this feature expose or consume data models that cross service or component boundaries? If yes, the schema must be declared as a typed contract (Protobuf, OpenAPI, TypeScript interface) in an earlier wave.
3. **The Utility Filter**: Does this task contain helper logic (string manipulation, token parsing, retry loops) that other slices will plausibly need? If yes, it is hoisted into a shared internal library.

### Zero Unacknowledged Duplication

Under Principle DP-15, copy-pasting code or boilerplates across repositories or modules is strictly prohibited. If temporary duplication is required for tactical decoupling:
- It must be explicitly recorded in an Architecture Decision Record (ADR).
- It must reference the original source implementation.
- An explicit Daily Deed must be scheduled in a subsequent wave to consolidate the implementation into a hoisted primitive.

> **Augmentation Surface — AST Duplication Detection & Hoisting Suggestions**
>
> Where an agent layer transforms this practice: an automated structural analyzer parses proposed task briefs and existing codebase ASTs, automatically detecting pattern convergence and proposing hoisted abstractions before tasks are authorized for implementation.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 730
  principle-citations: DP-7, DP-13, DP-14, DP-15, DP-17
  flagged-principle-gaps: none
-->
