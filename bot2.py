import random

class bot2:
    def addShips(self, ships):
        for ship in ships:
            if ship['name'] == 'carrier':
                ship['coordinates'] = [ [ 0, 0 ], [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 0, 4 ]]
            if ship['name'] == 'battleship':
                ship['coordinates'] = [ [ 1, 0 ], [ 1, 1 ], [ 1, 2 ], [ 1, 3 ] ]
            if ship['name'] == 'submarine':
                ship['coordinates'] = [ [ 2, 0 ], [ 2, 1 ], [ 2, 2 ] ]
            if ship['name'] == 'cruiser':
                ship['coordinates'] = [ [ 3, 0 ], [ 3, 1 ], [ 3, 2 ] ]
            if ship['name'] == 'destroyer':
                ship['coordinates'] = [ [ 4, 0 ], [ 4, 1 ] ]
        return ships

    def makeMove(self, misses, hits, sinks):
        return [ random.randint(0, 9), random.randint(0, 9) ]
