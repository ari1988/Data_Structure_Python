def rearrange(lst):
  return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(rearrange([10,-1,20,4,5,-9,-6]))

## Time Complexity
## The time complexity of the solution is O(n) as it is iterated over twice.