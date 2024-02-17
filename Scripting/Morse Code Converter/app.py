from config import art, morse_codes
import os


def morse_code_converter(message):
    morse_code = ""
    for i in message:
        morse_code += morse_codes[i.lower()]
    return f"Here is your message in morse code format:\n{morse_code}"

    
clear = lambda: os.system('clear')
is_running = True
while is_running:
    print(art)
    print("Welcome to the Morse Code Generator")
    message = input("Type your message: ")
    print(morse_code_converter(message))
    if input("type 'y' to continue or 'n' to end the program.\n").lower() == "y":
        clear()
        is_running
    else:
        print("Goodbye!")
        is_running = False
    