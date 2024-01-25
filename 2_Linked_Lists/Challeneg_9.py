from _LinkedList import LinkedList
from _Node import Node

def union(list1, list2):
  if (list1.is_empty()):
    return list2
  if (list2.is_empty()):
    return list1
  
  start = list1.get_head()

  while start.next_element:
    start = start.next_element

  start.next_element = list2.get_head()
  list1.remove_duplicates()
  return list1
## Time Complexity
## If we did not have to care for duplicates, The runtime complexity of this algorithm would be O(m) where m is the size of the first list. 
## However, because of duplicates, we need to traverse the whole union list. This increases the time complexity to O(l^2) where l = m + n. 
# Here, m is the size of the first list, and n is the size of the second list.
def intersection(list1,list2):
  result = LinkedList()
  current_node = list1.get_head()

  while current_node is not None:
    value = current_node.data
    if list2.search(value) is not None:
      result.insert_at_head(value)
    current_node = current_node.next_element

  # Remove duplicates if any
    result.remove_duplicates()
    return result


ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)
ulist1.insert_at_head(14)
ulist1.insert_at_head(21)
print("List 1")
ulist1.print_list()

ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(7)

print("List 2")
ulist2.print_list()

new_list = union(ulist1,ulist2)
print("Union of list 1 and 2")
new_list.print_list()

ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)

ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)

lst = intersection(ilist1, ilist2)
print("Intersection of list 1 and 2")
lst.print_list()