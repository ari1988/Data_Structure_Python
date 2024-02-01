def is_formation_possible(lst, word):
  if len(word) < 2 or len(lst) < 2:
    return False

  for i in range(len(word)):
    first = word[0:i]
    second = word[i:]
    check1 = False
    check2 = False
    if first in lst:
      check1 = True
    if second in lst:
      check2 = True
    if check1 and check2:
      return True
  return False

## Note: The solution only works for two words and not more.

keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))