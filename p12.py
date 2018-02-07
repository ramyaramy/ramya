def main():
    list=[]
    x,y=input().split(" ")
    x=int(x)
    y=int(y)
    for i in range(0,x):
        k=int(input())
        list.append(str(k))

    final=(list[-y:]+list[:-y])
    print( ' '.join(final))
if __name__ == '__main__':
    main()
