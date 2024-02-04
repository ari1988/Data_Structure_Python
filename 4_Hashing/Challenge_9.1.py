## Solution #2: Using collections#

import collections

def findFirstUnique(lst):
  orderdCounts = collections.OrderedDict()
  orderdCounts = orderdCounts.fromkeys(lst,0)
  for ele in lst:
    orderdCounts[ele] = orderdCounts[ele] + 1
  for ele in orderdCounts:
    if orderdCounts[ele] == 1:
      return ele
  return None

print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))

## This solution is different from the previous as now the dictionary is maintained in a specific order in the orderedCounts variable.

## Time Complexity
## The time complexity of this solution is linear, i.e., O(n)
