## Solution: Using a Set/Hash Table

from LinkedList import LinkedList
from Node import Node

def remove_duplicates(lst):
  current_node = lst.get_head()
  prev_node = lst.get_head()

  visited_nodes = set()

  ## # If List is not empty and there is more than 1 element in List
  if not lst.is_empty() and current_node.next_element:
    while current_node:
      value = current_node.data
      if value in visited_nodes:
        # current_node is already in the HashSet
        # connect prev_node with current_node's next element
        # to remove it
        prev_node.next_element = current_node.next_element
        current_node = current_node.next_element
        continue
      visited_nodes.add(current_node.data)
      prev_node = current_node
      current_node = current_node.next_element

## Every node we traverse is added to the visited_nodes set. If we reach a node that already exists in the set, it must be a duplicate.
## prev_node is used to keep track of the preceding node. This allows us to easily manipulate the previous and next nodes during the 
## deletion of our current_node.
      
## Time Complexity
## This is a linear algorithm, hence, the time complexity is O(n)

lst = LinkedList()
lst.insert_at_head(7)
lst.insert_at_head(7)
lst.insert_at_head(22)
lst.insert_at_head(14)
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()

remove_duplicates(lst)
lst.print_list()