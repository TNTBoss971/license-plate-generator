"""
License Plate Generator
By Sam Davidson


"""


from random import randint


user_string = ""
altered_string = ""
max_length = 8
shorten = False


def main():
    ask_for_input()


# 7
# ask the user for the text they will like translated
def ask_for_input():
    global user_string, altered_string, max_length

    while True:
        # ask for the input
        user_string = input("Input string you want to be translated: ")
        altered_string = user_string.upper()
        if check_for_invalid_characters():
            break

    # if the text is too long, ask the user if they want it to be shortened
    if len(user_string) > max_length:
        print(f"Your text ({user_string}) is too long to fit on a license plate!")
        if input("Would you like your text to automatically be shortened? (Y/N): ").upper() == "Y":
            shorten = True
        else:
            shorten = False
    else:
        shorten = False
    
    if shorten == True:
        shorten_string()

    print(f"Altered Text: {altered_string}")

    translate_string()

# check for any invalid characters
def check_for_invalid_characters():
    global user_string, altered_string

    # invalid_characters will store the characters so we can print them later
    invalid_characters = []

    for i in range(len(altered_string)):
        # the program will only accept letters, numbers, and spaces \/
        if not altered_string[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ":
            invalid_characters.append(altered_string[i])

    if len(invalid_characters) > 0:
        print(f"Your text ({user_string}) has invalid characters!")
        print(invalid_characters)
        print("Please only input letters, numbers, and spaces!")
        return False
    else:
        return True

# this function will call a variety of functions in order to make the text fit
def shorten_string():
    global altered_string, user_string, max_length

    print("...")

    # FIRST ATTEMPT: remove spaces
    altered_string = altered_string.replace(" ", "")

    if len(altered_string) > max_length: 
        # SECOND ATTEMPT: replace words with shorter counterparts
        replace_words()

    if len(altered_string) > max_length:
        # THIRD ATTEMPT: remove duplicate letters
        remove_duplicates()

    if len(altered_string) > max_length:
        # FOURTH ATTEMPT: remove random vowels
        remove_vowels()
    
    if len(altered_string) > max_length:
        # The program has failed to shorten the text enough
        # ask the user if they want to continue with the current shortened text, or use their original text
        print(f"Your text is too long. The program has failed to shorten it down to {max_length} characters.")
        print(f"Would you like to continue with the best this program can do ({altered_string})?")
        print(f"If your answer is No, the program will continue with the original string ({user_string})")
        if not input("(Y/N): ").upper() == "Y":
            altered_string = user_string.upper()

# check for any words that can be replaced with less characters (for > 4, your > ur, ect)
def replace_words():
    global altered_string, user_string
    
    # use user_string becuase it has spaces
    altered_string = user_string.upper()

    # letters
    #   a
    #   b
    altered_string = altered_string.replace("BEE", "B")
    altered_string = altered_string.replace("BE", "B")
    #   c
    altered_string = altered_string.replace("SEE", "C")
    altered_string = altered_string.replace("SEA", "C")
    #   d
    #   e
    #   f
    #   g
    #   h
    #   i
    altered_string = altered_string.replace("EYE", "I")
    #   j
    #   k
    #   l
    #   m
    #   n
    #   o
    altered_string = altered_string.replace("OH", "O")
    #   p
    altered_string = altered_string.replace("PEE", "P")
    altered_string = altered_string.replace("PEA", "P")
    #   q
    altered_string = altered_string.replace("QUEUE", "Q")
    #   r
    altered_string = altered_string.replace("ARE", "R")
    #   s
    #   t
    altered_string = altered_string.replace("TEA", "T")
    #   u
    altered_string = altered_string.replace("YOU", "U")
    #   v
    #   w
    #   x
    #   y
    altered_string = altered_string.replace("WHY", "Y")
    #   z


    # numbers
    #   1
    altered_string = altered_string.replace("ONE", "1")
    #   2
    altered_string = altered_string.replace("TWO", "2")
    altered_string = altered_string.replace("TOO", "2")
    altered_string = altered_string.replace("TO", "2")
    #   3
    altered_string = altered_string.replace("THREE", "3")
    #   4
    altered_string = altered_string.replace("FOR", "4")
    altered_string = altered_string.replace("FOURTY ", "4")
    altered_string = altered_string.replace("FOUR", "4")
    #   5
    altered_string = altered_string.replace("FIVE", "5")
    #   6
    altered_string = altered_string.replace("SIX", "6")
    #   7
    altered_string = altered_string.replace("SEVEN", "7")
    #   8
    altered_string = altered_string.replace("EIGHT", "8")
    #   9
    altered_string = altered_string.replace("NINE", "9")
    #   10
    altered_string = altered_string.replace("TEN", "10")

# remove letters that are the same as the previous ones
def remove_duplicates():
    global altered_string
    temp_string = ""
    l_index = 0

    for letter in altered_string:
        if l_index == 0 or letter != altered_string[l_index - 1]:
            temp_string = temp_string + letter

        
        l_index += 1

    altered_string = temp_string.replace(" ", "")

# remove random vowels until the text fits
def remove_vowels():
    global altered_string, max_length
    place_in_string = 0
    while len(altered_string) > max_length and altered_string.count("A") + altered_string.count("E") + altered_string.count("I") + altered_string.count("O") + altered_string.count("U") > 0:
        if place_in_string > len(altered_string) - 1:
            place_in_string = 0
        
        if altered_string[place_in_string] in "AEIOU" and randint(0,100) > 25:
            altered_string = replace_character(altered_string, place_in_string, "")

        place_in_string += 1
        #print(altered_string)


def translate_string():
    global user_string, altered_string
    convert_into_leet_speak()

    print("The translating process is complete!")
    print(f'Input: "{user_string}"')
    print(f'Final result: "{altered_string}"')


def convert_into_leet_speak():
    global altered_string
    place_in_string = 0
    for char in altered_string:
        if char == "A":
            altered_string = replace_character(altered_string, place_in_string, "4")
        if char == "B":
            altered_string = replace_character(altered_string, place_in_string, "8")
        if char == "E":
            altered_string = replace_character(altered_string, place_in_string, "3")
        if char == "L":
            altered_string = replace_character(altered_string, place_in_string, "1")
        if char == "O":
            altered_string = replace_character(altered_string, place_in_string, "0")
        if char == "S":
            altered_string = replace_character(altered_string, place_in_string, "5")
        if char == "T":
            altered_string = replace_character(altered_string, place_in_string, "7")
        if char == "Z":
            altered_string = replace_character(altered_string, place_in_string, "2")
        place_in_string += 1

def replace_character(strng, ind, charcter):
    returned_string = strng[0:ind] + charcter + strng[ind + 1:len(strng)]
    return returned_string


if __name__ == "__main__":
    main()