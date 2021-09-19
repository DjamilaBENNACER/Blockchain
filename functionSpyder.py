# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
l'indentation est très importante en python'
"""
def myFunct(int_in) : 
    return int_in/5
   
print("HELLO")

if __name__ == '__main__':
    print(myFunct(21))
else:
    print("primer imported, not invoked")
    
"""    
class myClass:
    def __init__(self):
        print("new instance created")
  
    def __del__(self):
        print("new instance deleted")

"""

class myClass1:
    oneval = 17
    def div(self, int_in) :
        try :
                return int_in/self.oneval
        except TypeError :
                print("Must pass integer to passs ")
                return 0
        except :
                print("Uknown error in div")
                return 0
                
            
    """__init__ represente le constructeur en python"""
    def __init__ (self, inval) :
        self.oneval = inval
 
class newClass (myClass1) :
    name1 = 'Levi'
    def __repr__(self) : 
        name1 = 'jeff'
        return (self.name1 + ": oneval is equal to " + str(self.oneval))
        
"""  self.oneval = 4"""
    

"""Quand je met le self sa change regarde bien 
si je met le self il m'affiche le Levi il prend le nom qui figure ds la classe
par contre si je le met pas il va me prendre celui qui se trouve dans
__repr__ """


"""Au lieu de faire tout ce ci on va le faire directement sur le constructeur"""    
""" C = myClass1() la c'est avant que je fasse le __init__ qui est le constructeur"""
"""C.oneval = 4  cette ligne est dans le constructeur remplacé par self.inval = 4
 """    
A = myClass1(4)
B = myClass1(10)
print(A.oneval)
print(A.div(34))
print(B.div(34))
N = newClass(12)
print(N.name1)
print(N.div(36))
print(N)
print(N.div('rutenbega'))
print(A)
print("Done~")