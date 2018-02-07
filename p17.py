def gcd(x,y):
    while y > 0:
        x, y = y, x % y
    return x
def lcm(x, y):
    return x * y / gcd(x, y)
x,y=map(int,input("Enter the values:").split(' '))
print(int(lcm(x,y)))
