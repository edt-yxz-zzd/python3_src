from sand.forgot_import import *
import sand

m = __import__(__name__)
table = fname2symtable(__file__) #get_symtable_of_module(m)
s = table2forgots(table)

#print(forgot_import(back=-1))

affsafs = 1

a=table.get_symbols()[2]


