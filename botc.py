import random
class bot1:
    def __init__(self):
        pass
       
    def anylize(self, cords):
        return {"left": cords[1], "right": 9 - (cords[1]), "up": cords[0], "down": 9 - (cords[0])}

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
        info = self.anylize(cords)
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

    def makeMove(self, misses, hits, sinks):
        if hits != []:
            if len(hits) == 1:
                return self.pursueHit(misses, hits, sinks)

            if len(hits) > 1:
                return self.pursueHits(misses, hits, sinks)
        else:
            return self.guess(misses, hits, sinks)

    def pursueHit(self, misses, hits, sinks):
        direckey = {"right": [0, 1], "left": [0, -1], "down": [1, 0], "up": [-1, 0]}
        while True:
            directions = ["right", "left", "down", "up"]
            coordinate = hits[0]
            info = self.anylize(coordinate)
            for item in info.keys():
                if info[item] == 0:
                    directions.remove(item)
            works = []
            for direction in directions:
                coordinates = [coordinate[0] + direckey[direction][0], coordinate[1] + direckey[direction][1]]
                if coordinates in misses or coordinates in sinks:
                    directions.remove(direction)
                    continue
                works.append(direction)
            direction = random.choice(works)
            return [coordinate[0] + direckey[direction][0], coordinate[1] + direckey[direction][1]]

    def pursueHits(self, misses, hits, sinks):
        direckey = {"right": [0, 1], "left": [0, -1], "down": [1, 0], "up": [-1, 0]}
        if hits[0][0] == hits[1][0]:
            mini = 10000
            maxi = 0
            for hit in hits:
                if hit[1] < mini[1]:
                    mini = hit
                if hit[1] > maxi[1]:
                    maxi = hit
            rightDistance = 9 - maxi[1]
            leftDistance = mini[1]
            if rightDistance == 0:
                direction = "left"
            elif leftDistance == 0:
                direction = "right"
            else:
                direction = random.choice(["right", "left"])
            if direction == "right":
                return [maxi[0], maxi[1] + 1]
            else:
                return [maxi[0], maxi[1] - 1]
        if hits[1][1] == hits[0][1]:
            mini = [9, 0]
            maxi = [0, 0]
            for hit in hits:
                if hit[0] < mini[0]:
                    mini = hit
                if hit[0] > maxi[0]:
                    maxi = hit
            rightDistance = 9 - maxi[0]
            leftDistance = mini[0]
            if rightDistance == 0:
                direction = "left"
            elif leftDistance == 0:
                direction = "right"
            else:
                direction = random.choice(["right", "left"])
            if direction == "right":
                return [maxi[0] + 1, maxi[1]]
            else:
                return [maxi[0] - 1, maxi[1]]

    def guess(self, misses, hits, sinks):
        while True:
            coordinate = [random.randint(1, 9), random.randint(1, 9)]
            if coordinate in misses or coordinate in sinks:
                continue

            if coordinate[1] % 2 == coordinate[0] % 2:
                return coordinate
            else:
                continue

cbot = bot1()
print(cbot.makeMove([[1, 1]], [[1, 2]], []))