s1,s2=input().split(' ')
x=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        x=x+1
if(x==1):
    print('yes')
else:
    print('no')
