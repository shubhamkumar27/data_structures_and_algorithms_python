def merge(list1,list2):
    final = []
    i=0
    j=0
    while(i<len(list1) and j<len(list2)):
        if list1[i]<=list2[j]:
            final.append(list1[i])
            i+=1
        elif list2[j]<list1[i]:
            final.append(list2[j])
            j+=1
    final = final + list1[i:] + list2[j:]
        
    print(final)

l1 = [1,3,5,7,9,10]
l2 = [0,2,4,6,8]
merge(l1,l2)