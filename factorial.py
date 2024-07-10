
import time
# Рекурсия. 

#Факториал без рекурсии

# n = 1234
# fact = 1

# for i in range(1, n + 1, 1):
#     fact *= i
# print(f"Факториал {n} = {fact}")

#Факториал c рекурсией

# def fact_r(n):
#     if n <= 1:
#         return 1
#     return n * fact_r(n-1)

# n = 195789
# fact = fact_r(n)
# print(f"Факториал {n} = {fact}")

#Числа фибоначи
start = time.time()



def fibonacci(n):
    
    if n <= 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

n=10

print(fibonacci(n))

end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

# The time of execution of above program is : 11426.26404762268 ms