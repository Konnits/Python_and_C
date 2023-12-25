from c_modules.myarray import Range
import numpy as np
import time

n = 100_000_000

start = time.time()
a = Range(n)
a.sum()
end = time.time()
print(f"Time for C: {end-start}")

start = time.time()
np.arange(n).sum()
end = time.time()
print(f"Time for numpy: {end-start}")