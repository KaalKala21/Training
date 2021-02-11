#with list
s1=str(input())
li[:0]=s1
for i in range(len(li)):
    li.insert(i+1,x=li.count(li[i]))
    if li[i] in li[i+1:]:
        li.pop(j)
    
