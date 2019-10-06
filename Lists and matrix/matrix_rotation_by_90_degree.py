def rotation(mat):
    n = len(mat)
    level = n//2
    l=0
    while(l<level):
        for i in range(l,n-1):
            mat[l][i],mat[i][n-1]=mat[i][n-1],mat[l][i]
            mat[l][i],mat[n-1][n-1-i+l]=mat[n-1][n-1-i+l],mat[l][i]
            mat[l][i],mat[n-1-i+l][l]=mat[n-1-i+l][l],mat[l][i]
        l+=1
        n-=1

    print(mat)

mat = [[1,2,5,10],
       [3,4,6,11],
       [7,8,9,12],
       [13,14,15,16]]

rotation(mat)