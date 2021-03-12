# program description
# :: python
# :: extension to previous program
# :: bounciness index added

# input variables
height = int(input("Enter Ball Height: "))
bounceIndex = float(input("Enter Ball Bounciness Index: "))
numberOfBounces = float(input("Enter Number Of Ball Bounces: "))

# calculation
distance = 0

distance = 0
while numberOfBounces > 0:
    distance += height
    height *= bounceIndex
    distance += height
    numberOfBounces -= 1

# output
print("Total Distance Traveled: " + str(distance) + " Units.")

