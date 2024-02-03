## Solution 1 : Using a Dictionary

def findSum(lst, k):
  foundValues = {}
  for ele in lst:
    try:
      foundValues[k-ele]
      return [k-ele,ele]
    except KeyError:
      foundValues[ele] = 0
  return "No numbers add upto k"

## The best way to solve this problem is to insert every element into a dictionary. This takes O(1) as constant time insertion.
## Then, for every element x in the list, we can just look up its complement, k-x, and, if found, return both k-x and x.

## Time Complexity
## Each lookup is a constant time operation. Overall the running time of this approach is O(n)

print(findSum([1, 3, 2, 4], 6))