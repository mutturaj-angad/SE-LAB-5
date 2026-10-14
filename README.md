# Lab 5: Static Code Analysis — Scholarship Disbursement Ledger

This project demonstrates a small in-memory scholarship ledger. It records awards, disburses an award once, counts awards by scheme, and prints an archive notice.

## Requirements and run

Python 3.13 was used for this submission. The program uses only the Python standard library at runtime.

```powershell
python scholarship_disbursement.py
```

## Tests and analysis

Install the analysis tools in a virtual environment, then run the tests and analyzers:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pylint bandit flake8
.\.venv\Scripts\python.exe -m unittest discover -v
.\.venv\Scripts\python.exe -m pylint --persistent=n scholarship_disbursement.py
.\.venv\Scripts\python.exe -m bandit -r scholarship_disbursement.py
.\.venv\Scripts\python.exe -m flake8 scholarship_disbursement.py
```

The repository includes preserved before-and-after reports for each analyzer. The original handout's `*_report.txt` names also contain the final analyzer outputs. See [issues.md](issues.md), [reflection.md](reflection.md), and [COMPLETION_REPORT.md](COMPLETION_REPORT.md) for the findings, reflection, and verification summary. The supplied handout PDF gives a general reflection objective but no explicit question list; reflection.md responds to that objective without inventing questions.
