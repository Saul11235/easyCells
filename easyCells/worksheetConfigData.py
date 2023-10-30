# easy cells
# writed by Edwin Saul https://edwinsaul.com

list_config_workSheet=[

        "nogrid",
        "noheaders",

        "viewNormal",
        "viewBreak",
        "viewPage",

        "landscape",
        "portrait",

        ]

#--------------------------------------------

custom_sytle_config={
        "toView": ["nogrid","landscape"],
        }

#--------------------------------------------

def config(c,worksheet):
    # hide grid
    if   c=="nogrid"      : worksheet.hide_gridlines(2)
    elif c=="noheaders"   : worksheet.hide_row_col_headers()
    elif c=="landscape"   : worksheet.set_landscape()
    elif c=="portrait"    : worksheet.set_portrait()
    elif c=="viewNormal"  : worksheet.set_page_view(0)
    elif c=="viewPage"    : worksheet.set_page_view(1)
    elif c=="viewBreak"   : worksheet.set_page_view(2)
    else:
        raise Exception("Error configuration "+str(c)+" not recognized")
