import sys
import random

class bots:
    def addShips(self, ships):
        for ship in ships:
            ships = self.addShip(ships, ship)
        return ships


    def addShip(self, ships, ship):
        neighborFail = 0
        while True:
            coordinates = self.getCoordinates(ship['size'])
            if self.invalidCoordinates(coordinates):
                continue
            if self.duplicateCoordinates(ships, coordinates):
                continue
            if self.edgeCoordinates(coordinates):
                continue
            if neighborFail < 100000:
                if self.neighbor(ships, coordinates):
                    neighborFail += 1
                    continue
            ship['coordinates'] = coordinates
            # print(coordinates)
            return ships


    def getCoordinates(self, size):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        coordinates = [ [ x, y ] ]
        direction = random.choice([ [ 0, -1 ], [ 1, 0 ], [ 0, 1 ], [ -1, 0 ] ])
        for _ in range(size - 1):
            x += direction[0]
            y += direction[1]
            coordinates.append([ x, y ])
        return coordinates


    def duplicateCoordinates(self, ships, coordinates):
        for coordinate in coordinates:
            for ship in ships:
                if 'coordinates' not in ship:
                    continue
                for shipCoordinate in ship['coordinates']:
                    if coordinate == shipCoordinate:
                        return True
        return False


    def neighbor(self, ships, coordinates):
        for coordinate in coordinates:
            for ship in ships:
                if 'coordinates' not in ship:
                    continue
                for shipCoordinate in ship['coordinates']:
                    if coordinate[0] + 1 == shipCoordinate[0] and coordinate[1] == shipCoordinate[1]:
                        return True
                    if coordinate[0] - 1 == shipCoordinate[0] and coordinate[1] == shipCoordinate[1]:
                        return True
                    if coordinate[1] + 1 == shipCoordinate[1] and coordinate[0] == shipCoordinate[0]:
                        return True
                    if coordinate[1] - 1 == shipCoordinate[1] and coordinate[0] == shipCoordinate[0]:
                        return True
        return False


    def invalidCoordinates(self, coordinates):
        for coordinate in coordinates:
            if coordinate[0] < 0 or coordinate[0] > 9:
                return True
            if coordinate[1] < 0 or coordinate[1] > 9:
                return True
        return False


    def edgeCoordinates(self, coordinates):
        for coordinate in coordinates:
            if coordinate[0] == 0 or coordinate[1] == 0:
                return True
            if coordinate[0] == 9 or coordinate[1] == 9:
                return True
        return False


    def makeMove(self, misses, hits, sinks):
        if len(hits) == 0:
            return [ random.randint(0, 9), random.randint(0, 9) ]

        if len(hits) == 1:
            return random.choice(self.getSingleHitOptions(hits[0], misses, sinks))

        options = self.horizontalLineWithOptions(hits, misses, sinks)
        if len(options) > 0:
            return random.choice(options)

        # options = self.verticalLineWithOptions(hits, misses, sinks)
        # if len(options) > 0:
        #     return random.choice(options)

        options = self.getMultipleHitOptions(hits, misses, sinks)
        return random.choice(options)


    def horizontalLineWithOptions(self, hits, misses, sinks):

        # Create a key/value pair where:
        # - the key is each x value that has atleast one hit
        # - the value is the number of hits on that x line
        # By doing this we are able to determine whether there's a
        # line on the line x (eg the value would be > 1)
        # print(hits)
        horizontalLines = {}
        for hit in hits:
            if hit[0] not in horizontalLines.keys():
                horizontalLines[hit[0]] = 1
            else:
                horizontalLines[hit[0]] += 1
        print(horizontalLines)


        # Determine the x value that contains the maximum number of hits
        xValue = -1
        maxLineLength = 0
        for x in horizontalLines.keys():
            if horizontalLines[x] > 1 and horizontalLines[x] > maxLineLength:
                maxLineLength = horizontalLines[x]
                xValue = x

        if xValue == -1:
            return []


        # Determine the y value for the space prior to the beginning
        # of the line and the y value for the space at the end of the
        # line.
        print('xValue', xValue)
        minY = 10
        maxY = -1
        for hit in hits:
            if hit[0] == xValue:
                # print(hit)
                if hit[1] - 1 > -1 and hit[1] - 1 < minY:
                    minY = hit[1] - 1
                if hit[1] + 1 < 10 and hit[1] + 1 > maxY:
                    maxY = hit[1] + 1

        options = []
        if minY > -1 and minY < 10 and [ xValue, minY ] not in misses and [ xValue, minY ] not in sinks:
            options.append([ xValue, minY ])
        if maxY > -1 and minY < 10 and [ xValue, maxY ] not in misses and [ xValue, maxY ] not in sinks:
            options.append([ xValue, maxY ])

        print(options)
        return options


    def verticalLineWithOptions(self, hits, misses, sinks):
        # print(hits)
        verticalLines = {}
        for hit in hits:
            if hit[1] not in verticalLines.keys():
                verticalLines[hit[1]] = 1
            else:
                verticalLines[hit[1]] += 1

        yValue = -1
        maxLineLength = 0
        for y in verticalLines.keys():
            if verticalLines[y] > 1 and verticalLines[y] > maxLineLength:
                maxLineLength = verticalLines[y]
                yValue = y

        if yValue == -1:
            return []

        # print('yValue', yValue)
        minX = 10
        maxX = -1
        for hit in hits:
            if hit[1] == yValue:
                # print(hit)
                if hit[0] - 1 < minX:
                    minX = hit[0] - 1
                if hit[0] + 1 > maxX:
                    maxX = hit[0] + 1

        # print(minX, maxX)
        options = []
        if minX > -1 and minX < 10 and [ minX, yValue ] not in misses and [ minX, yValue ] not in sinks:
            options.append([ minX, yValue ])
        if maxX > -1 and maxX < 10 and [ maxX, yValue ] not in misses and [ maxX, yValue ] not in sinks:
            options.append([ maxX, yValue ])

        # print(options)
        return options


    def getSingleHitOptions(self, hit, misses, sinks):
        options = []

        # N
        x = hit[0]
        y = hit[1] - 1
        if y >= 0 and y <= 9 and x not in misses and x not in sinks:
            options.append([ x, y ])

        # E
        x = hit[0] + 1
        y = hit[1]
        if x >= 0 and x <= 9 and x not in misses and x not in sinks:
            options.append([ x, y ])

        # S
        x = hit[0]
        y = hit[1] + 1
        if y >= 0 and y <= 9 and x not in misses and x not in sinks:
            options.append([ x, y ])

        # W
        x = hit[0] - 1
        y = hit[1]
        if x >= 0 and x <= 9 and x not in misses and x not in sinks:
            options.append([ x, y ])

        return options


    def getMultipleHitOptions(self, hits, misses, sinks):
        options = []
        for hit in hits:
            options += self.getSingleHitOptions(hit, misses, sinks)
        return options
