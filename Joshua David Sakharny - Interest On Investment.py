# program description
# :: python
# :: calculates interest on an investment

# input / variables
initInvestAmount = float(input("Initial Investment Amount: "))
numYearsList = list(range(1, (int(input("Number Of Years: ")) + 1)))
numYears = len(numYearsList)
intRate = float(input("Interest Rate: "))
totalIntEarned = 0


# calculation
# :: calculate interest multiplier for simpler variable manipulation
intMulti = (intRate / 100) + 1


# :: calculate yearly interest earned with yearly end balance
def cal_yearly_int_earned_end_balance(init_invest, num_years, int_rate):
    for year in num_years:
        yearly_int_earned = (init_invest * int_rate) - init_invest
        investment_inc = init_invest + yearly_int_earned

        yearly_end_balance = yearly_int_earned + init_invest
        init_invest = investment_inc

        print("Year {} Interest Earned: ${:0.2f}".format(year, yearly_int_earned))
        print("Year {} End Balance: ${:0.2f}".format(year, yearly_end_balance) + "\n")


# :: calculate total end balance
def cal_total_int_earned_end_balance(init_invest, num_years, int_rate, total_int_earned):
    while num_years > 0:
        yearly_int_earned = (init_invest * int_rate) - init_invest
        investment_inc = init_invest + yearly_int_earned

        yearly_end_balance = yearly_int_earned + init_invest
        init_invest = investment_inc

        total_int_earned += yearly_int_earned
        total_end_balance = yearly_end_balance

        num_years -= 1

        if num_years == 0:
            print("Total Interest Earned: $" + str(format(total_int_earned, '.2f')))
            print("Total End Balance: $" + str(format(total_end_balance, '.2f')))


# output
print("\n")
print("Initial Investment Amount: " + str(format(initInvestAmount, '.2f')) + "\n")
cal_yearly_int_earned_end_balance(initInvestAmount, numYearsList, intMulti)
cal_total_int_earned_end_balance(initInvestAmount, numYears, intMulti, totalIntEarned)
