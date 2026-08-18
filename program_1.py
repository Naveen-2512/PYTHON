import sys

def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():                    # check whether alphabate or not
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result
    

if len(sys.argv) != 4:                 # Command line argument
    print("Command line Argument : python program_1.py  <encode/decode> <text> <shift>")

    sys.exit()
    
method = sys.argv[1].lower()
text = sys.argv[2]

shift = int(sys.argv[3])       #displacement value  

if method == "encode":
    print("Encoded Text:", caesar_cipher(text, shift))

elif method == "decode":
    print("Decoded Text:", caesar_cipher(text, -shift))

else:
    print("Invalid method!.")