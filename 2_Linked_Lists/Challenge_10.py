from _LinkedList import LinkedList
from _Node import Node

# Double Iteration
def find_nth(lst,n):
  if lst.is_empty():
    return -1
  
  # Find length of list
  length = lst.length() - 1

  # Find the node which is at (len - n + 1) position from start
  current_node = lst.get_head()

  position = length - n + 1

  if position < 0 or position > length:
    return -1
  
  count = 0
  while count is not position:
    current_node = current_node.next_element
    count += 1

  if current_node:
    return current_node.data
  return -1
## Time Complexity
# It performs two iterations on the list so the complexity is O(n).

# two Pointers
def find_nth1(lst,n):
  if lst.is_empty():
    return -1
  
  nth_node = lst.get_head() # This iterator will reach the Nth node
  end_node = lst.get_head() # This iterator will reach the end of the list

  count = 0
  while count < n:
    if end_node is None:
      return -1
    end_node = end_node.next_element
    count +=1
  
  while end_node is not None:
    end_node = end_node.next_element
    nth_node = nth_node.next_element

  return nth_node.data


lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)


lst.print_list()
print(find_nth(lst, 5))
print(find_nth(lst, 1))
print(find_nth(lst, 10))

print(find_nth1(lst, 5))
print(find_nth1(lst, 1))
print(find_nth1(lst, 10))