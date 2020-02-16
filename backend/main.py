from fill import *
from building import *
from floor import *
from square import *
from buildingGenerator import *
#from google.cloud import firestore

HuangCenter = generateHuang()

def main(start, destinationName, level, building, accessible, sofar): #start tuple contains lat/long, destination string
    # start = square.coordinate(start)
    currentFloor = building.floors[level]
    allSquares = currentFloor.squares

    # def sendRooms():
    # # Project ID is determined by the GCLOUD_PROJECT environment variable
    #     db = firestore.Client()

    # # export GOOGLE_APPLICATION_CREDENTIALS="/Users/SahilMehta/Downloads/UMaps_Firestore.json"
    
    #     count = 0
    #     for key in allSquares:
    #         #print(type(allSquares[s]))
    #         for room in allSquares[key]:
    #             if count > 25:
    #                 break
    #             doc_ref = db.collection(u'Floor0').document(room.name + str(count))
    #             doc_ref.set({
    #                 u'x': room.x,
    #                 u'y': room.y,
    #                 u'accessible' : room.accessible,
    #                 u'valid' : room.valid,
    #                 u'name' : room.name
    #             })
    #             count += 1
    # sendRooms()

    # def sendRooms():
    # # Project ID is determined by the GCLOUD_PROJECT environment variable
    #     db = firestore.Client()

    # # export GOOGLE_APPLICATION_CREDENTIALS="/Users/SahilMehta/Downloads/UMaps_Firestore.json"
    
    #     count = 0
    #     for key in allSquares:
    #         #print(type(allSquares[s]))
    #         for room in allSquares[key]:
    #             doc_ref = db.collection(u'Floor1').document(room.name + str(count))
    #             doc_ref.set({
    #                 u'x': room.x,
    #                 u'y': room.y,
    #                 u'accessible' : room.accessible,
    #                 u'valid' : room.valid,
    #                 u'name' : room.name
    #             })
    #             count += 1
    # sendRooms()

    switchFloor = False

    if destinationName not in currentFloor.landmarks:
        switchFloor = True
        if accessible:
            destinations = currentFloor.squares["elevator"]
        else:
            destinations = currentFloor.squares["stair"] + currentFloor.squares["elevator"]
    else:
        destinations = currentFloor.squares[destinationName]
    
     #need to calculate a
    
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
            if not accessible:
                floorPlan[x][y] = square.valid 
            else:
                floorPlan[x][y] = square.accessible
    #print(floorPlan)
    # print(floorPlan)
    # print(floorPlan)
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
    print(floorPlan)
    for i in range(len(minPath)):
        print(minPath[i])
        if i + 1 != len(minPath):
           # continue
            print("↓")
        else:
            last = minPath[i]
            if not switchFloor:
                #continue
                print("You've arrived at the " + destinationName + "!")
    if switchFloor:
        for squareType in allSquares.keys():
            for square in allSquares[squareType]:
                x = square.x
                y = square.y
                if (x, y) == last:
                    if level == 0:
                        return main((square.switchX, square.switchY), destinationName, 1, HuangCenter, accessible, minPath + [(-1, 1)])
                    else:
                        return main((square.switchX, square.switchY), destinationName, 0, HuangCenter, accessible, minPath + [(-1, 0)])
    print(sofar + minPath)
    return sofar + minPath



if __name__ == '__main__':
    #main((15, 2), "Cafe Kitchen", 1, generateHuang(), False, []) #DEMO
    #main((15, 2), "lower", 1, generateHuang(), True, [])
    #main((15, 42), 'stair', 0, generateHuang(), False, [])
    #main((15, 2), 'NVIDIA', 1, generateHuang(), False, [])
    main((15, 2), 'NVIDIA', 1, generateHuang(), True, [])
    #main((30, 34), "NVIDIA", 0, HuangCenter, False, [])
    #main((15, 2), 'bathroom', 1, HuangCenter, True, [])