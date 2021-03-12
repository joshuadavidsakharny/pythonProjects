# single word decryption program
# upper and lower case functionality included
# asks user for input and encryption decryp
# outputs decrypted word

# UPPERCASE letter list
upAb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# lowercase letter list
lowAb = "abcdefghijklmnopqrstuvwxyz"

# input encrypted word
encryptInput = input("Enter Encrypted Word: ")
# :: stores encryption character length
encryptLen = len(encryptInput)

# input encryption decryp
encryptKey = int(input("Enter Decryption Key: "))


# decryption
def decrypt(n, encrypt_text):
    # stores output decryption
    output = ''

    # runs through upper and lower case lists and decrypts based on encryption decryp and modular wrap-around
    for a in encrypt_text:
        if a.isupper():
            try:
                i = (upAb.index(a) - n) % 26
                output += upAb[i]
            except ValueError:
                output += a
        else:
            try:
                i = (lowAb.index(a) - n) % 26
                output += lowAb[i]
            except ValueError:
                output += a
    # returns decryption
    return output


decryption = decrypt(encryptKey, encryptInput)

print('Decrypted Word:', decryption)
