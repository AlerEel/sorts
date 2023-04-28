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

left_index = 0
right_index = n - 1

while left_index <= right_index:
    is_sorted = True
    for i in range(left_index, right_index, +1):
        if arr[i] > arr[i+1]:
            is_sorted = False
            arr[i],arr[i+1] = arr[i+1], arr[i]
    right_index -= 1
    for i in range(right_index, left_index, -1):
        if arr[i] < arr[i-1]:
            is_sorted = False
            arr[i],arr[i-1] = arr[i-1], arr[i]
    left_index += 1
    if is_sorted is True:
        break

end = time.time()
print('Sorted')
print(arr)
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")