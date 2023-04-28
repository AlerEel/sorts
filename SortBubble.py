import random
import time

n = 5000*2
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print('Not sorted')
print(arr)
print("---------")

start = time.time()
###################################################

for i in range(n):
    is_sorted = True
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            is_sorted = False
            arr[j],arr[j+1] = arr[j+1], arr[j]
    n -= 1
     
    if is_sorted is True:
        break
           
#    print(arr)
#    print(n)

###################################################
end = time.time()

print('Sorted')
print(arr)
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

#Время работы цикла при n = 5000, без n -=1 после прохода 
# 1 time x 5000 = 2925.367832183838 ms
#Время работы цикла при n = 5000, с n -=1 после прохода 
# 2 time x 5000 = 2073.7462043762207 ms
#Время работы цикла при n = 10000, без n -=1 после прохода 
# 1 time x 10000 = 12812.604665756226 ms
#Время работы цикла при n = 10000, с n -=1 после прохода 
# 2 time x 10000 = 8313.22455406189 ms

# выход из цикла после окончания сортировки экономит примерно 
# 100 итераций на n = 5000