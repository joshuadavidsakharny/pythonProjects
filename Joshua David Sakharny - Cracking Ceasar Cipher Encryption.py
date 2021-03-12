# single word brute force decryption program
# upper and lower case functionality included
# asks user for input
# outputs all possible decryption combinations

# UPPERCASE letter list
upAb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# lowercase letter list
lowAb = "abcdefghijklmnopqrstuvwxyz"

# input encrypted word
encryptInput = input("Enter Encrypted Word: ")
# :: stores encryption character length
encryptLen = len(encryptInput)

for decryp in range(len(upAb)):
    # stores each attempted combination
    output = ''
    # runs though all 26 combinations
    for letter in encryptInput:
        # upper case functionality
        if letter.isupper():
            if letter in upAb:
                num = upAb.find(letter)
                num = num - decryp
                # wrap around
                if num < 0:
                    num = num + len(upAb)
                output = output + upAb[num]
            else:
                output = output + letter
        else:
            # lower case functionality
            if letter in lowAb:
                num = lowAb.find(letter)
                num = num - decryp
                # wrap around
                if num < 0:
                    num = num + len(lowAb)
                output = output + lowAb[num]
            else:
                output = output + letter

    # output using list technique to print entire brute force registry
    print('Hacking decryp #%s: %s' % (decryp, output))
