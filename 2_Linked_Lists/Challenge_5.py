from _LinkedList import LinkedList
from _Node import Node

def reverse(lst):
  # To reverse linked list, we need to keep track of three things
  previous = None # track of previous node
  current = lst.get_head() # The current node
  next = None

  # Reversal
  while current:
    next = current.next_element
    current.next_element = previous
    previous = current
    current = next

    #Set the last element as the new head node
    lst.head_node = previous
  return lst

## The brain of this solution lies in the loop which iterates through the list. For any current node, its link with the previous node is reversed and next stores the next node in the list:

## Store the current node’s next_element in next
## Set current node’s next_element to previous (reversal)
## Make the current node the new previous so that it can be used for the next iteration
## Use next to move on to the next node
## In the end, we simply point the head to the last node in our loop.

## Time Complexity
## The algorithm runs in O(n) since the list is traversed once.

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(4)
lst.insert_at_head(9)
lst.insert_at_head(10)
lst.print_list()

reverse(lst)
lst.print_list()