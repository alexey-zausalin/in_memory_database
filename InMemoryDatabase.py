class InMemoryDatabase:
    def __init__(self):
        # Initialize the in-memory database

    def get(self, key):
        """
        Get the value associated with the given key.
        :param key: The key to retrieve.
        :return: The value associated with the key or None if the key does not exist.
        """

    def set(self, key, value):
        """
        Store a key-value pair in the database.
        :param key: The key to store.
        :param value: The value to associate with the key.
        :return: None
        """

    def delete(self, key):
        """
        Delete the key-value pair associated with the given key.
        :param key: The key to delete.
        :return: None
        """

    def start_transaction(self):
        """
        Start a new transaction. All operations within this transaction are isolated from others.
        :return: None
        """

    def commit(self):
        """
        Commit all changes made within the current transaction to the database.
        :return: None
        """

    def rollback(self):
        """
        Roll back all changes made within the current transaction and discard them.
        :return: None
        """

if __name__ == '__main__':
    # Example 1 for commit a transaction
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.set("key1", "value2")
    db.commit()
    db.get("key") # -> Expect to get “value2”
    
    # Example 2 for rollback().
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.get("key1") #   -> Expect to get “value1”
    db.set("key1", "value2")
    db.get("key1") #   -> Expect to get ”value2”
    db.rollback()
    db.get("key") #   -> Expect to get “value1”
    
    # Example 3 for nested transactions
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.set("key1", "value2")
    db.get("key1") #   -> Expect to get ”value2”
    db.start_transaction()
    db.get("key1") #   -> Expect to get ”value2”
    db.delete("key1")
    db.commit()
    db.get("key") #    -> Expect to get None
    db.commit()
    db.get("key") #    -> Expect to get None
    
    # Example 4 for nested transactions with rol_back()
    db = InMemoryDatabase()
    db.set("key1", "value1")
    db.start_transaction()
    db.set("key1", "value2")
    db.get("key1") #   -> Expect to get ”value2”
    db.start_transaction()
