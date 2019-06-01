
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
    return [count, set(lst1)]









file = 'wrpi.txt'
print('File', file, get_words(file)[0], 'words')
print(get_words(file)[1])
