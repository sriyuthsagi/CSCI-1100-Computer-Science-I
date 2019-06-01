
line = []
for i in range(9):
  line.append(i)
"""
w = 0
for i in range(9):
  z = 0
  if w == 3:
    print('\n')
    w = 0  
  for y in range(9):
    if z == 3:
      print('   ', end='')
      z = 0
    print(line[i], ',', line[y], sep = "", end =" ")
    z += 1
  print('')
  w += 1
  
  
print('')
  """

x = (int(input('Input x =>')))
y = (int(input('Input y =>')))
x = 3*x
y = 3*y
for i in range(3):
  for j in range(3):
    print(line[i+y], ',', line[j+x], sep = "", end =" ")
  print('')
  
"""



for y in range(3):
  y = 3*y
  for x in range(3):
    for i in range(3):
      for j in range(3):
        print(line[i+y], ',', line[j+x], sep = "", end =" ")
      print('   ', end='') 
  print('')
  
  
  
  
  
  
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
         [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
         [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
         [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
         [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
         [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
         [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
         [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
         [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]
print(25*'-', sep='')
for y in range(3):
  y = 3*y
  for x in range(3):
    print('| ', end="")
    for i in range(3):
      for j in range(3):
        print(bd[i+y][j+x], sep = "", end =" ")
      print('| ', end="")
    print('') 
  print(25*'-', sep='')
  """