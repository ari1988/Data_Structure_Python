# What is a Queue?

The only significant difference between stacks and queues is that instead of using the LIFO principle, queues implement the FIFO method which is short for First in First Out.

According to FIFO, the first element inserted is the one that comes out first. You can think of a queue as a pipe with two ends called front and rear / back. Elements from a queue are always deleted from the front and added at the rear.

Queues are slightly trickier to implement as compared to stacks because we have to keep track of both ends of the array. The elements are inserted from the back and removed from the front.

## What are Queues used for?

- We want to prioritize something over another
- A resource is shared between multiple devices

| Function         | What does it do?                                  |
| ---------------  | -------------------------                         |
| enqueue(element) | insert elements at the end of the queue           |
| dequeue()        | removes an element from the start of the queue    |
| front()          | returns the first element of the queue            |
| rear()           | returns ther last element inserted into the queue |
| isEmpty()        | checks if the queue is empty                      |
| size()           | returns the size of the queue                     |

### Types of Queues

- Linear Queue
- Circular Queue
- Priority Queue
- Double-ended Queue

#### Circular Queue

circular queues are circular in structure which means that both ends are connected to form a circle. Initially, the front and rear part of the queue point to the same location. Eventually they move apart as more elements are inserted into the queue.
Circular queues are generally used in:

- Simulation of objects
- Event handling (do something when a particular event occurs)

#### Priority Queue

In priority queues, all elements have a priority associated with them and are sorted such that the most prioritized object appears at the front and the least prioritized object appears at the end of the queue. These queues are widely used in most operating systems to determine which programs should be given more priority.

#### Double-Ended Queue

The double-ended queue acts as a queue from both ends(back and front). It is a flexible data structure that provides enqueue and dequeue functionality on both ends in O(1).

##### Complexities of Queue Operations

| Operation       | Time Complexity |
| ---------       | --------------- |
| is_empty()      | O(1)            |
| front()         | O(1)            |
| rear()          | O(1)            |
| size()          | O(1)            |
| enqueue(element)| O(1)            |
| dequeue()       | O(1)            |
