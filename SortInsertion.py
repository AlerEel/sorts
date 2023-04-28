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



for i in range(n):
    val = arr[i]
    j = i - 1
    if j < 0:
        continue
    while val < arr[j] and j >= 0:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = val



end = time.time()

print('Sorted')
print(arr)

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")