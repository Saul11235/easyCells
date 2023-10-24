# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.move(4,15)

file.write("Hello World")

file.close()

if __name__=="__main__":
    print("test move")

