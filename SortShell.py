import random
import time
start = time.time()

n=500000
arr = list()

for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

def shell_sort(arr):
    step = len(arr) // 2
    while step > 0:
        for i in range(step, n, 1):
            current_index = i
            index_to_check = current_index - step
            while (current_index > 0 and
                   arr[index_to_check] > arr[current_index]):
                arr[current_index], arr[index_to_check] = arr[index_to_check], arr[current_index]
                current_index -= step
                index_to_check -= step
        step = step // 2
    return arr

print('Sorted:')
print(shell_sort(arr))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")