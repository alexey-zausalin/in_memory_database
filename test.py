import unittest

from in_memory_databese import InMemoryDatabase


class TestInMemoryDatabase(unittest.TestCase):

    def test_commit_a_transaction(self):
        """
        Test for commit a transaction
        """
        db = InMemoryDatabase()
        db.set("key1", "value1")
        db.start_transaction()
        db.set("key1", "value2")
        db.commit()
        self.assertEqual("value2", db.get("key1"))

    def test_rollback(self):
        """
        Test for rollback()
        """
        db = InMemoryDatabase()
        db.set("key1", "value1")

        db.start_transaction()
        self.assertEqual("value1", db.get("key1"))
        db.set("key1", "value2")
        self.assertEqual("value2", db.get("key1"))
        db.rollback()
        self.assertEqual("value1", db.get("key1"))

    def test_nested_transactions(self):
        """
        Test for nested transactions
        """
        db = InMemoryDatabase()
        db.set("key1", "value1")
        db.start_transaction()
        db.set("key1", "value2")
        self.assertEqual("value2", db.get("key1"))
        db.start_transaction()
        self.assertEqual("value2", db.get("key1"))
        db.delete("key1")
        db.commit()
        self.assertEqual(None, db.get("key1"))
        db.commit()
        self.assertEqual(None, db.get("key1"))

    def test_nested_transactions_with_rollback(self):
        """
        Test for nested transactions with rollback
        """
        db = InMemoryDatabase()
        db.set("key1", "value1")
        db.start_transaction()
        db.set("key1", "value2")
        self.assertEqual("value2", db.get("key1"))
        db.start_transaction()
        self.assertEqual("value2", db.get("key1"))
        db.delete("key1")
        db.rollback()
        self.assertEqual("value2", db.get("key1"))
        db.commit()
        self.assertEqual("value2", db.get("key1"))


if __name__ == '__main__':
    unittest.main()
