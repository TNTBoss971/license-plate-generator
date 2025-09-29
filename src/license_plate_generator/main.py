
user_string = ""





def start():
    ask_for_input()

def ask_for_input():
    user_string = input("Input string you want to be translated: ")
    print(user_string)

    if len(user_string) > 7:
        print(f"Your string ({user_string}) is too long!")



start()