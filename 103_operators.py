# Operators
# refer to https://www.w3schools.com/python/python_operators.asp

# arithmetic operators: add, subtract, multiply, divide, etc
print(1 + 2)
print(2 * 3)
print(3**2)  # 3 to the power of 2 (aka 3 squared)
print(10 / 3)
print(10 % 3)  # modulus (modulo) (remainder)
print(10 // 3)  # floor division (ignore remainder)

# assignment
x = 5
x += 3  # same as x = x + 3 (increment)
x -= 1  # decrement by one

# comparison operators (yielding a boolean)
print('2 > 3', 2 > 3)  # is 2 greater than 3
print('2 >= 4', 2 >= 4)  # is 2 greater than or equal to 4
print("'a' != 'b'", 'a' != 'b')  # is 'a' not equal to 'b'

print('(2 > 1) and (3 > 3)', (2 > 1) and (3 > 3))  # True and False => False
print('(2<1 ) or (3 > 2)', (2 < 1)
      or not (3 > 2))  # False or not(True) => False
print('(3 > 2) or (2<1 )', (3 > 2) or (2 < 1))  # True or False => True

# membership
fruits = ['apple', 'orange']
print('apple in fruits?', 'apple' in fruits)
print('grape NOT in fruits?', 'grape' not in fruits)

# Operator Precedence
print(100 + (5 * 3))  # same as 100 + (5 * 3)

# best practice today, use bracket/parenthesis to be more explicit
print('100 + (5 * 3)')  # some smart editor will automatically remove unnecessary brackets
