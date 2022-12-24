import random
import time
exchangeh=0
exchangeq=0
exchangeq2=0
#HeapSort Algorithm
def heapify(arr, n, i):
    global exchangeh
    count = 0
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2
    count += 1     
    if l < n and arr[i] < arr[l]:
        largest = l
    count += 1
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        exchangeh+=1
        count += heapify(arr, n, largest)
    return count

def heapSort(arr):
    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        heapify(arr, n, i)  
        count += heapify(arr, i, 0)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        count += heapify(arr, i, 0)
    return count


def quicksort(lista,izq,der):
  i = izq
  j = der
  swap_count = 0
  compare_count = 0
  pivote = (lista[der]+lista[izq]+lista[(der+izq)//2])//3

  while i <= j:
    while lista[i] < pivote:
      i += 1
    while pivote < lista[j]:
      j -= 1
    if i <= j:
      aux = lista[i]
      lista[i] = lista[j]
      lista[j] = aux
      swap_count += 1
      i += 1
      j -= 1
    compare_count += 1

  if izq < j:
    other_swap, other_compare = quicksort(lista, izq, j)
    swap_count += other_swap
    compare_count += other_compare
  if i < der:
    other_swap, other_compare = quicksort(lista, i, der)
    swap_count += other_swap
    compare_count += other_compare    

  return (swap_count, compare_count)




arr=[100,200,500,1000,2000,3000,4000,5000]
for i in arr:
      arrq = [x for x in range(i)]
      random.shuffle(arrq)

      arrh = [x for x in range(i)]
      random.shuffle(arrh)
      
      arrq2 = [x for x in range(i)]
      random.shuffle(arrq2)
      
      exchangeh=0
      exchangeq=0
      
      print("case:",i)
      
      # startq_time = time.time()
      # print("comparison",heapSort(arrh))
      # timeh = time.time() - startq_time
      # print("timeqh:",timeh)
      # print("exchangeh",exchangeh)
      

      starth_time = time.time()
      print("comparison:",quicksort(arrq,0,len(arrq)-1))
      timeq = time.time() - starth_time
      print("timeq:",timeq)
      
      
      # starth_time = time.time()
      # print("comparison:",quicksort2(arrq2,0,len(arrq2)-1))
      # timeq2 = time.time() - starth_time
      # print("timeq2:",timeq2)
      

