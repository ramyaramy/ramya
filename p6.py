max= 256
def Iso(str1, str2):
    X = len(str1)
    Y = len(str2)
    if X != Y:
        return False
    marked = [False] * max
    map = [-1] * max
    for i in range(Y):
        if map[ord(str1[i])] == -1:
            if marked[ord(str2[i])] == True:
                return False
            marked[ord(str2[i])] = True
            map[ord(str1[i])] = str2[i]
        elif map[ord(str1[i])] != str2[i]:
            return False
    return True
if __name__ == '__main__':
    str1,str2=input().split(" ")
    if Iso(str1,str2):
        print("yes")
    else:
        print("no")
