import random

# opening game line
print("Welcome to Lucky 7's Dice Game!")
print("(press enter to continue through rest of game)")
input()

# rules
print("If the dice rolls add up to 7, you win $4.00!")
input()
print("If not, you lose $1.00.")
input()
print("If balance = $0.00, Game Over.")
input()
print("Good luck! Have Fun!")
input()

# input balance
pot = float(input("Please enter the amount of money you want in the pot: "))
print("(press enter to start game)")
input()

# loops until balance amount is equal or less than 0
# :: counts amount of times played from previous win
winCount = 0
# :: counts amount of times played total
playCount = 0

while pot > 0:
    # rolls dice with seven faces
    dice_roll = random.randint(1, 7), random.randint(1, 7)
    print(dice_roll[0], dice_roll[1])

    # sums two dice rolls
    roll = sum(dice_roll)

    # calculates if dice roll is win or loss
    # prints added or deducted balance amount
    # prints updated balance
    if roll == 7:
        pot += 4
        print("Roll: 7 - Win!")
        print("$4.00 added to balance")
        print("Balance: $", ("{:.2f}".format(pot)))
        print("Amount Of Plays To Win: " + str(winCount))
        winCount = 0
    else:
        pot -= 1
        print("Roll: " + str(roll) + " - Loss.")
        print("$1.00 deducted from balance")
        print("Balance: $", ("{:.2f}".format(pot)))
        winCount += 1
    playCount += 1
    input()

print("Balance = $0.00 - GAME OVER!")
print("Total Plays: " + str(playCount) + " Plays.")
print("Thank you for playing Lucky 7's Dice Game. Come Again!")
