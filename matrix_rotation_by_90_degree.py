def rotation(mat):
    n = len(mat)
    for i in range(n-1):
        mat[0][i],mat[0][n-1]=mat[0][n-1],mat[0][i]
        mat[0][i],mat[n-1][n-1]=mat[n-1][n-1],mat[0][i]
        mat[0][i],mat[n-1][0]=mat[n-1][0],mat[0][i]
    print(mat)

mat = [[1,2],
       [3,4]]

rotation(mat)