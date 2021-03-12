# python program calculating employee total weekly pay

# input variables
hourlyWage = float(input("Hourly Wage: "))
totalRegHours = float(input("Total Regular Hours: "))
totalOTHours = float(input("Total Overtime Hours: "))

# calculate overtime
overtimePay = totalOTHours * (1.5 * hourlyWage)

# calculate total weekly pay
totalWeeklyPay = float(hourlyWage * totalRegHours + overtimePay)

# output
print("Total Weekly Pay: " + "$" + (str(format(totalWeeklyPay, '.2f'))))
