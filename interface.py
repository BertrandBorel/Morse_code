# importation : Tkinter
from tkinter import *
# importation : morse code dictionary
from data import morse_code

# initialization
root = Tk()

# title
root.title("Morse code application")
# size 
root.geometry("640x480")
# max and min size
root.maxsize(800,600)
root.minsize(640,480)
# background color
root.config(bg = "#87CEEB")

# user input
user_input1 = StringVar()
user_input2 = StringVar()

# Function 1    
def text_to_morse():
    input= user_input1.get()
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
    
    label = Label(root, text=code)
    label.grid()

# Function 2
def morse_to_text():
    input= user_input2.get()
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
    
    label = Label(root, text=result)
    label.grid()


# Label
label1 = Label(root, text="Morse code application", bg = "#87CEEB", fg="blue", font=("Arial", 25))
label1.grid(row=0, column=0)


# Input 1
input1 = Entry(root, textvariable=user_input1, width=20)
input1.grid(row=1, column=0)

# Add button 1 :
button1 = Button(root, text = "Text to morse", command=text_to_morse,  width=20)
button1.grid(row=1, column=1,  padx=15, pady=15)

# Input 2
input2 = Entry(root, textvariable=user_input2, width=20)
input2.grid(row=2, column=0)

# Add button 2 :
bouton2 = Button(root, text = "Morse to text", command=morse_to_text, width=20)
bouton2.grid(row=2, column=1, padx=15, pady=15)

# Exit button
bouton3 = Button(root, text = "Exit", command=root.destroy, width=20)
bouton3.grid(row=3, column=1, padx=30, pady=30)

# display
root.mainloop()