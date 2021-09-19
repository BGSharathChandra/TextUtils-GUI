from tkinter import *
from tkinter import filedialog


root = Tk()


root.title("TextUtils")

# ==Functions==
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


def open_file():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Text files","*.txt"))) 
    textbox.delete("1.0", "end")
    f = open(filename, "r")
    file_txt = f.read()
    f.close()
    textbox.insert(END, file_txt)



def save_file():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes = (("all files","*.*"),("Text files","*.txt"), ("Python Files","*.py")))
    if f is None:
        return
    text2save = str(textbox.get(1.0, END))
    f.write(text2save)
    f.close()



def clear_text():
    textbox.delete("1.0", "end")




# ==Body of the GUI== #
# ==Frames== #
# !!! Do not Change the Posistion of this Frame !!!
button_frame = Frame(root,bd = 2,relief = RIDGE,bg = "white",width = 200)
button_frame.pack(side = RIGHT,fill = Y)



# ==Text Box and Scroll Bar==
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y)


textbox = Text(root, bg="white", fg="red", width="50", height="10", font=("Helvetica", 15), yscrollcommand=scrollbar.set)
textbox.pack(fill= BOTH, expand=1)
scrollbar.config(command=textbox.yview)






# ==Buttons and Labels==
Label_Convert = Label(button_frame, text="Convert To",compound = LEFT,padx = 5 ,anchor="w",font=("times new roman", 20, "bold"),bg="white", bd=3).pack(side=TOP, fill=X)
Convert_to_Lowercase = Button(button_frame, text="Lower Case",compound = LEFT,padx = 5 ,anchor="w",command = Convert_to_Lowercase ,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
Convert_to_Lowercase.pack(side=TOP, fill=X)
                        
convert_to_uppercase = Button(button_frame, text="Upper Case",compound = LEFT,padx = 5 ,anchor="w",command = Convert_to_Uppercase,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
convert_to_uppercase.pack(side=TOP, fill=X)

Label_Remove = Label(button_frame, text="Remove",compound = LEFT,padx = 5 ,anchor="w",font=("times new roman", 20, "bold"),bg="white", bd=3)
Label_Remove.pack(side=TOP, fill=X)

removepunc = Button(button_frame, text="Punctuations",compound = LEFT,padx = 5 ,anchor="w",command = removepunc,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
removepunc.pack(side=TOP, fill=X)

remove_all_lines = Button(button_frame, text="All Lines",compound = LEFT,padx = 5 ,anchor="w",command = remove_all_lines,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
remove_all_lines.pack(side=TOP, fill=X)

remove_extraspace = Button(button_frame, text="Extra Spaces",  compound=LEFT, padx=5, anchor="w",command = extra_space_remover, font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
remove_extraspace.pack(side=TOP, fill=X)
                            
remove_numbers = Button(button_frame, text="Numbers",compound = LEFT,padx = 5 ,anchor="w",command = remove_numbers,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
remove_numbers.pack(side=TOP, fill=X)

open_file = Button(button_frame, text="Open File",compound = LEFT,padx = 5 ,anchor="w",command = open_file,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
open_file.pack(side=TOP, fill=X)

save_file = Button(button_frame, text="Save File",compound = LEFT,padx = 5 ,anchor="w",command = save_file,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
save_file.pack(side=TOP, fill=X)

clear_text = Button(button_frame, text="Clear",compound = LEFT,padx = 5 ,anchor="w",command = clear_text,font=("times new roman", 20, "bold"),bg="white", bd=3, cursor="hand2")
clear_text.pack(side=TOP, fill=X)


# == Binding Entry and Leave for the Buttons - Changing Color on Hover == 
colorOnHover = "Red"
colorOnLeave = "White"
Convert_to_Lowercase.bind('<Enter>', func=lambda e: Convert_to_Lowercase.config(background=colorOnHover))
Convert_to_Lowercase.bind('<Leave>', func=lambda e: Convert_to_Lowercase.config(background=colorOnLeave))

convert_to_uppercase.bind('<Enter>', func=lambda e: convert_to_uppercase.config(background=colorOnHover))
convert_to_uppercase.bind('<Leave>', func=lambda e: convert_to_uppercase.config(background=colorOnLeave))

removepunc.bind('<Enter>', func=lambda e: removepunc.config(background=colorOnHover))
removepunc.bind('<Leave>', func=lambda e: removepunc.config(background=colorOnLeave))

remove_all_lines.bind('<Enter>', func=lambda e: remove_all_lines.config(background=colorOnHover))
remove_all_lines.bind('<Leave>', func=lambda e: remove_all_lines.config(background=colorOnLeave))

remove_extraspace.bind('<Enter>', func=lambda e: remove_extraspace.config(background=colorOnHover))
remove_extraspace.bind('<Leave>', func=lambda e: remove_extraspace.config(background=colorOnLeave))

remove_numbers.bind('<Enter>', func=lambda e: remove_numbers.config(background=colorOnHover))
remove_numbers.bind('<Leave>', func=lambda e: remove_numbers.config(background=colorOnLeave))

open_file.bind('<Enter>', func=lambda e: open_file.config(background=colorOnHover))
open_file.bind('<Leave>', func=lambda e: open_file.config(background=colorOnLeave))

save_file.bind('<Enter>', func=lambda e: save_file.config(background=colorOnHover))
save_file.bind('<Leave>', func=lambda e: save_file.config(background=colorOnLeave))

clear_text.bind('<Enter>', func=lambda e: clear_text.config(background=colorOnHover))
clear_text.bind('<Leave>', func=lambda e: clear_text.config(background=colorOnLeave))




root.mainloop()