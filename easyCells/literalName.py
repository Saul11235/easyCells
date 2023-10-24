
def literalName(coorX,coorY):

    def division(bigNum,littleNum):
        remainer=int(bigNum%littleNum)
        division=int((bigNum-remainer)/littleNum)
        return(division,remainer)

    def getchar(num):
        listChar="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return str(listChar[num])

    def splitNum(num,base):
        l=[]; big=num; little=0
        if num>base: return[num]
        while big>=base:
            v=division(big,base)
            big=v[0]; little=v[1]; l.append(little)
            if big<base:l.append(big)
        return l

    textCHAR="x"
    listNumChar=splitNum(coorX,10)

    for x in listNumChar:
        nchar=getchar(x)
        textCHAR=nchar+textCHAR

    textNUM=str(int(coorY+1))

    return([textCHAR,textNUM])


#-------------------------------------------

if __name__=="__main__":
    #---------
    inix=0
    limx=21
    #--------
    iniy=0
    limy=iniy+1
    #-----------------------------
    for x in range(inix,limx):
        for y in range(iniy,limy):
            print(str([x,y])+"   "+str(literalName(x,y)))



