from LinkedList import LinkedList
from Node import Node


def detect_loop(lst):
    # Used to store nodes which we already visited
    visited_nodes = set()
    current_node = lst.get_head()

    # Traverse the set and put each node in the visitedNodes set
    # and if a node appears twice in the map
    # then it means there is a loop in the set
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)  # Insert node in visitedNodes set
        current_node = current_node.next_element
    return False

# ------------------------------
## We iterate over the whole linked list and add each visited node to a visited_nodes set.
## At every node, we check whether it has been visited or not.

## By principle, if a node is revisited, a cycle exists!

## Time Complexity
## We iterate the list once. On average, lookup in a set takes O(1) time. Hence, the average runtime of this algorithm is O(n).
## However, in the worst case, lookup can increase up to O(n), which would cause the algorithm to work in O(n^2).

lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
print(detect_loop(lst))

head = lst.get_head()
node = lst.get_head()

# Adding a loop
for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(lst))