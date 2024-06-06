class HashTable:
    """
    A hash table data structure.

    Args:
        size (int): The size of the hash table. Defaults to 10.

    Attributes:
        table (list): The hash table.
    """

    def __init__(self, size: int = 10):
        """
        Initializes a hash table object.

        Args:
            size (int): The size of the hash table. Defaults to 10.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
        """
        self.table = []

        # Initialize the hash table with empty lists
        for i in range(size):  # O(n) - for loop
            self.table.append([])

    def _hash(self, key) -> int:
        """
        Hashes the given key to a hash value.

        Args:
            key: The key to hash.

        Returns:
            int: The hash value.

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        # Hash the key and return the hash value
        return hash(key) % len(self.table)

    def get(self, key) -> any:
        """
        Gets the value for the given key in the hash table.

        Args:
            key: The key to get the value for.

        Returns:
            any: The value for the given key.

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        # Hash the key to get the hash value
        hash_value = self._hash(key)

        # Search for the key in the hash table and return the value if found
        for i in self.table[hash_value]:  # O(n) - for loop
            item_key, item_value = i
            if item_key == key:
                return i[1]

        # If the key is not found, return None
        return None

    def get_all(self) -> []:
        """
        Gets all the key-value pairs in the hash table.

        Returns:
            list: A list of key-value pairs in the hash table.

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
        """
        items = []
        num_items = self.__len__()  # O(n^2) - function call

        for i in range(num_items):
            items.append(self.get(i + 1))

        return items

    def add(self, key, value) -> None:
        """
        Sets the value for the given key in the hash table.

        Args:
            key: The key to set.
            value: The value to set.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        hash_value = self._hash(key)

        # Append the key-value pair to the hash table
        self.table[hash_value].append((key, value))

    def update(self, key, value):
        """
        Updates the value for the given key in the hash table.

        Args:
            key: The key to update.
            value: The value to update.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        hash_value = self._hash(key)

        # Search for the key in the hash table and update the value if found
        for i in range(len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i] = key, value
                return

    def __len__(self) -> int:
        """
        Returns the size of the hash table.

        Returns:
            int: The size of the hash table.

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n^2)
                average case = O(n^2)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        size = 0

        for i in self.table:  # O(n) - for loop
            size += len(i)  # O(n) - len function call

        return size
