def max_min(lst):
  result = []
  # iterate half list
  for i in range(len(lst)//2):
    result.append(lst[-(i+1)])
    result.append(lst[i])
  if len(lst) %2 == 1:
    result.append(lst[len(lst)//2])
  return result

print(max_min([1, 2, 3, 4, 5, 6,7]))

## Time Complexity
## The time complexity of this problem is O(n) as the list is iterated over once.
