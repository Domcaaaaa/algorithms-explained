#import heapq

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

#def heap_sort(arr):
    #n = len(arr)
    #for i in range(n // 2 - 1, -1, -1):
        #heapify(arr, n, i)

    #for i in range(n-1, 0, -1):
        #arr[i], arr[0] = arr[0], arr[i]
        #heapify(arr, i, 0)

# Testing
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

bubble_sort(arr)
print("Bubble sorted array:", arr)

selection_sort(arr)
print("Selection sorted array:", arr)

insertion_sort(arr)
print("Insertion sorted array:", arr)

merge_sort(arr)
print("Merge sorted array:", arr)

#heap_sort(arr)
#print("Heap sorted array:", arr)