#inputs
name = input('Name of robot => ')
print(name)
x = int(input('X location => '))
print(x)
y = int(input('Y location => '))
print(y)
comm = 'hi'
energy = 10

#commands
while not comm == 'end':
    print('Robot {0} is at ({1},{2}) with energy: {3}'.format(name, x, y, energy))
    comm = input('Enter a command (up/left/right/down/attack/end) => ')
    print(comm)
    comm = comm.lower()
    #different command cases
    if comm == "up":
        if energy < 1:
            energy = energy + 1 
        else:
            y = max(0, y-10)
            energy = min(energy+1, 10)
    if comm == "down":
        if energy < 1:
            energy = energy + 1 
        else:
            y = min(100, y+10)
            energy = min(energy+1, 10)
    if comm == "right":
        if energy < 1:
            energy = energy + 1  
        else:
            x = min(100, x+10)
            energy = min(energy+1, 10)
    if comm == "left":
        if energy < 1:
            energy = energy + 1  
        else:
            x = max(0, x-10)
            energy = min(energy+1, 10)
    if comm == "attack":
        if energy >= 3:
            energy -= 3