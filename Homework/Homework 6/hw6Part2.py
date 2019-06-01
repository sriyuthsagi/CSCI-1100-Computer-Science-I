
# imports and functions
import textwrap

# title function
def title(l, title):
    for i in range(len(l)):
        if title.lower() in l[i][0].lower():
            return l[i][0]

# return list function
def beastlist(l, title):
    for i in range(len(l)):
        if title.lower() in l[i][0].lower():
            return l[i][1:]

# unique list function
def unique(l1, l2, title):
    for i in range(len(l1)):
        if l1[i][0] != title:
            only= l1[i][1:]
            for j in range(len(only)):
                if only[j] in l2:
                    l2.remove(only[j])
    return l2          

# similar list function
def same(l, title, beastset):
    titles= []
    for i in range(len(l)):
        beast_set2 = set()
        if title.lower() != l[i][0].lower():
            for j in range(1, len(l[i])):
                beast_set2.add(l[i][j].strip())
        if beastset & beast_set2 != set() and title != l[i][0]:
            titles.append(l[i][0])
    return titles

# textwrap function
def text(l, string):
    l_sort = l.sort()
    blank = ''
    blank += string
    blank += ', '.join(l)
    line = textwrap.wrap(blank)
    for i in range(len(line)):
        print(line[i])







#list of titles and beasts
moviel= []
for line in open('titles.txt'):
    movies = line.strip().split('|')
    moviel.append(movies)
    
# main code: input => check for end => return results
while True:
    title = input('Enter a title (stop to end) => ')
    print(title)
    print()
    if title == 'stop':
        break
    elif title(moviel, title) != None:
        name = title(moviel, title)
        print('Found the following title: {}'.format(name))
        beastset = set(beastlist(moviel, name))
        beastset1 = sorted(beastset)
        text(beastset1, 'Beasts in this title: ')
        print()
        similar = same(moviel, name, beastset)
        text(similar, 'Other titles containing beasts in common: ')
        print()
        only = unique(moviel, beastset1, name)
        text(only, 'Beasts appearing only in this title: ')
        print()
    else:
        print('This title is not found!')
            
