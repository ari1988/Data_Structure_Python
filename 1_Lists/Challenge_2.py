def merge_arrays(lst1, lst2):
  ind1 = 0 # Creating 2 variables to track the 'current index'
  ind2 = 0

  # While both indeces are less than the length of their lists
  while ind1 < len(lst1) and ind2 < len(lst2):
    if(lst1[ind1] > lst2[ind2]):
      # insert list2's current index to list1
      lst1.insert(ind1, lst2[ind2])
      ind1 += 1
      ind2 += 1
    else:
      ind1 += 1
  
  if ind2 < len(lst2): # Append whatever is left of list2 to list1
    lst1.extend(lst2[ind2:])
  return lst1

print(merge_arrays([4, 5, 6], [-2, -1, 0, 7]))

# Time Complexity
## the time complexity is O(m(n+m))  where n and m are the lengths of the lists. Both lists are not traversed separately so we cannot say that 
## complexity is (m + n). In the worst-case, the second list has all the elements that are smaller than the elements of the first list. 
## In this case, the complexity will be O(mn).