class Square(object):
    valid = 1 #valid values of 1 > not passable, 0 = passable
    def __init__(self, x, y): #can't do it with latitude, longitude 
        #self.plusCode = number #might not need this if we store the information at a plus code level
        self.x = x
        self.y = y 
    
    def coordinate(loc): #location is a tuple with latitude, longitude 
        return tuple
    
    # def __str__():
    #     return ""

class Path(Square):
    def __init__(self, x, y, accessible, name):
        self.x = x
        self.y = y
        self.accessible = accessible
        self.valid = 0
        self.name = name


class Exit(Path):
    def __init__ (self, x, y, name):
        self.x = x
        self.y = y
        self.valid = 0
        self.name = name #used to distinguish what type of exit (elevator, exit, entrance) a certain Exit object is 
        
class Wall(Square):
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = "wall"



# class Room (Path):
#     def __init__(self, name):
#         self.name = name
        
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