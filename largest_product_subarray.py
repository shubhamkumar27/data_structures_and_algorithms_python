def product(arr):
    size = len(arr)
    maxm = arr[0]
    minm = arr[0]
    pre_max = arr[0]
    pre_min = arr[0]
    ans = arr[0]
    for i in range(1,size):
        pre_max = maxm
        pre_min = minm
        maxm = max(pre_max*arr[i],pre_min*arr[i],arr[i])
        minm = min(pre_max*arr[i],pre_min*arr[i],arr[i])
        ans = max(ans,maxm)
    print(ans)

arr = [-1,6,2,0,7,9]
product(arr)

