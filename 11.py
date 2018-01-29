n = input('Enter any number : ')
try:
    val = int(n)
    if n == str(n)[::-1]:
        print('yes')
    else:
        print('no')
except ValueError:
    print("it's not a valid )
