# test first writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("new sheet")

file.style("bold")
file.write("Text 1")

file.write("Text 2")

file.style("italic","b-yellow")
file.write("Text 3")

file.write("Text 3.1")

file.style()
file.write("Text 4")

file.close()

if __name__=="__main__":
    print("create file")

