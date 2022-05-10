# substitution_cipher_atbash
 
from microbit import *
 
# Atbash cipher.
def atbash(text):
    alpha  = "abcdefghijklmnopqrstuvwxyz 123456789:,{}"
    crypta = "gk4a1s{f2bclh5,wn}3uzj:q yxm7po8rd6et9vi"
    result = ""
 
    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]
 
    return result
 
# The script starts executing statements from here.
 
sleep(1000)
 
print("Set your keyboard to CAPS LOCK.")
print()
 
while True:
    plaintext = input("Enter a CAPS LOCK string: ")
    
    result = atbash(plaintext)
 
    print("result =", result)
