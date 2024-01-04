# modules

# built-in modules are already bundled, no installation is needed
# external modules (https://pypi.org/) require installation

# pip (Package Installer for Python),
# in real-world, we virtualize (encapsulate) development environment, and use pipenv

import datetime
import math  # all imports should be hoisted to top
import turtle

now = datetime.datetime.now()
print('now:', now)

future = datetime.datetime(2024, 1, 1)
print('future: ', future)

print('format date to human readable: ', now.strftime('%A, %B %d, %Y'))

#############################
print('Play with Math')
print('min of 3 numbers: ', min(3, 4, 2))
print('absolute value of -1 & 2: ', abs(-1), abs(2.1))
print('square root of 9: ', math.sqrt(9))
print('round up to nearest integer (3.2): ', math.ceil(3.2))
print('round down to nearest integer (4.9): ', math.floor(4.9))
print('PI is: ', math.pi)

#############################
print('Play with Turtle')
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.penup()
t.forward(100)
t.pendown()
t.forward(100)

while True:
  pass  # line#37-38:effectively: forever loop

# code below is unreachable
a = 1
if a > 4:
  pass  # noop (no operation)
else:
  print('hello')
