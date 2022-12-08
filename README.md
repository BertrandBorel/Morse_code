# Morse code  with Python

## Objectives :  
               - translate a sentence into Morse code
               - translate Morse code into a sentence

## Algorithm :

### 1 : translate a sentence into Morse code :
        - capitalize text
        - adding a space (for letters separation )
        - Morse code translation with a for loop :
            - for each letter : check in the dictionary and add the result
        - return the translation
        
        
### 2 : translate Morse code into a sentence :
        - replace double spaces (word separation) by a special character (here : "|")
        - separate each world (with .split() in a list )
        - Morse code translation with a for loop :
            - for each element (x) :  - if x is the special character, replace by a space 
                                      - else : check in the dictonary and add the result
        - text formatting (with .capitalize() ) and return the result


---

## Creation of a graphical interface (with Tkinter)


<img width="500" alt="Capture" src="https://user-images.githubusercontent.com/95342688/206486649-8d6325fb-a413-4c54-85e5-9facc7b63e0f.PNG">
