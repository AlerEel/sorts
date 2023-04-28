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
#########################################

for i in range(n - 1):
    index_sorted = i
    next_index = i + 1
    for j in range(i + 1, n, +1):
        if arr[j] < arr[index_sorted]:
            index_sorted = j
    arr[i], arr[index_sorted] = arr[index_sorted], arr[i]



###########################################
end = time.time()
print('Sorted')
print(arr)
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")