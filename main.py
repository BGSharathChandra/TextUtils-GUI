from tkinter import *

root = Tk()

root.minsize("750", "550")
root.maxsize("750", "550")
root.title("TextUtils")

# ==Functions==
def home():
    # ==Changing the Colour of the Buttons==
    home.config(bg="green")


def Convert_to_Lowercase():
    text = textbox.get(1.0, END)
    analyzed_text = text.lower()
    textbox.delete("1.0", "end")
    textbox.insert(END,analyzed_text)


def Convert_to_Uppercase():
    text = textbox.get("1.0", "end")
    analyzed_text = text.upper()
    textbox.delete("1.0", "end")
    textbox.insert(END,analyzed_text)

def removepunc():
    text = textbox.get(1.0, END)
    analyzed_text = text.upper()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed_text = ""
    
    for char in text:
        if char not in punctuations:
            analyzed_text = analyzed_text+char
    
    textbox.delete("1.0", "end")
    textbox.insert(END,analyzed_text)


def remove_all_lines():
    text = textbox.get(1.0, END)
    analyzed_text = text.replace('\n', '')
    textbox.delete("1.0", "end")
    textbox.insert(END,analyzed_text)

def extra_space_remover():
    text = textbox.get(1.0, END)
    analyzed_text = ""
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1]==" "):
            analyzed_text = analyzed_text + char
    textbox.delete("1.0", "end")
    textbox.insert(END,analyzed_text)


def remove_numbers():
    text = textbox.get(1.0, END)
    analyzed_text = text.upper()
    numbers = '''1234567890'''
    analyzed_text = ""
    
    for char in text:
        if char not in numbers:
            analyzed_text = analyzed_text+char
    
    textbox.delete("1.0", "end")
    textbox.insert(END,analyzed_text)


def clear_text():
    textbox.delete("1.0", "end")


# ==Nav Bar==

navf = Frame(root, bg="grey", height="40")
navf.pack(side=TOP, fill=X)

home = Button(navf, text="Home", bg="grey",fg="white", command=home, borderwidth=0)
home.place(x=50, y=9)



# ==Body of the GUI==


heading = Label(root, text="Welcome to Text Utils",fg="red", font=("Helvetica", 20)) #==Heading==
heading.pack(side = TOP,anchor="center",pady="5")



# ==Text Box and Scroll Bar==
scrollbar = Scrollbar(root)
scrollbar.place(x=650, y=99, height=235)

textbox = Text(root, bg="white", fg="red", width="50", height="10", font=("Helvetica", 15), yscrollcommand=scrollbar.set)
textbox.place(x = 95,y = 100)
scrollbar.config(command=textbox.yview)



# ==Creating Fame for our Buttons==
button_frame = Frame(root, bg="grey", width="350",height="300", borderwidth="10",pady = 10)
button_frame.place(x = 150,y = 360)


# ==Buttons==

Convert_to_Lowercase = Button(button_frame, text="Convert to Lowercase",cursor="hand2",command=Convert_to_Lowercase, bg="blue", fg="white")
Convert_to_Lowercase.grid(row=0, column=1, padx="10", pady="10")

convert_to_uppercase = Button(button_frame, text="Convert to Uppercase",cursor="hand2", command=Convert_to_Uppercase, bg="blue", fg="white")
convert_to_uppercase.grid(row=0, column=2,padx="10",pady="10")

removepunc = Button(button_frame, text="Remove Punctuation",cursor="hand2",command=removepunc, bg="blue", fg="white") #==Remove Punctuations Button==
removepunc.grid(row = 0, column = 3,padx="10",pady="10")


remove_all_lines = Button(button_frame, text="Remove All Lines",cursor="hand2",command=remove_all_lines, bg="blue", fg="white")
remove_all_lines.grid(row = 2, column = 1,padx="10",pady="10")

remove_extraspace = Button(button_frame, text="Remove Extra Space",cursor="hand2",command=extra_space_remover, bg="blue", fg="white")
remove_extraspace.grid(row = 2, column = 2,padx="10",pady="10")

remove_numbers = Button(button_frame, text="Remove Numbers",cursor="hand2",command=remove_numbers, bg="blue", fg="white")
remove_numbers.grid(row = 2, column = 3,padx="10",pady="10")


clear_text = Button(button_frame, text="Clear Text",cursor="hand2",command=clear_text, bg="blue", fg="white")
clear_text.grid(row = 4, column = 2,padx="10",pady="10")




root.mainloop()
