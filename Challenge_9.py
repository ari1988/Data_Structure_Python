def rearrange(lst):
  ## take 2 pointers.. plus and minus
  ## if -ve number encountered, move to left, and increment -ve so that next item is inserted at that point
  minus = 0
  new_list = []
  for i in range(len(lst)):
    if lst[i] < 0:
      new_list.insert(minus,lst[i])
      minus += 1
    else:
      new_list.append(lst[i])
  return new_list

print(rearrange([10,-1,20,4,5,-9,-6]))