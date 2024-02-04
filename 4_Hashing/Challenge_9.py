## Solution #1: Using a Python dictionary to keep count of repetitions

def findFirstUnique(lst):
  counts = {}
  # Initializing dictionary with pairs like (lst[i], count)
  counts = counts.fromkeys(lst, 0)
  for ele in lst:
    counts[ele] = counts[ele] + 1
  answer_key = None
  # Filter first non-repeating
  for ele in lst:
    if (counts[ele] == 1):
      answer_key = ele
      break
  return answer_key

## Caveat Note that Python dictionaries do not maintain the order that elements were added to them so this solution will not necessarily display the FIRST non-repeating
## integer when traversing the dictionary!

## Time Complexity
## Since the list is only iterated over only twice and the counts dictionary is initialized with linear time complexity,
## therefore the time complexity of this solution is linear, i.e., O(n)

print(findFirstUnique([1, 2, 3, 2]))
