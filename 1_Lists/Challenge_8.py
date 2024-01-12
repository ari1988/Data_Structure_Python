def right_rotate(lst, k):
  if len(lst) == 0:
    k = 0
  else:
    k = k % len(lst)
  return lst[-k:] + lst[:-k]

print(right_rotate([30,40,50,10,20],-1))

## The intuition behind taking the modulo is that we would get back the same list if we were to rotate the list len(lst) times. 
## That’s why we only need to rotate the list k % len(lst) times and not actually k.

# Time Complexity
## List slicing is in O(k) where k represents the number of elements that are sliced, and since the entire list is sliced.
## hence the total time complexity is in O(n).
