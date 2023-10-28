# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")
file.sheet("new sheet")

file.direction2()

for style in file.getListStyles():
    file.style(style)
    file.write(style)

file.close()

if __name__=="__main__":
    print("test styles")

