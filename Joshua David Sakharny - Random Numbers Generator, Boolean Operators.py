# this program takes in four inputs from the users as four numbers
# there is a random selection of four numbers from a random number generator
# the four input numbers from the user and the four randomly generated numbers are printed
# the matching numbers are alerted to the user

from random import randint

# constants
rangeSize = 10

# how to play
print("Welcome To The Lucky-4 Number Game!")
print("Enter 4 Numbers Between 1 And 10 To Start")

print("\n")

# input variables
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

# random number generation
A = randint(1, 10)
B = randint(1, 10)
C = randint(1, 10)
D = randint(1, 10)

print("\n")

# input and random generated chart top
print("Key:")
print("U = Entered Numbers")
print("O = Generated Numbers")
print("Match! = Win")
print("X = Loss")

print("\n")

print("|U, O|")

# print individual pairs + calculate winning numbers
wins = 0

print("[" + str(a) + ", " + str(A) + "]")
if a == A:
    print("Match!")
    wins += 1
else:
    print("X")
print("\n")

print("[" + str(b) + ", " + str(B) + "]")
if b == B:
    print("Match!")
    wins += 1
else:
    print("X")
print("\n")

print("[" + str(c) + ", " + str(C) + "]")
if c == C:
    print("Match!")
    wins += 1
else:
    print("X")
print("\n")

print("[" + str(d) + ", " + str(D) + "]")
if d == D:
    print("Match!")
    wins += 1
else:
    print("X")
print("\n")

# print winning matches
print("Winning Matches: " + str(wins))
