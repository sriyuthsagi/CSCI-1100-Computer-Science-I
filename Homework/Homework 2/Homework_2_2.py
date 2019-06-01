#functions
def time_to_seconds(day):
    sech = day[0]*60*60
    secm = day[1]*60
    totalsec = day[2] + sech + secm
    return totalsec

def seconds_to_str(seconds):
    hour = int((seconds - (seconds%(60*60))) / (60*60))
    minutes = int(((seconds%(60*60) - (seconds%60)))/60)
    seconds = int(seconds%60)
    nday = [hour, minutes, seconds]
    return nday


#basic info
day = [23, 56, 4]
print('A day in 2017 is', day[0], 'hours', day[1], 'minutes and', day[2], 'seconds long.')
print('Which is equivalent to', time_to_seconds(day), 'seconds.')


#predictions
year = int(input('Enter a future year => '))
print(year)
rate = int(time_to_seconds(day) + (year - 2017)*((6*60*60)/900000000))
print('A day in year {0:.0f} will be {1:.0f} seconds long'.format(year, rate))
newday = seconds_to_str(rate)
print('which is equivalent to', newday[0], 'hours', newday[1], 'mins', newday[2], 'secs')

