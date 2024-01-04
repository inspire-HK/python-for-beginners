# try-catch
# processing errors

# a = input('input number: ')
# b = input('divider: ')

try:
  x = 100
  print('trying to print x')
  x = 1 / 0  # try to comment out this line, and run
  print('x is: ', x)
except ZeroDivisionError as e:
  print('division by zero error: >>>>>>  (do something else)', type(e), e)
except Exception as err:
  print('other error: ', err)
else:
  print('no error')
finally:
  print('always executes')
