############ PROBLEM ################3
# A list of n-1 integers will be given and they will be in range 1 to n
# Find the missing number in list

######### USING SUM METHOD ##############

def sum_method(lis):
    n = len(lis)
    summ = (n+1)*(n+2)//2
    for i in lis:
        summ-=i
    print('Missing number is : '+str(summ))

######## USING XOR METHOD ###############

def xor_method(lis):
    x = lis[0]
    for i in lis[1:]:
        x = x^i

    y = 1
    for j in range(2,len(lis)+2):
        y = y^j

    z = x^y
    print('Missing number is : '+str(z))

l = [1,2,3,4,7,6,9,8]
sum_method(l)
xor_method(l)