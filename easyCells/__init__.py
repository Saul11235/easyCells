# easy cells

import xlsxwriter

try:    from literalName import literalName
except: from .literalName  import literalName

try:    from cellFormatsData import styles as cellstyles
except: from .cellFormatsData  import styles as cellstyles

class cells:

    def __init__(self,nameFile):
        #pointer cells
        self.__pointx=0
        self.__pointy=0
        #direction var
        self.__dirX=1
        self.__dirY=0
        #xlsxwriter objects
        self.workbook=xlsxwriter.Workbook(nameFile)
        self.__existsWorkSheet=False
        self.worksheet=None
        #data styles
        self.__dataStyles=cellstyles
        self.__listStyles=list(cellstyles.keys())
        self.__customStyle=[]
        self.__onlyOneStyle=[] #only for one use
        self.__lastStyle=None


    # get xlsxwriter objetcts
    #    getWorkBook
    #    getWorkSheet

    def getWorkBook(self):  return self.workbook
    def getWorkSheet(self): return self.worksheet

    # directions to write
    #    getCell          (0,0)
    #    getCellName      A1
    #    getCellNameAbs   $A$1
    #    getCellNameAbsX  $A1
    #    getCellNameAbsY  A$1

    def getCell(self):
        "retrun cell coordinate in format tuple"
        return (self.__pointx,self.__pointy)

    def getCellName(self): 
        "return name cell in format 'A1' 'B2' etc"
        _cellN=literalName(self.__pointx,self.__pointy)
        return str(_cellN[0])+str(_cellN[1])

    def getCellNameAbs(self): 
        "return name cell in format '$A$1' '$B$2' etc"
        _cellN=literalName(self.__pointx,self.__pointy)
        return "$"+str(_cellN[0])+"$"+str(_cellN[1])

    def getCellNameAbsX(self): 
        "return name cell in format '$A1' '$B2' etc"
        _cellN=literalName(self.__pointx,self.__pointy)
        return "$"+str(_cellN[0])+str(_cellN[1])
 
    def getCellNameAbsY(self): 
        "return name cell in format 'A$1' 'B$2' etc"
        _cellN=literalName(self.__pointx,self.__pointy)
        return str(_cellN[0])+"$"+str(_cellN[1])

    #  style functions
    def __makeStyle(self,inputList):
        stylesConfirmed=[]
        for element in inputList:
            print(element)

            pass
        pass

    def styles(self,**args):
        print("styles")
        for x in args: print(x)


    # directions to write
    #    dir1 - rigth
    #    dir2 - down 
    #    dir3 - left
    #    dir4 - up


    def direction1(self):
        "direction 1: left to rigth."
        self.__dirX=1; self.__dirY=0

    def direction2(self):
        "direction 2: up to down."
        self.__dirX=0; self.__dirY=1

    def direction3(self):
        "direction 3: rigth to left."
        self.__dirX=-1; self.__dirY=0

    def direction4(self):
        "direction 4: down to up."
        self.__dirX=0; self.__dirY=-1

    def step(self):
        "move the pointer to the next position"
        self.__pointx=self.__pointx+self.__dirX
        self.__pointy=self.__pointy+self.__dirY
        if self.__pointx<0: self.__pointx=0
        if self.__pointy<0: self.__pointy=0

    def nLine(self):
        "create an new line whit an carriage return"
        if   self.__dirX==1 and self.__dirY==0: # dir 1
            self.__pointy+=1
            self.__pointx=0
        elif self.__dirX==0 and self.__dirY==1: # dir 2
            self.__pointy=0
            self.__pointx+=1
        elif self.__dirX==-1 and self.__dirY==1: # dir 3
            self.__pointy-=1
            self.__pointx=0
        elif self.__dirX==0 and self.__dirY==-1: # dir 4
            self.__pointy=0
            self.__pointx-=1
        if self.__pointx<0: self.__pointx=0
        if self.__pointy<0: self.__pointy=0

    def move(self,X,Y):
        "relative move in X and Y cells to current cell"
        self.__pointx+=int(X)
        self.__pointy+=int(Y)
        if self.__pointx<0: self.__pointx=0
        if self.__pointy<0: self.__pointy=0
        pass

    def sheet(self,name_New_WorkSheet) :
        "create a new sheet whit a name"
        self.__existsWorkSheet=True
        self.worksheet=self.workbook.add_worksheet(name_New_WorkSheet)
        pass

    def write(self,content):
        "write an content in a cell"
        if self.__existsWorkSheet:
            self.worksheet.write(self.__pointy,self.__pointx,content)
            self.step()
        else:
            print("First declare sheet: using easyCells.easyCells.sheet(name)")

    def close(self):
        self.workbook.close()


if __name__=="__main__":
    a=cells("data.xlsx")
    print("ok")


