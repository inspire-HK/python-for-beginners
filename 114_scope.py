# scope

a = 1  # variable a is in global scope


def sum(x, y):
  total = x + y  # total only accessible within sum()
  a = 2
  print('local scope of a:', a)  # this "a" is a local "a"
  return total


sum(1, 2)

print('global scope of a:', a)  # global "a" is always 1
# print('But we can NOT access variable "total": ', total)
