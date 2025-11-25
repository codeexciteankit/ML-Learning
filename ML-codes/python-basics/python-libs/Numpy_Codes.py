
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


# ...existing code...
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
# ...existing code...



print(my_string.lower()) #hello, world!
print(my_string.upper()) #HELLO, WORLD!
print(my_string.replace("World", "Python")) #Hello, Python!
print(my_string.split(",")) #['Hello', ' World!']
print(my_string.strip()) #Hello, World! #here it removes any leading or trailing whitespace
print(len(my_string)) #13 #length of the string
print(my_string.find("World")) #7 #index of the first occurrence of the substring
print(my_string.startswith("Hello")) #True
print(my_string.endswith("!")) #True
print(my_string.count("o")) #2 #number of occurrences of the substring
print(my_string.isalpha()) #False #checks if all characters are alphabetic
print(my_string.isdigit()) #False #checks if all characters are digits
print(my_string.isalnum()) #False #checks if all characters are alphanumeric
print(my_string.title()) #Hello, World! #capitalizes the first letter of each word
print(my_string.capitalize()) #Hello, world! #capitalizes the first letter of the string
print(my_string.center(20)) #   Hello, World!    #centers the string within a specified width
print(my_string.zfill(20)) #0000000000Hello, World! #pads




