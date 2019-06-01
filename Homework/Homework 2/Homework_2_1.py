#1 - import and functions
from math import pi
def find_sphere_volume(radius):
    svolume = (4/3)*pi*(radius**3)
    return svolume
    
def find_cube_volume(side):
    cvolume = side**3
    return cvolume
    
    
#2 - input
side = input('Enter the side length of the cube (in.) => ')
print(side)
radius = input('Enter the radius of the gum ball (in.) => ')
print(radius)


#3 - calculations
side = float(side)
radius = float(radius)
gumtotal = int((side/(radius*2)))**3
print('A box of side length {0:.1f} will hold {1:.0f} gum balls of radius {2:}.'.format(side, gumtotal, radius))


#4 - calculations
svol = find_sphere_volume(radius)*gumtotal
print('The gum balls will take up {0:.2f} in^3'.format(svol))
cvol =  find_cube_volume(side)
density = (svol/cvol)*100
print('of the total volume of {0:.2f} in^3 or {1:.2f}%'.format(cvol, density))


#5 - calculations
cvol2 = find_sphere_volume(side/2)
print('A sphere with a diameter of {0:.1f} would have volume {1:.2f} in^3'.format(side, cvol2))


#6 - calculations
gumtotal2 = int((cvol2 * gumtotal) / cvol)
print('It would hold {0:.0f} gum balls at the same density.'.format(gumtotal2))




"""
 First write two functions, find_sphere_volume(radius) and find_cube_volume(side) to calculate the volume of a sphere given a radius and a cube given a side length
2. Now ask the user for the side length of the cube and the radius of the gum balls.
3. Calculate the total number of gum balls that can be contained in the cube, remembering that the number of gum balls along each dimension must be an integer.
4. Calculate the volume of the cube, the total volume of all the gum balls, and the ratio of the total volume of gum balls to the volume of the cube to get a percent. We will refer to this ratio of volumes as the density.
5. Now lets see what would happen if we change the shape of the container and keep the density of gum balls the same. Calculate the volume of a sphere with a diameter the same as the side length of the cube.
6. Assume the density of gum balls remains the same, how many gum balls can fit in the sphere? Hint: Calculate the volume of the sphere, multiply by the density, and divide by the volume
of a single gum ball. The number of gum balls must be an integer. A run of the program is below.

"""