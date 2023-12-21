import sys
import random
import traceback

# import botc
import botz
import bots

GAMES = 500

def main():
    wins = [
        {
            'name': 'zeenat',
            'wins': 0
        },
        {
            'name': 'shane',
            'wins': 0
        }
    ]
    games = 1
    while games <= GAMES:
        players = initPlayers()
        placeShips(players)
        printShips(players[0])
        printShips(players[1])

        # Randomize who goes first
        player = nextPlayer(random.choice([0, 1]))

        while True:
            if makeMove(players[player[0]], players[player[1]]):
                wins[player[0]]['wins'] += 1
                break
            player = nextPlayer(player[0])

        games += 1

    print(wins[0]['name'], wins[0]['wins'])
    print(wins[1]['name'], wins[1]['wins'])
    print(wins[0]['wins'] / wins[1]['wins'] * 100)


def nextPlayer(playerNumber):
    if playerNumber == 0:
        return [ 1, 0 ]
    return [ 0, 1 ]


def placeShips(players):
    for player in players:

        # Get bot ship placements
        ships = player['bot'].addShips(player['ships'])

        # Verify all ship placement coordinates
        coordinates = []
        for ship in ships:

            if len(ship['coordinates']) != ship['size']:
                print('ERROR: wrong number of coordinates: ', ship['name'], ship['size'], ship['coordinates'])
                sys.exit(1)

            for coordinate in ship['coordinates']:
                if coordinate in coordinates:
                    print('ERROR: duplicate ship coordinate: ', ship['name'], coordinate)
                    sys.exit(1)
                if coordinate[0] < 0 or coordinate[0] > 9:
                    print('ERROR: invalid x coordinate: ', ship['name'], coordinate)
                    sys.exit(1)
                if coordinate[1] < 0 or coordinate[1] > 9:
                    print('ERROR: invalid y coordinate: ', ship['name'], coordinate)
                    sys.exit(1)

                coordinates.append(coordinate)

        player['ships'] = ships


def makeMove(player, opponent):

    # Get coordinate guess from player
    coordinate = player['bot'].makeMove(player['misses'], player['hits'], player['sinks'])

    # If the guess was a duplicate, go to the next player
    # TODO: Combine these three sets on the stack here
    if coordinate[0] < 0 or coordinate[0] > 9:
        print('ERROR: invalid x coordinate in guess: ', coordinate)
        sys.exit(1)
    if coordinate[1] < 0 or coordinate[1] > 9:
        print('ERROR: invalid y coordinate in guess: ', coordinate)
        sys.exit(1)
    if coordinate in player['misses']:
        print(player['name'], coordinate, ' duplicate miss')
        return False
    if coordinate in player['hits']:
        print(player['name'], coordinate, ' duplicate hit')
        return False
    if coordinate in player['sinks']:
        print(player['name'], coordinate, ' duplicate sunk')
        return False

    # Go through all opponent ships
    hit = False
    for ship in opponent['ships']:

        # If the guess was a hit...
        if coordinate in ship['coordinates']:

            hit = True
            ship['hits'] += 1
            player['hits'].append(coordinate)
            print(player['name'], coordinate, ' hit')

            # Did the guess sink the ship?
            if ship['hits'] == ship['size']:
                print(player['name'], coordinate, ' sunk', ship['size'])
                for coordinate in ship['coordinates']:
                    player['hits'].remove(coordinate)
                    player['sinks'].append(coordinate)
                player['sunkShips'] += 1
                if player['sunkShips'] == 5:
                    return True

    if not hit:
        print(player['name'], coordinate, ' miss')
        player['misses'].append(coordinate)

    return False


def printShips(player):
    print("   ", end="")
    # for column in [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ]:
    for column in [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]:
        print(column, end=" ")
    print()

    for y in range(0, 10):
        # if y < 9:
        print("", y, end=" ")
        # else:
        #     print(y, end=" ")
        for x in range(0, 10):
            shipFound = False
            for ship in player['ships']:
                for coordinate in ship['coordinates']:
                    if coordinate[0] == x and coordinate[1] == y:
                        shipFound = True
                        print(ship['initials'], end=" ")
            if not shipFound:
                print(".", end=" ")
        print()
    print()


def initPlayers():
    return [
        {
            'name': 'zeenat',
            'bot': botz.bot1(),
            'sunkShips': 0,
            'ships': [
                {
                    'name': 'carrier',
                    'initials': 'C',
                    'size': 5,
                    'hits': 0
                },
                {
                    'name': 'battleship',
                    'initials': 'B',
                    'size': 4,
                    'hits': 0
                },
                {
                    'name': 'submarine',
                    'initials': 'S',
                    'size': 3,
                    'hits': 0
                },
                {
                    'name': 'cruiser',
                    'initials': 'R',
                    'size': 3,
                    'hits': 0
                },
                {
                    'name': 'destroyer',
                    'initials': 'D',
                    'size': 2,
                    'hits': 0
                },
            ],
            'misses': [],
            'hits': [],
            'sinks': [],
        },
        {
            'name': 'shane',
            'bot': bots.bots(),
            'sunkShips': 0,
            'ships': [
                {
                    'name': 'carrier',
                    'initials': 'C',
                    'size': 5,
                    'hits': 0
                },
                {
                    'name': 'battleship',
                    'initials': 'B',
                    'size': 4,
                    'hits': 0
                },
                {
                    'name': 'submarine',
                    'initials': 'S',
                    'size': 3,
                    'hits': 0
                },
                {
                    'name': 'cruiser',
                    'initials': 'R',
                    'size': 3,
                    'hits': 0
                },
                {
                    'name': 'destroyer',
                    'initials': 'D',
                    'size': 2,
                    'hits': 0
                },
            ],
            'misses': [],
            'hits': [],
            'sinks': [],
        }
    ]


main()
