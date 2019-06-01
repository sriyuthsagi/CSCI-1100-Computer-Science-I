
#input
word = input('Word => ')
print(word)
column = int(input('#columns => '))
print(column)
row = int(input('#rows => '))
print(row)
print('Your word is: ', word, '\n', sep="")
#extra variables
column1 = column - 1
columnchar = '*** ' * column1 + '***' + '\n'
centercol = int((column / 2) + 0.5)
centerrow = int((row / 2) + 0.5)
row1 = row - centerrow
col1 = column - centercol
row2 = row1 - 1
col2 = col1 - 1


#part a
print('(a)')
print(columnchar*row)


#part b
print('(b)')
print(columnchar * row1, '*** '*col1, 'CS1 ', '*** '*col2, '***', '\n', columnchar * row1, sep="")


#part c
print('(c)')
print('*** '*col1, ' |  ', '*** '*col2, '***', '\n', columnchar * row2, ' |  ', '*** '*col2, 'CS1 ', '*** '*col2, ' | ', '\n', columnchar * row2, '*** '*col1, ' |  ', '*** '*col2, '***', sep="")