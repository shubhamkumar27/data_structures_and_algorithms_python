def second_largest(arr):
    size = len(arr)
    if size < 2:
        print('Invalid')
        return
    if arr[0]>arr[1]:
        max1 = arr[0]
        max2 = arr[1]
    else:
        max1 = arr[1]
        max2 = arr[0]
    for e in range(2,size):
        if arr[e]>max1:
            max2 = max1
            max1 = arr[e]
        if max1>arr[e]>max2:
            max2 = arr[e]
    print(max2)

arr = [0,-1,-2,-3,4]
second_largest(arr)
            
