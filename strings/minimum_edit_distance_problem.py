######### RECURSIVE SOLUTION ####################
def min_edit(s1,s2):
    m = len(s1)
    n = len(s2)

    if m==0:
        return n

    if n==0:
        return m

    if s1[m-1]==s2[n-1]:
        return min_edit(s1[:m-1],s2[:n-1])

    else:
        return 1 + min(min_edit(s1[:m],s2[:n-1]),min_edit(s1[:m-1],s2[:n]),min_edit(s1[:m-1],s2[:n-1]))


########### USING DYNAMIC PROGRAMMING ####################
def min_edit_dp(s1,s2):
    m = len(s1)
    n = len(s2)

    dp_matrix = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i==0:
                dp_matrix[i][j] = j

            elif j==0:
                dp_matrix[i][j] = i

            elif s1[i-1]==s2[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1]

            else:
                dp_matrix[i][j] = min(dp_matrix[i][j-1],dp_matrix[i-1][j],dp_matrix[i-1][j-1])

    return dp_matrix[m][n]
    
s1 = 'shubhamkumar'
s2 = 'kumar'
print(min_edit_dp(s1,s2))
