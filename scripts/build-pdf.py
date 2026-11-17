#!/usr/bin/env python3
"""Typeset Ravenhelm Development Operations Methodology (RDOM) as publication-grade PDF using Typst.

Compiles two editions:
  dark   — bone on obsidian (screen edition, matching RLOM Dark and RROM Dark)
  print  — obsidian on bone paper (the print / digest edition)

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
    ("01-what-this-is.md", "01", "What This Is and Why Modern Engineering Drifts", "SCOPE: METHODOLOGY FRONT DOOR · APPLIES TO ALL TEAMS"),
    ("02-the-sovereign-triad.md", "02", "The Sovereign Triad: RLOM, RDOM, RROM", "FOUNDATION: THE SOVEREIGN TRIAD · RLOM · RDOM · RROM"),
    ("03-numbered-principles.md", "03", "The 24 Numbered Principles", "CANON: 24 NUMBERED PRINCIPLES · DP-1 THROUGH DP-24"),
    ("04-the-hierarchy-of-deeds.md", "04", "The Hierarchy of Deeds: Wyrd Rune to Daily Deed", "TAXONOMY: DEED HIERARCHY · WYRD RUNE TO DAILY DEED"),
    ("05-the-four-codices.md", "05", "The Four Codices: Shield, Cycle, Grimoire, Shield-Band", "STANDARDS: THE FOUR CODICES · SHIELD · CYCLE · GRIMOIRE · SHIELD-BAND"),
    ("06-the-engineering-okr-framework.md", "06", "The Engineering OKR Framework: Faster, Bigger, Cheaper, Effective", "ALIGNMENT: VALKNUT OKR MATRIX · FASTER · BIGGER · CHEAPER · EFFECTIVE"),
    ("07-ceremonies-of-truth.md", "07", "Ceremonies of Truth: Althing, Ráð, and Morning Muster", "CEREMONIES: ALTHING · RÁÐ · MORNING MUSTER · DOOM GATE"),
    ("08-the-dependency-dag-and-critical-chain.md", "08", "The Dependency DAG: Critical Path vs. Critical Chain", "TOPOLOGY: DEPENDENCY DAG · GOLDRATT CCPM · CRITICAL CHAIN"),
    ("09-topological-waves-replacing-sprints.md", "09", "Topological Waves: Replacing the Two-Week Sprint", "CADENCE: TOPOLOGICAL WAVES · HEIJUNKA LEVELING · BATCH CONTROL"),
    ("10-zero-collision-multi-agent-boundaries.md", "10", "Zero Collision by Construction: Multi-Agent Fleet Boundaries", "CONCURRENCY: ZERO-COLLISION BOUNDARIES · DISJOINT BLAST RADIUS"),
    ("11-jit-elaboration-and-anti-inventory.md", "11", "Just-In-Time Elaboration: Eradicating Inventory Waste (Muda)", "LEAN MANUFACTURE: JIT ELABORATION · ERADICATING INVENTORY MUDA"),
    ("12-the-dry-hoisting-protocol.md", "12", "The DRY Hoisting Protocol: Anti-Snowflake Planning", "REFACTORING: DRY HOISTING PROTOCOL · TWO-CONSUMER GATE"),
    ("13-six-sigma-wave-boundary-gates.md", "13", "Six Sigma Wave Boundary Gates: No Exit on a Promise", "QUALITY: SIX SIGMA WAVE GATES · DMAIC · TRIAD OF PROOF"),
    ("14-poka-yoke-interface-design.md", "14", "Poka-Yoke Interface Design & The Live System Rule", "ERROR PROOFING: SHINGO POKA-YOKE · TYPE STATES · LIVE SYSTEM RULE"),
    ("15-the-andon-cord-and-circuit-breakers.md", "15", "The Andon Cord Protocol & Upstream-Jump Circuit Breakers", "CIRCUIT BREAKERS: THE ANDON CORD · LIVE SILICON · STOP-THE-LINE"),
    ("16-workspace-custody-bare-and-worktrees.md", "16", "Workspace Custody: Bare Repositories and Disposable Worktrees", "INFRASTRUCTURE: CHECKOUT CUSTODY STANDARD · BARE & WORKTREES"),
    ("17-zero-waste-context-substrate-eat.md", "17", "The Zero-Waste Context Substrate: Topological Priming vs. Directory Dumps", "CONTEXT SUBSTRATE: EAT KNOWLEDGE SUBSTRATE · ZERO CONTEXT WASTE"),
    ("18-the-sovereign-engineering-organization.md", "18", "The Sovereign Engineering Organization: Operating Human-Agent Fleets", "ORGANIZATION: THE SOVEREIGN FLEET · HUMAN ARCHITECTS & AGENT SLICES"),
    ("appendix-a-presales-and-demo-ops.md", "A", "Presales, Solution Architecture & DemoOps Integration", "COMMERCIAL: DEMOOPS · EPHEMERAL SANDBOXES · PROTOTYPE HOISTING"),
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
  keywords: ("RDOM", "Ravenhelm", "Ehwaz", "Valknut", "Autonomous Agents", "Six Sigma", "Topological Waves")
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
)[#text(font: "IBM Plex Mono", size: 8.2pt, it)]

// Code styling: block code
#show raw.where(block: true): it => block(
  width: 100%,
  breakable: true,
  fill: card_bg,
  stroke: 0.5pt + card_border,
  inset: 7pt,
  radius: 3pt,
  spacing: 0.9em,
  text(font: "IBM Plex Mono", size: 7.2pt, fill: ink, it)
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
#show table: set text(font: "IBM Plex Mono", size: 7.2pt)
#show table.cell.where(y: 0): set text(weight: "bold", fill: ink)

// ==========================================
// 1. FRONT COVER
// ==========================================
#page(margin: 0in, numbering: none, header: none, footer: none)[
  #place(top + left, rect(width: 100%, height: 100%, fill: paper))
  #place(center + horizon, dy: -1.3in)[
    #image("{raven_logo}", width: 3.5in)
  ]
  #place(center + horizon, dy: 1.4in)[
    #set align(center)
    #text(font: "Source Serif 4", size: 24pt, weight: 600, fill: ink)[Ravenhelm Development Operations]
    #v(0.08in)
    #text(font: "Source Serif 4", size: 18pt, weight: 400, fill: garnet)[Methodology]
    #v(0.2in)
    #text(font: "IBM Plex Mono", size: 8.2pt, fill: ash, tracking: 0.14em)[A LEAN, TOPOLOGICAL, AND DEFECT-GATED FRAMEWORK FOR AUTONOMOUS AND HYBRID FLEETS]
    #v(0.55in)
    #text(font: "Source Serif 4", size: 11pt, weight: 600, fill: ink)[{BYLINE}]
    #v(0.05in)
    #text(font: "IBM Plex Mono", size: 7.5pt, fill: ash, tracking: 0.12em)[RAVENHELM LLC · 2026]
  ]
]

// ==========================================
// 2. VERSO / COPYRIGHT & IMPRINT
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(1fr)
  #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.04em, hyphenate: false)
  #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
  *Ravenhelm Development Operations Methodology (RDOM)* \\
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
  Typeset using Typst 0.15.1 on macOS. \\
  #v(0.4in)
]

// ==========================================
// 3. HALF TITLE & EPIGRAPH
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(2.3in)
  #align(center)[
    #text(font: "Source Serif 4", size: 14pt, weight: 600)[Ravenhelm Development Operations Methodology]
    #v(0.25in)
    #text(font: "Source Serif 4", size: 10.5pt, style: "italic", fill: ash)[
      "Concurrency is not granted by calendar fiat;\\
       it is earned through topological proof."
    ]
    #v(0.12in)
    #text(font: "IBM Plex Mono", size: 7.5pt, fill: garnet, tracking: 0.14em)[— THE FIRST CONCURRENCY INVARIANT (DP-2)]
  ]
]

// ==========================================
// 4. TABLE OF CONTENTS
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.4in)
  #align(center)[
    #text(font: "Source Serif 4", size: 18pt, weight: 600)[Contents]
  ]
  #v(0.25in)
  #outline(title: none, depth: 1, indent: auto)
]

// ==========================================
// 5. HOW TO READ IT
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.3in)
  #align(left)[
    #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[GUIDE]
    #v(0.08in)
    #heading(level: 1, numbering: none, outlined: true)[How to Read It]
    #v(0.05in)
    #line(length: 100%, stroke: 0.5pt + ash)
  ]
  #v(0.15in)

  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[IN ORDER] \\
  #set text(size: 8.8pt)
  The chapters build sequentially from foundational axioms to topological wave planning, zero-collision multi-agent fleet boundaries, DRY hoisting protocols, Six Sigma wave boundary gates, and the sovereign engineering organization. Chapter 3 (*The 24 Numbered Principles*) establishes the formal canon cited throughout every subsequent chapter as `DP-1` through `DP-24`.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[BY ROLE — THE INSTALL PATH] \\
  #set text(size: 8.8pt)
  *Chief Technology Officer & Architect:* Chapters 01, 02, 05, 06, 12, 18 (Sovereign Triad, Four Codices, DRY Hoisting, OKR Alignment). \\
  *Fleet Lead & Engineering Manager:* Chapters 04, 07, 08, 09, 11, 13 (Deed Hierarchy, Ceremonies, Dependency DAGs, Wave Gates). \\
  *Agent Engineer & Operator:* Chapters 03, 10, 14, 15, 16, 17 (Zero Collision, Type-State Poka-Yoke, Andon Cord, Bare Worktrees, EAT Substrate). \\
  *Systems Quality & Verification Auditor:* Chapters 07, 10, 13, 14, 15, Appendix A (Six Sigma Gates, Triad of Proof, Live Silicon, DemoOps).

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[BY NEED — RECOVERY & SCALING] \\
  #set text(size: 8.8pt)
  *Halting Sprint Collapses & Merge Collisions:* Read Chapters 01, 08, 09, 10. \\
  *Eliminating Multi-Agent Hallucinations & Snowflakes:* Read Chapters 10, 11, 12, 17. \\
  *Eradicating Downstream Defect Escapes:* Read Chapters 13, 14, 15.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[NAVIGATING THIS BOOK] \\
  #set text(size: 8.8pt)
  The bookmark outline carries every chapter and major section. Chapter openers feature metadata badges citing applicable codices and principles. Code symbols, AST byte manifests, and CLI recipes follow strict POSIX standards.
]

// ==========================================
// 6. THE PRINCIPLES AT A GLANCE
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.3in)
  #align(left)[
    #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[CANON]
    #v(0.08in)
    #heading(level: 1, numbering: none, outlined: true)[The Principles at a Glance]
    #v(0.05in)
    #line(length: 100%, stroke: 0.5pt + ash)
  ]
  #v(0.12in)
  #set text(font: "IBM Plex Mono", size: 7.2pt, fill: ash)
  #set par(justify: false, first-line-indent: 0em, leading: 0.8em)

  #text(weight: "bold", fill: garnet)[GROUP A — TOPOLOGICAL FOUNDATION & CRITICAL CHAIN] \\
  #text(fill: ink)[DP-1] A plan is a directed acyclic graph, not a task list \\
  #text(fill: ink)[DP-2] Concurrency is earned through topological proof; quality is gated by verified green \\
  #text(fill: ink)[DP-3] No two agents may possess write-intent on overlapping blast radii \\
  #text(fill: ink)[DP-4] Protect the critical chain over local resource utilization \\
  #text(fill: ink)[DP-5] The cost of an unaddressed blocker compounds exponentially with time \\
  \\
  #text(weight: "bold", fill: garnet)[GROUP B — JIT ELABORATION & ANTI-INVENTORY] \\
  #text(fill: ink)[DP-6] Speculative architecture is toxic inventory; detail decays with distance \\
  #text(fill: ink)[DP-7] Defect prevention upstream is an order of magnitude cheaper than downstream rework \\
  #text(fill: ink)[DP-8] Write the verification fixture before writing the execution logic \\
  #text(fill: ink)[DP-9] If a state transition is invalid, make it unrepresentable in the type system \\
  \\
  #text(weight: "bold", fill: garnet)[GROUP C — SILICON INTEGRITY & SIX SIGMA GATES] \\
  #text(fill: ink)[DP-10] Never mock what you have not already proven in live containerized silicon \\
  #text(fill: ink)[DP-11] A deed is not complete until witnessed by a passing test on clean silicon \\
  #text(fill: ink)[DP-12] Stop the line immediately upon defect escape \\
  #text(fill: ink)[DP-13] If code is written twice without being hoisted, the third use is a defect \\
  \\
  #text(weight: "bold", fill: garnet)[GROUP D — DRY HOISTING & TYPE ARCHITECTURE] \\
  #text(fill: ink)[DP-14] Refactoring is not an afterthought; it is the planned hoisting phase of wave execution \\
  #text(fill: ink)[DP-15] The interface belongs to the consumer; the implementation belongs to the producer \\
  #text(fill: ink)[DP-16] Every shared dependency must declare an explicit semantic contract \\
  #text(fill: ink)[DP-17] Every system must emit structured, traceable evidence of its state transitions \\
  #text(fill: ink)[DP-18] What works on the developer machine must work identically in production \\
  \\
  #text(weight: "bold", fill: garnet)[GROUP E — WORKSPACE CUSTODY & CONTEXT SUBSTRATE] \\
  #text(fill: ink)[DP-19] History lives once in a bare clone; worktrees are disposable projections \\
  #text(fill: ink)[DP-20] Prime on topology in \\<800 tokens; never dump directory trees \\
  #text(fill: ink)[DP-21] Never carry uncommitted work across branch boundaries via stash \\
  #text(fill: ink)[DP-22] Deletion of any workspace requires positive proof of custody \\
  #text(fill: ink)[DP-23] The atomic unit of delivery is the witnessed Daily Deed \\
  #text(fill: ink)[DP-24] Never rewrite an existing deed; supersede it with an explicit amendment
]

// ==========================================
// 7. RUNNING HEADERS & BODY PAGES
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
    for file_name, num, title, badge_text in CHAPTER_FILES:
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
  #heading(level: 1, numbering: (..n) => "{num}", outlined: true)[{title}]
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
  Version 1.0.0 (2026-11-17) \\
  Authored by {BYLINE}. \\
  {COPYRIGHT} \\
  Published by {IMPRINT}. \\
  Distributed under the Apache License, Version 2.0. \\
  Set in Source Serif 4 and IBM Plex Mono. \\
  Typeset using Typst 0.15.1 on macOS. \\
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
