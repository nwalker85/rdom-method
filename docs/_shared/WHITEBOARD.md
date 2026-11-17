# Central Whiteboard — RDOM Editorial Directives, Invariants & Chapter Tracker

> **Notice to all writing subagents and editors**: This whiteboard is the authoritative editorial control plane for expanding the *Ravenhelm Development Operations Methodology (RDOM)* manuscript. All subagents MUST strictly adhere to the invariants, directives, terminology, and structural rubrics declared below.

---

## 1. Core Invariants & Axioms

1. **Axiom of Concurrency (The Core Axiom)**:
   > *"Concurrency is earned through topological proof; quality is gated by verified green."*
   A plan is a directed acyclic graph ($G = (V, E)$), not a flat task list. Concurrency across engineers and agent swarms is safe *only* within the same topological wave where tasks share no edge dependencies.

2. **Axiom of Precedence**:
   > *"The Graph Precedes the Plan."* (Principle **DP-1**)
   Any implementation without an explicit DAG of preconditions is unverified speculation.

3. **Axiom of Quality (Six Sigma Wave Boundary)**:
   > *"Wave $N+1$ never opens on a promise; only on verified green."* (Principle **DP-7**)
   Defects compound exponentially downstream. No wave boundary is crossed based on "it compiles locally," mock passes, or promissory notes.

4. **Axiom of Evidence**:
   > *"If it isn't witnessed by a deed, it didn't happen."* (Principle **DP-11**)
   Every completion requires the Triad of Proof: deterministic passing automated tests against live environments, updated operational documentation/runbooks, and an executable showcase/walkthrough.

5. **Axiom of Anti-Inventory (*Muda*)**:
   > *"Specifying code for Wave $N+2$ while Wave $N$ is incomplete is inventory waste."* (Principle **DP-6**)
   Granular TDD specifications are elaborated Just-In-Time (JIT) for the active wave only.

6. **Axiom of the Circuit Breaker**:
   > *"Never branch outward to build against an unfinished upstream dependency."* (Principle **DP-5**, **DP-12**)
   When a blocker or broken dependency occurs, workers sound the Andon Cord immediately. Speculative mocking of broken upstream interfaces is prohibited.

---

## 2. Voice, Tone & Public Editorial Boundary

- **Tone**: Visceral, authoritative systems-engineering mindset. Grounded in real production battle scars, industrial engineering (Toyota Production System, Shigeo Shingo's Poka-Yoke, Six Sigma, Goldratt's Critical Chain), and modern distributed systems.
- **Style**: High information density. Concrete failure modes, technical precision, operational algorithms, mathematical formulas ($G=(V,E)$), and clear diagrams.
- **Forbidden**: Vague agile platitudes ("story points", "scrum ceremonies", "velocity tracking", "fail fast", "vibes"), hand-waving abstractions, generic motivational filler.
- **Neutralization**: Public manuscript standards apply. Conceptual doctrine names (*Ehwaz*, *Valknut*, *RLOM*, *RDOM*, *RROM*, *Althing*, *Ráð*, *Muster*) are celebrated and rigorously defined as formal methodology patterns. Do not leak internal private IP addresses, private customer names, or non-public credentials.

---

## 3. Standard Chapter Structural Specification

Every expanded chapter in `docs/chapters/` must target **1,800 to 2,800 words** of dense, comprehensive prose and follow this exact template:

```markdown
<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter N — [Title]

[Opening Hook: 3-4 paragraphs illustrating a vivid, catastrophic engineering failure mode that occurs in modern software organizations when this discipline is absent.]

### The Theoretical & Mechanical Foundation
[Mathematical or systems formulation, formal definitions, graph representations, and an explicit Mermaid diagram or ASCII architectural model.]

### Operational Mechanics & Step-by-Step Protocols
[Concrete implementation recipes, algorithms, state machines, policy gates, and tabular rules.]

### Concrete Anti-Patterns & Defect Escapes
[How teams deceive themselves; agile illusions; agent prompt thrash; detailed breakdowns of anti-patterns with names.]

### Upstream & Downstream Integration (The Sovereign Triad)
[Explicit interface contracts showing how this chapter connects upstream to RLOM demand/acceptance and downstream to RROM release/deployment.]

> **Augmentation Surface — [Surface Name]**
>
> Where an agent layer transforms this practice: [Explicit breakdown of how autonomous agents automate the mechanical burden without human bottleneck.]
>
> What the human architect keeps: [Inviolable human judgment, strategy, and sovereign authority.]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: [Actual Count, target 1800-2800]
  principle-citations: [Explicit DP-X list]
  flagged-principle-gaps: none
-->
```

---

## 4. Markdownlint & Formatting Rules

- **Zero lint errors**: Must pass `npx markdownlint-cli 'docs/**/*.md' 'README.md' --config .markdownlint.yml`.
- **Fenced code blocks**: Always declare a language tag (`mermaid`, `bash`, `text`, `yaml`, `json`, etc.).
- **No trailing spaces**: Clean line endings.
- **Header hierarchy**: Chapters begin with `## Chapter N — ...`, subsequent sections use `###`, subsections use `####`.
- **Proper list formatting**: Surround bulleted and numbered lists with blank lines.
- **No bare URLs**: Always use Markdown links `[text](url)`.

---

## 5. Chapter Expansion Registry & Progress Tracker

| Chapter | Title | Assigned Worker | Target Principles | Word Count Target | Status |
|:---|:---|:---|:---|:---:|:---:|
| **01** | What This Is and Why Modern Engineering Drifts | Worker-1 (Batch 1) | DP-1, DP-2, DP-3, DP-7, DP-12, DP-19 | 2,000+ | COMPLETED (2,471 words) |
| **02** | The Sovereign Triad (RLOM, RDOM, RROM) | Worker-2 (Batch 1) | DP-1, DP-7, DP-11, DP-23 | 2,000+ | COMPLETED (2,488 words) |
| **03** | The 24 Numbered Principles | Worker-3 (Batch 1) | DP-1 through DP-24 | 2,500+ | COMPLETED (3,078 words) |
| **04** | The Hierarchy of Deeds (Wyrd Rune to Daily Deed) | Worker-4 (Batch 2) | DP-1, DP-4, DP-11 | 2,000+ | COMPLETED (2,357 words) |
| **05** | The Four Codices (Shield, Cycle, Grimoire, Band) | Worker-5 (Batch 2) | DP-19, DP-20, DP-21 | 2,000+ | COMPLETED (2,475 words) |
| **06** | The Engineering OKR Framework | Worker-6 (Batch 2) | DP-4, DP-11, DP-23 | 2,000+ | COMPLETED (2,494 words) |
| **07** | Ceremonies of Truth (Althing, Ráð, Muster) | Worker-7 (Batch 3) | DP-1, DP-7, DP-12 | 2,000+ | COMPLETED (2,904 words) |
| **08** | The Dependency DAG: Critical Path vs. Critical Chain | Worker-8 (Batch 3) | DP-1, DP-2, DP-4 | 2,000+ | COMPLETED (2,424 words) |
| **09** | Topological Waves: Replacing the Two-Week Sprint | Worker-9 (Batch 3) | DP-2, DP-3, DP-7 | 2,000+ | COMPLETED (4,666 words) |
| **10** | Zero Collision by Construction (Multi-Agent Fleets) | Worker-10 (Batch 4) | DP-3, DP-10, DP-19 | 2,000+ | COMPLETED (4,148 words) |
| **11** | JIT Elaboration & Eradicating Inventory Waste | Worker-11 (Batch 4) | DP-6, DP-8, DP-14 | 2,000+ | COMPLETED (4,528 words) |
| **12** | The DRY Hoisting Protocol: Anti-Snowflake Planning | Worker-12 (Batch 4) | DP-13, DP-14, DP-15, DP-16 | 2,000+ | COMPLETED (4,311 words) |
| **13** | Six Sigma Wave Boundary Gates (No Exit on Promise) | Worker-13 (Batch 5) | DP-7, DP-8, DP-10, DP-11 | 2,000+ | COMPLETED (4,938 words) |
| **14** | Poka-Yoke Interface Design & The Live System Rule | Worker-14 (Batch 5) | DP-9, DP-10, DP-18 | 2,000+ | COMPLETED (4,515 words) |
| **15** | The Andon Cord Protocol & Upstream-Jump Circuit Breakers | Worker-15 (Batch 5) | DP-5, DP-12 | 2,000+ | COMPLETED (4,826 words) |
| **16** | Workspace Custody: Bare Repositories & Worktrees | Worker-16 (Batch 6) | DP-19, DP-21, DP-22, DP-24 | 2,000+ | COMPLETED (4,520 words) |
| **17** | The Zero-Waste Context Substrate (EAT Priming) | Worker-17 (Batch 6) | DP-20 | 2,000+ | COMPLETED (4,189 words) |
| **18** | The Sovereign Engineering Organization | Worker-18 (Batch 6) | DP-1..DP-24 | 2,200+ | COMPLETED (5,149 words) |
| **App A** | Presales, Solution Architecture & DemoOps | Worker-AppA (Batch 7) | DP-11, DP-18 | 2,000+ | COMPLETED (3,901 words) |
