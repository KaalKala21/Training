#input - aaabbccdeee
#output - a3b2c2d1e3
#using set
s1=str(input())
set1=set()
for i in range(len(s1)):
    set1.add(s1[i]+str(s1.count(s1[i])))
print(set1)
li=list(set1)
li.sort()
stri=""
for i in li:
    stri=stri+i
print(stri)
