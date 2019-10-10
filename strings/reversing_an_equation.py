def reverse(eq):
    n = len(eq)
    result=[]
    j=0
    for i in range(n):
        if(eq[i]=='+' or eq[i]=='-' or eq[i]=='/' or eq[i]=='*'):
            result.insert(0,eq[j:i])
            result.insert(0,eq[i])
            j = i+1
    result.insert(0,eq[j:])
    print(''.join(result))

eq = '324+12-23*9/21*2'
reverse(eq)