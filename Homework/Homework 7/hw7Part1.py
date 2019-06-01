

def read_file(file):
    file = open(file)
    file = file.read().split('\n')
    return file


def file_to_dict(file):
    file = read_file(file)
    i = 0
    while i < len(file):
        file[i] = file[i].split(',')
        i += 1
    file.pop()
    words = dict()
    for item in file:
        words[item[0]] = item[1]
    return (words)


def keyboard_file_to_dict(file):
    file = read_file(file)
    i = 0
    while i < len(file):
        file[i] = file[i].split(' ')
        i += 1
    replace = dict()
    i = 0
    while i < len(file):
        j = 1
        keys = []
        while j < len(file[i]):
            keys.append(file[i][j])
            j += 1
        replace[file[i][0]] = keys
        i += 1
    return (file)


def file_to_list(file):
    file = read_file(file)
    file = list(file)
    if '' in file:
        file.remove('')
    return (file)




def found(listfile, dictionary, indexlist):
    i = 0
    while i < len(listfile):
        indexlist.append(0)
        if listfile[i] in dictionary:
            indexlist[i] = 1
        i += 1
    return listfile, indexlist


def drop(listfile, dictionary, indexlist, wordfre):
    i = 0
    while i < len(listfile):
        if indexlist[i] != 1:
            j = 0
            for charecter in listfile[i]:
                newlistfile = listfile[i][:j] + listfile[i][j+1:]
                if newlistfile in dictionary:
                    wordfre[listfile[i]].append((dictionary[newlistfile], newlistfile))
                    if indexlist == 0:
                        indexlist[i] = 2
                    else:
                        indexlist[i] += 1
                j += 1
        i += 1
    return listfile, indexlist


def swap(listfile, dictionary, indexlist):
    i = 0
    while i < len(listfile):
        if indexlist[i] != 1:
            j = 0
            for charecter in listfile[i]:
                if j == 0:
                    newlistfile = listfile[i][1] + listfile[i][0] + listfile[i][2:]
                elif j == len(listfile[1]):
                    newlistfile = listfile[i][:j-1] + listfile[i][j] + listfile[i][j-1]
                else:
                    newlistfile = listfile[i][:j-1] + listfile[i][j] + listfile[i][j-1] + listfile[i][j+1:]
                if newlistfile in dictionary:
                    wordfre[listfile[i]].append((dictionary[newlistfile], newlistfile))
                    if indexlist[i] == 0:
                        indexlist[i] = 2
                    else:
                        indexlist[i] += 1
                j += 1
        i += 1
    return listfile, indexlist



def replace(listfile, dictionary, indexlist, keyboard):
    i = 0
    while i < len(listfile):
        if indexlist[i] != 1:
            j = 0
            for charecter in listfile[i]:
                a = 0
                if charecter == ' ':
                    charecter = ''
                while a < len(keyboard[charecter]):
                    newlistfile = listfile[i][:j] + keyboard[charecter][a] + listfile[i][j+1:]
                    if newlistfile in dictionary:
                        wordfre[listfile[i]].append((dictionary[newlistfile], newlistfile))
                        if indexlist[i] == 0:
                            indexlist = 2
                        else:
                            indexlist[i] += 1
                    a += 1
                j += 1
        i += 1
    return listfile, indexlist






"""
dictionary = input('Dictionary => ')
print(dictionary)
listfile = input('Input file => ')
print(listfile)
keyboard = input('Keyboard file =. ')
print(keyboard)
"""
dictionary = 'words_10percent.txt'
listfile = 'input_words.txt'
keyboard = 'keyboard.txt'


dictionary = file_to_dict(dictionary)
listfile = file_to_list(listfile)
keyboard = keyboard_file_to_dict(keyboard)


oldlistfile = list(listfile)

indexlist = []

wordfre = dict()

for i in range(len(listfile)):
    wordfre[listfile[i]] = list()

listfile, indexlist = found(listfile, dictionary, indexlist)
listfile, indexlist = drop(listfile, dictionary, indexlist, wordfre)
listfile, indexlist = swap(listfile, dictionary, indexlist)
listfile, indexlist = replace(listfile, dictionary, indexlist, keyboard)



special = []
for word in wordfre:
    wordfre[word] = set(wordfre[word])
    wordfre[word] = list(wordfre[word])
    wordfre[word] = sorted(wordfre[word])
    special.append(len(wordfre[word]))


print('Spellcheck results:')
i = 0
while i < len(listfile):
    if special[i] < indexlist[i]:
        indexlist[i] = special[i]
    if indexlist[i] == 0:
        index = 'NO MATCH'
    elif indexlist[i] == 1:
        index = 'FOUND'
    
    if indexlist[i] < 2:
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], listfile[i], index))
    elif indexlist[i] == 2:
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], wordfre[oldlistfile[i]][-1][1], 'MATCH 1'))
    elif indexlist[i] == 3:        
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], wordfre[oldlistfile[i]][-1][1], 'MATCH 1'))
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], wordfre[oldlistfile[i]][-2][1], 'MATCH 2'))
    elif indexlist[i] == 4:          
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], wordfre[oldlistfile[i]][-1][1], 'MATCH 1'))
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], wordfre[oldlistfile[i]][-2][1], 'MATCH 2'))
        print('{0:15} -> {1:15} :{2}'.format(oldlistfile[i], wordfre[oldlistfile[i]][-3][1], 'MATCH 3'))      