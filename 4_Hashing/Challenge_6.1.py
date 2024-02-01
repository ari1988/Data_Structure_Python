def find_sub_zero(my_list):
  result = []
  len_list = len(my_list)
  for i in range(len_list-2):
    added = my_list[i] + my_list[i+1]
    if added == 0:
      result.append([my_list[i], my_list[i+1]])
      return result
    elif my_list[i+2] is not None and (my_list[i] + my_list[i+1] + my_list[i+2]) == 0:
      result.append([my_list[i], my_list[i+1], my_list[i+2]])
  return result

my_list = [6, 4, -7, 3, 12, 9,-1,2,-1,1,-1]
print(find_sub_zero(my_list))
