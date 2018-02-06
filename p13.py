num=int(input())
sum=0
while num > 0:
    digit = num % 10
    sum = sum + (digit ** 2)
    num //= 10
print(sum)
