"""
License Plate Generator
By Sam Davidson


"""


user_string = ""
altered_string = ""
shorten = False


def main():
    ask_for_input()



# ask the user for the text they will like translated
def ask_for_input():
    global user_string, altered_string

    while True:
        # ask for the input
        user_string = input("Input string you want to be translated: ")
        altered_string = user_string.upper()
        if check_for_invalid_characters():
            break

    # if the text is too long, ask the user if they want it to be shortened
    if len(user_string) > 7:
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
    global altered_string, user_string

    print("...")

    # FIRST ATTEMPT: remove spaces
    altered_string = altered_string.replace(" ", "")

    if len(altered_string) > 7: 
        # SECOND ATTEMPT: replace words with shorter counterparts
        replace_words()

    if len(altered_string) > 7:
        # THIRD ATTEMPT: remove duplicate letters
        remove_duplicates()

    if len(altered_string) > 7:
        # FOURTH ATTEMPT: remove random vowels
        remove_vowels()
    
    if len(altered_string) > 7:
        # The program has failed to shorten the text enough
        # ask the user if they want to continue with the current shortened text, or use their original text
        print("Your text is too long. The program has failed to shorten it down to 7 characters.")
        print(f"Would you like to continue with the best this program can do ({altered_string})?")
        print(f"If your answer is No, the program will continue with the orignal string ({user_string})")
        if not input("(Y/N): ").upper() == "Y":
            altered_string = user_string.upper()

# check for any words that can be replaced with less characters (for > 4, your > ur, ect)
def replace_words():
    global altered_string
    
    # use user_string becuase it has spaces

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
    #   2
    #   3
    #   4
    altered_string = altered_string.replace("FOR", "4")
    altered_string = altered_string.replace("FOURTY ", "4")
    altered_string = altered_string.replace("FOUR", "4")
    #   5
    #   6
    #   7
    #   8
    #   9
    #   10

# remove letters that are the same as the previous ones
def remove_duplicates():
    pass

# remove random vowels until the text fits
def remove_vowels():
    pass

if __name__ == "__main__":
    main()