Lab 05: 2436 Hash Table Lab 05

Student Information

Name: Ahmed Ajlal
Date: 02/28/2026
Key Concepts

[Explain the main concepts from this lab in your own words]

This lab explored how a hash table works and what makes it enable constant time access. The basic concept is that a hash table has a function that maps keys to an array. The basic concept I learned from this lab is that a hash table can store and retrieve information in constant time, O(1). I learned that collisions occur when two keys are mapped to the same location. To solve these collisions, we can implement chaining or linear probing. The other important concept I learned from this lab is that we need to maintain a good load factor. To maintain a good load factor, we need to resize and rehash.

What I Learned

[Describe what you learned while completing this lab]

While performing the lab, I learned how to create a hash table from scratch, not relying on the in-built dictionary feature in Python. I learned more about the hashing process, such as how to calculate the index by performing modulo arithmetic. I also learned how to deal with collision in the hash table by means of linear probing and how to search in the hash table without getting stuck in an infinite loop. Performing these operations by hand helped me understand the efficiency of the hash table and how it can degrade in case of collision.

Challenges

[What was the most difficult part? How did you solve it?]

The most difficult aspect to deal with was the collision when inserting and searching the table. It was not easy to ensure that the probes wrapped around the table and ended at the correct place without an infinite loop. Another challenge was ensuring that when an existing key is updated, the count of elements is not increased. I resolved these issues by paying close attention to the starting point and the use of modulo arithmetic to traverse the table safely.

Reflection Questions

[Answer the reflection questions from the instructions file]

Advantages of a hash table:
Hash tables provide fast average-case insertion, search, and deletion (O(1)). They are efficient for storing and retrieving key–value pairs and are widely used in caching and databases.

Effect of the hash function:
A good hash function distributes keys evenly, reducing collisions and keeping operations fast. A poor hash function causes clustering, which slows performance toward O(n).

Other collision resolution techniques:
Besides linear probing, techniques include quadratic probing, double hashing, and separate chaining, where each index stores a list of elements.
