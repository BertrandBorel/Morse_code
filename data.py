'''Morse with Python
---------------------------------------------------------------------------------------------

- Morse code dictionary 
- function : translate a sentence into Morse code
- function : translate morse to text

---------------------------------------------------------------------------------------------'''


# Dictionary containing morse code
morse_code = { 
                # letters :
                "A" : ".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", 
                "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.",
                 "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", 
                 # word separation space (*2)
                 " ":" ",
                 # numbers :
                 "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", 
                 "8":"---..", "9":"----.", "0":"-----"
                 
                 }


# # test sentence
# test = "This is a test"



# Function : translate a sentence into Morse code
def text_to_morse(input):
    # capitalize text
    input = input.upper()
    output = ""
    # Adding a space (for letters separation)
    for x in input :
        output = output + x + " "
    
    # Morse code translation
    code = ""
    for x in output :
            value = morse_code[x]
            code = code + value 
    
    return code



# function: translate morse to text
def morse_to_text(input):
    # replace double spaces (word separation)
    input = input.replace("  ", " | ")
    # separation of each word 
    input = input.split()
    
    # morse code translation
    result = ""
    for x in input :
            if x == "|":
                # add a space
                result = result + " "
            else :
                # add the key of the dictionary 
                key = list(morse_code.keys())[list(morse_code.values()).index(x)]
                result = result + key
    
    # text formatting
    result = result.capitalize()
    
    return result



# # function call
# print("Morse text translation:\n", text_to_morse(test))

# # function call
# print("Morse code to text translation :\n", morse_to_text(" _ .... .. ...   .. ...     ._   _ . ... _ "))