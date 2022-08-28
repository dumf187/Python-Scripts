#from sys imort argv
from payloads import *

# class members in python are public
# all member functions are virtual.

# Objects can be bound to the same Object aka aliasing
class open_functions():
    def __init__():

        
# references to names in python are attribute referrences





#the innermost scope, which is searched first, contains the local names
#the scopes of any enclosing functions, which are searched starting with the nearest enclo#sing scope, contains non-local, but also non-global names
#the next-to-last scope contains the current module’s global names
#the outermost scope (searched last) is the namespace containing built-in names
           # self.pload = input("Geben Sie einen Pfad an, falls noch keiner festgelegt sein sollte")i
       #  self.open = open_as_lines(self)
       #  self.file = open_as_file(self) 
#   pload = open_functions()
# Bei gelegenheit -> self als argv parameter
     def open_as_lines():
         testlines = [""]
         with opent("testlines.txt", "r") as lines:
             for i in lines.readlines():
                 testlines.append(i)
         return testlines
                #print(i)

def open_as_file():
    pload_list = []
    with open("lines.txt", 'r+') as files:
        pload_list = [line.rstrip('\n') for line in files]
        print(pload_list)


#list_style_open = open_as_lines()
#list_style_file= open_as_file()

print("list_style_open+'\n'")
print("[*] OPEN STYLE [*]")
print("list_style_file+'\n'")
print("[<+> FILE STYLE <+>]")


print([<+> FILE STYLE <+>])


