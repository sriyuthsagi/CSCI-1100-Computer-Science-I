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



bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
         [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
         [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
         [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
         [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
         [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
         [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
         [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
         [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]
  
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
  



entery = int(input('Enter a row => '))
enterx = int(input('Enter a column => '))
enter = input('Enter a number => ')

print(ok_to_add(bd, enterx, entery, enter))
