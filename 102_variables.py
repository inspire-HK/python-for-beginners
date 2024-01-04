# This lesson will focus on variable types

# integer
i = 2
j = 3
k = i + j
print('i + j =', k)
print('\n')

# string
s = 'This is a string'
print('(', s, ') is type of ', type(s))

s1 = "This is also a string"
s2 = ' single-word'
s3 = s1 + s2
print('concatenate s1 & s2: ', s3) # combine two strings
print('length of s2 is: ', len(s2))

s4 = 'H\nW'  # \n is escape character (new line)
print('length of s4: ', len(s4))  # \n treats a 1 char

print('Hello World'.upper())  # convert to upper case; upper() is built-in function to string
print('LOWER case'.lower())  # convert to lower case
print('\n')  # new line (next line)

# float
f1 = 1.2
f2 = 2.0
f3 = 2.  # The "." indicating a floating number
print('type of f1: ', type(f1))
print('f2 equals to f3: ', f2 == f3)
print('\n')

# # boolean (True or False)
b1 = True  # capitalized T
b2 = False
print('negation of b1 is:', not b1)  # not True is False
print('\n')

# # list (also known as array)
fruits = ['apple', 'orange', 'pear']
print('fruits: ', fruits, type(fruits), len(fruits))
print('first & last fruit in the list: ', fruits[0], fruits[-1])

fruits.pop()  # remove last item from lst
print('after removing last item: ', fruits)

fruits.append('grape')  # add item to the end of lst
print('after adding grape: ', fruits)
print('\n')

# it is possible to make mixed-type list, but it is not recommended (bad coding practice)
mixed_list = [1, 'apple', 2.0, True]
print('mixed list: ', mixed_list)
print('\n')

# # slicing
long = '012345'
print('long[2:4]: ', long[2:4])  # including index of 2, excluding index of 4
print('first two chars: ', long[:2])
print('last two chars: ', long[-2:len(long)])
print('last two chars: ', long[-2:])

long_string = 'Hello World'
print('also work with string: ', long_string[0:5])
print('\n')

# casting (converting type)
i = 2
f = float(i)
print(' f is type of ', type(f), f)  # f is a float, value = 2.0

s = '1'
j = int(s)
print(' j is type of ', type(j), j)  # j is an integer, value = 1

x = 12
y = str(x)
print(' y is now a ', type(y), y)
print('\n')

# # advanced topics (complex number)
c = 1 + 2j
print('c is a complex number: ', type(c), c)

# note python prefers snake_case for variable & function naming convention
# e.g. last_name, say_hello()