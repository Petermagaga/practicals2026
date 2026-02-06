import random
import tkinter
from tkinter import  messagebox

from urllib3.filepost import writer

PASSWORD=[]# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letter=("A","B","C","D","e","f","g")
    number=("1","2","3","4","5","6","7","8","9")
    symbols=("$",'5/','^',"*")
    global  PASSWORD
    for l in range(10):
        PASSWORD+=random.choice(letter)
        PASSWORD +=random.choice(number)
        PASSWORD +=random.choice(symbols)
    random.shuffle(PASSWORD)
    past="".join(PASSWORD)
    password_entry.insert(0,past)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt","a") as datafile:
        website_=website_entry.get()
        email_=email_input.get()
        password=password_entry.get()

        if len(website_)==0 or len(email_)==0 or len(password)==0:
            messagebox.showinfo(title="oops",message="Please dont leave any fields empty")

        else:
            is_okay=messagebox.askyesnocancel(title="confirm if is right",message=f"These are the details entered: \n website: {website_},\n"
                                                                          f"email: {email_},\nPassword: {password}\n id it ok to save? ")
            if is_okay:
                datafile.write(f"website: {website_}email: |{email_}| password:{password}\n")
                website_entry.delete(0,tkinter.END)
                password_entry.delete(0,tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


image_canvas=tkinter.Canvas(width=200,height=200)
logo_image=tkinter.PhotoImage(file="logo.png")
image_canvas.create_image(100,100,image=logo_image)
image_canvas.grid(pady=20,padx=20,column=1,row=0)


website_label=tkinter.Label(text="Website",foreground='green')
website_label.grid(column=0,row=1,padx=20)

password_label=tkinter.Label(text="Password")
password_label.grid(column=0,row=3)

email_label=tkinter.Label(text="Email")
email_label.grid(column=0,row=2)

website_entry=tkinter.Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_input=tkinter.Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"Ptrmagaga@gmail")

password_entry=tkinter.Entry(width=20,)
password_entry.grid(column=1,row=3,padx=0)

generate_password=tkinter.Button(text="Generate Password",command=password_generator)
generate_password.grid(column=2,row=3,pady=0)

add_button =tkinter.Button(width=28,text="Add",foreground="red",background="green",
                           command=save)
add_button.grid(column=1,row=4,columnspan=2)














window.mainloop()