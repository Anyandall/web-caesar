from helpers import alphabet_position, rotate_character
import sys
import string

def encrypt(text, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""
    for character in text:
        encrypted_string += rotate_character(character, rot)
    return encrypted_string

def user_input_is_valid(cl_args):
    if cl_args[-1].isdigit():
        return True
    return False

def main():
    if len(sys.argv) > 1:
        if user_input_is_valid(sys.argv):
            message = str(input("Type a message to encrypt: "))
            rotation = int(sys.argv[1])
        elif not user_input_is_valid(sys.argv):
            print ("Error: Command line argument must be an integer!")
            sys.exit()
    else:
        message = str(input("Type a message to encrypt: "))
        rotation = int(input("Cipher rotation? "))
    print (encrypt(message, rotation))


if __name__ == "__main__":
    main()