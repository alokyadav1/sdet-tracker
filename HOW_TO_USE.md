# How to Use This Tracker

## 1. Create the repo

Create a new GitHub repository (private is fine — this is a personal tracker,
nothing here needs to be public). Don't initialize it with a README, since this
zip already has one.

## 2. Push these files

```bash
cd sdet-tracker
git init
git add .
git commit -m "chore: initial 8-month SDET tracker"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 3. Wire up the badges

Open `README.md` and replace `<your-username>/<your-repo>` in the three badge
URLs near the top with your actual path, e.g. `alok-k/sdet-8-month-tracker`.
Commit and push that one-line change.

## 4. Confirm Actions are enabled

New repos have Actions on by default. If pushes to `tracker/**/*.md` don't
trigger a run, check **Settings → Actions → General → Actions permissions** and
make sure it's not disabled.

## 5. Daily use

Open the file for whatever phase/track you're on right now, e.g.:

```
tracker/theory/phase-2-api-testing.md
tracker/automation/phase-2-api-testing.md
```

Do the task, flip `- [ ]` to `- [x]`, commit, push:

```bash
git add tracker/
git commit -m "progress: week 6 automation — GET/POST automated"
git push
```

Within ~30 seconds the Action re-runs `scripts/generate_progress.py`, updates
`PROGRESS.md`, and refreshes the three badge JSON files. Refresh the repo page
or `README.md` to see the new percentage.

## 6. Weekly review

Every week in the plan ends with a Sunday review day. Good moment to also open
`PROGRESS.md` and glance at the phase table — if theory and automation
percentages for the current phase are drifting far apart, that's worth
noticing (e.g. if you've check off every automation box but skipped the
theory ones, you're building without the reasoning to defend it in an
interview, which is exactly the gap this plan exists to close).

## 7. Optional: GitHub Issues + Projects board

If you'd rather have a kanban view:

1. Go to **Issues → New Issue** and pick either **📘 Theory Task** or
   **🤖 Automation Task**.
2. Fill in the week, phase, and task (copy text straight from the relevant
   `tracker/` file).
3. Create a **Projects (v2)** board (top-level **Projects** tab on your
   profile or the repo's **Projects** tab → **New project** → *Board* template).
4. Add a `Track` field with two options, `Theory` / `Automation`, and group the
   board by it — that gives you the same two-track separation as a kanban view.

This is entirely optional and doesn't replace the checkbox files — use
whichever (or both) fits how you think.

## 8. Resetting or regenerating

- **Just want current numbers?** `python3 scripts/generate_progress.py` — safe,
  read-only with respect to your checkmarks, only rewrites `PROGRESS.md` and
  `badges/`.
- **Want to wipe all progress and start over, or you edited the task data in
  `scripts/generate_tracker.py`?** `python3 scripts/generate_tracker.py` —
  ⚠️ this overwrites every file in `tracker/theory/` and `tracker/automation/`
  from scratch, erasing any `[x]` you've already set. Commit your current
  state first if you want to keep a snapshot you can look back at.

## 9. If you extend the plan later

`scripts/generate_tracker.py` is a plain Python dict (`WEEKS`) keyed by week
number, with each day tagged `"theory"`, `"automation"`, or `"both"`. Adding a
Week 33+ (e.g. if you extend back toward the original 12-month scope) is just
adding another entry to that dict and re-running the generator — no need to
hand-write new markdown files.
