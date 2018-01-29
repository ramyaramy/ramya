num = int(input("Enter a number: "))
if num<=1000:
   for i in range(2,num):
       if (((num % i) == 0) and (num//i)):
           print("not")

           break
   else:
            print("yes")
else:
   print("enter less then 1000")
