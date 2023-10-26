# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")


for x in range(100):
    for y in range(4000):
        var=file.getCellName()
        file.write(str(var))
    file.nLine()

file.close()

if __name__=="__main__":
    print("print name cells")

