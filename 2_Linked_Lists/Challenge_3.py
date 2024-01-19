from _LinkedList import LinkedList
from _Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}

def delete(lst, value):
    deleted = False
    if lst.is_empty():
        print("List is Empty")
        return deleted
    current_node = lst.get_head() # Get current node
    previous_node = None # Get Previous node
    if current_node.data == value:
        lst.head_node = current_node.next_element
        current_node.next_element = None
        deleted = True
        return deleted
    
    # Traversing/Searching for Node to delete
    while current_node is not None:
        if value == current_node.data:
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element
    if deleted:
        print(str(value)+ " is deleted!")
    else:
        print(str(value)+ " is not in list!")
    return deleted

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 2)
lst.print_list()