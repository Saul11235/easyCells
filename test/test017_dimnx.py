# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.dimnx(30,0.5)
file.write("x")
file.write("x")
file.write("x")


file.close()

if __name__=="__main__":
    print("dim n X")

