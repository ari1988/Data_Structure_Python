def is_subset(list1, list2):
  s = set(list1) # Create a set with list1 values
  # Traverse list 2 elements
  for elem in list2:
    if elem not in s:
      return False
  return True

list1 = [9, 4, 7, 1, -2, 6, 5]
list2 = [7, 1, -2]
list3 = [10, 12]
print(is_subset(list1, list2))
print(is_subset(list1, list3))

## The solution is very simple when working with the Pythonic hash table Set. 
## We simply iterate over list2 and list3 to see whether their elements can be found in list1.
## At the back end, the values are checked against their hashed indices in list1.

## Time Complexity
## For a lookup list with m elements and a subset list with n elements, the time complexity is O(m+n).