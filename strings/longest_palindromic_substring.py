def check(string):
    maxl = 0
    start = 0
    n = len(string)
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        mat[i][i]=1

    # for string of length 2
    for i in range(n-1):
        if string[i]==string[i+1]:
            mat[i][i+1]=1
            maxl=2
    
    # for string of length >2
    k = 3
    while(k<=n):
        for i in range(n-k+1):
            j = i+k-1
            if string[i]==string[j] and mat[i+1][j-1]:
                mat[i][j]=1
                if k > maxl:
                    maxl = k
                    start = i
        k+=1
    print(start,'and',maxl)
    print(string[start:start+maxl])


check('forgeeksfofskeegfor')