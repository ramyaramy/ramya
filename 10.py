num=int(input("enter any number "))
count=0
while(num>0):
    num=num//10
    count=count+1
print("number of digits in a given number =%d" %count)
