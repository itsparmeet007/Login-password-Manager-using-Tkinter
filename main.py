from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+','-','_','=','@','^','~','[',']','{','}','?',':',';',',','.','/']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #messagebox
    if len(website)== 0 or len(password)==0:
        messagebox.showinfo(title =website,message = "Please fill the requred details")
    else:
        is_ok = messagebox.askokcancel(title = "Error",message = f"These are the details entered : \nEmail:{email}"f"\n Password : {password},\n Is it is ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website }|{email }|{password }\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0,END)
            email_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50 )

canvas = Canvas(width = 350, height = 300)
logo_img = PhotoImage(file = "logo1.png")
canvas.create_image(105,105,image = logo_img)
canvas.grid(column = 2, row = 2)

#Labels
Website_label = Label(text = "Website : ",font = ("Arial",14,"bold"))
Website_label.grid(column = 1, row = 3)
email_label = Label(text = "Email : ",font = ("Arial",14,"bold"))
email_label.grid(column = 1, row = 4)
Password_label = Label(text = "Password : ",font = ("Arial",14,"bold"))
Password_label.grid(column = 1, row = 5)

#Entries
website_entry = Entry(width = 50)
website_entry.grid(column = 2, row = 3)
website_entry.focus()
email_entry = Entry(width = 50)
email_entry.grid(column = 2, row = 4)
password_entry = Entry(width = 50)
password_entry.grid(column = 2, row = 5)

#buttons
generate_pass = Button(text = "Generate Password",width = 15,command = password_generator)
generate_pass.grid(column = 3, row = 5)
add_pass = Button(text = "Add Password",width = 45,command = save)
add_pass.grid(column = 2, row = 6)

window.mainloop()

