#import hw5util and inputing then opening the file
import hw5util
file = input('Enter the filename => ')
print(file)
games, players, predictions = hw5util.read_predictions(file) 



#initial list variables
ppointlist = []
tpointlist = []
winner = []
gamepoints = []
hard = []



#calculating points
print('Player points:')
for i in range(len(players)):
    ppoints = 0
    gpointlist = []
    for j in range(len(games)):
        gpoints = 0
        x = predictions[i][j]
        y = (games[j][-2], games[j][-1])
        if y[0] > y[1] and x[0] > x[1]:
            ppoints += 2
            gpoints += 2
        elif y[1] > y[0] and x[1] > x[0]:
            ppoints += 2
            gpoints += 2
        elif y[0] == y[1] and x[0] == x[1]:
            ppoints += 2
            gpoints += 2
        if y[0] == x[0]:
            ppoints += 1
            gpoints += 1
        if y[1] == x[1]:
            ppoints += 1
            gpoints += 1
        gpointlist.append(gpoints)
    print("{0:<10}:{1:>4}".format(players[i], ppoints))
    ppointlist.append(ppoints)
    tpointlist.append(gpointlist)
print('')



#finding winner and how many points he had
mx = max(ppointlist)
for i in range(len(players)):
    if ppointlist[i] == mx:
        winner.append(players[i])
print('Winner(s): (max points: {})'.format(mx))
for i in range(len(winner)):
    print(winner[i])
print('')



#finding gamepoints
print('Game points:')
for i in range(len(games)):
    gamepoint = 0
    for j in range(len(players)):
        gamepoint = gamepoint + tpointlist[j][i]
    gamepoints.append(gamepoint)
for i in range(len(games)):
    gamename = games[i][3] + ' vs ' + games[i][4]
    print("{0:<30}:{1:>4}".format(gamename, gamepoints[i]))
print('')



#finding hardest game
mn = min(gamepoints)
for i in range(len(games)):
    if gamepoints[i] == mn:
        hard.append(games[i])
print('Hardest game(s) (min points: {})'.format(mn))
for i in range(len(hard)):
    gamename = hard[i][3] + ' vs ' + hard[i][4]
    print(gamename)
