import square
import utils 

#map names to list of every square w/ that name, i.e. elevators to all elevators 
class Floor(object):
    squares = {}
    def __init__(self, level, width, length): 
        self.level = level 
        self.width = width #x
        self.length = length #y

    def addSquare(add, name):
        squares[name] = squares.get(name, []) + add
    
    def removeSquare(rem): #new must be 
        if isinstance(rem, Square):
            squares[rem.name].remove(rem)
        