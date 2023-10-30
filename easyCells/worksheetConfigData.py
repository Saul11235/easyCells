# easy cells
# writed by Edwin Saul https://edwinsaul.com

list_config_workSheet=[
        "nogrid",
        "landscape",
        ]

custom_sytle_config={
        "toView": ["nogrid","landscape"],
        }
def get_list_config_worksheet() :
    return list_config_workSheet

def config(c,worksheet):
    # hide grid
    print(c)
    if   c=="nogrid"      : worksheet.hide_gridlines()
    elif c=="landscape"   : worksheet.set_landscape()
    else:
        raise Exception("Error configuration "+str(c)+" not recognized")
