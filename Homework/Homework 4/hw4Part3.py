
#import
import hw4_util


#finf university function
def find_university(data, uname):
    pos = 2000
    for slist in data:
        if slist[0] == uname:
            pos  = slist[1]
    return pos


#importing data
data = hw4_util.read_university_file("university_data.csv")


#inputs
name = input('University name => ')
print(name)
your = find_university(data, name)
uni1 = int(input('Line number for first university to compare (1-1000) => '))
print(uni1)
uni2 = int(input('Line number for second university to compare (1-1000) => '))
print(uni2)


#data display
if your == 2000:
    print('University not found')
else:
    print('First university:', data[uni1][0])
    print('Second university:', data[uni2][0])    
    print('')
    print("{0:>25}{1:>12}{2:>12}{3:>12}".format('', 'First', 'Second', 'Yours'))
    i = 1
    while i < len(data[0]):
        print("{0:>25}{1:>12}{2:>12}{3:>12}".format(data[0][i], data[uni1][i], data[uni2][i], data[your][i]))
        i += 1    

