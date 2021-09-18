from tkinter import *
root = Tk()

root.minsize("850", "550")


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




# ==Body of the GUI== #
# ==Frames== #
button_frame = Frame(root,bd = 2,relief = RIDGE,bg = "white",width = 200)
button_frame.pack(side = RIGHT,fill = Y)


# ==Text Box and Scroll Bar==
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y)

textbox = Text(root, bg="white", fg="red", width="50", height="10", font=("Helvetica", 15), yscrollcommand=scrollbar.set)
textbox.pack(fill= BOTH, expand=1)
scrollbar.config(command=textbox.yview)



# ==Creating Fame for our Buttons==



# ==Buttons and Labels==
Label_Convert = Label(button_frame, text="Convert To",compound = LEFT,padx = 5 ,anchor="w",font=("times new roman", 20, "bold"),bg="white", bd=3).pack(side=TOP, fill=X)
Convert_to_Lowercase = Button(button_frame, text="Lower Case",compound = LEFT,padx = 5 ,anchor="w",command = Convert_to_Lowercase ,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
                        
convert_to_uppercase = Button(button_frame, text="Upper Case",compound = LEFT,padx = 5 ,anchor="w",command = Convert_to_Uppercase,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

Label_Remove = Label(button_frame, text="Remove",compound = LEFT,padx = 5 ,anchor="w",font=("times new roman", 20, "bold"),bg="white", bd=3).pack(side=TOP, fill=X)

removepunc = Button(button_frame, text="Punctuations",compound = LEFT,padx = 5 ,anchor="w",command = removepunc,font=("times new roman", 20, "bold"),
                            bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

remove_all_lines = Button(button_frame, text="All Lines",compound = LEFT,padx = 5 ,anchor="w",command = remove_all_lines,font=("times new roman", 20, "bold"),
                            bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

remove_extraspace = Button(button_frame, text="Extra Spaces",  compound=LEFT, padx=5, anchor="w",command = extra_space_remover, font=("times new roman", 20, "bold"),
                              bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
                            
remove_numbers = Button(button_frame, text="Numbers",compound = LEFT,padx = 5 ,anchor="w",command = remove_numbers,font=("times new roman", 20, "bold"),
                            bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

clear_text = Button(button_frame, text="Clear",compound = LEFT,padx = 5 ,anchor="w",command = clear_text,font=("times new roman", 20, "bold"),
                            bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)


# clear_text = Button(button_frame, text="Clear Text",cursor="hand2",command=clear_text, bg="blue", fg="white")
# clear_text.grid(row = 4, column = 2,padx="10",pady="10")




root.mainloop()
