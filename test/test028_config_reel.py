# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

for style in file.getListConfigs():
    file.sheet(style)
    file.config(style)
    file.write(style)

file.close()

if __name__=="__main__":
    print("Reel config pages")

