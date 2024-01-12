def find_second_maximum(lst):
  first_max = second_max = float('-inf')
  # find first max
  for item in lst:
    if item > first_max:
      first_max = item
  # Find max relative to first_max
  for item in lst:
    if item != first_max and item > second_max:
      second_max = item
  return second_max

print(find_second_maximum([9,2,3,6]))