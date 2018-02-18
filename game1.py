#move and route acccording to value
class robot:
    N=0
    E=1
    S=2
    W=3
    x=0
    y=0
    dir=N
    def robot(direction):
        if value=='R':
            dir=(dir+1)%4
            print("dir",dir)
    def robot(move):
        if dir==N:
            y+=1
            print("moved to",y)
        elif dir==E:
            x+=1
            print("moved to",x)
        elif dir==S:
            y-=1
            print("moved to",y)
        else:
            x+=1
            print("moved to",x)

if __name__=='__main__':
    path=0
    for i in range(7):
        path=input(" ")
    if path=='M':
        path=robot.robot(direction)
    elif path=='R':
        path=robot.robot(move)

