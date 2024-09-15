def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j+1] = key

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n-i-1):
            if arr[j + 1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
    
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

lst = [7,3,13,4,2,99,56,20,1,4,6,28,93,10]
mergeSort(lst)
print(lst)
