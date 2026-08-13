from tkinter import *
from tkinter import messagebox
from pathlib import Path
from random import choice, randint, shuffle
import pyperclip
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def password_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
   


# ---------------------------- SAVE PASSWORD ------------------------------- #




def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if website == "" or password == "":
            messagebox.showinfo(title="Incomplete Fields", message="Some Fields are missing")
    else:

        is_ok = messagebox.askyesnocancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n is it ok to save?")

        
        

            

        if is_ok:
            with open("passwordFile.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Get the logo image from the same folder as main.py
image_path = Path(__file__).parent / "logo.png"
logo_png = PhotoImage(file=str(image_path))

# Create canvas
canvas = Canvas(
    width=200,
    height=200,
    highlightthickness=0
)

# Put image in the centre of the canvas
canvas.create_image(
    100,
    100,
    image=logo_png
)

# Put canvas on the window
canvas.grid(row=0, column=1)


# Labels

website_label = Label(text="Website:",
                     font=FONT_NAME,
                     )
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=FONT_NAME)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT_NAME)
password_label.grid(row=3, column=0)






# Entry
website_entry = Entry( width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "test@gmail.com")

password_entry = Entry(width=21 )
password_entry.grid(row=3, column=1,columnspan=2, sticky="w")


#Buttons
generate_password_button = Button(text="Generate Passowrd", command=password_gen)
generate_password_button.grid(row=3, column=2, sticky="w")

add_password_button = Button(command=save, text="Add", width=36)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()