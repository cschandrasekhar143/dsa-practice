import random
def QuickSort(arr,start,end):
    if(end -1 <= start):
        return 
    low = start-1 
    high = end
    pivot = random.randint(start,end-1)
    arr[start],arr[pivot] = arr[pivot],arr[start]
    pivot_val = arr[start]
    mid = start
    while True:
        if(mid >= end):
            break
        if(mid == high):
            break

        if(arr[mid] == pivot_val):
            mid+=1
        elif(arr[mid] < pivot_val):
            low += 1
            arr[low],arr[mid] = arr[mid],arr[low]
            mid+=1
        else:
            high -= 1
            arr[mid],arr[high] = arr[high],arr[mid]

    QuickSort(arr,start,low+1)
    QuickSort(arr,high,end)