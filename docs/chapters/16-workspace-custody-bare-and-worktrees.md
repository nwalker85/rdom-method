<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 16 — Workspace Custody: The Bare Repository and Disposable Worktrees

In standard developer practice, git repositories are cloned as monolithic working copies. When an engineer needs to switch tasks, review a teammate’s pull request, or experiment with a fix, they execute `git stash`, checkout another branch, and pray that the stash applies cleanly when they return. In high-concurrency environments with autonomous coding agents, this practice leads to catastrophic state corruption, clobbered files, and lost working progress.

RDOM establishes the **Checkout Custody Standard** governed by dedicated git worktrees projected from a central bare repository (DP-19).

```
  CANONICAL REPOSITORY STORAGE (History Lives Once):
  /Users/nate/src/github.com/org/repo/
  ├── .bare/                     <-- Bare git repository (objects, refs, packfiles)
  ├── .git                       <-- Pointer to .bare
  │
  DISPOSABLE WORKING TREES (Projections of Canonical Identity):
  ├── main/                      <-- Clean mirror of origin/main (read-only baseline)
  ├── feat-auth-service/         <-- Agent A Worktree (Branch: feat/auth-service)
  ├── feat-billing-worker/       <-- Agent B Worktree (Branch: feat/billing-worker)
  └── fix-upstream-schema/       <-- Engineer Hotfix Worktree (Branch: fix/upstream-schema)
```

### The Architecture of Workspace Custody

1. **History Lives Once in `.bare/`**:
   The repository history, object database, and reflog live exclusively in a single `.bare/` directory. No developer or agent ever writes code directly inside `.bare/`.
2. **Worktrees are Disposable Projections**:
   Every branch, task, or agent run operates within its own dedicated, isolated directory created via `git worktree add`. Each worktree has its own separate index, working files, and HEAD, completely isolated from all other concurrent worktrees.
3. **Zero Ambient Mutation on Hosts (DP-21)**:
   Builds, tests, and environment configurations within a worktree must never mutate system-wide dependencies, global Python/Node packages, or root filesystems. Toolchains must be isolated via hermetic package managers (`uv`, `pnpm`, or Nix/Docker containers).
4. **WIP Commits Replace Git Stash (DP-22)**:
   `git stash` is strictly forbidden across branch transitions. Stashes are untracked, fragile, and lack commit metadata. State persistence is accomplished through frequent, structured `wip: <state>` commits pushed to the remote feature branch.

### The Worktree Lifecycle Protocol

```
  [ DAG Authorization ] ──> git worktree add <path> -b feat/<task>
                                    │
                                    ▼
                             [ TDD Execution ]
                                    │
                                    ▼
                             [ WIP Commits ] (DP-22)
                                    │
                                    ▼
                             [ Green CI Verification ] (DP-7)
                                    │
                                    ▼
                             [ Pull Request Review & Merge ] (DP-23)
                                    │
                                    ▼
  [ Custody Proof Verified ] ──> git worktree remove <path> (DP-24)
```

### Clean Worktree Disposal (DP-24)

A worktree is a temporary workspace, not an archival storage unit. However, a worktree may never be unmounted or deleted blindly. Deletion is gated by **Custody Proof**:
1. All changes have been committed and pushed to the remote repository.
2. The pull request has been formally merged into `main` (or explicitly abandoned with an ADR).
3. No untracked artifacts, logs, or uncommitted files remain that have not been reconciled.
4. The worktree is cleanly removed using `git worktree remove`, leaving the object repository pristine.

> **Augmentation Surface — Automated Worktree Management**
>
> Where an agent layer transforms this practice: the orchestration system automatically provisions an isolated worktree for each dispatched agent task, monitors commit cadence, and safely tears down the worktree once the pull request is merged, completely automating workspace hygiene.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a
  word-count: 730
  principle-citations: DP-7, DP-19, DP-21, DP-22, DP-23, DP-24
  flagged-principle-gaps: none
-->
