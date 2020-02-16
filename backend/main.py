from fill import *
from building import *
from floor import *
from square import *
from buildingGenerator import *

def main(start, destinationName, level, building): #start tuple contains lat/long, destination string
    # start = square.coordinate(start)
    currentFloor = building.floors[level]
    allSquares = currentFloor.squares
    destinations = currentFloor.squares[destinationName] #need to calculate a
    
    #mark down (0, 0) as the top, north west corner on the floor plans 
    floorPlan = []
    for row in range(currentFloor.length):
        floorPlan.append([])
        for col in range(currentFloor.width):
            floorPlan[row].append([])
    
    for squareType in allSquares.keys():
        for square in allSquares[squareType]:
            x = square.x
            y = square.y
            floorPlan[x][y] = square.valid 
    print(floorPlan)
    # print(currentFloor.length, currentFloor.width)
    #get the latitude/longitude of the entrance; make an arbitrary scale 
# 1> invalid numbers
# visualize a floor as a rectangle and fill in the invalid spaces (outside of the floor + the walls into the array)
    
    # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # start = (0, 0)
    # end = (7, 6)
    paths = []
    for destination in destinations:
        dX = destination.x
        dY = destination.y
        path = astar(floorPlan, start, (dX, dY))
    #print(path)
        paths.append(path)
    minPath = min(paths, key=len)
    for coord in minPath:
        floorPlan[coord[0]][coord[1]] = 9
    print(minPath)
    print(floorPlan)


if __name__ == '__main__':
    main((8, 2), "bathroom", 1, generate()) #DEMO