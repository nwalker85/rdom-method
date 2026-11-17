#!/usr/bin/env bash
#
# compile.sh — concatenate the 18 RDOM chapters (plus Appendix A) into a single-file edition.
#
# Usage:
#   ./scripts/compile.sh > build/rdom.md
#   ./scripts/compile.sh --with-shared > build/rdom-annotated.md
#
# Output: a single Markdown document with a generated table of contents,
# chapters in canonical order, and a horizontal rule between each chapter.
#
# Notes:
#   - Chapters carry their own license header; the compiled doc preserves the
#     first one and strips duplicates from later chapters.
#   - Chapters end with a <!-- RUBRIC_CHECK --> HTML comment; the compiled doc
#     keeps these (useful for audit) but they could be stripped for publication.
#
# Exit codes:
#   0 — success
#   1 — chapter file missing
#   2 — invalid argument

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHAPTERS_DIR="${ROOT}/docs/chapters"
SHARED_DIR="${ROOT}/docs/_shared"

WITH_SHARED=0
case "${1:-}" in
    --with-shared) WITH_SHARED=1 ;;
    "" ) ;;
    *)
        echo "Usage: $0 [--with-shared]" >&2
        exit 2
        ;;
esac

CHAPTERS=(
    "01-what-this-is.md"
    "02-the-sovereign-triad.md"
    "03-numbered-principles.md"
    "04-the-hierarchy-of-deeds.md"
    "05-the-four-codices.md"
    "06-the-engineering-okr-framework.md"
    "07-ceremonies-of-truth.md"
    "08-the-dependency-dag-and-critical-chain.md"
    "09-topological-waves-replacing-sprints.md"
    "10-zero-collision-multi-agent-boundaries.md"
    "11-jit-elaboration-and-anti-inventory.md"
    "12-the-dry-hoisting-protocol.md"
    "13-six-sigma-wave-boundary-gates.md"
    "14-poka-yoke-interface-design.md"
    "15-the-andon-cord-and-circuit-breakers.md"
    "16-workspace-custody-bare-and-worktrees.md"
    "17-zero-waste-context-substrate-eat.md"
    "18-the-sovereign-engineering-organization.md"
    "appendix-a-presales-and-demo-ops.md"
)

# Verify all chapter files exist before printing anything
for ch in "${CHAPTERS[@]}"; do
    if [ ! -f "${CHAPTERS_DIR}/${ch}" ]; then
        echo "ERROR: missing chapter file: ${CHAPTERS_DIR}/${ch}" >&2
        exit 1
    fi
done

# Title block (license header from chapter 1 is preserved at the top)
printf '# Ravenhelm Development Operations Methodology (RDOM)\n\n'
printf '*A Lean, Topological, and Defect-Gated Framework for Autonomous and Hybrid Software Engineering Fleets.*\n\n'
printf '© 2026 Ravenhelm LLC. Licensed material.\n\n'
printf -- '---\n\n'

# Generated table of contents
printf '## Table of contents\n\n'
i=1
for ch in "${CHAPTERS[@]}"; do
    title=$(grep -m1 -E '^## (Chapter|Appendix)' "${CHAPTERS_DIR}/${ch}" | sed 's/^## //')
    if [ -z "${title}" ]; then
        title="Chapter ${i}"
    fi
    anchor=$(printf '%s' "${title}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | tr -s '-')
    printf -- '- [%s](#%s)\n' "${title}" "${anchor}"
    i=$((i + 1))
done
printf '\n---\n\n'

# Optionally include the authoring spec (useful for internal review builds)
if [ "${WITH_SHARED}" -eq 1 ]; then
    printf '## Authoring spec (internal)\n\n'
    printf '### CONTEXT\n\n'
    cat "${SHARED_DIR}/CONTEXT.md"
    printf '\n---\n\n'
    printf '### PRINCIPLES scaffold\n\n'
    cat "${SHARED_DIR}/PRINCIPLES.md"
    printf '\n---\n\n'
fi

# Chapters — strip the license header from all chapters after the first (kept at the top of the compiled doc)
first=1
for ch in "${CHAPTERS[@]}"; do
    if [ "${first}" -eq 1 ]; then
        cat "${CHAPTERS_DIR}/${ch}"
        first=0
    else
        # Skip leading license HTML comments and blank line
        sed -e '/^<!-- LICENSE:/d' -e '/^<!-- All rights reserved/d' -e '/^<!-- Inquiries:/d' "${CHAPTERS_DIR}/${ch}"
    fi
    printf '\n---\n\n'
done
