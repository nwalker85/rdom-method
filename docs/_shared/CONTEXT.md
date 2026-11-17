# Authoring Context & Style Guide — RDOM

This specification defines the voice, conventions, and quality criteria for all chapters of the **Ravenhelm Development Operations Methodology (RDOM)**.

---

## 1. Voice and Tone

- **Pragmatic, authoritative, systems-engineering mindset.** Grounded in real production scars, factory floor realities, and verifiable software execution.
- **Direct and evidence-driven.** Avoid motivational buzzwords, generic agile platitudes, and hand-waving abstractions.
- **Neutralized public voice.** Neutralize internal private infrastructure names, customer identities, or private lab hostnames into clean, universal architecture patterns while preserving the full technical depth of Valknut, Ehwaz, RLOM, and RROM.

---

## 2. Structure of Each Chapter

Each chapter markdown file in `docs/chapters/` must follow this uniform structure:

1. **YAML Frontmatter**:

   ```yaml
   ---
   title: "Chapter Title"
   chapter: "01"
   part: "Part Name"
   principles: ["DP-1", "DP-2"]
   summary: "A two-sentence summary of what this chapter establishes."
   ---
   ```

2. **Opening Hook**: A concrete, visceral engineering failure mode that occurs when this discipline is missing.
3. **The Core Framework**: Theoretical foundations, formal mechanics, and architectural diagrams (Mermaid or ASCII).
4. **Concrete Implementation & Rules**: Step-by-step recipes, algorithms, or policy gates.
5. **Anti-Patterns & Failure Modes**: Concrete ways teams get this wrong.
6. **Integration Points**: How this chapter connects upstream to RLOM and downstream to RROM.
7. **`<!-- RUBRIC_CHECK -->` Block**: An HTML comment validating chapter completeness, word count targets, and principle citations.

---

## 3. Chapter Index

The book comprises 18 core chapters grouped into four parts, plus Appendix A:

### Part I: Strategic Intent & Cadence (The Macro Engine)

- **Chapter 01**: What This Is and Why Modern Engineering Drifts
- **Chapter 02**: The Sovereign Triad (RLOM, RDOM, RROM)
- **Chapter 03**: The 24 Numbered Principles
- **Chapter 04**: The Hierarchy of Deeds (Wyrd Rune to Daily Deed)
- **Chapter 05**: The Four Codices (Shield, Cycle, Grimoire, Shield-Band)
- **Chapter 06**: The Engineering OKR Framework (Faster, Bigger, Cheaper, Effective)
- **Chapter 07**: Ceremonies of Truth (Althing, Ráð, and Morning Muster)

### Part II: The Ehwaz Planning Doctrine (The Topological Engine)

- **Chapter 08**: The Dependency DAG: Critical Path vs. Critical Chain
- **Chapter 09**: Topological Waves: Replacing the Two-Week Sprint
- **Chapter 10**: Zero Collision by Construction (Multi-Agent Fleet Boundaries)
- **Chapter 11**: Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)
- **Chapter 12**: The DRY Hoisting Protocol: Anti-Snowflake Planning

### Part III: Execution Mechanics (The Micro Engine)

- **Chapter 13**: Six Sigma Wave Boundary Gates (No Exit on a Promise)
- **Chapter 14**: Poka-Yoke Interface Design & The Live System Rule
- **Chapter 15**: The Andon Cord Protocol & Upstream-Jump Circuit Breakers
- **Chapter 16**: Workspace Custody: The Bare Repository and Disposable Worktrees
- **Chapter 17**: The Zero-Waste Context Substrate (Topological Priming vs. Directory Dumps)

### Part IV: Governance & Integration

- **Chapter 18**: The Sovereign Engineering Organization: Operating Human-Agent Fleets
- **Appendix A**: Presales, Solution Architecture & DemoOps Integration
