def parse_line(string):
    if string.count('/') < 3:
        return None    
    splt = string.split('/')
    if not splt[-3].isdigit() or not splt[-2].isdigit() or not splt[-1].isdigit():
        return None
    combine = '/'.join(splt[0:-3])
    result = (int(splt[-3]), int(splt[-2]), int(splt[-1]), combine)
    return result

def get_line(fname,parno,lineno):
    fname = str(fname)+'.txt'
    file = open(fname)
    text = []
    k = 1
    while k == 1:
        text.append(file.readline().split('\n'))
        if text[-1] == ['']:
            text.pop()
            break
    for i in range(len(text)):
        text[i] = text[i][0]
    parac = 1
    for i in range(len(text)):
        if text[i] == '':
            if not text[i+1] == '' and not text[x-1] == '':
                parac += 1
            if parac == parno:
                linen = i
                break
    result = text[linen+ lineno]
    return result
    

x = int(input('File = '))
y = int(input('Para = '))
z = int(input('Line = '))



print(get_line(x, y, z))