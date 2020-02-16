import square
import utils 

class Floor(object):
    squares = {}
    def __init__(self, level): 
        self.level = level 

    def addSquare(new, pluscode):
        squares[pluscode] = new
    
    def removeSquare(rem): #new must be 
        if isinstance(rem) == Square:
            key = squares.getKey(rem)
            del squares[key]
        else if rem.type() == String: #pluscode type, might change
            del squares[rem]
    

