# Stacks

Stacks follow the Last in First Out (LIFO) ordering. This means that the last element added is the element on the top and the first element added is at the bottom.

## What are Stacks Used for?

There are many famous algorithms such as Depth First Search and the Expression Evaluation Algorithm, which harness the functionality of Stacks. Stacks are used:

- To backtrack to the previous task/state, for example, in recursive code
- To store a partially completed task, for example, when you are exploring two different
  paths on a Graph from a point while figuring out the smallest path to the target.

### Complexities of Stack Operations

| Operation     | Time Complexity |
| ---------     | --------------- |
| push(element) | O(1)            |
| pop()         | O(1)            |
| peek()        | O(1)            |
| is_empty()    | O(1)            |
| size()        | O(1)            |
