# easy cells

import xlsxwriter

try:    from literalName   import literalName
except: from .literalName  import literalName

try:    from cellFormatsData   import styles as cellstyles
except: from .cellFormatsData  import styles as cellstyles

try:    from cellFormatsData   import builds as buildstyles
except: from .cellFormatsData  import builds as buildstyles

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
        # styles
        self.__dicStyles={}
        self.__configStyles()
        self.__currentStyle=None
        # filters
        self.__infiFilterX=0
        self.__infiFilterY=0
            

    # get xlsxwriter objetcts
    #    sheet(name_New_WorkSheet)
    #    close
    #    getWorkBook
    #    getWorkSheet


    def sheet(self,name_New_WorkSheet,*colorTab) :
        "create a new sheet whit a name, and add color"
        self.__existsWorkSheet=True
        self.__pointx=0
        self.__pointy=0
        self.__currentStyle=None
        try: self.worksheet=self.workbook.add_worksheet(name_New_WorkSheet)
        except: raise Exception("Error creating new worksheet: "+str(name_New_WorkSheet))
        if len(colorTab):
            try: self.worksheet.set_tab_color(colorTab[0])
            except: raise Exception("Error "+str(colorTab[0])+" is not a valid color for a worksheet")


    def close(self):
        self.workbook.close()


    def getWorkBook(self):  return self.workbook
    def getWorkSheet(self): return self.worksheet

    # write functions
    #   write(content,*dimcells)
    #   writeM(*contents)


    def writeM(self,*contents):
        "write multiple cells"
        for content in contents:
            self.write(content)


    def write(self,content,*dimcells):
        "write an content in a cell or an agrupment of these"
        dimCells=[]
        if len(dimcells):
            try:
                dimCells.append(abs(int(dimcells[0]-1)))
                dimCells.append(abs(int(dimcells[1]-1)))
            except: pass
            dimCells.append(0);dimCells.append(0)
        #----------------------------
        if self.__existsWorkSheet and not(len(dimcells)):
            if self.__currentStyle==None:
                self.worksheet.write(self.__pointy,self.__pointx,content)
            else:
                self.worksheet.write(self.__pointy,self.__pointx,content,self.__currentStyle)
            self.step()
        #----------------------------
        elif self.__existsWorkSheet and len(dimcells):
            if self.__currentStyle==None:
                self.worksheet.merge_range(self.__pointy,self.__pointx,self.__pointy+dimCells[1],self.__pointx+dimCells[0],content)
            else:
                self.worksheet.merge_range(self.__pointy,self.__pointx,self.__pointy+dimCells[1],self.__pointx+dimCells[0],content,self.__currentStyle)
            self.move(dimCells[0],dimCells[1])    
            self.step()
        #----------------------------
        else:
            raise Exception("First declare sheet: using easyCells.easyCells.sheet(name)")


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
    #   newStyle(nameSytle , * contents)
    #   getListStyles 
    #   style (*namestyles)
    #   noStyle 

    def __configStyles(self):
        #config styles from extern data
        self.__dicStyles=cellstyles
        for custom in buildstyles.keys():
            self.newStyle(custom,*tuple(buildstyles[custom]))

    def __isValidStyle(self,obj):
        is_valid=False
        try:self.getListStyles().index(obj);is_valid=True
        except:pass
        return is_valid

    def __getStyle(self,obj): return self.__dicStyles[obj]

    def newStyle(self,nameSytle,*contents):
        newStyle={}
        listSubStyles=[]
        for content in contents:
            if type(content)==dict: listSubStyles.append(content)
            else:
                if self.__isValidStyle(content):
                    listSubStyles.append(self.__getStyle(content))
                else:
                    raise Exception("Error "+str(content)+" is not a valid style")
        for dicStyle in listSubStyles:
            for item in dicStyle.keys():
                newStyle[item]=dicStyle[item]
        if newStyle!={}:
            self.__dicStyles[nameSytle]=newStyle

    def getListStyles(self): return list(self.__dicStyles.keys())

    def style(self,*nameSytles):
        if len(nameSytles)==0:
            self.noStyle()
        elif len(nameSytles)==1 and self.__isValidStyle(nameSytles[0]):
            dict_style=self.__getStyle(nameSytles[0])
            newStyle=self.workbook.add_format(dict_style)
            self.__currentStyle=newStyle
        elif len(nameSytles)==1 and not(self.__isValidStyle(nameSytles[0])):
            raise Exception("Error "+str(nameSytle)+" is no a valid style")
        else:
            list_dic_styles=[]
            for name in nameSytles:
                if self.__isValidStyle(name):
                    list_dic_styles.append(self.__getStyle(name))
                else:
                    raise Exception("Error "+str(name)+" is no a valid style")
            dict_style={}
            for d in list_dic_styles:
                for e in d.keys():
                    dict_style[e]=d[e]
            newStyle=self.workbook.add_format(dict_style)
            self.__currentStyle=newStyle


    def noStyle(self): self.__currentStyle=None

    # Set Filters to manage data
    #   beginFilter() 
    #   endFilter()

    def beginFilter(self):
        self.__infiFilterX=self.__pointx
        self.__infiFilterY=self.__pointy

    def endFilter(self):
        self.backStep()
        self.worksheet.autofilter(self.__infiFilterY,self.__infiFilterX,self.__pointy,self.__pointx)
        self.step()

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

    # functions move    
    #   step
    #   backStep
    #   perpendicularStep
    #   perpendicularBackStep
    #   nLine
    #   move
    #   absoluteMove

    def __verifiPointers(self):
        if self.__pointx<0: self.__pointx=0
        if self.__pointy<0: self.__pointy=0

    def step(self):
        "move the pointer to the next position"
        self.__pointx=self.__pointx+self.__dirX
        self.__pointy=self.__pointy+self.__dirY
        self.__verifiPointers()

    def backStep(self):
        "move the pointer to the back position"
        self.__pointx=self.__pointx-self.__dirX
        self.__pointy=self.__pointy-self.__dirY
        self.__verifiPointers()

    def perpendicularStep(self):
        "move the pointer to the next position"
        self.__pointx=self.__pointx+self.__dirY
        self.__pointy=self.__pointy+self.__dirX
        self.__verifiPointers()

    def perpendicularBackStep(self):
        "move the pointer to the back position"
        self.__pointx=self.__pointx-self.__dirY
        self.__pointy=self.__pointy-self.__dirX
        self.__verifiPointers()

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
        self.__verifiPointers()

    def move(self,X,Y):
        "relative move in X and Y cells to current cell"
        self.__pointx+=int(X)
        self.__pointy+=int(Y)
        self.__verifiPointers()

    def absoluteMove(self,X,Y):
        "relative move in X and Y cells to current cell"
        self.__pointx=int(X)
        self.__pointy=int(Y)
        self.__verifiPointers()

    # dimensionCells functions
    #   dimx (*dims)

    def dimx(self,*dims):
        list_ints=[]
        for dim in dims:
            try: list_ints.append(abs(float(dim)))
            except: pass
        if len(dims)==len(list_ints):
            _px=self.__pointx
            for x in range(len(list_ints)):
                self.worksheet.set_column(_px+x,_px+x,list_ints[x])
        else:raise Exception("Error "+str(dims)+" must be integers")

    def dimy(self,*dims):
        list_ints=[]
        for dim in dims:
            try: list_ints.append(abs(float(dim)))
            except: pass
        if len(dims)==len(list_ints):
            _py=self.__pointy
            for y in range(len(list_ints)):
                self.worksheet.set_row(_py+y,list_ints[y])
        else:raise Exception("Error "+str(dims)+" must be integers")

    def dimnx(self,ncells,dim):
        if type(ncells)==int or (type(dim)==int or type(dim)==float):
            self.dimx(*tuple([dim]*abs(ncells)))
        else:raise Exception("Error "+str(ncells)+" must be an int, and "+str(dim)+" must be an number")

    def dimny(self,ncells,dim):
        if type(ncells)==int or (type(dim)==int or type(dim)==float):
            self.dimy(*tuple([dim]*abs(ncells)))
        else:raise Exception("Error "+str(ncells)+" must be an int, and "+str(dim)+" must be an number")


    #---------------------------------------
    # visualization functions
    def splitView(self) : 
        self.worksheet.freeze_panes(self.__pointy,self.__pointx)
    #---------------------------------------
    


if __name__=="__main__":
    a=cells("data.xlsx")
    print("ok")


