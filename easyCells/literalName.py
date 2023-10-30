# easy cells
# writed by Edwin Saul https://edwinsaul.com

def literalName(coorX,coorY):

    def division(bigNum,littleNum):
        remainer=int(int(bigNum)%int(littleNum))
        division=int((int(bigNum)-int(remainer))/int(littleNum))
        return(division,remainer)

    def getchar(num):
        listChar="-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return str(listChar[num])

    def splitNum(num,base):  #divides a num 1=A; 27=AA; etc
        if num<base: return [num+1]
        from math import log
        l=[]; _count=num+1
        _exp_max=int(  log(abs(num)+1)/log(base)   )+1
        for x in range(_exp_max,0,-1):
            _div=division(_count,pow(base,x))
            _numerator=_div[0]
            _remainer=_div[1]
            l.append(_numerator)
            if x==1: l.append(_remainer)
            _count=_remainer
        return l

    def clearZerosBefore(listChars):
        zeroFound=False
        try: listChars.index(0); zeroFound=True
        except: return listChars
        ll=[]; firstNum=False #clear zero digits 00010 - 10
        for x in listChars: 
            if x==0 and not(firstNum): pass
            else: ll.append(x); firstNum=True
        return ll  #return list of digits

    def clearZerosIn(listChars,base):
        zeroFound=False
        try: listChars.index(0); zeroFound=True
        except: return listChars
        v=listChars.index(0)
        listChars[v-1]=listChars[v-1]-1
        listChars[v]=base
        return listChars

    def haveZeros(listChars):
        try: listChars.index(0); return True
        except: return False

    textCHAR=""

    listNumChar=splitNum(coorX,26) #list of numbers

    while haveZeros(listNumChar):
        listNumChar=clearZerosBefore(listNumChar)
        listNumChar=clearZerosIn(listNumChar,26)

    for x in listNumChar: #making string
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



