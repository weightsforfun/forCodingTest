import numpy as np
import timeit
import random
import time

def heapify(arr, len_arr, i):
    global num_swaps
    global num_comps
    maxima = i
    l = 2 * i + 1
    r = 2 * i + 2
    num_comps += 1
    if l < len_arr and arr[i] < arr[l]:
        maxima = l
    num_comps += 1
    if r < len_arr and arr[maxima] < arr[r]:
        maxima = r
    if maxima != i:
        num_swaps += 1
        arr[i], arr[maxima] = arr[maxima], arr[i]
        heapify(arr, len_arr, maxima)



def heap_sort(arr):
    global num_swaps
    global num_comps
    len_arr = len(arr)
    heapify(arr, len_arr, 0)
    for i in range(len_arr, -1, -1):
        heapify(arr, len_arr, i)
    for i in range(len_arr - 1, 0, -1):
        num_swaps += 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr=[100,200,500,1000,2000,3000,4000,5000]
for i in arr:
      arrq = [x for x in range(i)]
      random.shuffle(arrq)
      num_swaps = 0
      num_comps = 0
      starth_time = time.time()
      heap_sort(arrq)
      timeq = time.time() - starth_time
      print(i)
      print(num_comps)
      print(num_swaps)
      print("timeq:",timeq)

