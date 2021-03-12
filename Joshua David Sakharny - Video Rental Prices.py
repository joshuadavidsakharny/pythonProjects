# python program / video rental price

# static variables / price
newVideoPrice = float(3.00)
oldVideoPrice = float(2.00)

# input variables
newVideoNum = float(input("Quantity / New Video(s): "))
oldVideoNum = float(input("Quantity / Old Video(s): "))

# calculate totals
newVideoTotalPrice = float(newVideoPrice * newVideoNum)
oldVideoTotalPrice = float(oldVideoPrice * oldVideoNum)
totalRentalPrice = float(newVideoTotalPrice + oldVideoTotalPrice)

# output
print("Total Cost Of Rental: $" + str(format(totalRentalPrice, '.2f')))
