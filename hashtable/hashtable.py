class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.fecs = 0
        self.storage = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.fecs / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2. NO!! I SHALL NOT!!!
        """
        # Your code here
        FNV_prime = 2**40 + 2**8 + 0xb3
        hash = 14695981039346656037
        for i in key:
            hash *= FNV_prime
            hash = hash ^ ord(i)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1. NO!! I SHALL NOT!!!
        """
        # Your code here
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        hashEntry = HashTableEntry(key, value)
        noodle = self.storage[i]

        if noodle is not None:
            self.storage[i] = hashEntry
            self.storage[i].next = noodle
        else:
            self.storage[i] = hashEntry
        self.fecs += 1

        # Code below is for no collisions
        # hashValue = self.hash_index(key)
        # self.storage[hashValue] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # Old Code for no Collisions
        # hashValue = self.hash_index(key)
        # self.storage[hashValue] = None
        
        i = self.hash_index(key)
        oldy = None
        noodle = self.storage[i]
        if noodle.key == key:
            self.storage[i] = noodle.next
            return
        while noodle != None:
            if noodle.key == key:
                oldy.next = noodle.next
                self.storage[i].next = None
                return
            oldy = noodle
            noodle = noodle.next
        self.fecs -= 1
        return

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # Old Code for no Collisions
        # hashValue = self.hash_index(key)
        # return self.storage[hashValue]

        i = self.hash_index(key)
        noodles = self.storage[i]
        if noodles is not None:
            while noodles:
                if noodles.key == key:
                    return noodles.value
                noodles = noodles.next
        return noodles

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        for i in range(len(old_storage)):
            oldone = old_storage[i]
            if oldone:
                while oldone:
                    if oldone.key:
                        self.put(oldone.key, oldone.value)
                        oldone = oldone.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
