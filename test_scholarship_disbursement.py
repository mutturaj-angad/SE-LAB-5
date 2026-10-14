"""Focused tests for scholarship ledger behavior and input handling."""

import unittest

from scholarship_disbursement import AwardLedger


class AwardLedgerTests(unittest.TestCase):
    """Verify award recording, counting, and one-time disbursement."""

    def setUp(self):
        self.ledger = AwardLedger()

    def test_grant_uses_values_as_data_and_counts_scheme(self):
        student = "O'Neil'); DROP TABLE awards; --"
        self.ledger.grant(student, "Merit", 125)

        self.assertEqual(self.ledger.by_scheme_count("Merit"), 1)
        self.assertEqual(self.ledger.by_scheme_count("Other"), 0)
        self.assertEqual(self.ledger.by_scheme_count(None), 0)

    def test_audit_lists_are_independent_unless_supplied(self):
        first_audit = self.ledger.grant("A", "Merit", 10)
        second_audit = self.ledger.grant("B", "Merit", 20)
        shared_audit = ["Earlier"]
        result = self.ledger.grant("C", "Merit", 30, shared_audit)

        self.assertEqual(first_audit, ["A"])
        self.assertEqual(second_audit, ["B"])
        self.assertIs(result, shared_audit)
        self.assertEqual(shared_audit, ["Earlier", "C"])

    def test_award_can_be_disbursed_only_once(self):
        self.ledger.grant("A", "Merit", 500)

        self.assertEqual(self.ledger.disburse(1), 500)
        self.assertIsNone(self.ledger.disburse(1))
        self.assertIsNone(self.ledger.disburse(999))
        self.assertEqual(self.ledger.disbursed_total, 500)


if __name__ == "__main__":
    unittest.main()
