# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.direction3()

file.move(4,15)



for x in range(10):
    file.write("text"+str(x))
file.nLine()
for y in range(11):
    file.write("another-text"+str(y))


file.close()

if __name__=="__main__":
    print("test direction 3")

