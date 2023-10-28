# formats for cells syles

styles={
         
        # basic font types
        "bold"       :{"bold":True},
        "italic"     :{"italic":True},
        "underline"  :{"underline":True},

        # font color
        "f-blue"     :{"font_color":"blue"},
        "f-red"      :{"font_color":"red"},

        # background color
        "b-gray"     :{"bg_color":"gray"},


        }

builds= {
        "note_1":["bold","f-blue"],
        "note_2":["bold","f-red"],
        "note_3":["bold","f-red",{"font_color":"green"}],
        }


if __name__=="__main__": print("ok")

