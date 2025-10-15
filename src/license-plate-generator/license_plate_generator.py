"""
License Plate Generator
By Sam Davidson


"""


from random import randint

class Storage:
    def __init__(self):
        self.user_string = ""
        self.altered_string = ""
max_length = 8
shorten = False
store = Storage()

def main():
    ask_for_input()



# ask the user for the text they will like translated
def ask_for_input():

    while True:
        # ask for the input
        store.user_string = input("Input string you want to be translated: ")
        store.altered_string = store.user_string.upper()
        if check_for_invalid_characters():
            break

    # if the text is too long, ask the user if they want it to be shortened
    if len(store.user_string) > max_length:
        print(f"Your text ({store.user_string}) is too long to fit on a license plate!")
        if input("Would you like your text to automatically be shortened? (Y/N): ").upper() == "Y":
            shorten = True
        else:
            shorten = False
    else:
        shorten = False
    
    if shorten == True:
        shorten_string()

    # print(f"Altered Text: {store.altered_string}")

    translate_string()

# check for any invalid characters
def check_for_invalid_characters():

    # invalid_characters will store the characters so we can print them later
    invalid_characters = []

    for i in range(len(store.altered_string)):
        # the program will only accept letters, numbers, and spaces \/
        if not store.altered_string[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ":
            invalid_characters.append(store.altered_string[i])

    if len(invalid_characters) > 0:
        print(f"Your text ({store.user_string}) has invalid characters!")
        print(invalid_characters)
        print("Please only input letters, numbers, and spaces!")
        return False
    else:
        return True

# this function will call a variety of functions in order to make the text fit
def shorten_string():

    print("...")

    # FIRST ATTEMPT: remove spaces
    store.altered_string = store.altered_string.replace(" ", "")

    if len(store.altered_string) > max_length: 
        # SECOND ATTEMPT: replace words with shorter counterparts
        replace_words()

    if len(store.altered_string) > max_length:
        # THIRD ATTEMPT: remove duplicate letters
        remove_duplicates()

    if len(store.altered_string) > max_length:
        # FOURTH ATTEMPT: remove random vowels
        remove_vowels()
    
    if len(store.altered_string) > max_length:
        # The program has failed to shorten the text enough
        # ask the user if they want to continue with the current shortened text, or use their original text
        print(f"Your text is too long. The program has failed to shorten it down to {max_length} characters.")
        print(f"Would you like to continue with the best this program can do ({store.altered_string})?")
        print(f"If your answer is No, the program will continue with the original string ({store.user_string})")
        if not input("(Y/N): ").upper() == "Y":
            store.altered_string = store.user_string.upper()
    

# check for any words that can be replaced with less characters (for > 4, your > ur, ect)
def replace_words():
    
    # use user_string becuase it has spaces
    store.altered_string = store.user_string.upper()

    # letters
    #   a
    #   b
    store.altered_string = store.altered_string.replace("BEE", "B")
    store.altered_string = store.altered_string.replace("BE", "B")
    #   c
    store.altered_string = store.altered_string.replace("SEE", "C")
    store.altered_string = store.altered_string.replace("SEA", "C")
    #   d
    #   e
    #   f
    #   g
    #   h
    #   i
    store.altered_string = store.altered_string.replace("EYE", "I")
    #   j
    #   k
    #   l
    #   m
    #   n
    #   o
    store.altered_string = store.altered_string.replace("OH", "O")
    #   p
    store.altered_string = store.altered_string.replace("PEE", "P")
    store.altered_string = store.altered_string.replace("PEA", "P")
    #   q
    store.altered_string = store.altered_string.replace("QUEUE", "Q")
    #   r
    store.altered_string = store.altered_string.replace("ARE", "R")
    #   s
    #   t
    store.altered_string = store.altered_string.replace("TEA", "T")
    #   u
    store.altered_string = store.altered_string.replace("YOU", "U")
    #   v
    #   w
    #   x
    #   y
    store.altered_string = store.altered_string.replace("WHY", "Y")
    #   z


    # numbers
    #   1
    store.altered_string = store.altered_string.replace("ONE", "1")
    #   2
    store.altered_string = store.altered_string.replace("TWO", "2")
    store.altered_string = store.altered_string.replace("TOO", "2")
    store.altered_string = store.altered_string.replace("TO", "2")
    #   3
    store.altered_string = store.altered_string.replace("THREE", "3")
    #   4
    store.altered_string = store.altered_string.replace("FOR", "4")
    store.altered_string = store.altered_string.replace("FOURTY ", "4")
    store.altered_string = store.altered_string.replace("FOUR", "4")
    #   5
    store.altered_string = store.altered_string.replace("FIVE", "5")
    #   6
    store.altered_string = store.altered_string.replace("SIX", "6")
    #   7
    store.altered_string = store.altered_string.replace("SEVEN", "7")
    #   8
    store.altered_string = store.altered_string.replace("EIGHT", "8")
    #   9
    store.altered_string = store.altered_string.replace("NINE", "9")
    #   10
    store.altered_string = store.altered_string.replace("TEN", "10")

    
# remove letters that are the same as the previous ones
def remove_duplicates():
    temp_string = ""
    l_index = 0

    for letter in store.altered_string:
        if l_index == 0 or letter != store.altered_string[l_index - 1]:
            temp_string = temp_string + letter

        
        l_index += 1
    
    store.altered_string = store.altered_string.replace(" ", "")


# remove random vowels until the text fits
def remove_vowels():
    place_in_string = 0
    while len(store.altered_string) > max_length and get_vowel_count(store.altered_string) > 0:
        if place_in_string > len(store.altered_string) - 1:
            place_in_string = 0
        
        if store.altered_string[place_in_string] in "AEIOU" and randint(0,100) > 25:
            store.altered_string = replace_character(store.altered_string, place_in_string, "")

        place_in_string += 1
        #print(store.altered_string)
        


def translate_string():
    convert_into_leet_speak()

    print("The translating process is complete!")
    print(f'Input: "{store.user_string}"')
    print(f'Final result: "{store.altered_string}"')


def convert_into_leet_speak():
    place_in_string = 0
    for char in store.altered_string:
        if randint(0, 100) > 50:
            if char == "A":
                store.altered_string = replace_character(store.altered_string, place_in_string, "4")
            if char == "B":
                store.altered_string = replace_character(store.altered_string, place_in_string, "8")
            if char == "E":
                store.altered_string = replace_character(store.altered_string, place_in_string, "3")
            if char == "L":
                store.altered_string = replace_character(store.altered_string, place_in_string, "1")
            if char == "O":
                store.altered_string = replace_character(store.altered_string, place_in_string, "0")
            if char == "S":
                store.altered_string = replace_character(store.altered_string, place_in_string, "5")
            if char == "T":
                store.altered_string = replace_character(store.altered_string, place_in_string, "7")
            if char == "Z":
                store.altered_string = replace_character(store.altered_string, place_in_string, "2")
        place_in_string += 1

def replace_character(strng, ind, charcter):
    returned_string = strng[0:ind] + charcter + strng[ind + 1:len(strng)]
    return returned_string

def get_vowel_count(strng):
    count = 0
    count += store.altered_string.count("A")
    count += store.altered_string.count("E")
    count += store.altered_string.count("I")
    count += store.altered_string.count("O")
    count += store.altered_string.count("U")
    return count

if __name__ == "__main__":
    main()