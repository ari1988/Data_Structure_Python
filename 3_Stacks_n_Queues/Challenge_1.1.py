def printB(number):
  lst = ["1"]

  for i in range(1,number):
    s1 = str(lst[i-1]) + "0"
    s2 = str(lst[i-1])+ "1"
    lst.append(s1)
    lst.append(s2)
  return lst[:number]
print(printB(100))