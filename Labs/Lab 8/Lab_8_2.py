
def get_words(file):
    file = open(file)
    string = file.readline()
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
    return [count, lst1, ls]









file1 = 'wrpi.txt'
file2 = 'csa.txt'
name1 = file1[0:-4]
name2 = file2[0:-4]
print('Comparing clubs ', name1, ' and ', name2, ':', sep ='')
result1 =get_words(file1)[1]
result2 =get_words(file2)[1]
print('')
intersect = list(set(result1).intersection(result2))
print('Same words:', set(intersect))
for i in range(len(intersect)):
    result1.remove(intersect[i])
    result2.remove(intersect[i])
print('')
print('Unique to ', name1, ': ', result1, sep='')
print('')
print('Unique to ', name2, ': ', result2, sep='')
print(len(result1))
print(len(result2))