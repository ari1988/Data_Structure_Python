def rearrange(lst):
  neg = []
  pos = []
  for ele in lst:
    if ele < 0:
      neg.append(ele)
    else:
      pos.append(ele)
  # merge two lists and return
  return neg + pos

print(rearrange([10, -1, 20, 4, 5, -9, -6]))


## Time Complexity
## Since the given list is only iterated over once, the time complexity of this solution is O(n)