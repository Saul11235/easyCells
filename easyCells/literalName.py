
def literalName(coorX,coorY):

    def division(bigNum,littleNum):
        remainer=int(int(bigNum)%int(littleNum))
        division=int((int(bigNum)-int(remainer))/int(littleNum))
        return(division,remainer)

    def getchar(num):
        if num==0: return ""
        listChar="-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return str(listChar[num])

    def splitNum(num,base):  #divides a num 1=A; 27=AA; etc
        if num<base: return [num+1]
        from math import log
        l=[]; _count=num
        _exp_max=int(  log(abs(num)+1)/log(base)   )+1
        for x in range(_exp_max,0,-1):
            _div=division(_count,pow(base,x))
            if _div[0]>0:
                if _div[1]==0: _div= (_div[0]-1,base)
                _count=_div[1]
                l.append(_div[0])
                if _div[1]<=base:
                    print(_div)
                    l.append(_div[1])
                    _count=0
        return l  #return list of digits

    textCHAR=""
    listNumChar=splitNum(coorX,26)

    for x in listNumChar:
        nchar=getchar(x)
        textCHAR=textCHAR+nchar

    textNUM=str(int(coorY+1))

    return([textCHAR,textNUM])


#-------------------------------------------

if __name__=="__main__":
    #---------
    inix=24
    limx=400
    #--------
    iniy=0
    limy=iniy+1
    #-----------------------------
    for x in range(inix,limx):
        for y in range(iniy,limy):
            print(str([x,y])+"   "+str(literalName(x,y)))



