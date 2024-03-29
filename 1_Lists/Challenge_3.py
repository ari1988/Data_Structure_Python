def find_sum(lst, k):
  lst.sort() # sort the list

  index1 = 0
  index2 = len(lst) - 1
  result = []
  sum = 0
  # iterate from front and back
  # move accordingly to reach the sum to be equal to k
  # returns false when the two indices meet
  while (index1 != index2):
    sum = lst[index1] + lst[index2]
    if sum < k:
      index1 += 1
    elif sum > k:
      index2 -= 1
    else:
      result.append(lst[index1])
      result.append(lst[index2])
      return result
  return False

print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))

# Time Complexity
## The linear scan takes O(n) and sort takes O(nlogn). The time complexity becomes O(nlogn) + O(n) because
## the sort and the linear scan are done one after the other. The overall would be O(nlogn) in the worst case.