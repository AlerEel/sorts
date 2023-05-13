import random
import time

n = 5000

arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print('Not sorted')
print(arr)
print("---------")

start = time.time()

def merge(arrl, arrr):
    sorted_arr = list()
    corrent_left = 0
    corrent_right = 0

    lenl = len(arrl)
    lenr = len(arrr)
    for i in range(lenl + lenr):
        

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_side = list()
    right_side = list()

    for i in range(0, mid):
        val = arr[i]
        left_side.append(val)

    for i in range(mid, len(arr)):
        val = arr[i]
        right_side.append(val)
    
    # left_side = arr[:mid]
    # right_side = arr[mid:]
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    result = merge(left_side, right_side)
    return result




end = time.time()

print('Sorted')
print(arr)

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")