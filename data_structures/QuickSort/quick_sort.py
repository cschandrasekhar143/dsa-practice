def quick_sort(arr,p,r):
    if(p >= r):
        return
    pivot = partition(arr,p,r)
    quick_sort(arr,p,(pivot-1))
    quick_sort(arr,pivot+1,r)

def partition(arr,p,r):
    pivot_val = arr[r]
    i = p - 1
    for j in range(p,r):
        if(arr[j] <= pivot_val):
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i + 1

def hoare_partition(arr,p,r):
    j = r + 1
    i = p - 1
    x = arr[p]
    while True:
         
        while True:
            j -= 1
            if(arr[j] <= x):
                break
        
        while True:
            i += 1
            if(arr[i] >= x):
                break    

        if (i >= j):
            break
        else:
            arr[j],arr[i] = arr[i],arr[j]
            
    return j
        