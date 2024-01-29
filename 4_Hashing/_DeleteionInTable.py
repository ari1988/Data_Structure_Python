## Deletion in Table
## Deletion can take up to O(n) time where n is the number of hash entries in the table. 
## If they all get stored in the same bucket, we would have to traverse the whole bucket to reach the entry we want to delete. 
## The average case, however, is still O(1).

from HashTable import HashTable

ht = HashTable()
ht.insert(2, "London")
ht.insert(7, "Paris")
ht.insert(8, "Cairo")
print("size:", ht.get_size())
ht.delete(2)
print("size:", ht.get_size())
ht.search(2)