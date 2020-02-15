class Square(object):
    valid = False
    def __init__(self, number):
        self.plusCode = number #might not need this if we store the information at a plus code level 

class Path(Square):
    def __init__(self, accessible, start, end):
        self.accessible = accessible
        self.valid = True


class Exit(Paths):
    def __init__ (self, name):
        self.valid = True
        self.name = name #used to distinguish what type of exit (elevator, exit, entrance) a certain Exit object is 
        
class Wall(Square):
    def __init__(self):


class Room (Path):
    def __init__(self):
        
    #NUMBER = PLUS CODE COORDINATE
    #
    # 
    # building class check max and min level 
    # 
    # 
    # fill class > that takes the entire "grid" or all of the objects + the 2 squares we want to navigate
    # between and solves a path 
    #
    # Building class > contiains all of the square objects > update the grid class + fill with different squares
    #
    # Floor class  > everything on a single floor 
    #
    # Square class > plus code code 
    #   
    #   Paths > inherit from the square
    #       -valid pathmaking tiles
    #       -attribute for accessibility friendliness
    #
    #       Exits > inherit from the square
    #           -doors, elevators, stairs
    #
    #   Walls > inherit from the square
    #       -invalid squares for pathmaking
    # 
    # different types of specific squares that that inherit from square and have attributes  