# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.style("b-gray")

for x in range(10):
    file.write("text"+str(x),2)


file.style("b-yellow")
for y in range(11):
    file.write("another-text"+str(y),2,3)


file.close()

if __name__=="__main__":
    print("create file")

