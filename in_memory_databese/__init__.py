class InMemoryDatabase:
    def __init__(self):
        # Initialize the in-memory database
        self.data = {}
        self.transactions = []

    def get(self, key):
        """
        Get the value associated with the given key.
        :param key: The key to retrieve.
        :return: The value associated with the key or None if the key does not exist.
        """
        return self.data.get(key, None)

    def set(self, key, value):
        """
        Store a key-value pair in the database.
        :param key: The key to store.
        :param value: The value to associate with the key.
        :return: None
        """
        self._save_old_value_for_transaction(key)
        self.data[key] = value

        return None

    def delete(self, key):
        """
        Delete the key-value pair associated with the given key.
        :param key: The key to delete.
        :return: None
        """
        self._save_old_value_for_transaction(key)
        del self.data[key]

        return None

    def start_transaction(self):
        """
        Start a new transaction. All operations within this transaction are isolated from others.
        :return: None
        """
        self.transactions.append([])

        return None

    def commit(self):
        """
        Commit all changes made within the current transaction to the database.
        :return: None
        """
        self.transactions.pop()

        return None

    def rollback(self):
        """
        Roll back all changes made within the current transaction and discard them.
        :return: None
        """
        for (key, old_value) in reversed(self.transactions.pop()):
            if old_value is None:
                del self.data[key]
            else:
                self.data[key] = old_value

        return None

    def _save_old_value_for_transaction(self, key):
        if self.transactions:
            transaction = self.transactions[-1]
            transaction.append((key, self.data.get(key, None)))


if __name__ == '__main__':
    # Example 1 for commit a transaction
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.set("key1", "value2")
    db.commit()
    db.get("key1")  # -> Expect to get “value2”

    # Example 2 for rollback().
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.get("key1")  # -> Expect to get “value1”
    db.set("key1", "value2")
    db.get("key1")  # -> Expect to get ”value2”
    db.rollback()
    db.get("key1")  # -> Expect to get “value1”

    # Example 3 for nested transactions
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.set("key1", "value2")
    db.get("key1")  # -> Expect to get ”value2”
    db.start_transaction()
    db.get("key1")  # -> Expect to get ”value2”
    db.delete("key1")
    db.commit()
    db.get("key1")  # -> Expect to get None
    db.commit()
    db.get("key1")  # -> Expect to get None

    # Example 4 for nested transactions with rollback()
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.set("key1", "value2")
    db.get("key1")  # -> Expect to get ”value2”
    db.start_transaction()
    db.get("key1")  # -> Expect to get ”value2”
    db.delete("key1")
    db.rollback()
    db.get("key1")  # -> Expect to get “value2”
    db.commit()
    db.get("key1")  # -> Expect to get “value2”
