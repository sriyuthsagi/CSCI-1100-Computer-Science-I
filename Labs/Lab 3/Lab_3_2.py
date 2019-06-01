

def skewfun(time):
    avg = sum(time)/len(time)
    var = (time[0]-avg)**2 + (time[1]-avg)**2 + (time[2]-avg)**2 + (time[3]-avg)**2 + (time[4]-avg)**2
    var /= 5
    skew = (time[0]-avg)**3 + (time[1]-avg)**3 + (time[2]-avg)**3 + (time[3]-avg)**3 + (time[4]-avg)**3
    skew /= 5
    skew = skew/var**3**0.5    
    return skew

def stats(time):
    mn = min(time)
    mx = max(time)
    avg = sum(time)/len(time)
    stat = [mn, mx, avg]
    return stat
    


name_1 = "Stan"
## The following are Stan's 5 latest running times for 3 miles
time_1 = [34, 34, 35, 31, 29]


name_2 = "Kyle"
## The following are Kyle's 5 latest running times for 3 miles
time_2 = [30, 31, 29, 29, 28]


name_3 = "Cartman"
## The following are Cartman's 5 latest running times for 3 miles
time_3 = [36, 31, 32, 33, 33]


name_4 = "Kenny"
## The following are Kenny's 5 latest running times for 3 miles
time_4 = [33, 32, 34, 31, 15]


name_5 = "Bebe"
## The following are Bebe's 5 latest running times for 3 miles
time_5 = [27, 29, 29, 28, 30]


# Process results
skew1 = skewfun(time_1)
print ("{0}'s running times have a skew of {1:.2f}".format(name_1,skew1))

skew2 = skewfun(time_2)
print ("{0}'s running times have a skew of {1:.2f}".format(name_2,skew2))

skew3 = skewfun(time_3)
print ("{0}'s running times have a skew of {1:.2f}".format(name_3,skew3))

skew4 = skewfun(time_4)
print ("{0}'s running times have a skew of {1:.2f}".format(name_4,skew4))

skew5 = skewfun(time_5)
print ("{0}'s running times have a skew of {1:.2f}".format(name_5,skew5))

#additional results
stat1 = stats(time_1)
print(name_1, 's stats-- min: {0:.0f}, max: {1:.0f}, avg: {2:.1f}'.format(stat1[0], stat1[1], stat1[2]), sep="")

stat2 = stats(time_2)
print(name_2, 's stats-- min: {:.0f}, max: {:.0f}, avg: {:.1f}'.format(stat2[0], stat2[1], stat2[2]), sep="")

stat3 = stats(time_3)
print(name_3, 's stats-- min: {:.0f}, max: {:.0f}, avg: {:.1f}'.format(stat3[0], stat3[1], stat3[2]), sep="")

stat4 = stats(time_4)
print(name_4, 's stats-- min: {:.0f}, max: {:.0f}, avg: {:.1f}'.format(stat4[0], stat4[1], stat4[2]), sep="")

stat5 = stats(time_5)
print(name_5, 's stats-- min: {:.0f}, max: {:.0f}, avg: {:.1f}'.format(stat5[0], stat5[1], stat5[2]), sep="")

