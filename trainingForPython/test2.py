import numpy as np
import timeit
import random
import time

change_count=0

def heapify(arr, n, i):
    global change_count
    count = 0
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        count += 1
        arr[i],arr[largest] = arr[largest],arr[i]
        change_count+=1
        count += heapify(arr, n, largest)
    return count

def heapSort(arr):
    global change_count
    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        heapify(arr, n, i)  
        count += heapify(arr, i, 0)
    for i in range(n-1, 0, -1):
        change_count+=1
        arr[i], arr[0] = arr[0], arr[i] 
        count += heapify(arr, i, 0)
    return count


arr = [x for x in range(100)]
random.shuffle(arr)

num_swaps = 0
num_comps = 0

print(heapSort(arr),change_count)

