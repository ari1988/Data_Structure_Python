def find_first_unique(lst):
    for index1 in range(len(lst)):
        index2 = 0
        # iterate the second list using index2
        while(index2 < len(lst)):
            if (index1 != index2 and lst[index1] == lst[index2]):
                break
            index2 += 1
        if (index2 == len(lst)):
            return lst[index1]
    return None


print(find_first_unique([9, 2, 3, 2, 6, 6]))

# Time Complexity
## The time complexity of this solution is O(n^2) since the entire list is iterated n times for each element→ n*n