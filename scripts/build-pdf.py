#!/usr/bin/env python3
"""Typeset Ravenhelm Development Operations Methodology (RDOM) as publication-grade PDF using Typst.

Compiles two editions:
  dark   - bone on obsidian (screen edition, matching RLOM Dark and RROM Dark)
  print  - obsidian on bone paper (the print / digest edition)

Faces: Source Serif 4 (proposition/body), IBM Plex Mono (evidence/folios/code/colophon).
Trim: 5.5 x 8.5 in (digest chapbook / executive monograph).
"""
import os
import re
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT, "docs", "chapters")
ASSETS_DIR = os.path.join(ROOT, "assets")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
OUTDIR = ROOT

BYLINE = "Nathan Walker"
IMPRINT = "Ravenhelm Publishing Series LLC"
COPYRIGHT = "© 2026 Ravenhelm LLC. All rights reserved."

CHAPTER_FILES = [
    ("01-what-this-is.md", "01", "What This Is and Why Modern Engineering Drifts", "SCOPE: METHODOLOGY FRONT DOOR · BOOK II OF THE TRILOGY", "The Social Layer Does Not Transfer · The Ehwaz Doctrine · Four Pillars of RDOM"),
    ("02-the-sovereign-triad.md", "02", "The Sovereign Triad: RLOM, RDOM, RROM", "FOUNDATION: THE SOVEREIGN TRIAD · RLOM · RDOM · RROM", "The Three Dombocs · Interface Contracts · Cascading Failure Modes · Fleet Orchestration"),
    ("03-numbered-principles.md", "03", "The 24 Numbered Principles", "CANON: 24 NUMBERED PRINCIPLES · DP-1 THROUGH DP-24", "Ehwaz Doctrine & Concurrency · Six Sigma & TDD Gates · DRY Architecture · Workspace Custody"),
    ("04-the-hierarchy-of-deeds.md", "04", "The Topological Work Hierarchy: From Strategic Invariant to Atomic Commit", "TAXONOMY: TOPOLOGICAL WORK HIERARCHY · INVARIANT TO COMMIT", "Curing Altitude Drift · Strategic Invariants · Quarterly Contracts · Lineage Traceability"),
    ("05-the-four-codices.md", "05", "The Four Operational Contracts: Repository Law, Cadence, Architecture, and Fleet Custody", "CONTRACTS: REPOSITORY LAW · CADENCE · ARCHITECTURE · FLEET CUSTODY", "AGENTS.md Law · The Cadence Ledger · ADRs & Runbooks · Fleet Custody & Routing"),
    ("06-the-engineering-okr-framework.md", "06", "The Four-Dimensional Engineering Scorecard: Faster, Bigger, Cheaper, Effective", "SCORECARD: FASTER · BIGGER · CHEAPER · EFFECTIVE", "Balanced Engineering Control Matrix · CI & Quota Physics · Quarterly Cadence · Metric Alignment"),
    ("07-ceremonies-of-truth.md", "07", "Ceremonies of Truth: Quarterly Invariant Review, Monthly Architecture Review, and the Daily Fleet Sweep", "CEREMONIES: QUARTERLY REVIEW · MONTHLY REVIEW · DAILY FLEET SWEEP", "Reconciling the Docket · Flushing Court Cards · Sweeping Active Panes · Automated Gates"),
    ("08-the-dependency-dag-and-critical-chain.md", "08", "The Dependency DAG: Critical Path vs. Critical Chain", "TOPOLOGY: DEPENDENCY DAG · GOLDRATT CCPM · CRITICAL CHAIN", "The Ehwaz Doctrine Part I · Goldratt CCPM · Feeding Buffers · Curing Upstream Jumps"),
    ("09-topological-waves-replacing-sprints.md", "09", "Topological Waves: Replacing the Two-Week Sprint", "CADENCE: TOPOLOGICAL WAVES · HEIJUNKA LEVELING · BATCH CONTROL", "The Ehwaz Doctrine Part II · Wave Boundary Math · Doomcourt Dispatch · Defect-Free Waves"),
    ("10-zero-collision-multi-agent-boundaries.md", "10", "Zero Collision by Construction: Multi-Agent Fleet Boundaries", "CONCURRENCY: ZERO-COLLISION BOUNDARIES · DISJOINT BLAST RADIUS", "Disjoint Write Surfaces · Modern git merge-tree · Isolated Test Schemas · Merge Gates"),
    ("11-jit-elaboration-and-anti-inventory.md", "11", "Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)", "LEAN MANUFACTURE: JIT ELABORATION · ERADICATING INVENTORY MUDA", "Anti-Inventory Canon · Open-Wave TDD Detailing · Future-Wave Contracts · Eliminating Stale Specs"),
    ("12-the-dry-hoisting-protocol.md", "12", "The DRY Hoisting Protocol: Anti-Snowflake Planning", "REFACTORING: DRY HOISTING PROTOCOL · HOIST VS. DEFER", "Planning-Time DRY Scan · Hoist-vs-Defer Test · Consumption Contracts · Project Factory Scaffolds"),
    ("13-six-sigma-wave-boundary-gates.md", "13", "Six Sigma Wave Boundary Gates: No Exit on a Promise", "QUALITY: SIX SIGMA WAVE GATES · CHECKS THAT CAN FAIL · TRIAD OF PROOF", "Checks That Prove They Can Fail · Caller Reachability · Triad of Proof · Zero-Defect Handoff"),
    ("14-poka-yoke-interface-design.md", "14", "Poka-Yoke Interface Design & The Live System Rule", "ERROR PROOFING: SHINGO POKA-YOKE · GRANULARITY EXACT · LIVE SYSTEM", "Pricing Verification Below Guessing · Boundary Parsers · Live System Truth · Anti-Mock Rule"),
    ("15-the-andon-cord-and-circuit-breakers.md", "15", "The Andon Cord Protocol & Upstream-Jump Circuit Breakers", "CIRCUIT BREAKERS: THE ANDON CORD · DOOM MOMENTUM · STOP-THE-LINE", "Stop-the-Line Authority · Rescuing Uncommitted Diffs · Five Whys Root Cause · Replan Cards"),
    ("16-workspace-custody-bare-and-worktrees.md", "16", "Workspace Custody: Bare Repositories and Disposable Worktrees", "INFRASTRUCTURE: CHECKOUT CUSTODY STANDARD · BARE & WORKTREES", "Checkout Custody Standard · Fetch Refspecs · One Worktree Per PR · Custody-Gated Disposal"),
    ("17-zero-waste-context-substrate-eat.md", "17", "The Zero-Waste Context Substrate: Topological Priming vs. Directory Dumps", "CONTEXT SUBSTRATE: EAT KNOWLEDGE SUBSTRATE · ZERO CONTEXT WASTE", "EAT Knowledge Substrate · Sub-800 Token Priming · Sub-10ms AST Byte Reads · Context Economics"),
    ("18-the-sovereign-engineering-organization.md", "18", "The Sovereign Engineering Organization: Operating Human-Agent Fleets", "ORGANIZATION: THE SOVEREIGN FLEET · HUMAN ARCHITECTS & AGENT SLICES", "Declarative Cores, Dumb Edges · Supervisor-Worker Topology · Governance Rails · Sovereign Scale"),
    ("appendix-a-presales-and-demo-ops.md", "A", "Presales, Solution Architecture & DemoOps Integration", "COMMERCIAL: DEMOOPS · EPHEMERAL SANDBOXES · PROTOTYPE HOISTING", "Ephemeral Sandboxes · Prototype Hoisting · Zero-Drift Customer Demos · Commercial Rails"),
]

def markdown_to_typst_via_pandoc(md_path, edition):
    """Converts a Markdown file to Typst syntax via pandoc with post-processing."""
    raw_md = open(md_path, "r", encoding="utf-8").read()

    # Strip HTML license comments and rubric checks
    cleaned_md = re.sub(r"<!--.*?-->", "", raw_md, flags=re.S)

    # Strip the top-level chapter heading since Typst renders custom chapter opener
    cleaned_md = re.sub(r"^\s*#+\s+(Chapter\s+\d+|Appendix\s+[A-Z]).*?\n", "", cleaned_md, count=1, flags=re.M)

    res = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "typst"],
        input=cleaned_md,
        text=True,
        capture_output=True,
        check=True
    )
    return res.stdout

def build_typst_document(edition):
    """Assembles the complete Typst source code for the requested edition."""
    if edition == "print":
        ink = "#0B0C0E"
        paper = "#EDE8DC"
        ash = "#6F6A62"
        garnet = "#A3222F"
        gold = "#96752C"
        card_bg = "#E2DDD1"
        card_border = "#B0A898"
        raven_logo = "assets/ravenhelm-raven-black-eye.svg"
    else:  # dark
        ink = "#EDE8DC"
        paper = "#0B0C0E"
        ash = "#8E939B"
        garnet = "#A3222F"
        gold = "#C4A45A"
        card_bg = "#14171C"
        card_border = "#2B303A"
        raven_logo = "assets/ravenhelm-raven-bone-eye.svg"

    def format_toc_title(t):
        wrap_targets = [
            "The Topological Work Hierarchy: From Strategic Invariant to Atomic Commit",
            "The Four Operational Contracts: Repository Law, Cadence, Architecture, and Fleet Custody",
            "The Four-Dimensional Engineering Scorecard: Faster, Bigger, Cheaper, Effective",
            "Ceremonies of Truth: Quarterly Invariant Review, Monthly Architecture Review, and the Daily Fleet Sweep",
            "Zero Collision by Construction: Multi-Agent Fleet Boundaries",
            "Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)",
            "Workspace Custody: Bare Repositories and Disposable Worktrees",
        ]
        if t in wrap_targets and ": " in t:
            p1, p2 = t.split(": ", 1)
            return p1 + ":#linebreak()" + p2
        return t

    toc_p1_lines = []
    for file_name, num, title, badge_text, summary in CHAPTER_FILES[:9]:
        label_id = f"ch-{num.lower()}"
        toc_title = format_toc_title(title)
        toc_p1_lines.append(f'  #toc-entry("{num}", [{toc_title}], "{label_id}", "{summary}")')
    toc_p1_str = "\n".join(toc_p1_lines)

    toc_p2_lines = []
    for file_name, num, title, badge_text, summary in CHAPTER_FILES[9:]:
        label_id = f"ch-{num.lower()}"
        toc_title = format_toc_title(title)
        toc_p2_lines.append(f'  #toc-entry("{num}", [{toc_title}], "{label_id}", "{summary}")')
    toc_p2_str = "\n".join(toc_p2_lines)

    preamble = f'''
#let ink = rgb("{ink}")
#let paper = rgb("{paper}")
#let ash = rgb("{ash}")
#let garnet = rgb("{garnet}")
#let gold = rgb("{gold}")
#let card_bg = rgb("{card_bg}")
#let card_border = rgb("{card_border}")

#set document(
  title: "Ravenhelm Development Operations Methodology (RDOM)",
  author: "{BYLINE}",
  keywords: ("RDOM", "Ravenhelm", "Ehwaz", "Critical Chain", "Autonomous Agents", "Six Sigma", "Topological Waves")
)

#set page(
  width: 5.5in,
  height: 8.5in,
  margin: (top: 0.85in, bottom: 0.85in, inside: 0.85in, outside: 0.75in),
  fill: paper
)

#set text(
  font: "Source Serif 4",
  size: 9.6pt,
  fill: ink,
  lang: "en",
  hyphenate: true
)

#set par(
  justify: true,
  leading: 0.68em,
  first-line-indent: 1.1em,
  spacing: 0.72em
)

// Suppress heading hyphenation
#show heading: set text(hyphenate: false)

// Headings styling
#show heading.where(level: 1): it => block(
  spacing: 0.4em,
  text(font: "Source Serif 4", size: 19pt, weight: 600, fill: ink)[#it.body]
)

#show heading.where(level: 2): it => block(
  spacing: 1.1em,
  text(font: "Source Serif 4", size: 13pt, weight: 600, fill: garnet)[#it.body]
)

#show heading.where(level: 3): it => block(
  spacing: 0.9em,
  text(font: "Source Serif 4", size: 10.5pt, weight: 600, fill: ink)[#it.body]
)

#show heading.where(level: 4): it => block(
  spacing: 0.7em,
  text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: ash, tracking: 0.08em)[#it.body]
)

// Code styling: inline raw code
#show raw.where(block: false): it => box(
  fill: card_bg,
  inset: (x: 2.5pt, y: 0pt),
  outset: (y: 2.5pt),
  radius: 2pt
)[#text(font: "IBM Plex Mono", size: 8.0pt, it)]

// Code styling: block code
#show raw.where(block: true): it => block(
  width: 100%,
  clip: true,
  breakable: true,
  fill: card_bg,
  stroke: 0.5pt + card_border,
  inset: 7pt,
  radius: 3pt,
  spacing: 0.9em,
  text(font: "IBM Plex Mono", size: 6.8pt, fill: ink, it)
)

// Quote / Callout styling
#show quote: it => block(
  width: 100%,
  breakable: true,
  fill: card_bg,
  stroke: (left: 2.5pt + garnet, rest: 0.5pt + card_border),
  inset: (x: 9pt, y: 7pt),
  radius: (right: 3pt),
  spacing: 0.9em,
  text(style: "italic", size: 8.8pt, it.body)
)

// Table styling
#show table: set text(font: "IBM Plex Mono", size: 6.8pt)
#show table.cell.where(y: 0): set text(weight: "bold", fill: ink)

// Math equation styling
#show math.equation.where(block: true): set text(size: 8.2pt)

// Table of Contents custom entry helpers (RLOM standard)
#let toc-prelim(title, label-id) = [
  #v(0.25em)
  #block(width: 100%)[
    #text(font: "Source Serif 4", size: 8.6pt, style: "italic", fill: ink)[#link(label(label-id))[#title]]
    #box(width: 1fr, pad(x: 4pt, repeat([#text(fill: ash, size: 7pt)[. ]])))
    #text(font: "IBM Plex Mono", size: 7.8pt, fill: ash)[#context counter(page).at(label(label-id)).first()]
  ]
]

#let toc-entry(num, title, label-id, summary) = [
  #v(0.22em)
  #grid(
    columns: (18pt, 1fr),
    gutter: 5pt,
    text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet)[#num],
    [
      #block(width: 100%)[
        #text(font: "Source Serif 4", size: 8.2pt, weight: 600, fill: ink)[#link(label(label-id))[#title]]
        #box(width: 1fr, pad(x: 4pt, repeat([#text(fill: ash, size: 7pt)[. ]])))
        #text(font: "IBM Plex Mono", size: 7.8pt, fill: ash)[#context counter(page).at(label(label-id)).first()]
      ]
      #v(0.04em)
      #text(font: "Source Serif 4", size: 6.8pt, fill: ash)[#summary]
    ]
  )
]

// ==========================================
// 1. FRONT COVER
// ==========================================
#page(
  margin: (x: 0.85in, top: 0.9in, bottom: 0.9in),
  numbering: none,
  header: none,
  footer: none
)[
  #align(center)[
    #v(0.35in)
    #image("{raven_logo}", width: 2.25in)
    #v(0.40in)
    #text(font: "IBM Plex Mono", size: 7.0pt, fill: garnet, tracking: 0.14em)[THE RAVENHELM OPERATIONS METHODOLOGY · BOOK II]
    #v(0.12in)
    #text(font: "Source Serif 4", size: 16.5pt, weight: 600, fill: ink)[Ravenhelm Development Operations]
    #v(0.08in)
    #text(font: "Source Serif 4", size: 14.5pt, weight: 400, fill: garnet)[Methodology]
    #v(0.28in)
    #block(width: 82%)[
      #set par(leading: 0.65em)
      #text(font: "IBM Plex Mono", size: 7.0pt, fill: ash, tracking: 0.10em)[A LEAN, TOPOLOGICAL, AND DEFECT-GATED FRAMEWORK FOR AUTONOMOUS AND HYBRID FLEETS]
    ]
    #v(1fr)
    #text(font: "Source Serif 4", size: 10.5pt, weight: 600, fill: ink)[{BYLINE}]
    #v(0.06in)
    #text(font: "IBM Plex Mono", size: 7.2pt, fill: ash, tracking: 0.12em)[RAVENHELM LLC · 2026]
    #v(0.15in)
  ]
]

// ==========================================
// 2. VERSO / COPYRIGHT & IMPRINT
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(1.4in)
  #align(center)[
    #text(font: "Source Serif 4", size: 13pt, weight: 600)[Ravenhelm Development Operations Methodology]
    #v(0.18in)
    #text(font: "Source Serif 4", size: 9.5pt, style: "italic", fill: ash)[
      "Concurrency is not granted by calendar fiat;\\
       it is earned through topological proof."
    ]
    #v(0.08in)
    #text(font: "IBM Plex Mono", size: 7pt, fill: garnet, tracking: 0.14em)[THE FIRST CONCURRENCY INVARIANT (DP-2)]
  ]
  #v(1fr)
  #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.04em, hyphenate: false)
  #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
  *Ravenhelm Development Operations Methodology (RDOM)* \\
  Book II of *The Ravenhelm Operations Methodology* (*RLOM · RDOM · RROM*) \\
  Version 1.0.0 (2026-11-17) \\
  Authored by {BYLINE}. \\
  {COPYRIGHT} \\
  Published by {IMPRINT}. \\
  \\
  Distributed under the *Apache License, Version 2.0*. \\
  Free to read, implement, fork, and distribute internally within any engineering organization. \\
  Commercial training, certification, and enterprise fleet advisory products reserved by Ravenhelm LLC. \\
  \\
  Inquiries: nate\\@ravenhelm.co · ravenhelm.co \\
  Source repository: github.com/nwalker85/rdom-method \\
  \\
  Set in Source Serif 4 and IBM Plex Mono. \\
  Typeset using Typst on macOS. \\
  #v(0.4in)
]

// ==========================================
// 3. TABLE OF CONTENTS (RLOM STANDARD)
// ==========================================
#page(
  margin: (top: 0.65in, bottom: 0.65in, inside: 0.85in, outside: 0.75in),
  numbering: none,
  header: none,
  footer: none
)[
  #v(0.08in)
  #align(left)[
    #text(font: "Source Serif 4", size: 20pt, weight: 600, fill: ink)[Contents]
  ]
  #v(0.12in)

  #toc-prelim("How to read it", "front-how-to-read")
  #toc-prelim("The principles at a glance", "front-principles")

  #v(0.6em)

{toc_p1_str}
]

#page(
  margin: (top: 0.65in, bottom: 0.65in, inside: 0.85in, outside: 0.75in),
  numbering: none,
  header: none,
  footer: none
)[
  #v(0.12in)
{toc_p2_str}
]

// ==========================================
// 4. HOW TO READ IT
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.3in)
  #align(left)[
    #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[GUIDE]
    #v(0.08in)
    #heading(level: 1, numbering: none, outlined: true)[How to Read It] <front-how-to-read>
    #v(0.05in)
    #line(length: 100%, stroke: 0.5pt + ash)
  ]
  #v(0.15in)

  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[IN ORDER] \\
  #set text(size: 8.8pt)
  The chapters build sequentially from foundational axioms to topological wave planning, zero-collision multi-agent fleet boundaries, DRY hoisting protocols, Six Sigma wave boundary gates, and the sovereign engineering organization. Chapter 3 (*The 24 Numbered Principles*) establishes the formal canon cited throughout every subsequent chapter as `DP-1` through `DP-24`.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[BY ROLE - THE INSTALL PATH] \\
  #set text(size: 8.8pt)
  *Chief Technology Officer & Architect:* Chapters 01, 02, 05, 06, 12, 18 (Sovereign Triad, Four Operational Contracts, DRY Hoisting, Four-Dimensional Scorecard). \\
  *Fleet Lead & Engineering Manager:* Chapters 04, 07, 08, 09, 11, 13 (Topological Work Hierarchy, Ceremonies of Truth, Dependency DAGs, Wave Gates). \\
  *Agent Engineer & Operator:* Chapters 03, 10, 14, 15, 16, 17 (Zero Collision, Poka-Yoke Interfaces, Andon Cord, Bare Worktrees, EAT Substrate). \\
  *Systems Quality & Verification Auditor:* Chapters 07, 10, 13, 14, 15, Appendix A (Six Sigma Gates, Triad of Proof, Live Running System, DemoOps).

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[BY NEED - RECOVERY & SCALING] \\
  #set text(size: 8.8pt)
  *Halting Sprint Collapses & Merge Collisions:* Read Chapters 01, 08, 09, 10. \\
  *Eliminating Multi-Agent Hallucinations & Snowflakes:* Read Chapters 10, 11, 12, 17. \\
  *Eradicating Downstream Defect Escapes:* Read Chapters 13, 14, 15.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[NAVIGATING THIS BOOK] \\
  #set text(size: 8.8pt)
  The bookmark outline carries every chapter and major section. Chapter openers feature metadata badges citing applicable operational contracts and principles. Code symbols, AST byte manifests, and CLI recipes follow strict POSIX standards.
]

// ==========================================
// 5. THE PRINCIPLES AT A GLANCE
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.3in)
  #align(left)[
    #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[CANON]
    #v(0.08in)
    #heading(level: 1, numbering: none, outlined: true)[The Principles at a Glance] <front-principles>
    #v(0.05in)
    #line(length: 100%, stroke: 0.5pt + ash)
  ]
  #v(0.12in)
  #set text(font: "IBM Plex Mono", size: 7.2pt, fill: ash)
  #set par(justify: false, first-line-indent: 0em, leading: 0.8em)

  #text(weight: "bold", fill: garnet)[PILLAR I - THE DEPENDENCY WAVEFRONT (THE EHWAZ DOCTRINE)] \\
  #text(fill: ink)[DP-1] The Graph Precedes the Plan: every plan opens with a dependency DAG \\
  #text(fill: ink)[DP-2] Topological Wave Partitioning: group work into discrete resolved waves \\
  #text(fill: ink)[DP-3] Zero Collision by Construction: disjoint write surfaces within waves \\
  #text(fill: ink)[DP-4] The Critical Chain Floor: the longest dependent path sets the schedule floor \\
  #text(fill: ink)[DP-5] Upstream-Jump Circuit Breaker: never branch outward on unfinished deps \\
  #text(fill: ink)[DP-6] Progressive JIT Elaboration: detail only the open wave; avoid Muda \\
  \\
  #text(weight: "bold", fill: garnet)[PILLAR II - SIX SIGMA DEFECT PREVENTION & TDD GATES] \\
  #text(fill: ink)[DP-7] Verified Green Precedes Promotion: checks must prove they can fail \\
  #text(fill: ink)[DP-8] Red-Green-Refactor as State Transitions: failing test before code \\
  #text(fill: ink)[DP-9] Poka-Yoke Interface Design: price verification below guessing \\
  #text(fill: ink)[DP-10] Live Running System as Truth: verify entrypoint call graphs, not mocks \\
  #text(fill: ink)[DP-11] Witnessed Deliverable Attachment: Code, Docs, and Executable Showcase \\
  #text(fill: ink)[DP-12] The Andon Cord Protocol: halt dispatch and inspect uncommitted diffs \\
  \\
  #text(weight: "bold", fill: garnet)[PILLAR III - DRY ARCHITECTURE & ANTI-SNOWFLAKE HOISTING] \\
  #text(fill: ink)[DP-13] Planning-Time DRY Refactoring: scan the DAG for snowflakes upfront \\
  #text(fill: ink)[DP-14] The Hoist-vs-Defer Rule: hoist known interfaces; schedule guessed ones \\
  #text(fill: ink)[DP-15] Zero Unacknowledged Duplication: bind repeats to extraction contracts \\
  #text(fill: ink)[DP-16] Scaffolding from Working Reality: extract templates from proven prod code \\
  #text(fill: ink)[DP-17] Shared Substrate Invariance: never re-roll estate gateway or vault crates \\
  #text(fill: ink)[DP-18] Locality Invariance: authoritative root AGENTS.md travels with code \\
  \\
  #text(weight: "bold", fill: garnet)[PILLAR IV - WORKSPACE CUSTODY & MULTI-AGENT ERGONOMICS] \\
  #text(fill: ink)[DP-19] Dedicated Worktree Custody: canonical .bare/ hub and one worktree per PR \\
  #text(fill: ink)[DP-20] Anti-Thrash Context Priming: orient in \\<800 tokens via eat prime \\
  #text(fill: ink)[DP-21] Zero Ambient Mutation on Hosts: never edit live servers over SSH \\
  #text(fill: ink)[DP-22] WIP Commit Checkpointing: commit dirty state; never use git stash \\
  #text(fill: ink)[DP-23] The PR Boundary & Supervisor Merge Gate: human-approved squash & ship \\
  #text(fill: ink)[DP-24] Custody-Gated Worktree Disposal: prove zero unpushed/dirty work first
]

// ==========================================
// 6. RUNNING HEADERS & BODY PAGES
// ==========================================
#set page(
  numbering: "1",
  number-align: center,
  footer: context [
    #set text(font: "IBM Plex Mono", size: 7.5pt, fill: ash, tracking: 0.08em)
    #align(center)[#counter(page).display("1")]
  ],
  header: context [
    #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.14em)
    #let page_num = counter(page).get().first()
    #let is_chapter_opener = query(heading.where(level: 1)).any(h => h.location().page() == page_num)
    #if not is_chapter_opener [
      #if calc.odd(page_num) [
        #align(right)[RAVENHELM DEVELOPMENT OPERATIONS METHODOLOGY]
      ] else [
        #align(left)[{BYLINE} · RDOM METHOD]
      ]
    ]
  ]
)

'''

    body_chapters = []
    for file_name, num, title, badge_text, summary in CHAPTER_FILES:
        chapter_path = os.path.join(DOCS_DIR, file_name)
        if not os.path.exists(chapter_path):
            continue
        typst_content = markdown_to_typst_via_pandoc(chapter_path, edition)

        is_appendix = num in ("A", "B")
        label_prefix = "APPENDIX" if is_appendix else "CHAPTER"

        chapter_header = f"""
#pagebreak()
#v(0.8in)
#align(left)[
  #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[{label_prefix} · {num}]
  #v(0.08in)
  #heading(level: 1, numbering: (..n) => "{num}", outlined: true)[{title}] <ch-{num.lower()}>
  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.08em)[{badge_text}]
  #v(0.05in)
  #line(length: 100%, stroke: 0.5pt + ash)
]
#v(0.3in)
"""
        chapter_block = chapter_header + typst_content
        body_chapters.append(chapter_block)

    colophon = f'''
// ==========================================
// 8. COLOPHON
// ==========================================
#pagebreak()
#set page(numbering: none, header: none, footer: none)
#v(1fr)
#align(center)[
  #image("{raven_logo}", width: 1.1in)
  #v(0.25in)
  #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.04em, hyphenate: false)
  #set par(justify: false, first-line-indent: 0em, leading: 0.95em)
  Ravenhelm Development Operations Methodology (RDOM) \\
  Book II of The Ravenhelm Operations Methodology (RLOM · RDOM · RROM) \\
  Version 1.0.0 (2026-11-17) \\
  Authored by {BYLINE}. \\
  {COPYRIGHT} \\
  Published by {IMPRINT}. \\
  Distributed under the Apache License, Version 2.0. \\
  Set in Source Serif 4 and IBM Plex Mono. \\
  Typeset using Typst on macOS. \\
  ravenhelm.co · nwalker.cc
]
#v(0.6in)
'''

    return preamble + "\n".join(body_chapters) + colophon

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    for edition in ("dark", "print"):
        typ_content = build_typst_document(edition)
        typ_path = os.path.join(OUTDIR, f"build-rdom-{edition}.typ")
        with open(typ_path, "w", encoding="utf-8") as f:
            f.write(typ_content)

        if edition == "dark":
            pdf_path = os.path.join(OUTDIR, "RDOM-v1.0.0-dark.pdf")
        else:
            pdf_path = os.path.join(OUTDIR, "RDOM-v1.0.0.pdf")

        cmd = [
            "typst", "compile",
            "--root", ROOT,
            "--font-path", FONTS_DIR,
            typ_path,
            pdf_path
        ]
        print(f"Compiling {edition} edition -> {pdf_path}...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error compiling {edition}:", res.stderr, file=sys.stderr)
            sys.exit(res.returncode)
        print(f"Successfully compiled {pdf_path}")

        # Clean up temporary .typ file
        if os.path.exists(typ_path):
            os.remove(typ_path)

if __name__ == "__main__":
    main()
