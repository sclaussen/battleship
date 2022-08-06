import random
class bot1:
    def __init__(self):
        pass

    def addShips(self, ships):
        dictships = []
        for shipName in ships:
            coordinates = False
            ship = ships[shipName]
            while coordinates == False:
                coordinates = getShip(ship, shipName)
            dictships.append({"name": shipName, "coordinates": coordinates})

    def getShip(self, ship, shipName):
        cords = [random.randint(0, 9), random.randint(0, 9)]
        info = anylize(cords)
        directions = []
        for direc in info:
            if ship["size"] <= info[direc]:
                directions.append(direc)

        direction = random.choice(directions)
        direckey = {"right": [0, 1], "left": [0, -1], "down": [1, 0], "up": [-1, 0]}
        coordinates = []
        for j in range(ship["size"]):
            coordinates.append([cords[0] + j * direckey[direction][0], cords[1] + j * direckey[direction][1]])

        for coordinate in coordinates:
            for dictship in dictships:
                if coordinate in dictship["coordinates"]:
                    return False
        return coordinates



        return dictships

    def makeMove(self, misses, hits, sinks):
        if hits != []:
            return pursueHit(misses, hits, sinks)

    def pursueHit(self, misses, hits, sinks):
        direckey = {"right": [0, 1], "left": [0, -1], "down": [1, 0], "up": [-1, 0]}
        if len(hits) == 1:
            possibleDirections = ["right", "left", "down", "up"]
            info = anylize(hits[0])
            for infokey in info.keys():
                if info[infokey] == 0:
                    possibleDirections.remove(infokey)
                    continue
                if [hits[0][0] + direckey[infokey][0], hits[0][1] + direckey[infokey][1]] in misses or [hits[0][0] + direckey[infokey][0], hits[0][1] + direckey[infokey][1]] in sinks:
                    possibleDirections.remove(infokey)
            direction = random.choice(possibleDirections)
            return [hits[0][0] + direckey[direction][0], hits[0][1] + direckey[direction][1]]
        else:
            if hits[len(hits) - 1][0] == hits[0][0]:
                info1 = anylize(hits[len(hits) - 1])
                info2 = anylize(hits[0])
                if info1["right"] <= info2["right"]:
                    rightinfo = info1
                    leftinfo = info2
                else:
                    rightinfo = info2
                    leftinfo = info1

                possibleDirections = ["left", "right"]
                if rightinfo["right"] == 0:
                    possibleDirections.remove("right")




    def anylize(self, cords):
        return {"right": cords[1], "left": 10 - (cords[1]), "down": cords[0], "up": 10 - (cords[0])}
