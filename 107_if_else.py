# condition if-else

a = 4
b = 3

if (a > b):  # () is not needed, ":" indicating a new block below
  print('a is greater than b')
  print('more step...., more info.....')
# do something else
elif a == b:
  print('a equals to b')
# more operations
else:
  print('a must be less than b')

# short hand
if a > b:
  print('a is greater than b (2)')

# if elif else (short hand)
if a > b: print('a is greater than b (3)')
elif a == b: print('a equals to b')
else:
  print('a must be less than b')

# print('#######')
print('a is greater than b (4)') if a > b else print('something else....')

# # nested condition
weekdays = ['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
is_raining = False
today = weekdays[2]
if today == 'tue':
  if is_raining:  # nested condition
    print('go to work')
  else:
    print('go to school')
else:
  print('do whatever you want')
