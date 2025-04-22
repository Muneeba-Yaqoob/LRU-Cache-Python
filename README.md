# LRU-Cache-Python
This repository contains a Python implementation of the **Least Recently Used (LRU) Cache**. It utilizes a doubly linked list and a dictionary to efficiently manage cache items and their access order. The LRU Cache ensures that the least recently used items are evicted when the cache reaches its capacity.
Features
Efficient O(1) Operations: The `get` and `put` operations are implemented with constant time complexity, O(1), using a combination of a doubly linked list and a dictionary.
Cache Miss Tracking: Tracks the number of cache misses and provides a miss rate percentage.
Cache Visualization: Prints the current state of the cache and plots the miss rate over time.
Capacity Management: The cache ensures that the least recently used item is evicted when the cache exceeds its capacity.
How It Works:
The LRU Cache is backed by a doubly linked list where the most recently used items are placed at the head, and the least recently used items are at the tail. A dictionary is used for fast lookups of cache items, which provides the ability to perform put and get operations in constant time, O(1).
Key Operations:
put(key, value): Inserts a key-value pair into the cache. If the cache is full, the least recently used item is removed.
get(key): Retrieves the value associated with the given key. If the key is not in the cache, it returns -1.
miss_rate(): Returns the cache miss rate as a percentage.
plot_miss_rate(): Plots the miss rate over time.
print_LRU(): Prints the current state of the cache.
