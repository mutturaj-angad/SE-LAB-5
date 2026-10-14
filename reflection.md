# Reflection

The supplied handout states that students should reflect on how static analysis contributes to code quality and maintainability, but it does not provide a separate list of exact reflection questions. The responses below address that stated reflection objective using the issues and results from this project.

## Issues found and fixes applied

Bandit found SQL string interpolation that could allow SQL injection. I changed the insert to use SQLite placeholders. It also found shell execution and a broad exception handler that hid failures; I removed the shell command and printed the archive notice directly. Pylint identified a mutable list default, which could share audit data between calls, so the method now creates a new list unless one is passed in. I also tested the disbursement behavior and found that paying the same award twice increased the total twice. The ledger now selects only unpaid awards.

## What the three tools contributed

Pylint checked code quality and common programming mistakes, including naming, documentation, global state, and the mutable default. Bandit identified security-sensitive patterns, including SQL construction and shell use. Flake8 reported formatting problems such as long lines and a comparison to None. The tools overlap in some areas but bring different perspectives to a review.

The original Pylint score was 5.00/10 and the final score was 10.00/10. Bandit reported one Medium and three Low findings before the fixes and no findings afterward. Flake8 reported six violations before the fixes and none afterward.

## Why static analysis matters

Static analysis can flag risky code before it is exercised with every possible input. It made several issues in this small program easier to see and gave concrete diagnostics to verify after changes. The tools do not prove the application is correct: my repeat-disbursement test found a data-integrity bug that the analyzer reports did not flag. I learned to use analyzer results together with tests and a review of the program's behavior.
