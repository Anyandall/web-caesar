def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter in alphabet:
        char_value = alphabet.index(letter)
    if letter in alphabet.upper():
        char_value = alphabet.upper().index(letter)
    return char_value

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char not in alphabet and char not in alphabet.upper():
        return char
    new_char_value = (alphabet_position(char) + rot) % 26    
    if char in alphabet:
        new_char = alphabet[new_char_value]
    if char in alphabet.upper():
        new_char = alphabet.upper()[new_char_value]
    return new_char

def alphabet_dictionary():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_dictionary = {}
    for num in range(26):
        new_dictionary[(alphabet[num])] = num
    return (new_dictionary)