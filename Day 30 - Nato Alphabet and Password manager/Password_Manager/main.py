from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random letters, symbols and numbers
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine everything into one list
    password_list = password_letters + password_symbols + password_numbers

    # Shuffle the password
    shuffle(password_list)

    # Convert the list into a string
    password = "".join(password_list)

    # Clear any existing password before adding the new one
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # Get the information entered by the user
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create the dictionary that will be saved to JSON
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check that website and password are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty."
        )

    else:
        try:
            # Try to open the existing JSON file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, create a new one
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Add or update the website information
            data.update(new_data)

            # Save the updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            # Clear website and password fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    # Get the website entered by the user
    website = website_entry.get()

    try:
        # Open and read the JSON file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No data file found."
        )

    else:
        # Check if the website exists in the dictionary
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            # Clear the current email before inserting the saved one
            email_entry.delete(0, END)
            email_entry.insert(0, email)

            # Clear the password before inserting the saved one
            password_entry.delete(0, END)
            password_entry.insert(0, password)

            # Display the saved details
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )

        else:
            messagebox.showinfo(
                title="Error",
                message=f"No details for {website} exist."
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# ---------------------------- CANVAS ------------------------------- #

canvas = Canvas(height=200, width=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)


# ---------------------------- LABELS ------------------------------- #

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# ---------------------------- ENTRIES ------------------------------- #

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "diogo@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# ---------------------------- BUTTONS ------------------------------- #

search_button = Button(
    text="Search",
    width=13,
    command=find_password
)
search_button.grid(row=1, column=2)

generate_password_button = Button(
    text="Generate Password",
    command=generate_password
)
generate_password_button.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=36,
    command=save
)
add_button.grid(row=4, column=1, columnspan=2)


# Keep the window running
window.mainloop()