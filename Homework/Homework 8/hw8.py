from Person import *
from Universe import *
import json





data = input('Input file => ')

print(data)
data = json.loads(open(data).read())


print('All universes\n----------------------------------------')
universe = universe(data[0]['universe_name'], data[0]['rewards'], data[0]['portals'])
print(universe)
rewards = universe.prewards()
portals = universe.pportals()
for i in range(len(rewards)):
    print(rewards[i])
for i in range(len(portals)):
    print(portals[i])
    
    
print('\nAll individuals\n----------------------------------------')
people =[]
for i in range(len(data[0]['individuals'])):
    people.append(person(data[0]['individuals'][i][0], data[0]['individuals'][i][1], data[0]['universe_name'], data[0]['individuals'][i][2], data[0]['individuals'][i][3], data[0]['individuals'][i][4], data[0]['individuals'][i][5], data[0]['universe_name'], [], 0))
for i in range(len(people)):
    print(people[i])


print('\nStart simulation\n----------------------------------------')

ending = len(people)
step = 1
while ending == False:
    for i in people:
        for j in universe.rewards:
            if i.rewardcheck(j):
                i.addreward(j)
                i.sumreward()
                
                print(i.rewardprint(j, step))
                print(i, '\n')
                
        i.newlocation()
        
    
    step += 1      
        
    
    
    




print('\n----------------------------------------\nSimulation stopped at step', step)
print('0 individuals still moving')
print('Winners:')
winner = []
pointtotals = []
for i in people:
    pointtotals.append(i.points)
winning = max(pointtotals)
for i in people:
    if i.points == winning:
        winner.append(i)
winner = [people[0]]
for i in winner:
    print(i)
    print('Rewards:')
if len(winner) == 1:
    print(people[0].rewards)