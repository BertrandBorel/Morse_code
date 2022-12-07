''' Morse with Python
---------------------------------------------------------------------------------------------

Objectives =   - translate a sentence into Morse code
               - translate Morse code into a sentence

---------------------------------------------------------------------------------------------

# Algorithm

## 1 : translate a sentence into Morse code :
        - capitalize text
        - adding a space (for letters separation )
        - Morse code translation with a for loop :
            - for each letter : check in the dictionary and add the result
        - return the translation

## 2 : translate Morse code into a sentence :
        - replace double spaces (word separation) by a special character (here : "|")
        - separate each world (with .split() in a list )
        - Morse code translation with a for loop :
            - for each element (x) :  - if x is the special character, replace by a space 
                                      - else : check in the dictonary and add the result
        - text formatting (with .capitalize() ) and return the result
        
--------------------------------------------------------------------------------------------- '''


# import morse dictionary and 2 functions 
from data import morse_code, text_to_morse, morse_to_text




# test sentence
test = "This is a test"


# function call
print("Morse text translation:\n", text_to_morse(test))

# function call
print("Morse code to text translation :\n", morse_to_text("_ .... .. ...   .. ...   ._   _ . ... _"))
# print("Morse code to text translation :\n", morse_to_text(text_to_morse(test)))