# Function

# Good Practice: function name should be a verb (or a task), e.g. say(), add(), sum(), average()

print('function without arguments')

def say_hello(): # function name: say_hello
  print('Hello !')

say_hello()  # calling the function (execute function call)

def average(x, y):
  print((x + y) / 2)

average(20, 30)
average(1, 2)

###############
print('function with argument')

def greet(name:str): # good practice to have type annotation
  print('Hello, ' + name)

greet('Alex')
greet('jacky')

###############
print('function with multiple "positional" argument')

def greet2(name: str, age=15):  # age default 10, if no value provide, age is assigned to 10
  print(name + ' is ' + str(age) + ' year old')

greet2('John', 12)
greet2('Peter')  # default to age of 10

################
print('Arbitrary Arguments, *args')

def sum(*numbers: int): # * "points" or "references" to a tuple
  total = 0
  # numbers[0] = 11 # error because tuple is immutable

  for n in numbers:
    total += n

  return total

total1 = sum(2, 3, 4, 5)
print('sum: ', sum(1, 2, 3))

###############
print('Arbitrary Keyword Arguments, **kwargs')  # somewhat aka named arguments

def print_full_name(**name):  # **name is a dictionary
  print('Full name is: ', [name['first_name'], name['last_name']])

print_full_name(first_name='John', last_name='Doe')
