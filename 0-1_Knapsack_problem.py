############# USING RECURSION ####################

def knapsack(w,n,wt,val):

    if n==0 or w==0:
        return 0

    if wt[n-1]>w:
        return knapsack(w,n-1,wt,val)

    else:
        return max(val[n-1]+knapsack(w-wt[n-1],n-1,wt,val),knapsack(w,n-1,wt,val))

############## USING DYNAMIC PROGRAMMING ###############

def dp_knapsack(w, n, wt, val):
    K = [[0 for x in range(w + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i - 1] <= j:
                K[i][j] = max(val[i - 1] + K[i - 1][j - wt[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    return K[n][w]

wt=[2,4,6,8]
w=12
val=[100,300,200,50]
n=len(wt)
print(dp_knapsack(w,n,wt,val))

