# program description
# :: calculates result of number of iterations of pi

# constants
iterInc = 1

# input variables
numIter = int(input("Enter Number Of Iterations: "))

# calculation
outNumIter = numIter


def pi_approx(num_iterations):
    frc_inc = 3.0
    f_val = 1.0

    for i in range(num_iterations):
        f_val = f_val - ((1 / frc_inc) * (-1) ** i)
        frc_inc += 2

    return 4 * f_val


# output
print("Pi Approximation Based On " + str(outNumIter) + " Iterations: " + str(pi_approx(numIter)))
