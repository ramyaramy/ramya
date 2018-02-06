str=input()
list=[]
vowels=['a','e','i','o','u']
for i in str:
     if i in vowels:
        x=i.replace(i,'')
        list.append(x)
     else:
        list.append(i)

final=''.join(list)
print(final[::-1])
