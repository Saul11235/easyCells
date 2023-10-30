# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet","red")
file.write("hello")

file.sheet("new sheet2","blue")
file.write("hello 2")

file.sheet("new sheet 3","yellow")
file.write("hello 3")

file.close()

if __name__=="__main__":
    print("create file")

