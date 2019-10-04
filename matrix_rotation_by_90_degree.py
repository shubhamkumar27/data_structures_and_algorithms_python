def rotation(mat):
    n = len(mat)
    # for i in range(n):
    swap(mat[0][0],mat[0][n-1]) #=mat[0][n-1],mat[0][0]
    mat[0][0],mat[n-1][n-1]=mat[n-1][n-1],mat[0][0]
    mat[0][0],mat[n-1][0]=mat[n-1][0],mat[0][0]
    print(mat)

def swap(a,b):
    a,b = b,a

mat = [[1,2],
       [3,4]]

rotation(mat)