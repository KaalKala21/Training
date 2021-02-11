s1=str(input())
di1=dict()
stri=""
di1={x:s1.count(x) for x in s1}
#for x in s1:
#   di1[x]=s1.count(x)
for x in di1:
    stri=stri+x+str(di1[x])
print(stri)
