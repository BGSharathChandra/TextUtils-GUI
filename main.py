from tkinter import *

root = Tk()

root.minsize("750", "500")
root.maxsize("750", "500")
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

def clear_text():
    textbox.delete("1.0", "end")


# ==Nav Bar==

navf = Frame(root, bg="grey", height="40")
navf.pack(side=TOP, fill=X)

home = Button(navf, text="Home", bg="grey",fg="white", command=home, borderwidth=0)
home.place(x=50, y=9)



# ==Body of the GUI==


heading = Label(root, text="Welcome to Text Utils",fg="red", font=("Helvetica", 20)) #==Heading==
heading.pack(side = TOP,anchor="w",pady="5")



# ==Text Box==
scrollbar = Scrollbar(root)
scrollbar.place(x=610, y=100, height=243)

textbox = Text(root, bg="white", fg="red", width="50", height="10", font=("Helvetica", 15), yscrollcommand=scrollbar.set)
textbox.place(x = 60,y = 100)
scrollbar.config(command=textbox.yview)

# ==Creating Fame for our Buttons==
button_frame = Frame(root, bg="grey", width="350",height="300", borderwidth="10")
button_frame.pack(side=BOTTOM, anchor="center", pady="5")


# ==Buttons==

Convert_to_Lowercase = Button(button_frame, text="Convert to Lowercase",command=Convert_to_Lowercase, bg="blue", fg="white")
Convert_to_Lowercase.grid(row=0, column=1, padx="10", pady="10")

convert_to_uppercase = Button(button_frame, text="Convert to Uppercase", command=Convert_to_Uppercase, bg="blue", fg="white")
convert_to_uppercase.grid(row=0, column=2,padx="10",pady="10")

removepunc = Button(button_frame, text="Remove Punctuation",command=removepunc, bg="blue", fg="white") #==Remove Punctuations Button==
removepunc.grid(row = 2, column = 1,padx="10",pady="10")


clear_text = Button(button_frame, text="Clear Text",command=clear_text, bg="blue", fg="white")
clear_text.grid(row = 2, column = 2,padx="10",pady="10")




root.mainloop()