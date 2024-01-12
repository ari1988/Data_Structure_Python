def find_first_unique(lst):
  arr1 = []
  for ele in lst:
    if ele not in arr1:
      arr1.append(ele)
    else:
      arr1.remove(ele)
  return arr1[0]

print(find_first_unique([9,2,3,2,6,6]))
