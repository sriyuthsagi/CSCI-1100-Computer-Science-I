
def get_words(string):
    string = string.lower()
    string = string.replace('.', ' ').replace(',', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ')
    ls = string.split('|')
    lst = ls[1].split(' ')
    count = 0
    lst1 = []
    for i in range(len(lst)):
        if len(lst[i]) >= 4:
            count += 1
            lst1.append(lst[i])
    return [count, lst1]






file1 = 'wrpi.txt'
file1 = open(file1)
file1 = file1.readline()
result1 =get_words(file1)[1]

file2 = 'allclubs.txt'
string = []
for line in open(file2):
    line = line.split('\n')
    string.append(line[0])


clubs = []
clubname = []
for value in range(len(string)):
    clubs.append(get_words(string[value])[1])
    clubname.append(string[value].split('|')[0])


intersects = []
for i in range(len(clubs)):
    intersects.append(len(list(set(result1).intersection(clubs[i]))))


highest = []
for j in range(6):
    high = intersects.index(max(intersects))
    highest.append(high)
    intersects.pop(high)

for k in range(5):
    print(clubname[highest[k+1]])





"""
file1 = 'wrpi.txt'
file2 = 'csa.txt'
name1 = file1[0:-4]
name2 = file2[0:-4]
print('Comparing clubs ', name1, ' and ', name2, ':', sep ='')
result1 =get_words(file1)[1]
result2 =get_words(file2)[1]
print('')
intersect = list(set(result1).intersection(result2))
print(intersect)
for i in range(len(intersect)):
    result1.remove(intersect[i])
    result2.remove(intersect[i])
print('')
print('Unique to ', name1, ': ', result1, sep='')
print('')
print('Unique to ', name2, ': ', result2, sep='')
"""