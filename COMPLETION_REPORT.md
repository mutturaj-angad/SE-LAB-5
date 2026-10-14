# Lab 5 Completion Report

## Project summary

Completed the scholarship ledger static-analysis lab. The application uses parameterized SQLite values, tracks ledger state per instance, prevents an award from being disbursed twice, and retains the demo's grant, count, and archive behavior.

## Deliverables

- `scholarship_disbursement.py`: corrected application.
- `test_scholarship_disbursement.py`: three regression tests.
- `issues.md`: verified issue table with original line numbers, analyzer IDs, severity/confidence, fixes, and verification.
- `reflection.md`: clearly labelled draft. The lab handout PDF was not found, so it does not claim to answer the instructor's exact questions.
- `README.md`: setup, run, test, and analysis commands.
- Before/after reports: `pylint_before.txt`, `pylint_after.txt`, `bandit_before.txt`, `bandit_after.txt`, `flake8_before.txt`, and `flake8_after.txt`.
- Final handout-name reports: `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt`.
- Execution evidence: `baseline_runtime.txt`, `runtime_after.txt`, and `tests_after.txt`.

## Issues addressed

Bandit reported SQL interpolation (B608, Medium severity/Medium confidence), shell execution (B605 and B607, Low/High), and a swallowed exception (B110, Low/High). Pylint reported mutable default state (W0102), global state and consistency/naming/documentation issues. Flake8 reported six style violations. Behavioral testing also exposed repeat-disbursement double-counting. The fixes and results are detailed in `issues.md`.

## Verified results

Verification was rerun in the repository clone on 2026-10-14 using Python 3.13.5, Pylint 4.1.3, Bandit 1.9.4, and Flake8 7.4.1.

- Pylint: **5.00/10 before; 10.00/10 after**.
- Bandit: **one Medium and three Low findings before; zero findings after**.
- Flake8: **six violations before; zero after**.
- `.venv\Scripts\python.exe -m unittest discover -v`: **3 tests passed**.
- Demo: exited successfully; printed `50000 None`, `1 50000`, and `archiving awards`.
- `git show --check` passed for each of the three analyzer commits. The clone's working tree was clean after those commits.

## Repository, commits, and push

The supplied repository was cloned from `https://github.com/mutturaj-angad/SE-LAB-5.git`. At clone time it was empty, with no existing commits or files. The clone's branch is `main`, tracking `origin/main`. No existing student changes were overwritten.

The three requested commits were created and pushed to `origin/main`:

1. `571191e` - `fix(security): parameterize SQL and remove shell archiving`
2. `23e5cf1` - `fix(quality): isolate ledger state and prevent duplicate payouts`
3. `987ffd5` - `style(flake8): wrap long docstrings and add analysis deliverables`

The non-force push succeeded. The final remote branch was checked against local `main` after pushing the report update. A documentation-only follow-up commit records this report; see `git log` for its hash.

## Remaining limitation

The exact handout questions remain unavailable. Provide `Lab_5_Static_Code_Analysis_Student_handout.pdf` to replace the labelled reflection draft with answers to the instructor's exact questions. No other code, test, report, commit, or push work remains.
