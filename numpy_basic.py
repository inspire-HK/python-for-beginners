# Reference https://www.w3schools.com/python/numpy/numpy_getting_started.asp

# Please install numpy package
# $ pip install numpy

# numpy handles n-dimensional array much faster than list, and provides many helper functions
import numpy as np

print('numpy version: ', np.__version__)

arr = np.array([1, 2, 3, 4])
print('type & value of arr: ', type(arr), arr)
print('dtype (data type) of arr: ', arr.dtype)

print('### separator ### \n')
###########################

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('type & value of 2D arr: ', type(arr2d), arr2d)
print('number of dimensions in 2D array: ', arr2d.ndim)

print('pick entire row: ', arr2d[1])
print('pick an element: ', arr2d[1, 0])
print('pick some elements: ', arr2d[2, 1:3])
print('let try negative index: ', arr2d[2, -2])

print('### separator ### \n')
###########################

arr = np.array([1, 2, 3, 4])
x = arr.copy()  # make a copy of arr
arr[0] = 42  # change arr
print('arr >>', arr)
print('x is a copy, remains the same: ', x)

y = arr.view()
arr[1] = 11
print(
    'y is a view, so change is in effect: ',
    y,
)

print('### separator ### \n')
###########################

arr = np.array([[1, 2, 3], [4, 5, 6]])
print('shape of 2D array: ', arr.shape)

days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print('shape of days', days.shape)
weekdays = days.reshape(2, 7)
print('Reshape to weekdays (Mon~Sun): ', weekdays)

flatten = weekdays.reshape(-1)
print('flatten n-dimension array to 1D: ', flatten)

###########################
