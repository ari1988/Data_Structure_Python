def findSum(lst, value):
  foundValues = set()
  for ele in lst:
    if (value - ele) in foundValues:
      return [value-ele, ele]
    foundValues.add(ele)
  return False

## Note that set.add method adds an element if element is not present in the set.

## Time Complexity
## The time complexity of the solution above is O(n)

print(findSum([1,2,3,4],6))