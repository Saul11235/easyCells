# test writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("data Table","red")

file.dimx(3,10,20,20,20)

file.style("bold","f-blue","f-20")
file.write("Data Table1",5); file.nLine()


file.style("italic","b-black","f-white")
file.writeM("Nro","Name","Favourite Colour","Favourite Drink","Favourite Fruit")
file.nLine()

file.style()
file.beginFilter()

file.writeM(1,"Saul","blue","soda","orange")
file.nLine()


file.writeM(2,"Larry","white","soda","apple")
file.nLine()


file.writeM(3,"Bruno","red","coffe","orange")
file.nLine()


file.writeM(4,"Mary","red","soda","apple")
file.nLine()


file.writeM(5,"Lucy","yellow","water","orange")
file.nLine()


file.writeM(6,"Sofia","blue","coffe","orange")
file.endFilter()
file.nLine()



file.close()

if __name__=="__main__":
    print("create filter")

