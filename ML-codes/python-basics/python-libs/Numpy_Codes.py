
import numpy as np

print(np.__version__)  # Check NumPy version
# Python list vs NumPy speed test (just to see the difference)
import time

python_list = list(range(1000000))
numpy_array = np.arange(1000000)

# Python list addition
start = time.time()
python_list = [x + 5 for x in python_list]
print("Python List Time:", time.time() - start)

# NumPy array addition
start = time.time()
numpy_array = numpy_array + 5
print("NumPy Array Time:", time.time() - start)
 
#######################################################################
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) # Output: <class 'numpy.ndarray'> // NumPy arrays are of type 'ndarray'

#######################################################################

arr = np.array(69) # 0D array
print(arr)

arr = np.array([1,2,4,5,6,7]) # 1D array
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3D array 
print(arr)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
