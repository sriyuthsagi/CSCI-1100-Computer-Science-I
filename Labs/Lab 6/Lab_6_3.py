import lab06_util

def ok_to_add(data, x, y, z):
  if not data[y][x] == '.':
    return False
  for v in data:
    if v[x] == z:
        return False
  for v in range(9):
    if data[v][y] == z:
        return False
  x1 = 3*(x // 3)
  y1 = 3*(y // 3)
  for i in range(3):
    for j in range(3):
      if data[j+x1][i+y1] == v:
        return False
  return True



file = input('Input file =>')
bd = lab06_util.read_sudoku(file)
correct = lab06_util.read_sudoku('solved.txt')

print(25*'-', sep='', end='')
w = 0
for i in range(9):
  z = 0
  if w == 3:
    print('\n', 25*'-', sep='', end='')
    w = 0  
  print('\n| ', end='')
  for y in range(9):
    if z == 3:
      print('| ', end="")
      z = 0
    print(bd[i][y], sep = "", end=" ")
    z += 1
  print('| ', end="")
  w += 1
print('\n', 25*'-', sep='', end='')
print('')

while not bd == correct:
  entery = int(input('Enter a row => '))
  enterx = int(input('Enter a column => '))
  enter = input('Enter a number => ')
  if ok_to_add(bd, enterx, entery, enter):
    bd[entery][enterx] = enter
  else:
    print('This value does not work')  
  print(25*'-', sep='', end='')
  w = 0
  for i in range(9):
    z = 0
    if w == 3:
      print('\n', 25*'-', sep='', end='')
      w = 0  
    print('\n| ', end='')
    for y in range(9):
      if z == 3:
        print('| ', end="")
        z = 0
      print(bd[i][y], sep = "", end=" ")
      z += 1
    print('| ', end="")
    w += 1
  print('\n', 25*'-', sep='', end='')
  print('')