#variable input
rsun = input('Enter the radius of the Sun (miles) -> ')
print(rsun)
rmoon = input('Enter the radius of the Moon (miles) -> ')
print(rmoon)
sedist = input('Enter the maximum distance to the Sun (miles) -> ')
print(sedist)
medist = input('Enter the minimum distance to the Moon (miles) -> ')
print(medist)
moverate = input('Enter the rate the Moon is moving away (in/year) -> ')
print(moverate)

#calculation
medistactual = float(sedist) * (float(rmoon)/float(rsun))
part1 = 'The Moon will have exactly the same apparent size as the Sun when it is {0:.2f} miles away.'. format(medistactual)
print(part1)
moondist = float(medistactual) - float(medist)
part2 = 'The Moon will need to recede another {0:.2f} miles'. format(moondist)
print(part2)
moontime = int((moondist * 63360) / float(moverate))
part3 = 'Which will occur in {0:.0f} years at the current rate.'. format(moontime)
print(part3)


"""
Enter the radius of the Sun (miles) -> 432288
432288
Enter the radius of the Moon (miles) -> 1079
1079
Enter the maximum distance to the Sun (miles) -> 94500000
94500000
Enter the minimum distance to the Moon (miles) -> 221500
221500
Enter the rate the Moon is moving away (in/year) -> 1.6
1.6
Distance_Moon_to_Earth = Distance_Sun_to_Earth*(Radius_of_Moon/Radius_of_Sun)
"""