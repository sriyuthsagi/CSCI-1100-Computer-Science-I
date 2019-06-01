def parse_line(string):
    if string.count('/') < 3:
        return None    
    splt = string.split('/')
    if not splt[-3].isdigit() or not splt[-2].isdigit() or not splt[-1].isdigit():
        return None
    combine = '/'.join(splt[0:-3])
    result = (int(splt[-3]), int(splt[-2]), int(splt[-1]), combine)
    return result




print(parse_line('Here is some random text, like 5/4=3./12/3/4'))

"""
Here is some random text, like 5/4=3./12/3/4
"""