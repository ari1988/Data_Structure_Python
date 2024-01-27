from Queue import MyQueue

def find_bin(number):
  result = []
  queue = MyQueue()
  queue.enqueue(1)
  for i in range(number):
    result.append(str(queue.dequeue()))
    s1 = result[i] + "0"
    s2 = result[i] + "1"
    queue.enqueue(s1)
    queue.enqueue(s2)

  return result

##  The size of Queue should be 1 more than the number because, for a single number, 
# we’re enqueuing two variations of it, one with appended 0 while the other with 1 being appended.

## Time Complexity
## he time complexity of this solution is in O(n) as constant-time operations are executed for n times.

print(find_bin(5))