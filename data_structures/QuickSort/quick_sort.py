def quick_sort_lomuto(arr,p,r):
    if(p >= r):
        return
    q = lomuto_partition(arr,p,r)
    quick_sort_lomuto(arr,p,q-1)
    quick_sort_lomuto(arr,q+1,r)


def lomuto_partition_random(arr,p,r):
    pivot = arr[r]
    i = p - 1
    for j in range(p,r):
        if(arr[j] <= pivot):
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[r] = arr[r], arr[i+1]
    return i + 1

def lomuto_partition(arr,p,r):
    pivot = arr[r]
    i = p - 1
    for j in range(p,r):
        if(arr[j] <= pivot):
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[r] = arr[r], arr[i+1]
    return i + 1


def quick_sort_hoare(arr,p,r):
    if(p >= r):
        return 
    q = hoare_partition(arr,p,r)
    quick_sort_hoare(arr,p,q)
    quick_sort_hoare(arr,q+1,r)

def hoare_partition(arr,p,r):
    i = p - 1
    j = r + 1
    pivot = arr[p] 
    while True:
        while True:
            i += 1
            if(arr[i] >= pivot):
                break

        while True:
            j -= 1
            if(arr[j] <= pivot):
                break
        if(i >= j):
            break
        else:
            arr[i],arr[j] = arr[j],arr[i]
    return j


def quick_sort_hoare_tre(arr,p,r):
    while True:
        if(p >= r):
            return 
        q = hoare_partition(arr,p,r)
        quick_sort_hoare_tre(arr,p,q)
        p = q + 1
        
def quick_sort_hoare_tre_optimized(arr,p,r):
    while p < r: 
        q = hoare_partition(arr,p,r)
        if((q - p) < (r - q)):
            quick_sort_hoare_tre_optimized(arr,p,q)
            p = q + 1
        else:
            quick_sort_hoare_tre_optimized(arr,q+1,r)
            r = q