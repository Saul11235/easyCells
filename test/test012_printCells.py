# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")


for x in range(200):
    for y in range(200):
        var=file.getCell()
        file.write(str(var))
    file.nLine()

file.close()

if __name__=="__main__":
    print("print cells")

