class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        


# Hash table can't have fewer than this many slots
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        

    def insert_at_head(self, node):
        # print(node.value, 'node')
        if self.head == None:
            self.head = node
            # print(self.head.value, 'if')
        else:
            node.next = self.head
            self.head = node
            # print(self.head.value, 'else')

    def find(self, value):
        # print("find was called")
        # print(self.head, 'self.head')
        cur = self.head
        # print(cur.value, value, 'cur.val, val')
        while cur is not None:
            
            if cur.value == value:
                # print(cur, "cur")
                return cur.value
            cur = cur.next
        print("here")
        return None

    def delete(self, value):
        cur = self.head
        if cur.value == value:
            self.head = self.head.next
            return cur
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """


    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.count = 0



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):                                                                                                                           
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity
    

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        slot = self.hash_index(key)
        hashdex = self.storage[slot]
        while hashdex is not None and hashdex != key:
            hashdex = hashdex.next
        if hashdex is not None:
            hashdex.value = value
            # print(hashdex.value, hashdex.key, slot, 'hashdex if')
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[slot]
            self.storage[slot] = new_entry
            # print(self.storage[slot].value, self.storage[slot].key, slot, 'hashdex else')



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        slot = self.hash_index(key)
        hash_entry = self.storage[slot]
        prev_entry = hash_entry

        while hash_entry is not None:
            if hash_entry.key == key:
                hash_entry.value = None
                # prev_entry.next = hash_entry.next
                return 
            else:
                prev_entry = hash_entry
                hash_entry = hash_entry.next
        print("Key is not found")
        return

        
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        slot = self.hash_index(key)
        hash_entry = self.storage[slot]

        while hash_entry is not None:
            if hash_entry.key == key:
                return hash_entry.value
            else:
                hash_entry = hash_entry.next
                
        



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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
    ht.get("line_1")
    ht.get("line_2")
    ht.get("line_3")
    ht.get("line_4")

    print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")

