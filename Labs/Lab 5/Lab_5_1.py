import lab05_util


def findrest(lst):
    print('{} ({})'.format(lst[0], lst[5]))
    lst[3] = lst[3].split("+")
    print('\t {} \n \t {}'.format(lst[3][0], lst[3][1]))
    average = sum(lst[6]) / (len(lst[6]))
    print('Average Score: {:.2f}'.format(average))


restaurants = lab05_util.read_yelp('yelp.txt')

findrest(restaurants[0])
print('')
findrest(restaurants[4])