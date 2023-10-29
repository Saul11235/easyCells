# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.dimny(30,45)
file.write("y")
file.write("y")
file.write("y")


file.close()

if __name__=="__main__":
    print("dim n Y")

