# Python Lambda function is also known as anonymous function (basically function without a function name)

x = lambda a: a + 10
print(x(5))

# in long form
def add_10(a):
  return a + 10

print(add_10(5))


# closure, typical usage: function returns another function
def multiply(n):
  return lambda a: a * n

def multiply_long(n):

  def fn(a):
    return a * n

  return fn


double = multiply(2)
print('doubling:', double(11))

double2 = multiply_long(2)
print('doubling (long):', double2(11))

triple = multiply(3)
print('tripling:', triple(4))
