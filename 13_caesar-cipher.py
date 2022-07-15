# Lab 13 : Using Functions to Implement a Caesar Cipher

# Creating a user-defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Encrypting a message.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Getting a cipher key
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Encrypting a message
""" plan out the algorithm for encryption as follows:
    1. Take three arguments: the message, the cipherKey, and the alphabet.
    2. Initialize variables.
    3. Use a for loop to traverse each letter in the message.
    4. For a specific letter, find the position.
    5. For a specific letter, determine the new position given the cipher key.
    6. If current letter is in the alphabet, append the new letter to the encrypted message.
    7. If current letter is not in the alphabet, append the current letter.
    8. Return the encrypted message after exhausting all the letters in the message. 
"""
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypting a message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Creating a main function
""" plan out your logic:

    1. Define a string variable to contain the English alphabet.
    2. To be able to shift letters, double your alphabet string.
    3. Get a message to encrypt from the user.
    4. Get a cipher key from the user.
    5. Encrypt the message.
    6. Decrypt the message. 
"""
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

# call the function
runCaesarCipherProgram()