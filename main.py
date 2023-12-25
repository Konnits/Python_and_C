from c_modules.myarray import Range
import numpy as np
import time

n = 100_000_000

n_test = 50
times = []

for _ in range(n_test):
    start = time.time()
    a = Range(n)
    a.sum()
    end = time.time()
    del a
    times.append(end-start)
print(f"Time for C: {np.mean(times)}")

times = []
for _ in range(n_test):
    start = time.time()
    b = np.arange(n)
    b.sum()
    end = time.time()
    del b
    times.append(end-start)
print(f"Time for numpy: {np.mean(times)}")