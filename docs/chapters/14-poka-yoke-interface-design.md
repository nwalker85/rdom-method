<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 14 — Poka-Yoke Interface Design & The Live System Rule

In Japanese lean manufacturing, *Poka-Yoke* refers to mistake-proofing mechanisms designed into the physical tooling so that an operator literally cannot make an error—such as electrical plugs shaped so they can only be inserted in the correct orientation, or jigs that prevent misaligned assembly.

In software engineering, systems are too often built with fragile, permissive interfaces: string-typed parameters where enums are needed, optional configuration fields with undocumented defaults, and silent fallbacks that swallow errors. When an AI agent or engineer passes an invalid parameter, the system runs for twenty minutes before failing silently or corrupting downstream state.

RDOM establishes **Poka-Yoke Interface Design** (DP-9) and **The Live System Rule** (DP-10) as fundamental engineering disciplines.

```
  Permissive & Fragile Interface (Defect Prone):
  func CreateUser(data map[string]interface{}) error
  // Fails at runtime if "email" is misspelled as "e_mail", or type is wrong int.

  Poka-Yoke Interface (Mistake-Proof by Construction):
  type CreateUserRequest struct {
      Email     EmailAddress `validate:"required,email"`
      Role      UserRole     `validate:"required,oneof=Admin Member Guest"`
      TenantID  TenantUUID   `validate:"required"`
  }
  func CreateUser(ctx context.Context, req CreateUserRequest) (UserResponse, error)
  // Impossible to compile or invoke with invalid keys or types.
```

### The Invariants of Poka-Yoke Interface Design

1. **Strong Typing over Stringly-Typed Primitives**:
   Never pass raw strings for identifiers, statuses, or configurations. Use nominal types, validated domain wrappers (e.g., `TenantUUID`, `SemanticVersion`), and exhaustive enums.
2. **Schema-First Contract Generation**:
   All internal and external interfaces must be declared in formal schema languages (Protocol Buffers, OpenAPI v3, JSON Schema, or Zod). Client SDKs, mock servers, and validation logic must be generated directly from the schema, not handwritten.
3. **Fail-Fast Invariants**:
   If an incoming request, environment variable, or configuration file violates a precondition, the application must crash or reject the request immediately at startup or ingestion. Never default silently or assume missing values.
4. **Hermetic Tool and CLI Arguments**:
   Internal CLI tools and developer scripts must use strict flag validation. Mutually exclusive flags must be enforced at argument parse time; required flags must terminate execution with an actionable error message if omitted.

### Principle DP-10: The Live System Rule

A common trap in agentic software development is debugging against stale documentation, outdated memory files, or cached repo assumptions. An agent assumes a service runs on port 8080 because a README from six months ago said so, wasting hours trying to reach an unresponsive endpoint.

**The Live System Rule** dictates:
> *Before proposing, implementing, or validating any fix or integration, you must independently confirm the hypothesis against the live running system. State the observable evidence from the running process, then act.*

#### Live Verification Checklist

- **Process Verification**: Is the process actually listening on the claimed port (`lsof -iTCP:<port> -sTCP:LISTEN`)?
- **Health Verification**: Does the `/healthz` or `/livez` endpoint return HTTP 200 with an expected version string?
- **Database Schema Verification**: Does the column actually exist in the running database instance, or only in an unapplied migration file?
- **Container Digest Verification**: Is the running container executing the expected immutable OCI digest?

> **Augmentation Surface — Live System Introspection Tools**
>
> Where an agent layer transforms this practice: agents are equipped with read-only inspection tools that query live container states, inspect running database schemas, and verify port listeners before formulating implementation plans.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 730
  principle-citations: DP-9, DP-10
  flagged-principle-gaps: none
-->
