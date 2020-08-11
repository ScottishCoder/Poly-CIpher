# Polygraphic Cipher

# Set Alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

# Class containing cipher methods needed for enc and dec
class PolygraphicCipher:

    def __init__(self, keystream, plaintext, encry=False, decry=False):
        self.keystream = keystream  # contains key
        self.plaintext = plaintext  # << represents both plaintext and ciphertext
        if encry == True:  # < if user wants to encrypt, call encrypt() method
            updatedKey = self.keyConstructor(plaintext, keystream)  # Call method to generate key to length of plaintext
            self.encrypt(updatedKey, self.plaintext)  # Call encryption method
        elif decry == True:  # < if user wants to decrypt, call decrypt() method
            self.decrypt(self.keystream, self.plaintext) # Call decrypt method
        else:
            # If no method provided, be it enc or dec, then let user know
            print('No method provided!')
    # Generate the correct key with the same size as the plaintext
    def keyConstructor(self,text, key):
        # Get key, put into a list with each letter having its own index
        keyMorph = list(key)
        # if the len of the text is equal to the key, proceed without altering the key
        if len(text) == len(keyMorph):
            return (keyMorph)
        else:  # if plaintext is larger than they key, run code to alter
            # get len of text sub from key
            for i in range(len(text) -
                           len(keyMorph)):
                # append to key morph list the key using mod and the index of the key
                keyMorph.append(key[i % len(key)])
        # method returns the value. If plaintext is hello, and the key is br. It will now be brbrb
        return ("".join(keyMorph))

    # Main encryption method.
    def encrypt(self, keystream, plaintext):  # < Encrypt method

        # Key pos holds the index positions of each letter in our key
        keyPos = []
        # text pos holds the index positions of each letter in our text
        textPos = []
        # Keys equal to the keystream parameter of the method
        keys = keystream
        # Print a general message showing the updated key
        print('---------- UPDATED KEY ----------')
        print(keys)
        print('----------------------------------')
        # Char will be equal to the plaintext parameter being passed into the encrypt method
        chars = plaintext
        # for every char in chars, if hello, it gets (h e l l o) per iteration
        for char in chars:
            # Find the index position of our char using the alphabet list
            plaintextPos = alphabet.index(char)
            # Create a dictionary. Not really needed tbh, but it can be used to display the char too.
            packed = {'Char': char, 'Position': plaintextPos}
            # Append the data onto the textPos list.
            textPos.append(packed)

        # no need repeating myself. Applies same logic as the above code, but gets key indexes and appends.
        for key in keys:
            plaintextPos = alphabet.index(key)
            packed = {'Char': key, 'Position': plaintextPos}
            keyPos.append(packed)

        # Key data will store the sole index position of the key char
        keyData = []
        # Text data will hold the sole index position of the plaintext char
        # Like I mentioned before, I could have skipped this by not using a dict. But too much has been done now.
        textData = []

        # For text indexes in the text pos list
        for txtidx in textPos:
            # Get the index position of that char and store into var
            plaintextCharacterIndex = txtidx['Position']
            # Append the index value of the text data onto the textData list
            textData.append(plaintextCharacterIndex)

        # No need to repeat, applies same logic as above code, but appends key index position instead
        for keytxtPos in keyPos:
            keyTextCharacterIndex = keytxtPos['Position']
            keyData.append(keyTextCharacterIndex)

        # Print a general statement showing the positions of both plain text and key
        print(textData, 'Plain Text positions')

        print(keyData, 'Key Text positions')

        print('---------- ADDING VALUES ----------')

        # Using list comprehension. Add key data with text data. So both indexes [0] + [0]
        # This keep iterating until all values are added up and stored as a list
        calc = [keyData + textData for keyData, textData in zip(keyData, textData)]
        print(calc)
        print('-----------------------------------')

        # Cipher placement list will contain the new index positions
        cipherPlacement = []

        # for each index position in calc << our new index values
        for i in calc:
            # Using mod 26 to get cipher text index position
            # Modulo doesn't divide, but rather gets the remainder value.
            # This is needed so as to not go over index size of 26
            ind = i % 26
            # Append the newly acquired index position to the cipherPlacement list
            cipherPlacement.append(ind)

        # Print general statement showing the mod 26 positions
        print('---------- MOD 26 INDEX POSITIONS ----------')

        print(cipherPlacement)

        print('--------------------------------------------')

        # Ciphertext variable is an emtpy string. Ciphertext will be concatenated onto this variable
        cipherText = ''

        # for b << len of the cipherPlacement list so we only iterate through the provided length
        for b in range(len(cipherPlacement)):
            # concatenate onto the cipherText variable the new char using the new cipherPlacement index values
            cipherText = cipherText + alphabet[cipherPlacement[b]]

        # Print the newly acquired cipher text and key used to encrypt the plaintext message
        print('========== KEY ==========')
        print(keys)
        print('=========================')
        print('========== CIPHERTEXT ==========')
        print(cipherText)
        print('================================')

    # Decrypt logic is exactly the sae. Look for comment in method which highlights different
    def decrypt(self, keystream, ciphertext):
        keyPos = []
        ciphPos = []
        keys = keystream
        print('---------- UPDATED KEY ----------')
        print(keys)
        print('----------------------------------')
        chars = ciphertext
        for char in chars:
            plaintextPos = alphabet.index(char)
            packed = {'Char': char, 'Position': plaintextPos}
            ciphPos.append(packed)

        for key in keys:
            ciphertextKeyPos = alphabet.index(key)
            packed = {'Char': key, 'Position': ciphertextKeyPos}
            keyPos.append(packed)

        keyData = []
        textData = []

        for txtidx in ciphPos:
            plaintextCharacterIndex = txtidx['Position']
            # plaintextChar = txtidx['Char']
            textData.append(plaintextCharacterIndex)
            # textData.append(plaintextChar)

        for keytxtPos in keyPos:
            keyTextCharacterIndex = keytxtPos['Position']
            keyData.append(keyTextCharacterIndex)
            # keyTextCharacter = keytxtPos['Char']
            # keyData.append(keyTextCharacter)

        print(textData, 'Plain Text positions')
        print(keyData, 'Key Text positions')

        print('---------- SUBTRACTING VALUES ----------')
        # DIFFERENCE HERE!!! Text data is SUBTRACTED (-) from Key data
        calc = [textData - keyData for keyData, textData in zip(keyData, textData)]
        print(calc)
        print('-----------------------------------')

        cipherPlacement = []

        for i in calc:
            ind = i % 26
            cipherPlacement.append(ind)

        print('---------- MOD 26 INDEX POSITIONS ----------')

        print(cipherPlacement)

        print('--------------------------------------------')

        plaintext = ''

        for b in range(len(cipherPlacement)):
            plaintext = plaintext + alphabet[cipherPlacement[b]]

        print('========== PLAINTEXT ==========')
        print(plaintext)
        print('================================')
        print('========== KEY ==========')
        print(keys)
        print('=========================')


# General Print statement greeting user
print('The Polygraphic Cipher')
print('Please follow the instructions!')
# User input is stored into user variable.
user = input('Would you like to Encrypt or Decrypt? (e) or (d):')
# if user chooses e, the code will execute within statement for encryption
if user == "e" or user == "E":
    # Gets users plaintext they wish to encrypt and converts it to upper << less hassle lol
    plaintext = input('Please input the plaintext you wish to encrypt: ').upper()
    # Gets users key data and stores it into keystream variable
    keystream = input('Please input the key you wish to use: ').upper()
    # Call on the PolygraphicCipher class. Provide arguments, set encr to True
    PolygraphicCipher(keystream, plaintext, encry=True)
# If the user selects d the code will execute within statement for decryption
elif user == "d":
    # Get cipher text from input and store into ciphertext variable
    ciphertext = input('Please input the ciphertext you wish to decrypt: ').upper()
    # Get the key needed for decryption from the input and store into keystream variable
    keystream = input('Please input the key used for encryption: ').upper()
    # Call on PolygraphicCipher. Provide arguments and set decry to True
    PolygraphicCipher(keystream, ciphertext, decry=True)
# If an other option has been detected, just close the program
else:
    # Exit program
    exit()
