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

s1 = 'shubham'
s2 = ''
print(min_edit(s1,s2))
    
