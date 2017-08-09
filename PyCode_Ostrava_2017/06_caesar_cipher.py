# def caesar(plainText, shift):
#   cipherText = ""
#   for ch in plainText:
#     if ch.isalpha():
#       stayInAlphabet = ord(ch) + shift
#       if stayInAlphabet > ord('z'):
#         stayInAlphabet -= 26
#       finalLetter = chr(stayInAlphabet)
#       cipherText += finalLetter
#   print ("Your ciphertext is: ", cipherText)
#   return cipherText
#
# caesar('AHOJ', 1)

import string
def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    print (plaintext.translate(table))

caesar('ahoj', 1) # just lowercase