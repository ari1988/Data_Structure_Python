def find_minimum(lst):
  if (len(lst) <= 0):
    return None
  minimum = lst[0]
  for ele in lst:
    # Update if found a smaller element
    if ele < minimum:
      minimum = ele
  return minimum

print(find_minimum([100, 12, 34, 40]))
print(find_minimum([9, 2, 3, 6]))

# Time Complexity
## Since the entire list is iterated over once, this algorithm is in linear time O(n)
