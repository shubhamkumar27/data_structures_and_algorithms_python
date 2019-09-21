############ PROBLEM ################3
# A list of n-1 integers will be given and they will be in range 1 to n
# Find the missing number in list

######### USING SUM METHOD ##############3

def sum_method(lis):
    n = len(lis)
    sum = (n+1)*(n+2)//2
    for i in lis:
        sum-=i
    print('Missing number is : '+str(sum))

l = [1,2,3,4,7,6,9,8]
sum_method(l)