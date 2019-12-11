def quicksort(arr,start,end):
    if start<end:
        pivot = partition(arr,start,end)
        quicksort(arr,start,pivot-1)
        quicksort(arr,pivot+1,end)


def partition(arr,start,end):
    p = arr[end]
    return p
