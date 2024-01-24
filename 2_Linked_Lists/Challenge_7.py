from _LinkedList import LinkedList
from _Node import Node

## Solution: 1 #Using Two Pointers
## Time Complexity : We are traversing the linked list at twice the speed, so it is certainly faster. However, the bottleneck complexity is still O(n).
def find_mid_1(lst):
  if lst.is_empty():
    return -1
  current_node = lst.get_head()
  if current_node.next_element == None:
    #Only 1 element exist in array so return its value.
    return current_node.data
  
  mid_node = current_node
  current_node = current_node.next_element.next_element
  #Move mid_node (Slower) one step at a time
  #Move current_node (Faster) two steps at a time
  #When current_node reaches at end, mid_node will be at the middle of List 
  while current_node:
    mid_node = mid_node.next_element
    current_node = current_node.next_element
    if current_node:
      current_node = current_node.next_element #it help makes 2 hops
  if mid_node:
    return mid_node.data
  return -1

## Solution: 2 #Using Brute Force Method
## Time Complexity : We are traversing the linked list at twice the speed, so it is certainly faster. However, the bottleneck complexity is still O(n).
def find_mid_2(lst):
  if lst.is_empty():
    return None
  node = lst.get_head()
  mid = 0
  if lst.length() % 2 == 0:
    mid = lst.length() // 2
  else:
    mid = lst.length()// 2 + 1

  for i in range(mid - 1):
    node = node.next_element
  return node.data

lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(15)
lst.insert_at_head(20)
lst.insert_at_head(30)
lst.insert_at_head(40)
lst.insert_at_head(45)
lst.insert_at_head(100)

lst.print_list()
print(find_mid_1(lst))
print(find_mid_2(lst))