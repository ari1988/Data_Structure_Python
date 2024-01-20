from _Node import Node
from _LinkedList import LinkedList

def length(lst):
  # start from the first element
  current_node = lst.get_head()
  length = 0
  while current_node:
    length += 1
    current_node = current_node.next_element
  return length
## Time Complexity
## Since this is a linear algorithm, the time complexity will be O(n).

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
lst.insert_at_head(0)
print(length(lst))