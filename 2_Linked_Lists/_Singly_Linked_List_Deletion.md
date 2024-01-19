# Singly Linked List Deletion

The deletion operation combines principles from both insertion and search. It uses the search functionality to find the value in the list.
Deletion is one of the instances where linked lists are more efficient than arrays. In an array, you have to shift all the elements backward if one element is deleted. Even then, the end of the array is empty and it takes up unnecessary memory.

In the case of linked lists, the node can simply be removed in constant time.

---

## Types of Deletion

There are three basic delete operations for linked lists:

- Deletion at the head
- Deletion by value
- Deletion at the tail

### Delete at head

This operation simply deletes the first node from a list. If the list is empty, the function does nothing.

```python
from LinkedList import LinkedList
from Node import Node


def delete_at_head(lst):
    # Get Head and firstElement of List
    first_element = lst.get_head()

    # if List is not empty then link head to the
    # nextElement of firstElement.
    if first_element is not None:
        lst.head_node = first_element.next_element
        first_element.next_element = None
    return


lst = LinkedList()
for i in range(11):
    lst.insert_at_head(i)

lst.print_list()

delete_at_head(lst)
delete_at_head(lst)

lst.print_list()
```

#### Explanation

Time Complexity: `O(1)`

There is nothing too complicated going on here. We access the first element of the list

`first_element = lst.get_head()`
first_element can either be a node (the list is not empty) or not intialized (if the list is empty).

If a node is found, its `next_element` becomes the head.

Now, `first_element` has been removed from the linked list and its deletion from memory will be handled by Python since we haven’t specified a destructor.
