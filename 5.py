a=int(input("please enter the first value"))
b=int(input("please enter the second value"))
c=int(input("please enter the third value"))

if (a > b and a > c):
          print("{0} is largest than both {1} and {2}".format(a,b,c))
elif (b > a and b > c):
          print("{0} is largest than both {1} and {2}".format(b,a,c))
elif (c > a and c > b):
          print("{0} is largest than both {1} and {2}".format(c,a,b))
else:
         print("either any two value or all the three values are equal")
