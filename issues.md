# Static Analysis Issues

The line numbers below refer to the original `scholarship_disbursement.py` before edits. Tool names and diagnostic codes come from the captured `*_before.txt` reports. “Final verification” reflects the final source analysis and focused tests.

| Issue | Category | Original line | Detection and severity | Why it matters | Fix implemented | Final verification |
|---|---|---:|---|---|---|---|
| I-01 | Security | 10 | Bandit B608; Medium severity, Medium confidence | Interpolating student and scheme strings into SQL can break queries and permit SQL injection. | Replaced interpolation with SQLite placeholders and bound values in `AwardLedger.grant`. | B608 absent from `bandit_after.txt`; malicious-looking student input test passes and the table remains queryable. |
| I-02 | Security | 26 | Bandit B605 and B607; Low severity, High confidence | `os.system` starts a shell using a partial executable lookup and adds an unnecessary command execution path. | Removed shell execution; the demo archive notice is printed directly. | B605 and B607 absent from `bandit_after.txt`; demo runs and prints the archive notice. |
| I-03 | Maintainability | 27–28 | Bandit B110; Low severity, High confidence; Pylint W0718 | A broad exception handler that silently ignores failures hides problems and makes the archive action appear successful. | Removed the unnecessary shell operation and its catch-all handler. | B110 and W0718 absent from final reports; archive demo runs successfully. |
| I-04 | Bug | 9 | Pylint W0102 | A mutable list default is shared between calls, so audit entries can leak between unrelated grants. | Changed the default to `None` and create a fresh result list per call; callers may still pass a shared audit list. | W0102 absent from `pylint_after.txt`; independent-default and supplied-list tests pass. |
| I-05 | Bug | 16–21 | Manual behavior check; not reported by the three analyzers | Repeating a successful disbursement counted the same award amount multiple times. | Only select awards whose `disbursed` flag is zero, and return `None` when an award is missing or already paid. | Regression test verifies a repeated call returns `None` and the total remains unchanged. |
| I-06 | Style / maintainability | 5, 31–32 | Flake8 E501 and E711; Pylint C0103, C0114, C0116, C0301, C0121 | Long lines, missing documentation, inconsistent naming, and equality comparison with `None` make the code harder to read and maintain. | Added module/function documentation, snake_case naming, wrapped long statements, and `is None`; moved state into `AwardLedger`. | `flake8_after.txt` is empty; Pylint reports 10.00/10. |

## Reports

`pylint_before.txt`, `bandit_before.txt`, and `flake8_before.txt` are preserved baseline outputs. The corresponding `*_after.txt` files contain final outputs. The handout's requested `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt` are also included as copies of the final reports.
