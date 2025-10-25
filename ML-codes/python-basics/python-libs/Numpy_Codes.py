
import numpy as np

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
