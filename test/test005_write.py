# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

for x in range(10):
    file.write("text"+str(x))

for y in range(11):
    file.write("another-text"+str(y))


file.close()

if __name__=="__main__":
    print("create file")

