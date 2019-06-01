
# functions
# DROP function
def drop(word):
    l = list(word)
    letterset = set()
    for i in range(len(l)):
        l = list(word)
        l.pop(i)
        trial = ''.join(l)
        if trial in dicti:
            letterset.add(trial)
    dropped = sorted(letterset)
    if len(dropped) > 0:
        return dropped[0]

# SWAP function
def swap(word):
    l = list(word)
    letterset = set()
    for i in range(len(l)-1):
        l = list(word)
        l[i], l[i+1] = l[i+1], l[i]
        trial = ''.join(l)
        if trial in dicti:
            letterset.add(trial)
    swapped = sorted(letterset)
    if len(swapped) > 0:
        return swapped[0]

# REPLACE function
def replace(word):
    l = list(word)
    letterset = set()
    letter = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z' ]
    for i in range(len(l)):
        l = list(word)
        for character in letter:
            l[i] = character
            trial = ''.join(l)
            if trial in dicti:
                letterset.add(trial)
    replaced = sorted(letterset)
    if len(replaced) > 0:
        return replaced[0] 






# inputs
file1 = input('Dictionary file => ')
print(file1)
file2 = input('Input file => ')
print(file2)
file1 = open(file1)
file2 = open(file2)

# dictionary set
dicti = set()
for word in file1:
    word = word.strip('\n')
    dicti.add(word)

# autocorrect
for word in file2:
    word = word.strip('\n')
    if word in dicti:
        print('{0:15} -> {0:15} :FOUND'.format(word))
    elif drop(word) in dicti:
        print('{0:15} -> {1:15} :DROP'.format(word, drop(word)))
    elif swap(word) in dicti:
        print('{0:15} -> {1:15} :SWAP'.format(word, swap(word)))
    elif replace(word) in dicti:
        print('{0:15} -> {1:15} :REPLACE'.format(word, replace(word)))
    else:
        print('{0:15} -> {0:15} :NO MATCH'.format(word))