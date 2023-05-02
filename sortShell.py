# Shell sort, Сортировка Шелла
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

step = len(arr) // 2
while step > 0:
    for i in range(step, n, 1):
        value = arr[i]
        current_index = i
        index_to_check = current_index - step



###########################################
end = time.time()
print('Sorted')
print(arr)
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")