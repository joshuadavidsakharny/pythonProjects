# asks for input in binary and prints output in decimal base

# input
binIn = int(input("Please Enter Binary Value: "))


# conversion
def bin_deci(bi):
    # function storage
    deci, a, n = 0, 0, 0
    # runs through each binary digit and translates
    while bi != 0:
        dec = bi % 10
        deci = deci + dec * pow(2, a)
        bi = bi // 10
        a += 1
    print(deci)


# output
print("Decimal Conversion: " + str(bin_deci(binIn)))
