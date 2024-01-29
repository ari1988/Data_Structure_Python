from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if queue.is_empty() or k > queue.size() or k < 0:
        return None
    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())
    return None

## Time Complexity
## The time complexity of this function is O(n) where n is the size of the queue as the entire queue is iterated over. 
## k elements are iterated over in the first two loops and size-k are iterated over in the last loop which sums up to n iterations.

if __name__ == "__main__" :
    # testing our logic
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    print("the queue before reversing:")
    print(queue.items)
    reverseK(queue, 5)
    print("the queue after reversing:")
    print(queue.items)