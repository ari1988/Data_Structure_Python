from HashTable import HashTable


def is_formation_possible(lst, word):

    if len(word) < 2 or len(lst) < 2:
        return False

    hash_table = HashTable()
    for elem in lst:
        hash_table.insert(elem, True)

    for i in range(1, len(word)):
        # Slice the word into two strings in each iteration
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False

        if hash_table.search(first) is not None:
            check1 = True
        if hash_table.search(second) is not None:
            check2 = True

        # Return True If both substrings are present in the hash table
        if check1 and check2:
            return True

    return False

## Time Complexity#
## We perform the insert operation m times for a list of size m. After that, 
## we linearly traverse the word of size n once. Furthermore, we slice strings of size n in each iteration. Hence the total time complexity is 
## O(m+n^2)

keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))