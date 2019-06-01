import lab05_util
import webbrowser


def findrest(lst):
    print('{} ({})'.format(lst[0], lst[5]))
    lst[3] = lst[3].split("+")
    print('\t {} \n \t {}'.format(lst[3][0], lst[3][1]))
    if len(lst[6]) > 3:
        average = (sum(lst[6]) - min(lst[6]) - max(lst[6])) / (len(lst[6]) - 2)
    else:
        average = sum(lst[6])/len(lst[3])
    if average > 4:
        print('This restaurant is rated very good, based on {} reviews.'.format(len(lst[6])))
    elif average > 3:
        print('This restaurant is rated above average, based on {} reviews.'.format(len(lst[6])))
    elif average > 2:
        print('This restaurant is rated average, based on {} reviews.'.format(len(lst[6])))
    else:
        print('This restaurant is rated bad, based on {} reviews.'.format(len(lst[6])))        


restaurants = lab05_util.read_yelp('yelp.txt')

rid = int(input('Enter restaurant ID => '))

if rid > (len(restaurants)-1) or rid < 0:
    print('This ID is invalid')
else:
    findrest(restaurants[rid])
    choice = int(input('What would you like to do next? \n1. Visit the homepage \n2. Show on Google Maps \n3. Show directions to this restaurant \nYour choice (1-3)? ==>'))
    if choice == 1:
        webbrowser.open(restaurants[rid][4])
    if choice == 2:
        webbrowser.open('http://www.google.com/maps/place/{}'.format(restaurants[3][3]))
    if choice == 3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street, Troy NY/{}'.format(restaurants[3][3]))    