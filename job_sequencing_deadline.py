
def sequencing(arr):
    #### sorting to get the max no. of job to schedule
    arr.sort(key=lambda x: x[1], reverse=True)
    t = arr[0][1]
    #### sorting jobs according to profit in decreasing order
    arr.sort(key=lambda x: x[2], reverse=True)
    slots=[False]*t
    jobs=['empty']*t
    for i in range(len(arr)):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if slots[j]==False:
                slots[j]=True
                jobs[j]=arr[i][0]
                break
    return jobs


arr = [['a', 2, 100],
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

#print(sequencing(arr))
ar = [1,2,2,3,3,4,4,5,5,6,6,7]
res = ar[0]
for i in range(1,len(ar)):
    res = res ^ ar[i]
    print(res)
print(res)

