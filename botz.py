import random
from tkinter import Y
from weakref import WeakSet
class bot1:
    def __init__(self):
        pass


    def addShips(self, ships):
        for ship in ships:
            value = False
            while value == False:
                x, y = getrandomcoordinates()
                direction = getrandomdirection(x, y, ship['size'])
                coords = getcoordinatesofship(x, y, direction, ship['size'])
                value = checkcoordinates(coords, ships)
                if value == True:
                    ship['coordinates']=coords

        return ships

    def makeMove(self, misses, hits, sinks):

        if misses == [] and hits == [] and sinks == []:
            return [ random.randint(0, 9), random.randint(0, 9) ]

        if hits == []:
            value = False
            while(value == False):
                x, y = getrandomcoordinates()
                value = checkcoordinatesIn(misses, sinks, [x, y])
            
            return [x,y]

        return getNextHit(hits, misses, sinks)


def getNextHit(hits, misses, sinks):
    hitsLen = len(hits)
    
    # vertical
    if (hitsLen > 1) and (hits[0][0] == hits[1][0]):
        # south
        nextHit = [hits[hitsLen-1][0], hits[hitsLen-1][1]+1]
        if (nextHit not in misses and nextHit not in sinks):
            return nextHit
        # north
        nextHit = [hits[0][0], hits[0][1]-1]
        if (nextHit not in misses and nextHit not in sinks):
            return nextHit
        # 2 adjacent ships
      # TODO consider the case where the 2 ships are adjacent and there is 1 hit on each

    # horizontal
    if (hitsLen > 1) and (hits[0][1] == hits[1][1]):
        # east
        nextHit = [hits[hitsLen-1][0]+1, hits[hitsLen-1][1]]
        if (nextHit not in misses and nextHit not in sinks):
            return nextHit
        # west
        nextHit = [hits[0][0]-1, hits[0][1]]
        if (nextHit not in misses and nextHit not in sinks):
            return nextHit
      # TODO consider the case where the 2 ships are adjacent and there is 1 hit on each

    nextHit = [hits[0][0], hits[0][1]+1]
    if (nextHit not in misses and nextHit not in sinks):
        return nextHit
    nextHit = [hits[0][0], hits[0][1]-1]
    if (nextHit not in misses and nextHit not in sinks):
        return nextHit
    nextHit = [hits[0][0]+1, hits[0][1]]
    if (nextHit not in misses and nextHit not in sinks):
        return nextHit
    nextHit = [hits[0][0]-1, hits[0][1]]
    if (nextHit not in misses and nextHit not in sinks):
        return nextHit



def checkcoordinatesIn(misses, sinks, coord):
    if inList(coord, misses) or inList(coord,sinks):
        return False

    return True


def checkcoordinates(coords, ships):
    for ship in ships:
        if 'coordinates' in ship and isSubset(coords, ship['coordinates']):
            return False

    return True

def inList(coord, coordinates):

    if coordinates == []:
        return False

    for coordinate in coordinates:
        if coord[0] == coordinate[0] and coord[1] == coordinate[1]:
            return True
    return False

def isSubset(coords, coordinates):
    if coordinates == []:
        return False
    for coord in coords:
        for coordinate in coordinates:
            if coord[0] == coordinate[0] and coord[1] == coordinate[1]:
                return True
    return False

def getcoordinatesofship(x, y, dir, size):

    coords = [[x,y]]
    if dir == 0: #west
        while size > 1:
            x = x - 1
            size = size - 1
            coords.append([x, y])
        return coords

    if dir == 1: #south
        while size > 1:
            y = y + 1
            size = size - 1
            coords.append([x, y])
        return coords

    if dir == 2: #east
        while size > 1:
            x = x + 1
            size = size - 1
            coords.append([x, y])
        return coords

    if dir == 3: #north
        while size > 1:
            y = y - 1
            size = size - 1
            coords.append([x, y])
        return coords


def getrandomcoordinates():
    x = random.randint(0, 9)
    y = random.randint(0, 9)

    print("random coord: ", x, y)
    return x,y

def getrandomdirection(x, y, size):
    if x - size < -1 and y - size < -1:
        direction = random.randint(1, 2)
        return direction
    if x + size > 9 and y + size > 9:
        direction = 0
        return direction
    if x - size < -1 and y + size > 9:
        direction = random.randint(2, 3)
        return direction
    if x + size > 9 and y - size < -1:
        direction = random.randint(0, 1)
        return direction
    if x - size < -1:
        direction = random.randint(1, 3)
        return direction
    if y - size < -1:
        direction = random.randint(0, 2)
        return direction
    if x + size > 9:
        direction = random.randint(0, 1)
        return direction
    if y + size > 9:
        direction = random.randint(2, 3)
        return direction
    return random.randint(0,3)


