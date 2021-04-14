# import numba
from Board import NpBoard, checkArray
import random
import timeit
from time import time

size = 4
b = NpBoard(size=size)


from Board import checkArray
import numpy as np
import random
# b = NpBoard(size=size)

arr = [(random.randrange(size), random.randrange(size)) for x in range(size)]
arr = np.array(arr)


t1 = time()
for x in range(100000):
    checkArray(arr, (random.randrange(size), random.randrange(size)))


# t = timeit.timeit(s, setup, number=10000)

print(time() - t1 )


exit()