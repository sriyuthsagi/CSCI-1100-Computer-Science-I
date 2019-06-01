
def next_step(grav, thrust, alt, speed):
    accel = grav - (grav*thrust)
    speedn = speed + accel
    altn = alt - speedn
    return (altn, speedn)



alt = float(input('Enter starting altitude (meters) => '))
print(alt)

grav = float(input('Enter the gravitational acceleration (m/second^2) => '))
print(grav)

fuel = float(input('Enter the total units of fuel => '))
print(fuel)
fueli = fuel

time = 0
speed = 0
speedl = []
stat = []

while alt > 0:
    print('Time {0} - Altitude: {1:.2f}. Speed: {2:.2f}'.format(time, alt, speed))
    if fuel > 0:
        thrust = float(input('Enter the thrust => '))
        print(thrust)
        if thrust > fuel:
            print('Out of fuel, able to use thrust of {0:.2f}'.format(fuel))
            thrust = fuel
        fuel = fuel - thrust
    alt = next_step(grav, thrust, alt, speed)[0]
    speed = next_step(grav, thrust, alt, speed)[1]
    thrust = 0
    time += 1
    speedl.append(speed)
    stat.append([speed, time, alt])
print('Time {0} - Altitude: 0.00. Speed: {1:.2f}'.format(time, speed, alt))
if speed > 2.2:
    print('Crashed ...\nKapow ...\n... All astronauts are now shorter and you owe us a lander...\n')
else:
    print('Nice landing!\nThe world salutes you!')


maxspeed = speedl.index(max(speedl))
position = stat[maxspeed]
print('Maximum speed of {0:.2f} was reached at time {1} and an altitude of {2:.2f}.'.format(position[0], position[1], position[2]))
fuelused = fueli - fuel
print('After that you used {0:.2f} units of fuel.'.format(fuelused))
print('At the end you had {0:.2f} units of fuel left.'.format(fuel))



"""
Enter starting altitude (meters) => 100.0
100.0
Enter the gravitational acceleration (m/second^2) => 19.6
19.6
Enter the total units of fuel => 100.0
100.0
Time 0 - Altitude: 100.00, Speed: 0.00
Enter the thrust => 0.0
0.0
Time 1 - Altitude: 80.40, Speed: 19.60
Enter the thrust => 0.0
0.0
Time 2 - Altitude: 41.20, Speed: 39.20
Enter the thrust => 0.0
0.0
Time 3 - Altitude: 0.00, Speed: 58.80
Crashed ...
Kapow ...
... All astronauts are now shorter and you owe us a lander...
Maximum speed of 58.80 was reached at time 3 and an altitude of 0.00.
After that you used 0.00 units of fuel.
At the end you had 100.00 units of fuel left.
"""