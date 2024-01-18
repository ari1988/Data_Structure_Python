from _Node import Node
from _LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Searches a value in the given list.


def search(lst, value):
    current_node = lst.get_head()

    while current_node:
        if current_node.data == value:
            return True
        current_node = current_node.next_element
    return False

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.print_list()
print(search(lst, 4))