def find_pair(my_list):
  result = []
  my_dict = dict()
  len_list = len(my_list)
  pair_count = 0
  pair_dict = dict()
  for i in range(len_list):
    for j in range(i+1, len_list):
      added = my_list[i] + my_list[j]
      if added not in my_dict:
        my_dict[added] = [my_list[i], my_list[j]]
      else:
        prev_pair = my_dict.get(added)
        second_pair = [my_list[i],my_list[j]]
        result.append(prev_pair)
        result.append(second_pair)
        pair_count += 1
        pair_dict[added] = [prev_pair, second_pair]
        # return result
  return pair_dict

## Time Complexity
my_list = [3, 4, 7, 1, 12, 9, 0]
print(find_pair(my_list))