import matplotlib.pyplot as plt
class Doubly_LL:
    """
       A class to represent a node in a doubly linked list.

       Attributes:
       ----------
       prev : Doubly_LL or None
           A reference to the previous node in the list. Defaults to None.
       next : Doubly_LL or None
           A reference to the next node in the list. Defaults to None.
       data : any
           The data stored in the node.

       Methods:
       -------
       insert_after_head(node):
           Inserts a new node immediately after the current node.

       delete_node(node_ad):
           Deletes a specified node from the doubly linked list.
           Ensures the previous and next pointers of adjacent nodes are updated.
           Returns the data of the deleted node.
       """
    def __init__(self, data) :
        self.prev = None
        self.next = None
        self.data = data

    def insert_after_head(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def delete_node(self, node_ad):
        if node_ad.prev:
            node_ad.prev.next = node_ad.next
        if node_ad.next:
            node_ad.next.prev = node_ad.prev
        node_ad.prev = None
        node_ad.next = None
        return node_ad.data


class LRU_Cache:
    """
        A class to implement a Least Recently Used (LRU) Cache with efficient operations.

        Attributes:
        ----------
        capacity : int
            Maximum number of elements the cache can hold.
        head : Doubly_LL
            Dummy head node of the doubly linked list.
        tail : Doubly_LL
            Dummy tail node of the doubly linked list.
        dic : dict
            Dictionary for O(1) key-value lookups.
        count : int
            Current number of elements in the cache.
        total_accesses : int
            Total number of `get` and `put` operations performed.
        miss_count : int
            Total number of cache misses.
        miss_rates : list
            Miss rate over time for plotting purposes.

        Methods:
        -------
        put(key, value):
            Inserts a key-value pair into the cache.
            Updates the least recently used status for existing keys.

        get(key):
            Retrieves the value associated with a key, or -1 if the key is not in the cache.
            Updates the least recently used status.

        miss_rate():
            Calculates the miss rate as a percentage of total accesses.

        plot_miss_rate():
            Plots the cache miss rate over time using matplotlib.

        print_LRU():
            Prints the current state of the cache from most to least recently used.
        """
    def __init__(self, capacity) :
        if not (1 <= capacity <= 50):
            raise ValueError("Capacity must be between 1 and 50")
        self.capacity = capacity
        self.head = Doubly_LL((-1, -1))
        self.tail = Doubly_LL((-1, -1))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
        self.count = 0
        self.total_accesses = 0
        self.miss_count = 0
        self.miss_rates = []

    def put(self, key, value):
        if not (0 <= key <= 100):
            raise ValueError("Key must be between 0 and 100")
        if not (0 <= value <= 100):
            raise ValueError("Value must be between 0 and 100")
        self.total_accesses += 1

        if key in self.dic:
            # Cache hit: Update value and move to the front
            node_ad = self.dic[key]
            node_ad.data = (key, value)
            self.head.delete_node(node_ad)
            self.head.insert_after_head(node_ad)
        else:
            # Cache miss
            self.miss_count += 1
            if self.count == self.capacity:
                # Remove the least recently used item if the cache is full
                lru_key = self.tail.prev.data[0]
                self.tail.delete_node(self.tail.prev)
                del self.dic[lru_key]
                self.count -= 1

            # Add the new node to the front
            new_node = Doubly_LL((key, value))
            self.head.insert_after_head(new_node)
            self.dic[key] = new_node
            self.count += 1

        current_miss_rate = self.miss_rate()
        self.miss_rates.append(current_miss_rate)

    def get(self, key):
        if not (0 <= key <= 100):
            raise ValueError("Key must be between 0 and 100")
        self.total_accesses += 1

        if key not in self.dic:
            self.miss_count += 1
            return -1

        # Cache hit: Move the accessed node to the front
        node_ad = self.dic[key]
        self.head.delete_node(node_ad)
        self.head.insert_after_head(node_ad)
        return node_ad.data[1]

    def miss_rate(self):
        """Calculates the miss rate for the current run."""
        if self.total_accesses == 0:
            return 0.0
        return (self.miss_count / self.total_accesses)*100

    def plot_miss_rate(self):
        """Plot the miss rate over time using matplotlib."""
        plt.plot(self.miss_rates, label="Miss Rate")
        plt.xlabel('Operations')
        plt.ylabel('Miss Rate')
        plt.title('Miss Rate Over Time')
        plt.legend()
        plt.show()


    def print_LRU(self):
        a = self.head.next
        while a != self.tail:
            print(a.data, end=" <-> ")
            a = a.next
        print("END")


operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

#Initialize the LRUCache
lru_cache = None
output = []
#
for i, operation in enumerate(operations):
    if operation == "LRUCache":
        capacity = values[i][0]
        lru_cache = LRU_Cache(capacity)
        output.append(None)
    elif operation == "put":
        key, value = values[i]
        lru_cache.put(key, value)
        output.append(None)
    elif operation == "get":
        key = values[i][0]
        result = lru_cache.get(key)
        output.append(result)

print("Output:", output)
print(lru_cache.miss_rate())

#Create an LRU Cache with capacity 50
capacity = 50
lru_cache = LRU_Cache(capacity)
# Fill the cache with keys 0-49 and values 0-49
print(">>> Filling the cache with keys 0-49 and values 0-49")
for i in range(50):
    lru_cache.put(i, i)
    print(f"LRU Cache after putting ({i}, {i}):")
    lru_cache.print_LRU()

print("\nFinal LRU Cache State:")
lru_cache.print_LRU()
print(f"Total Miss Rate: {lru_cache.miss_rate():.2f}%\n")

# Retrieve the odd-numbered keys from the cache
print(">>> Retrieving odd-numbered keys")
for i in range(1, 100, 2):
    result = lru_cache.get(i)
    print(f"Get {i}: {result}")
    print("LRU Cache state:")
    lru_cache.print_LRU()

print("\nFinal LRU Cache State:")
lru_cache.print_LRU()
print(f"Total Miss Rate: {lru_cache.miss_rate():.2f}%\n")

# Refilling the cache with prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(">>> Refilling the cache with prime number keys (0-100)")
prime_numbers = [i for i in range(101) if is_prime(i)]
for prime in prime_numbers:
    lru_cache.put(prime, prime)
    print(f"LRU Cache after putting prime ({prime}, {prime}):")
    lru_cache.print_LRU()

print("\nFinal LRU Cache State:")
lru_cache.print_LRU()
print(f"Total Miss Rate: {lru_cache.miss_rate():.2f}%\n")

# Plot miss rate
print(">>> Plotting miss rate")
lru_cache.plot_miss_rate()


