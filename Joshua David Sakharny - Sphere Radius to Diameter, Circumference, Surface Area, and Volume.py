# python program / sphere radius to diameter, circumference, surface area and volume

# import modules
import math

# input variables
radian = float(input("Sphere Radius: "))

# calculate / diameter
diameter = int(2 * radian)

# calculate / circumference
circumference = radian * math.pi * 2

# calculate / surface area
surfaceArea = 4 * math.pi * radian ** 2

# calculate / volume
volume = (4 / 3) * (math.pi * radian ** 3)

# output
print("Sphere Diameter: " + str(diameter) + "n\"")
print("Sphere Circumference: " + str(circumference) + "n\"")
print("Sphere Surface Area: " + str(surfaceArea) + "n\"")
print("Sphere Volume: " + str(volume))
