def quicksort(arr,start,end):
    if start<end:
        pivot_index = partition(arr,start,end)
        quicksort(arr,start,pivot_index-1)
        quicksort(arr,pivot_index+1,end)
    return arr


def partition(arr,start,end):
    pivot = arr[end]
    pivot_index = start
    for i in range(start,end):
        if arr[i]<=pivot:
            arr[i],arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index+=1
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]      
    return pivot_index

l = [2,5,8,6,1,0,9]
print(quicksort(l,0,len(l)-1))