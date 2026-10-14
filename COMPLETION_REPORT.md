# Lab 5 Completion Report

## Project summary

The scholarship ledger now uses parameterized SQL, handles audit lists safely, avoids shell execution and silent exception handling, and prevents repeated disbursement of an already paid award. The demonstration still grants two awards, disburses the first, counts the Merit award, and prints an archive notice.

## Files changed and created

- Updated `scholarship_disbursement.py` with the corrected ledger and runnable demonstration.
- Updated `README.md` with runtime, test, and analysis commands.
- Added `test_scholarship_disbursement.py` with three focused regression tests.
- Added `issues.md` and `reflection.md`.
- Added the six before/after reports: `pylint_before.txt`, `pylint_after.txt`, `bandit_before.txt`, `bandit_after.txt`, `flake8_before.txt`, and `flake8_after.txt`.
- Added the handout's final report names: `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt`.
- Added `baseline_runtime.txt`, `runtime_after.txt`, and `tests_after.txt` as execution evidence.

## Issues and fixes

The original SQL string interpolation was reported as Bandit B608 (Medium severity, Medium confidence). Bandit also reported B605 and B607 for shell execution (Low, High confidence), and B110 for a try/except/pass block (Low, High confidence). Pylint reported the mutable default argument (W0102), naming and documentation problems, and comparison to `None`. Flake8 reported six line-length/`None` comparison violations. A regression check also exposed double-counting on repeat disbursement. Details, original line references, and final checks are in `issues.md`.

## Analyzer results

- **Pylint:** before 5.00/10; after 10.00/10.
- **Bandit:** before one Medium finding and three Low findings; after zero findings (zero Low, Medium, or High).
- **Flake8:** before six reported violations; after no output (zero violations).

The before reports preserve the pre-edit findings. Final reports were generated against the corrected `scholarship_disbursement.py` using Python 3.13.5, Pylint 4.1.3, Bandit 1.9.4, and Flake8 7.4.1 in `.venv`.

## Tests and runtime verification

- On 2026-10-14, reran `.venv\Scripts\python.exe -m unittest discover -v`: **3 tests passed**.
- On 2026-10-14, reran Pylint with `--persistent=n`: exit 0, **10.00/10**; Bandit: exit 0, **no issues identified**; Flake8: exit 0, **no output**.
- Reran `.venv\Scripts\python.exe scholarship_disbursement.py`: exit 0; output was `50000 None`, `1 50000`, and `archiving awards`.
- Recreated the before reports from the original script contents in an isolated temporary directory. Pylint scored **5.00/10**; Bandit reported B608 (Medium/Medium), B605, B607, and B110 (Low/High); Flake8 reported six violations. The temporary source directory was removed.
- `git diff --check` cannot run meaningfully here because the project folder has no Git metadata. A local text audit found no conflict markers; the original Bandit baseline includes one trailing whitespace character in tool output.

## Deliverable inventory

Source, README, tests, issues table, reflection draft, six before/after reports, three final report-name copies, runtime evidence, test evidence, and this completion report are present. The handout PDF was not found in the workspace. Consequently, `reflection.md` is explicitly a draft responding to the requested topics, not a claim to answer the handout's exact questions.

## Git and push

The project directory is not a Git repository: `git status`, `git remote -v`, and `git log` report that no `.git` repository exists here. A search under `C:\Users\Lenovo` and `C:\SEM 5` found one other clone, `C:\SEM 5\DBMS LAB\researchiq`. It is a TypeScript research application on branch `master`, has no configured remote, and contains numerous pre-existing modified and untracked files; it is unrelated to this scholarship project. It was not modified. No matching scholarship clone was found. No commits were created and no push was attempted. **Commit hashes: none. Push status: not attempted.**

## Remaining limitations

- Provide the original scholarship repository clone (or its correct local path) so the changes can be reconciled and committed after inspecting that clone's existing work. Three commits and a push remain undone; no applicable scholarship remote/branch is verified.
- Provide `Lab_5_Static_Code_Analysis_Student_handout.pdf`. No matching PDF was found under `C:\Users\Lenovo`, `C:\SEM 5`, or the Codex attachments directory. Until supplied, `reflection.md` remains explicitly labelled as a draft and does not claim to answer the exact instructor questions.
