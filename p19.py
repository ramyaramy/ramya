a=int(input())
l=list(1 for i in range(a))
y=[]
for i in range(2,a,1):
    if l[i]==1:
        for j in range(i*i,a,i):
            l[j]=0
        if a%i==0:
            y.append(i)
print(" ".join(str(x) for x in y))
