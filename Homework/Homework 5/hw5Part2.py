#inputs
file = input('Filename => ')
print(file)
month = input('Month => ')
print(month)
file = open(file) 



#initial list variables
tmin = []
tmax = []
tavg = []
tavg2 = []
years = []
yrange = []
data = []



#creating a list from the file
k = 1
while k == 1:
    data.append(file.readline().split(','))
    if data[-1] == ['']:
        data.pop()
        break



#creating basic lists to split different variables from the main list and finding averages
monthlen = len(str(month))
for i in range(len(data)):
    data[i][10] = data[i][10].strip('\n')
    data[i][11] = data[i][11].strip('\n') 
    if monthlen == 1:
        if data[i][1][-1] == str(month) and data[i][1][-2] == '0':
            if not data[i][9] == '':
                tavg2.append(float(data[i][9]))
                tavg.append([data[i][9], data[i][1][0:4]])
                years.append(data[i][1][0:4])
            if not data[i][10] == '':
                tmax.append([data[i][10], data[i][1][0:4]])
            if not data[i][11] == '':
                tmin.append([data[i][11], data[i][1][0:4]])            
    if monthlen == 2:
        if data[i][1][-1] == str(month)[1] and data[i][1][-2] == str(month)[0]:
            if not data[i][9] == '':
                tavg2.append(float(data[i][9]))
                tavg.append([data[i][9], data[i][1][0:4]])
                years.append(data[i][1][0:4])
            if not data[i][10] == '':
                tmax.append([data[i][10], data[i][1][0:4]])
            if not data[i][11] == '':
                tmin.append([data[i][11], data[i][1][0:4]])
                
                
                
#finding lowest min
mmin = tmin[0][0]
minyear = []
for i in range(len(tmin)):
    if tmin[i][0] <= mmin:
        mmin = tmin[i][0]
for i in range(len(tmin)):
    if tmin[i][0] == mmin:
        minyear.append(tmin[i][1])



#finding highest max
mmax = tmax[0][0]
maxyear = []
for i in range(len(tmax)):
    if tmax[i][0] >= mmax:
        mmax = tmax[i][0]
for i in range(len(tmax)):
    if tmax[i][0] == mmax:
        maxyear.append(tmax[i][1])



#finding average
avgfinal = sum(tavg2)/len(tavg2)



#basic prints
print('Earliest recorded average {0:.2f} in {1}'.format(float(tavg[0][0]), tavg[0][1]))
print('Latest recorded average {0:.2f} in {1}'.format(float(tavg[-1][0]), tavg[-1][1]))
print('Average temperature: {0:.2f}'.format(avgfinal))
print('Lowest min value recorded: {0:.2f} in year(s): {1}'.format(float(mmin), minyear[0]))
print('Highest max value recorded: {0:.2f} in year(s): {1}'.format(float(mmax), maxyear[0]))



#creating histogram
print('Histogram of average temperature')
if len(years) <= 10:
    print('{}-{}: {}'.format(years[0], years[-1], '*'*int(avgfinal)))
if len(years) > 10:
    for i in range(0, len(years), 10):
        if i+9 < len(years):
            yrange.append((years[i], years[i+9]))
        else:
            yrange.append((years[i], years[-1]))
for i in range(len(yrange)):
    avgrange = 0
    count = 0
    for j in range(1, len(years)):
        if int(years[j]) >= int(yrange[i][0]) and int(years[j]) <= int(yrange[i][1]):
            avgrange = avgrange + float(tavg[j][0])
            count += 1
    print('{}-{}: {}'.format(yrange[i][0], yrange[i][-1], '*'*int(avgrange/count)))