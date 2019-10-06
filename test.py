def test(lis):
    max_end = 0
    max_sum = 0
    s=0
    st=0
    end=0
    for i in range(len(lis)):
        max_end += lis[i]
        if max_end < 0:
            max_end = 0
            s=i+1
        if max_sum<max_end:
            max_sum = max_end
            st=s
            end=i
    print(max_sum)
    print(lis[st:end+1])

lis = [1,2,-1,-4,3,-7,8,-1,9,-1]
test(lis)

#################  
