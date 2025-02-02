import time
import random
import numpy as np
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибір середнього елемента як pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, repetitions=5):
    times = []
    for _ in range(repetitions):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)
    return np.mean(times)

# Генерація тестових масивів
sizes = [10_000, 50_000, 100_000, 500_000]
test_arrays = {size: [random.randint(0, 1_000_000) for _ in range(size)] for size in sizes}

# Вимірювання часу виконання
results = []
for size in sizes:
    rand_time = measure_time(randomized_quick_sort, test_arrays[size])
    det_time = measure_time(deterministic_quick_sort, test_arrays[size])
    results.append((size, rand_time, det_time))
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

# Візуалізація
sizes, rand_times, det_times = zip(*results)
plt.figure(figsize=(10, 5))
plt.plot(sizes, rand_times, marker='o', label='Рандомізований QuickSort')
plt.plot(sizes, det_times, marker='s', label='Детермінований QuickSort')
plt.xlabel("Розмір масиву")
plt.ylabel("Час виконання (секунди)")
plt.title("Порівняння часу виконання QuickSort")
plt.legend()
plt.grid()
plt.show()
