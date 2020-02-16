from utils import *
class Building(object):
    floors = {}
    def __init__(self, top_floor, bot_floor, name):
        self.top_floor = top_floor
        self.bot_floor = bot_floor
        self.name = name
    
    def addFloor(self, floor, level):
        self.floors[level] = floor

    def removeFloor(val):
        if isinstance(val) == Floor:
            key = getKey(floor, floors)
            del floors[key]
        elif val.type() == int:
            del floors[val]
    
    # def generateFloors(floors):


    #     #generate by adding one at a time? 
    #     #plusCode
    #     # 
