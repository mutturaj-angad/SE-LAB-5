# Reflection (Draft)

The lab handout PDF and its exact four reflection questions were not present in the workspace. This is a clearly labelled draft based on the topics named in the README and task instructions; it does not claim to reproduce the instructor's questions.

## 1. What issues did you find, and how did you fix them?

The original code built an SQL command by inserting student and scheme text directly into the query. I changed it to use SQLite placeholders so those values are treated as data. The `grant` function also used a list as its default argument, which could cause audit entries to be shared across calls. It now creates a new list when no audit list is supplied. The archive function invoked a shell command and silently ignored every exception, so I replaced it with a direct print operation. I also found by checking the behavior that disbursing the same award twice increased the total twice; the ledger now only disburses an unpaid award. Finally, I corrected naming, `None` comparison, documentation, and line-length issues.

## 2. How are Pylint, Bandit, and Flake8 different?

Pylint checks many aspects of Python code quality, such as naming, documentation, control flow, and common programming mistakes, and gives an overall score. Bandit searches Python syntax for patterns that can create security risks. Flake8 focuses on style and simple code problems such as unused imports and lines that exceed the configured length. Their results overlap in places, but each tool has a different focus.

## 3. Why is static code analysis important?

Static analysis can find potential defects without needing every input or execution path to be run. It gives developers an early way to notice risky patterns and inconsistent code. The tools do not prove a program is correct, so their findings still need to be checked against the intended behavior and verified with tests.

## 4. What did you learn from comparing the reports and testing the fixes?

The original Pylint score was 5.00/10. After the code changes, it was 10.00/10. Bandit first reported a medium SQL injection concern and three low-severity shell or exception-handling findings; the final Bandit report has no findings. Flake8 initially reported six style violations and the final report is empty. Regression tests also checked malicious-looking SQL input, independent audit lists, scheme counts, missing awards, and repeat disbursement. This showed me that analyzer output is useful, but behavioral tests can catch problems such as double-counting that these reports did not identify.
