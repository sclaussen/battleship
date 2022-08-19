import random
class bot1:
    def __init__(self):
        pass
       
    def anylize(self, cords):
        return {"left": cords[1], "right": 9 - (cords[1]), "up": cords[0], "down": 9 - (cords[0])}

    def addShips(self, ships):
        createdShips = []
        for ship in ships:
            continued = True
            while continued == True:
                cords = self.getShip(ship)
                val = False
                for cord in cords:
                    for createdShip in createdShips:
                        if cord in createdShip:
                            val = True
                if val == True:
                    continue
                else:
                    continued = False
                    createdShips.append(cords)
                    ships[ships.index(ship)]["coordinates"] = cords
        return ships

    def getShip(self, ship):
        length = ship["size"]
        direckey = {"right": [0, 1], "left": [0, -1], "down": [1, 0], "up": [-1, 0]}
        while True:
            directions = ["right", "left", "down", "up"]
            coordinate = [random.randint(0, 9), random.randint(0, 9)]
            info = self.anylize(coordinate)
            works = []
            for item in info.keys():
                if info[item] == 0:
                    directions.remove(item)
                    continue
                works.append(item)
            direction = random.choice(works)
            cords = []
            for j in range(length):
                c = [coordinate[0] + j * direckey[direction][0], coordinate[1] + j * direckey[direction][1]]
                if c[0] > 9 or c[1] > 9 or c[0] < 0 or c[1] < 0:
                    return self.getShip(ship)
                cords.append(c)
            return cords


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
            worksDirection = []
            for item in info.keys():
                if info[item] == 0:
                    directions.remove(item)
                    continue
                worksDirection.append(item)
            works = []
            for direction in worksDirection:
                coordinates = [coordinate[0] + direckey[direction][0], coordinate[1] + direckey[direction][1]]
                if coordinates in misses or coordinates in sinks:
                    directions.remove(direction)
                    continue
                works.append(direction)
            direction = random.choice(works)
            return [coordinate[0] + direckey[direction][0], coordinate[1] + direckey[direction][1]]

    def pursueHits(self, misses, hits, sinks):
        direckey = {"right": [0, 1], "left": [0, -1], "down": [1, 0], "up": [-1, 0]}
        contaction = []
        while True:
            if hits[0][0] == hits[1][0]:
                mini = [9, 0]
                maxi = [0, 0]
                for hit in hits:
                    if hit[0] < mini[0]:
                        mini = hit
                    if hit[0] > maxi[0]:
                        maxi = hit
                rightDistance = 9 - maxi[1]
                leftDistance = mini[1]
                if rightDistance == 0:
                    direction = "left"
                if leftDistance == 0:
                    direction = "left"
                if not leftDistance == 0 and not rightDistance == 0:
                    direction = random.choice(["left", "right"])
                if leftDistance == 0 and rightDistance == 0:
                    direction = random.choice(["up", "down"])

                if "left" in contaction and "right" in contaction:
                    cords = random.choice(hits)
                    dire = random.choice(["up", "down"])
                    if [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]] in misses or [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]] in sinks or [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]] in hits:
                        continue
                    return [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]]

                if direction == "right":
                    if [maxi[0], maxi[1] + 1] in misses or [maxi[0], maxi[1] + 1] in sinks or [maxi[0], maxi[1] + 1] in hits:
                        contaction.append("right")
                        continue
                    return [maxi[0], maxi[1] + 1]
                if direction == "left":
                    if [mini[0], mini[1] - 1] in misses or [mini[0], mini[1] - 1] in sinks or [mini[0], mini[1] - 1] in hits:
                        contaction.append("left")
                        continue
                    return [mini[0], mini[1] - 1]

            if hits[1][1] == hits[0][1]:
                mini = [9, 0]
                maxi = [0, 0]
                for hit in hits:
                    if hit[0] < mini[0]:
                        mini = hit
                    if hit[0] > maxi[0]:
                        maxi = hit
                downDistance = 9 - maxi[0]
                upDistance = mini[0]
                if downDistance == 0:
                    direction = "up"
                if upDistance == 0:
                    direction = "down"
                if not upDistance == 0 and not downDistance == 0:
                    direction = random.choice(["down", "up"])
                if upDistance == 0 and downDistance == 0:
                    direction = random.choice(["left", "right"])

                if "up" in contaction and "down" in contaction:
                    cords = random.choice(hits)
                    dire = random.choice(["left", "right"])
                    if [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]] in misses or [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]] in sinks or [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]] in hits:
                        continue
                    return [cords[0] + direckey[dire][0], cords[1] + direckey[dire][1]]

                if direction == "down":
                    if [maxi[0] + 1, maxi[1]] in misses or [maxi[0] + 1, maxi[1]] in sinks or [maxi[0] + 1, maxi[1]] in hits:
                        contanction.append("down")
                        continue
                    return [maxi[0] + 1, maxi[1]]
                if direction == "up":
                    if [mini[0] - 1, mini[1]] in misses or [mini[0] - 1, mini[1]] in sinks or [mini[0] - 1, mini[1]] in hits:
                        contaction.append("up")
                        continue
                    return [mini[0] - 1, mini[1]]

    def guess(self, misses, hits, sinks):
        while True:
            coordinate = [random.randint(1, 9), random.randint(1, 9)]
            if coordinate in misses or coordinate in sinks:
                continue

            if coordinate[1] % 2 == coordinate[0] % 2:
                return coordinate
            else:
                continue

