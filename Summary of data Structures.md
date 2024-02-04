# Overview of Linear & Non-Linear Data Structures

## Linear Data Structures

In linear data structures, each element is connected to either one (the next element) or two (the next and previous) more elements. Traversal in these structures is linear, meaning that insertion, deletion, and search work in O(n).

**Lists, linked lists, stacks**, and **queues** are all example of linear data structures.

## Non-Linear Data Structures

The exact opposite of linear data structures is non-linear data structures. In a non-linear data structure, each element can be connected to several other data elements. Traversal is not linear and, hence, search, insertion, and deletion can work in O(log n) and even O(1) time.

**Trees, graph**s and **hash tables** are all non-linear data structures.

### Time and Space Complexity Cheat Table

| Data Structure | Insert | Delete | Search | Space Complexity |
| -------------- | ------ | ------ | ------ | ---------------- |
| Array          | O(n)   | O(n)   | O(n)   |     O(n)         |
| Singly Linked list | O(1) (insert at head) | O(1) (delete at head) | O(n) | O(n) |
| Stack | O(1)(Push) | O(1)(Pop) | O(n) | O(n) |
| Queue | O(1)(enqueue) | O(1)(dequeu) | O(n) |O(n) |
