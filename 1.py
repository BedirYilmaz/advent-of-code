import os
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)



depth_measurements = np.loadtxt("input_1", dtype=np.int32)

# Part 1

# print(depth_measurements[:10])
# print(np.diff(depth_measurements)[:10])
# print((np.diff(depth_measurements) > 0)[:10])

print((np.diff(depth_measurements) > 0).sum())

# Part 2

cumulative = np.cumsum(depth_measurements)
cumulative[3:] - cumulative[:-3]
cumulative[3:] = cumulative[3:] - cumulative[:-3]

print((np.diff(cumulative[2:]) > 0).sum())
