from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters)for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers)for _ in range(nr_numbers)]

    password_list = password_letter+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!', message=" Please do not leave the field empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)  # take the data from json to python and it is a dictionary format
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updateing old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
               #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0,END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message='No Data File Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title='website', message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", messag =f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady =50)

canvas = Canvas(width=200, height =200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(column=1, row=0)

#Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entry box
web_entry = Entry(width=20)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"meichi308@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

#Buttons
password_gen_but = Button(text = "Generate Password", width = 11, command= generate_password)
password_gen_but.grid(column =2, row= 3)

add_but = Button(text = "Add", width=33, command= save)
add_but.grid(column =1, row= 4,columnspan=2)

search_but = Button(text = "Search", width = 11, command = find_password)
search_but.grid(column =2, row= 1)

window.mainloop()