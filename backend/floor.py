from square import *
from utils import *

#map names to list of every square w/ that name, i.e. elevators to all elevators 
class Floor(object):
    squares = {}
    def __init__(self, level, width, length): 
        self.level = level 
        self.width = width #col
        self.length = length #row

    def addSquare(self, add, name):
        self.squares[name] = self.squares.get(name, []) + [add]
    
    def removeSquare(rem): #new must be 
        if isinstance(rem, Square):
            squares[rem.name].remove(rem)
        