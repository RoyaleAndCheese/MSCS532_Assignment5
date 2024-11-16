import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    # Choosing the last element as the pivot
    pivot = arr[-1] 

    # Elements less than or equal to pivot
    left = [x for x in arr[:-1] if x <= pivot]

    # Elements greater than pivot
    right = [x for x in arr[:-1] if x > pivot]  
    
    # Recursive sorting of left and right partitions
    return quicksort(left) + [pivot] + quicksort(right)


# Usage:
array = [8, 3, 1, 7, 0, 10, 2]
sorted_array = quicksort(array)

print("Original array:", array)
print("Sorted array:", sorted_array)




'''Randomized quicksort'''
def randomized_partition(arr, low, high):
    # Randomly select a pivot index and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# usage:
if __name__ == "__main__":
    array = [34, 7, 23, 32, 5, 62, 32, 7]
    print("Original Array:", array)
    randomized_quicksort(array, 0, len(array) - 1)
    print("Sorted Array:", array)




#testing:

#  Already sorted array
def generate_sorted_array(size, start_value=1, step=1):
    # Generate a sorted array with `size` elements, starting from `start_value`, increasing by `step`
    return [start_value + i * step for i in range(size)]

arr_sorted = generate_sorted_array(500)

start = time.time()
print("Array with sorted elements:", quicksort(arr_sorted))
det_time = time.time() - start
print(f"Already sorted array - QuickSort Time: {det_time:.5f} seconds")


start = time.time()
print("Array with sorted elements:", randomized_quicksort(arr_sorted, 0, len(arr_sorted) - 1))
det_time = time.time() - start
print(f"Already sorted array- Randomized QuickSort Time: {det_time:.5f} seconds")




 # Random array
def generate_random_unsorted_array(size, min_value=1, max_value=1000):
    # Generate an array with `size` elements, values between `min_value` and `max_value`
    return [random.randint(min_value, max_value) for _ in range(size)]

arr_random = generate_random_unsorted_array(500)
##print(arr_random)

start = time.time()
print("Random:", quicksort(arr_random))
det_time = time.time() - start
print(f"Random array - QuickSort Time: {det_time:.5f} seconds")


start = time.time()
print("Array with sorted elements:", randomized_quicksort(arr_random, 0, len(arr_random) - 1))
det_time = time.time() - start
print(f"Random array- Randomized QuickSort Time: {det_time:.5f} seconds")




 # Reverse sorted array
def generate_reverse_sorted_array(size, start_value=500, step=1):
    # Generate a reverse sorted array with `size` elements, starting from `start_value` and decreasing by `step`
    return [start_value - i * step for i in range(size)]

arr_reverse_sorted = generate_reverse_sorted_array(500)

start = time.time()
print("Reverse sorted array:", quicksort(arr_reverse_sorted))
det_time = time.time() - start
print(f"Reverse sorted array - QuickSort Time: {det_time:.5f} seconds")


start = time.time()
print("Array with sorted elements:", randomized_quicksort(arr_reverse_sorted, 0, len(arr_reverse_sorted) - 1))
det_time = time.time() - start
print(f"Reverse sorted array- Randomized QuickSort Time: {det_time:.5f} seconds")

