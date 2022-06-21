message = input("Type a message to convert to morse. ").upper()

morse_code_bank = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "......."
}

morse_code = ""

def encode():
    global morse_code
    for i in message:
        if i in morse_code_bank:
            new = morse_code_bank[i]
            morse_code = morse_code + new + " "
    print(f"Your morse code is: {morse_code}")

decoded_morse = ""
def decode():
    global morse_code
    global decoded_morse
    decoded_list = morse_code.split()
    for item in decoded_list:
        for key, value in morse_code_bank.items():
            if item == value:
                decoded_morse += key
    print(f"Your decoded message is: {decoded_morse.lower()}")



def playgame():
    if message != "":
        encode()
        question = input("Would you like to decode the message?(yes/no): ").lower()
        if question == "yes":
            decode()
playgame()
