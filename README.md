# SDET Progress Tracker — 8-Month Plan (32 Weeks)

![Overall](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/alokyadav1/sdet-tracker/main/badges/overall.json)
![Theory](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/alokyadav1/sdet-tracker/main/badges/theory.json)
![Automation](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/alokyadav1/sdet-tracker/main/badges/automation.json)

This repo tracks execution of the 8-month (32-week) Senior/4-5yr-SDET-calibrated
learning plan, split into two independent, checkbox-based tracks:

- **📘 Theory** — concepts, strategy docs, ADRs, decision-making, articulation/mock-interview practice
- **🤖 Automation** — hands-on coding, framework building, CI/CD, tool usage

Both tracks are further split into the same **8 phases**, so you can see at a
glance whether a phase is theory-heavy, automation-heavy, or balanced.

## How progress is tracked

Every task lives as a `- [ ]` checkbox inside a markdown file under `tracker/`.
Check a box, commit, push — a GitHub Action (`.github/workflows/update-progress.yml`)
automatically recomputes `PROGRESS.md` and the three badges above within about 30
seconds. No manual bookkeeping, no spreadsheet, no third-party service.

See **[PROGRESS.md](PROGRESS.md)** for the current per-phase breakdown.

## Structure

```
sdet-tracker/
├── tracker/
│   ├── theory/          ← 8 files, one per phase (phase-1 ... phase-8)
│   └── automation/       ← same 8 phases, mirrored
├── scripts/
│   ├── generate_tracker.py    ← single source of truth for all 32 weeks' tasks
│   └── generate_progress.py   ← scans checkboxes, writes PROGRESS.md + badges/
├── badges/                    ← auto-generated shields.io endpoint JSON (don't hand-edit)
├── .github/
│   ├── ISSUE_TEMPLATE/         ← optional: track individual tasks as GitHub Issues instead
│   └── workflows/update-progress.yml
└── PROGRESS.md                ← auto-generated summary (don't hand-edit)
```

## The 8 phases

| # | Phase | Weeks |
|---|---|---|
| 1 | QA Foundations & Test Strategy, at Architect Level | 1–3 |
| 2 | API Testing at Senior Depth | 4–8 |
| 3 | Advanced JavaScript/TypeScript for Framework Architecture | 9–10 |
| 4 | Git, Code Review Discipline, and Q1 Capstone | 11–12 |
| 5 | Playwright & Framework Architecture at Depth | 13–15 |
| 6 | CI/CD Ownership at Scale | 16–18 |
| 7 | Performance, AI-in-QA, and System Design | 19–24 |
| 8 | Interview Machine + Portfolio + DSA | 25–32 |

Open `tracker/theory/phase-N-<slug>.md` or `tracker/automation/phase-N-<slug>.md`
for the week-by-week, day-by-day checklist for any phase.

## Daily workflow

1. Open the theory or automation file for your current phase.
2. Do the task for today.
3. Check the box: `- [ ]` → `- [x]`.
4. Commit and push. That's it — the Action handles the rest.

Some tasks (full-loop mocks, buffer days) genuinely span both tracks. Those are
marked with 🔗 and appear in **both** files — check both copies when you finish one.

## Optional: GitHub Issues + Projects board

If you'd rather work from a kanban board than markdown checklists, two issue
forms are included — **📘 Theory Task** and **🤖 Automation Task**
(`.github/ISSUE_TEMPLATE/`). Create an Issue per task, add it to a GitHub
Projects (v2) board with `Theory` / `Automation` as swimlanes, and use that
alongside or instead of the checkbox files. See [HOW_TO_USE.md](HOW_TO_USE.md)
for the two-minute setup.

## Regenerating

Both scripts are pure Python stdlib (no `pip install` needed):

```bash
python3 scripts/generate_progress.py   # safe to run anytime — recomputes from current checkboxes
python3 scripts/generate_tracker.py    # ⚠ resets all checkboxes — only run if you mean to
```

Full setup instructions: **[HOW_TO_USE.md](HOW_TO_USE.md)**
