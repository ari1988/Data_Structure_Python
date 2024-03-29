from HashTable import HashTable

table = HashTable()  # Create a HashTable
print(table.is_empty())
table.insert("This", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Driver", 5)
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))

## Opeartion            ## Average      ## Worst
#  Search                # O(1)          # O(n)
#  Insertion             # O(1)          # O(n)
#  Deletion              # O(1)          # O(n)
