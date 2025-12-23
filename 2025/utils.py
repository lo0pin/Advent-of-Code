"""prints the values of a given variable
    format: 
    debug(list=list)
    @output:
"""
def debug(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}\t")
    print()

#einheitliches Format für  einen String
############## CHAPTER 1 ###############
def ausgabe(inp):
    print(inp.upper().center(len(inp)+2," ").center(40, "#"))
