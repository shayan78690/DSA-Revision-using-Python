from os import *
from sys import *
from collections import *
from math import *

def rearrange(nums):
    arr = []
    pos = []
    neg = []
    for a in nums:
        if a > 0:
            pos.append(a)
        else:
            neg.append(a)
    i = j = 0
    while i < len(pos) and j < len(neg):
        arr.append(pos[i])
        arr.append(neg[j])
        i += 1
        j += 1
    while i < len(pos):
        arr.append(pos[i])
        i += 1
    while j < len(neg):
        arr.append(neg[j])
        j += 1
    for idx in range(len(nums)):
        nums[idx] = arr[idx]
        
    return nums


lis = [1,2,-4,-5,3,4]
print(rearrange(lis))