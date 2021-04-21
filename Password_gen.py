from tkinter import * 
import random, string 
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(FALSE, FALSE)
root.title("Zia - PASSWORD GENERATOR")

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack(side = BOTTOM)
Label(root, text = 'A Zia Din Project', font ='arial 15 bold').pack(side = BOTTOM)

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len , width = 15).pack()

pass_string = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    
    for y in range(pass_len.get() - 0):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    pass_string.set(password)

Button(root, text = "GENERATE PASSWORD" , command = 
Generator ).pack(pady=5)

Entry(root , textvariable = pass_string).pack()

def Copy_password():
    pyperclip.copy(pass_string.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

root.mainloop()

