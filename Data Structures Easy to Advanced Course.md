# Data Structures Easy to Advanced Course

## Additional resources

- William Fiset Github: <https://github.com/williamfiset>
- YT link: <https://www.youtube.com/watch?v=RBSGKlAvoiM>

## Table of contents

01. Abstract data types
02. Introduction to Big-O
03. Dynamic and Static Arrays
04. Dynamic Array Code
05. Linked Lists Introduction
06. Doubly Linked List Code
07. Stack Introduction
08. Stack Implementation
09. Stack Code
10. Queue Introduction
11. Queue Implementation
12. Queue Code
13. Priority Queue Introduction
14. Priority Queue Min Heaps and Max Heaps
15. Priority Queue Inserting Elements
16. Priority Queue Removing Elements
17. Priority Queue Code
18. Union Find Introduction
19. Union Find Kruskal's Algorithm
20. Union Find - Union and Find Operations
21. Union Find Path Compression
22. Union Find Code
23. Binary Search Tree Introduction
24. Binary Search Tree Insertion
25. Binary Search Tree Removal
26. Binary Search Tree Traversals
27. Binary Search Tree Code
28. Hash table hash function
29. Hash table separate chaining
30. Hash table separate chaining source code
31. Hash table open addressing
32. Hash table linear probing
33. Hash table quadratic probing
34. Hash table double hashing
35. Hash table open addressing removing
36. Hash table open addressing code
37. Fenwick Tree range queries
38. Fenwick Tree point updates
39. Fenwick Tree construction
40. Fenwick tree source code
41. Suffix Array introduction
42. Longest Common Prefix (LCP) array
43. Suffix array finding unique substrings
44. Longest common substring problem suffix
45. Longest common substring problem suffix 1.2
46. Longest Repeated Substring suffix array
47. Balanced binary search tree rotations
48. AVL tree insertion
49. AVL tree removals
50. AVL tree source code
51. Indexed Priority Queue | Data Structure
52. Indexed Priority Queue | Data Structure | Source Code

## 01. Abstract data types

- Q: **What is a Data structure?**
- A: a data Structure (DS) is a way of organizing data so that it can be used efficiently.

- Q: **Why DS**?
- A1: They are essential ingredients in creating fast & powerful algorithms.
- A2: Why help manage and organize data
- A3: They make code cleaner and easier to understand

### Abstract Data Types vs. Data Structures

An abstract data type (ADT) is an abstraction of a data structure which provides only the interface to which a data structure must adhere to.

The interface does not give any specific details about how something should be implemented or in what programming language.

Abstract data type is like a mode of transportation from a to b.
specific modes like walking or biking is a data structure.

Abstraction (ADT) | Implementation (DS)
--- | ---
Vehicle | Golf car, bicycle, smart car
List | Dynamic array, Linked List
Queue | Linked List Based Queue, Array Based Queue, Stack Based Queue
Map | Tree Map, Hash Map

## 02. Introduction to Big-O aka. Computational Complexity Analysis

As programmers, we often find ourselves asking the same two questions, over and over again:

- how much **time** does this algorithm need to finish
- how much **space** does this algorithm need for its computation

### Big-O Notation

Big-O notation gives an upper bound of the complexity in the **worst** case, helping to quantify performance as the input size becomes arbitrarily large.

n - the size of the input. Complexities ordered from smallest to largest

 Complexity | Big-O
 ---: | ---
Constant Time | O(1)
Logarithmic Time | O(log(n))
Linear Time | O(n)
Linearithmic Time | O(n * log(n))
Quadric time | O(n**2)
Cubic time | O(n**3)
Exponential time | O(b**n), b>1
Factorial Time | O(n!)

### Big O Properties

-  O(n+c) = O(n), we can remove constant values added to big-O notation.
-  O(n*c) = O(n), we can remove constant values multiplied to big-O notation.
- f(n) = 7 \* log(n)\*\*3 + 15 \* n\*\*2 + 2*m\*\*3 + 8 ~> O(f(n)) = O(n\*\*3), as n\*\*3 is the most dominant term in the function.

### Constant Time | O(1) examples

```python
a = 1
b = 2
c = a + 5 * b

i = 0
while i > 11:
    i=i+11
```

### Linear Time | O(n) examples

```python
i=0
while i<n:
  i=i+1
```

f(n) = n

O(f(n)) = O(n)

```python
i=0
while i<n:
  i=i+3
```

f(n) = n/3

O(f(n)) = O(n)

### Quadric time | O(n**2) examples

```python
for i in range(0, n)
    for j in range(0,n)
 ```

```python
for i in range(0, n)
    for j in range(i,n)
 ```

f(n) = n*n = n**2

O(f(n)) = O(n**2)

### Logarithmic Time | O(log(n)) example with binary search

```python
low, high = 0, len(n)
while low < high:
    mid = (low + high) /2

    if array[mid] == value:
        return mid
    elif array[mid] < value:
        low = mid + 1
    elif array[mid] > value:
        high = mid - 1
return False
```

O(log2(n)) = O(log(n))

### Other Big-O Examples

- Finding all subsets of a set O(2**n)
- Finding all permutations of a string O(n!)
- Sorting using mergesort O(n*log(n))
- Iterating over all the cells in a matrix if size m and n O(n*m)

