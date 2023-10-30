# test writed by: ESPM

from easyCells import cells

file=cells("example.xlsx")

file.sheet("data Table","red")

# config  worksheet  
file.config("nogrid","landscape")

file.dimx(3,10,20,20,20)
file.dimy(30)

file.style("bold","f-blue","f-20","center")
file.write("Data Table1",5); file.nLine()


file.style("italic","b-black","f-white")
file.writeM("Nro","Name","Favourite Colour","Favourite Drink","Favourite Fruit")
file.nLine()


file.splitView()
file.beginFilter()
file.style("b-yellow","f-red","bold")
file.write("x")
file.nLine()

file.style("b-lightblue","center")

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
    print("split view")

