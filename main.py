from art import logo


morse = {'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/ '
    }

listofchar = [key for key in morse]

def morse_converter():
    text = input("Enter text to be encoded in morse code:\n").upper()

    end_text = ""

    # for item in text:
    #     flag = 0
    #     for key in morse:
    #         if item == key:
    #             end_text += morse[key] + " "
    #             flag = 1
    #             break
    #     if item == " ":
    #         end_text += "/ "
    #     elif flag == 0:
    #         end_text += item

    for t in text:
        if t in listofchar:
            end_text += morse[t] + " "
        else:
            end_text += t


    print(f"The morse is:\n{end_text}")


print(logo)
machine_on = True
while machine_on:
    switch = input("Do you want to use text to morse converter. Type 'y' or 'n':")
    if switch == 'y':
        morse_converter()
    else:
        machine_on = False
        print("Thank you!")
