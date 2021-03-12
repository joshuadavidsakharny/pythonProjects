# program description
# :: python
# :: displays annual salary increase schedule
# :: for specified number of years

# input variables
initSalary = int(input("Enter Starting Salary: "))
percentInc = (float(input("Enter Percentage Increase: ")) / 100)
numYears = list(range(1, (int(input("Enter Number Of Years In Schedule: ")) + 1)))


# calculation
def calculate_salary(init_salary, percent_inc, num_years):
    for year in num_years:
        salary_inc = init_salary * percent_inc
        new_salary = init_salary + salary_inc
        init_salary = new_salary
        print("{} Year Salary: ${:0.2f}".format(year, new_salary))


# output
calculate_salary(initSalary, percentInc, numYears)
