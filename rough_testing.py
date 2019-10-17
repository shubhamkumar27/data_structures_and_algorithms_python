# def test(lis):
#     max_end = 0
#     max_sum = 0
#     s=0
#     st=0
#     end=0
#     for i in range(len(lis)):
#         max_end += lis[i]
#         if max_end < 0:
#             max_end = 0
#             s=i+1
#         if max_sum<max_end:
#             max_sum = max_end
#             st=s
#             end=i
#     print(max_sum)
#     print(lis[st:end+1])

# lis = [1,2,2,-1,1,-4,3,-4,8,-1,9,-1]
# test(lis)

# def toString(List): 
#     return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
# def permute(a, l, r): 
#     if l==r: 
#         print(toString(a))
#     else: 
#         for i in range(l,r+1): 
#             a[l], a[i] = a[i], a[l]
#             print(i,l)
#             permute(a, l+1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack
#             print(a) 
  
# Driver program to test the above function 
# string = "ABC"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n-1) 
# v = input().split(' ')
# given = int(v[0])
# k = int(v[1])
# for i in range(k):
#     if given%10==0:
#         given=given//10
#     else:
#         given=given-1
# print(given)
# def check(persons,opinions):
#     for i in range(persons):
#         if int(opinions[i]) == 1:
#             return 'HARD'
#     return 'EASY'
# persons = int(input())
# opinions = input().split(' ')
# print(check(persons,opinions))
def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    i=0
    l=len(s)
    for k in range(numrows):
        while(i<s):
            print(s[i],end='')
            i=i+2*numrows-2