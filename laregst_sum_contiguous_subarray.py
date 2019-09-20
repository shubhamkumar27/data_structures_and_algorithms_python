############# USING KADANE'S ALGORITHM ###############

def subarray(arr):
    max_so_far = 0
    max = 0
    start = 0
    end = 0
    s = 0
    for i in range(len(arr)):
        max = max + arr[i]
        if max < 0:
            max = 0
            s = i+1
        if max_so_far < max:
            max_so_far = max
            start = s
            end = i
    print('Largest sum is of subarray : '+str(arr[start:end+1]))
    print('Largest sum is : '+str(max_so_far))

a = [1,2,-1,-4,3,-7,8,-1,9,-1]

print(subarray(a))