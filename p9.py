def main():
    start,end=input().split(" ")
    start=int(start)
    end=int(end)
    list=[]
    for num in range(start,end+1):
        if num > 1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                list.append(num)
    print(len(list))
if __name__ == '__main__':
    main()
