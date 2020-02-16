import fill
import building
import floor
import square

def main(start, destinationName, level, building): #start tuple contains lat/long, destination string
    start = square.coordinate(start)
    currentFloor = building.floors[level]
    allSquares = currentFloors.squares
    destinations = currentFloor.squares[destinationName] #need to calculate a
    
    #mark down (0, 0) as the top, north west corner on the floor plans 
    floorPlan = []
    for row in range(currentFloor.width):
        floorPlan.append([])
        for col in range(currentFloor.length):
            floorPlan[row].append(0)
    
    for squareType in allSquares.keys():
        for square in allSquares[squareType]:
            x = square.x
            y = square.y
            floorPlan[x][y] = square.valid 

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
    path = fill.astar(floorPlan, start, destination)
    #print(path)
    paths.append(path)
print(min(paths, key=len))


if __name__ == '__main__':
    main()