
import time
# Рекурсия. 

#Факториал без рекурсии

def fact(n):
    fact = 1
    for i in range(1, n + 1, 1):
        fact *= i
    return fact


#Факториал c рекурсией

def fact_r(n):
    if n <= 1:
        return 1
    return n * fact_r(n-1)

#Числа фибоначи
def fibonacci(n):
    if n > 1:
        if n <= 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    else: return 0


n=15

start = time.time()
print(f"Число фибоначчи № {n} = {fibonacci(n)}")
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

# # The time of execution of above program is : 11426.26404762268 ms
# start = time.time()
# print(f"Факториал {n} = {fact(n)}")
# end = time.time()
# print("The time of execution of above program is :",
#       (end-start) * 10**3, "ms")
#
# start = time.time()
# print(f"Факториал {n} = {fact_r(n)}")
# end = time.time()
# print("The time of execution of above program is :",
#       (end-start) * 10**3, "ms")
