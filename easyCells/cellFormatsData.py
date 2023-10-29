# formats for cells syles

styles={
         
        # basic font types
        "bold"       :{"bold":True},
        "italic"     :{"italic":True},
        "underline"  :{"underline":True},

        # font color
        "f-blue"     :{"font_color":"blue"},
        "f-red"      :{"font_color":"red"},
        "f-black"    :{"font_color":"black"},
        "f-white"    :{"font_color":"white"},

        # font size

        1            :{"font_size":1},
        2            :{"font_size":2},

        # background color
        "b-gray"     :{"bg_color":"gray"},
        "b-yellow"   :{"bg_color":"yellow"},
        "b-blue"     :{"bg_color":"blue"},
        "b-black"    :{"bg_color":"black"},
        "b-white"    :{"bg_color":"white"},


        }

builds= {
        "note_1":["bold","f-blue"],
        "note_2":["bold","f-red"],
        "note_3":["bold","f-red",{"font_color":"green"}],
        }


if __name__=="__main__": print("ok")

