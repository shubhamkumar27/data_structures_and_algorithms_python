def rotate(arr,k):
    n = len(arr)
    gc = gcd(n,k)
    for i in range(gc):
        temp = arr[i]
        j=i
        while 1:
            d = (j+k)%n
            if d==i:
                arr[j]=temp
                break
            arr[j] = arr[d]
            j=d

    print(arr)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

arr = [1,2,3,4,5,6,7,8,9]
rotate(arr,3)