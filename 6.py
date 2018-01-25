year=int(input("enter the year to check leap year"))
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is leap year")
else:
    print("%d is not the leap year")
