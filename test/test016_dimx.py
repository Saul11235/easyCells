# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.dimx(100,100,200)


file.close()

if __name__=="__main__":
    print("dim X")

