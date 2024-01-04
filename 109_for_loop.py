# iterate over a sequence (list, tuple, dictionary, set, or string)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)
  print('hello')  # do something else .....

# print("\n string has length, & it is iterable")
for x in "banana":
  print(x)

print("\n break also work in 'for loop'")
for x in fruits:
  if x == "banana":  # break the for-loop when matching "banana"
    break
  print(x)

print("\n popular way for loop")
for x in range(6):
  print(x)

for x in range(4, 10, 2):  # starting with 4 to (10-1), stepping of 2
  print(x)