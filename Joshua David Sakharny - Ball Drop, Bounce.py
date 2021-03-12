# program description
# :: python
# :: allows user to enter initial height of ball before dropped
# :: outputs total distance traveled by ball based on number of bounces

# constants
bounceIndex = float(0.6)

# input variables
height = int(input("Enter Ball Height: "))
numberOfBounces = float(input("Enter Number Of Ball Bounces: "))

# calculation
distance = 0
while numberOfBounces > 0:
    distance += height
    height *= bounceIndex
    distance += height
    numberOfBounces -= 1

# output
print("Total Distance Traveled: " + str(distance) + " Units.")










