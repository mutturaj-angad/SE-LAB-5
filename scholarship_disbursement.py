"""An in-memory ledger for scholarship awards and disbursements."""

import sqlite3


class AwardLedger:
    """Store scholarship awards and track their disbursement totals."""

    def __init__(self):
        self._connection = sqlite3.connect(":memory:")
        self._connection.execute(
            "CREATE TABLE awards ("
            "id INTEGER PRIMARY KEY, student TEXT, scheme TEXT, "
            "amount INTEGER, disbursed INTEGER)"
        )
        self.disbursed_total = 0

    def grant(self, student, scheme, amount, audit=None):
        """Record an award and add its student to the optional audit list."""
        self._connection.execute(
            "INSERT INTO awards (student, scheme, amount, disbursed) "
            "VALUES (?, ?, ?, 0)",
            (student, scheme, amount),
        )
        if audit is not None:
            audit.append(student)
            return audit
        return [student]

    def disburse(self, award_id):
        """Disburse once, returning the amount or None if unavailable."""
        row = self._connection.execute(
            "SELECT amount FROM awards WHERE id = ? AND disbursed = 0",
            (award_id,),
        ).fetchone()
        if row is None:
            return None

        self._connection.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?", (award_id,)
        )
        self.disbursed_total += row[0]
        return row[0]

    def archive(self):
        """Announce the archive operation performed by this demo ledger."""
        print("archiving awards")

    def by_scheme_count(self, scheme):
        """Return the number of awards for a scheme, or zero for None."""
        if scheme is None:
            return 0
        return self._connection.execute(
            "SELECT COUNT(*) FROM awards WHERE scheme = ?", (scheme,)
        ).fetchone()[0]


def main():
    """Run a short demonstration of granting and disbursing awards."""
    ledger = AwardLedger()
    ledger.grant("Ishaan", "Merit", 50000)
    ledger.grant("Divya", "Need-based", 75000)
    print(ledger.disburse(1), ledger.disburse(9))
    print(ledger.by_scheme_count("Merit"), ledger.disbursed_total)
    ledger.archive()


if __name__ == "__main__":
    main()
