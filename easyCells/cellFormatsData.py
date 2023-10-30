# easy cells
# writed by Edwin Saul https://edwinsaul.com

styles={
        # aligment
        "left"       :{"align":"left"},
        "right"      :{"align":"right"},
        "center"     :{"align":"center"},
        "justify"    :{"align":"justify"},
        "vcenter"    :{"valign":"vcenter"},
        "vjustify"   :{"align":"vjustify"},
        "top"        :{"valign":"top"},
        "bottom"     :{"valign":"bottom"},


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
        "f-10"       :{"font_size":10},
        "f-20"       :{"font_size":20},


        # background color
        "b-gray"     :{"bg_color":"gray"},
        "b-yellow"   :{"bg_color":"yellow"},
        "b-blue"     :{"bg_color":"blue"},
        "b-lightblue":{"bg_color":"#ADD8E6"},
        "b-black"    :{"bg_color":"black"},
        "b-white"    :{"bg_color":"white"},

        }

#-------------------------------------------

builds= {
        "CENTER":["center","vcenter"],
        "note_1":["bold","f-blue"],
        "note_2":["bold","f-red"],
        "note_3":["bold","f-red",{"font_color":"green"}],
        }


if __name__=="__main__": print("ok")

