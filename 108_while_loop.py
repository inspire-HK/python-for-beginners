# simple while loop
i = 0
while i < 6:
  print(i)
  i += 1  # increment i by 1

print('######')

# break (exit) the while loop if condition meets
i = 1
while i < 6:
  print(i)
  if i == 4:
    break
  i += 1

# continue to next iteration
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue  # skip print() if condition meets
  print(i, 'hello')
