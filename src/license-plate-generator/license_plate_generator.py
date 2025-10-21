"""
License Plate Generator
By Sam Davidson

This program will take an input string
and convert it into something you might
find on a license plate
"""


from random import randint

class Storage:
    def __init__(self):
        self.user_str = ""
        self.alt_str = ""

max_len = 8
shorten = False
store = Storage()

def main():
    ask_for_input()


def ask_for_input():
    """
    asks the user for the text they will like translated
    """

    while True:
        # ask for the input
        store.user_str = input("Input string to be translated: ")
        store.alt_str = store.user_str.upper()
        if check_for_invalid_characters():
            break

    # if the text is too long, ask the user if they want it to be 
    # shortened
    if len(store.user_str) > max_len:
        print(f"{store.user_str} is longer than {max_len} characters,")
        print("and won't be able to fit on a license plate!")
        print("Do you want your text to automatically be shortened?")
        if input("(Y/N): ").upper() == "Y":
            shorten = True
        else:
            shorten = False
    else:
        shorten = False
    
    if shorten == True:
        shorten_string()


    translate_string()

def check_for_invalid_characters():
    """
    checks the user's input for any invalid characters
    """


    # invalid_characters will store the characters to print later
    invalid_characters = []

    for i in range(len(store.alt_str)):
        # the program will only accept letters, numbers, and spaces
        valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
        if not store.alt_str[i] in valid_char:
            invalid_characters.append(store.alt_str[i])

    if len(invalid_characters) > 0:
        print(f"Your text ({store.user_str}) has invalid characters!")
        print(invalid_characters)
        print("Please only input letters, numbers, and spaces!")
        return False
    else:
        return True

def shorten_string():
    """
    calls a variety of functions in an effort to reduce the length of
    of the input string
    """

    print("...")

    # FIRST ATTEMPT: remove spaces
    store.alt_str = store.alt_str.replace(" ", "")

    if len(store.alt_str) > max_len: 
        # SECOND ATTEMPT: replace words with shorter counterparts
        replace_words()

    if len(store.alt_str) > max_len:
        # THIRD ATTEMPT: remove duplicate letters
        remove_duplicates()

    if len(store.alt_str) > max_len:
        # FOURTH ATTEMPT: remove random vowels
        remove_vowels()
    
    if len(store.alt_str) > max_len:
        # The program has failed to shorten the text enough
        # ask the user if they want to continue with the current 
        # shortened text, or use their original text
        print(f"""Your text is too long. The program has failed to 
shorten it down to {max_len} characters. Would you like to continue with
the best this program can do ({store.alt_str})? If your answer is No, 
the program will continue with the input string ({store.user_str})""")
        if not input("(Y/N): ").upper() == "Y":
            store.alt_str = store.user_str.upper()
    


def replace_words():
    """
    check for any words that can be replaced with less characters
    (for > 4, your > ur, ect)
    """
    
    # use user_string becuase it has spaces
    store.alt_str = store.user_str.upper()

    # letters
    #   a
    #   b
    store.alt_str = store.alt_str.replace("BEE", "B")
    store.alt_str = store.alt_str.replace("BE", "B")
    #   c
    store.alt_str = store.alt_str.replace("SEE", "C")
    store.alt_str = store.alt_str.replace("SEA", "C")
    #   d
    #   e
    #   f
    #   g
    #   h
    #   i
    store.alt_str = store.alt_str.replace("EYE", "I")
    #   j
    #   k
    #   l
    #   m
    #   n
    #   o
    store.alt_str = store.alt_str.replace("OH", "O")
    #   p
    store.alt_str = store.alt_str.replace("PEE", "P")
    store.alt_str = store.alt_str.replace("PEA", "P")
    #   q
    store.alt_str = store.alt_str.replace("QUEUE", "Q")
    #   r
    store.alt_str = store.alt_str.replace("ARE", "R")
    #   s
    #   t
    store.alt_str = store.alt_str.replace("TEA", "T")
    #   u
    store.alt_str = store.alt_str.replace("YOU", "U")
    #   v
    #   w
    #   x
    #   y
    store.alt_str = store.alt_str.replace("WHY", "Y")
    #   z


    # numbers
    #   1
    store.alt_str = store.alt_str.replace("ONE", "1")
    #   2
    store.alt_str = store.alt_str.replace("TWO", "2")
    store.alt_str = store.alt_str.replace("TOO", "2")
    store.alt_str = store.alt_str.replace("TO", "2")
    #   3
    store.alt_str = store.alt_str.replace("THREE", "3")
    #   4
    store.alt_str = store.alt_str.replace("FOR", "4")
    store.alt_str = store.alt_str.replace("FOURTY ", "4")
    store.alt_str = store.alt_str.replace("FOUR", "4")
    #   5
    store.alt_str = store.alt_str.replace("FIVE", "5")
    #   6
    store.alt_str = store.alt_str.replace("SIX", "6")
    #   7
    store.alt_str = store.alt_str.replace("SEVEN", "7")
    #   8
    store.alt_str = store.alt_str.replace("EIGHT", "8")
    #   9
    store.alt_str = store.alt_str.replace("NINE", "9")
    #   10
    store.alt_str = store.alt_str.replace("TEN", "10")

    
# remove letters that are the same as the previous ones
def remove_duplicates():
    temp_string = ""
    l_index = 0

    for letter in store.alt_str:
        if l_index == 0 or letter != store.alt_str[l_index - 1]:
            temp_string = temp_string + letter

        
        l_index += 1
    
    # store.alt_str = store.alt_str.replace(" ", "")



def remove_vowels():
    """
    remove random vowels until the text is equal to or less than the
    limit
    """
    pos = 0
    # find vowels that are next to spaces
    vowel_indexs = find_end_vowels(store.alt_str)

    while (len(store.alt_str.replace(" ", "")) > max_len and
     get_vowel_count(store.alt_str) > 0):
        if pos > len(store.alt_str) - 1:
            pos = 0
        
        if store.alt_str[pos] in "AEIOU" and randint(0,100) > 75:
            # priortize removing vowels that are not next to spaces
            # as vowels on the end tend to be important
            if (not pos in vowel_indexs or 
            get_vowel_count(store.alt_str) <= len(vowel_indexs)):
                # replace the vowel with nothing, removing it
                store.alt_str = replace_char(store.alt_str,pos,"")
                # as the indexs are now not accurate, refind vowels
                vowel_indexs = find_end_vowels(store.alt_str)

        pos += 1
        #print(store.altered_string)
    store.alt_str = store.alt_str.replace(" ", "")


def find_end_vowels(txt: str):
    """
    find vowels that are on the start and end of words
    """
    pos = 0
    index_output = []
    # for each letter in the input
    for letter in txt:
        # if the letter is on the very start or end,
        # or it has a space on either side
        if (pos==len(txt)-1 or pos==0 or txt[pos-1]==" " or 
        txt[pos+1]==" "):
            # and its a vowel
            if letter in "AEIOU":
                # add the vowel to the output
                index_output.append(pos)
        pos += 1
    
    return index_output

def translate_string():
    convert_into_leet_speak()

    print("The translating process is complete!")
    print(f'Input: "{store.user_str}"')
    print(f'Final result: "{store.alt_str}"')


def convert_into_leet_speak():
    """
    replace random characters in string with leet speak
    """
    pos = 0
    for char in store.alt_str:
        if randint(0, 100) > 75:
            if char == "A":
                store.alt_str = replace_char(store.alt_str, pos, "4")
            if char == "B":
                store.alt_str = replace_char(store.alt_str, pos, "8")
            if char == "E":
                store.alt_str = replace_char(store.alt_str, pos, "3")
            if char == "L":
                store.alt_str = replace_char(store.alt_str, pos, "1")
            if char == "O":
                store.alt_str = replace_char(store.alt_str, pos, "0")
            if char == "S":
                store.alt_str = replace_char(store.alt_str, pos, "5")
            if char == "T":
                store.alt_str = replace_char(store.alt_str, pos, "7")
            if char == "Z":
                store.alt_str = replace_char(store.alt_str, pos, "2")
        pos += 1

def replace_char(strng, ind, character):
    """
    replace the character at the index of a given string and replace it
    with an other character 
    """
    returned_string = strng[0:ind]+character+strng[ind+1:len(strng)]
    return returned_string

def get_vowel_count(strng):
    """
    counts the number of vowels in a string
    """
    count = 0
    count += strng.count("A")
    count += strng.count("E")
    count += strng.count("I")
    count += strng.count("O")
    count += strng.count("U")
    return count

if __name__ == "__main__":
    main()