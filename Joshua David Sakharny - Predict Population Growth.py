# program description
# :: python
# :: takes in set of input variables
# :: displays prediction of total population

# input variables
numOrganisms = int(input("Enter Initial Number Of Organisms: "))
rateOfGrowth = int(input("Enter Rate Of Growth: "))
numHours = int(input("Enter Necessary Number Of Hours For Rate Of Growth: "))
totalHours = int(input("Enter Total Growth Hours: "))

# calculation
hours = 0
while hours <= totalHours:
    numOrganisms *= rateOfGrowth
    hours += numHours
    if hours == totalHours:
        break

# output
print("Total Population: " + str(numOrganisms) + " Organisms")
