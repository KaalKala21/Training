x=int(input("total entries"))
print(x)
li=[]
for i in range(x):
    n=input("enter name")
    p=float(input("enter points"))
    li1=[n,p]
    li.append(li1)
for k in range(x):
    for j in range(x-1):
        if li[j][1]<li[j+1][1]:
            z=li[j]
            li[j]=li[j+1]
            li[j+1]=z
        elif li[j][1]==li[j+1][1]:
            if li[j][0]<li[j+1][0]:
                z=li[j]
                li[j]=li[j+1]
                li[j+1]=z
            else:
                z=li[j+1]
                li[j+1]=li[j]
                li[j]=z
for i in range(x):
    print(li[i][0])
