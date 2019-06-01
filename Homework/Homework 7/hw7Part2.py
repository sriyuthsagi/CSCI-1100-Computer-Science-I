
#import
import json
movies = json.loads(open("movies.json").read())
ratings = json.loads(open("ratings.json").read())


#inputs
minyear = int(input('Min year => '))
print(minyear)
maxyear = int(input('Max year => '))
print(maxyear)
w1 = input('Weight for IMDB => ')
print(w1)
w1 = float(w1)
w2 = input('Weight for Twitter => ')
print(w2)
w2 = float(w2)


#deleting movies
movies1 = dict()
for i, value in movies.items():
    if not(list(ratings.keys()).count(i) == 0 or len(ratings[i]) < 3):
        movies1[i] = movies[i]


#useful movies
movies2 = []
for i, value in movies1.items():
    if movies1[i]['movie_year'] >= minyear and movies1[i]['movie_year'] <= maxyear and len(ratings[i]) > 2:
        movies2.append(i)


#rating calculations
ratings1 = []
for i in movies2:
    rating = sum(ratings[i]) / len(ratings[i])
    rating = (w1 * movies1[i]['rating'] + w2 * rating) / (w1 + w2)
    ratings1.append((rating, i))
ratings1 = sorted(ratings1)


#top 10
top10 = []
i = -1
while i > -11:
    top10.append((ratings1[i][0], ratings1[i][1]))
    i -= 1


#bottom 10
bottom10 = []
i = 0
while i < 10:
    bottom10.append((ratings1[i][0], ratings1[i][1]))
    i += 1


#output
print('10 Highest rated movies')
for i in top10:
    print('{} ({})'.format(movies[i[1]]['name'], movies[i[1]]['movie_year']))
    print(' '*9, 'Rating: {:.2f}'.format(i[0]))
    print(' '*9, 'Genres: {}'.format((', ').join(movies[i[1]]['genre'])))

print('')
print('10 lowest rated movies')
for i in bottom10:
    print('{} ({})'.format(movies[i[1]]['name'], movies[i[1]]['movie_year']))
    print(' '*9, 'Rating: {:.2f}'.format(i[0]))
    print(' '*9, 'Genres: {}'.format((', ').join(movies[i[1]]['genre'])))