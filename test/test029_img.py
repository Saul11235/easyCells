# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")
file.sheet("new sheet")
file.direction2()


for x in range(10):
    file.write("text"+str(x))

file.nLine()

for y in range(11):
    file.write("another-text"+str(y))

file.img("img.png")
file.step(10)
file.write("----")

file.img("img.png",2,2)


file.close()

if __name__=="__main__":
    print("create ")

