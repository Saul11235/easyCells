# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.dimy(1,2,3,5,10.30,1.9,8,20.10,0,1,2.5,3.5,0)
file.write("y")
file.write("y")
file.write("y")


file.close()

if __name__=="__main__":
    print("dim Y")

