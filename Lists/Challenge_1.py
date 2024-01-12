def remove_even(lst):
    # Write your code here!
    return [a for a in lst if a % 2 != 0]

print(remove_even([3, 2, 41, 3, 34]))

## newList = [expression(i) for i in oldList if filter(i)]

# Time Complexity
## The time complexity of this solution is O(n), since only the syntax has changed while the algorithm still iterates over all elements of the list.