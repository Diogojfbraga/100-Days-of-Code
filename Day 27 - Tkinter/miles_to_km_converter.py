from tkinter import *

# -------------------- Window setup --------------------
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# -------------------- Conversion function --------------------
def milesToKm():
    # Get the number entered by the user
    miles = float(miles_entry.get())

    # Convert miles to kilometres
    result = miles * 1.609

    # Display the result in the window
    text_result.config(text=result)

    # Also print the result in the terminal
    print(result)


# -------------------- Miles input --------------------
miles_entry = Entry(width=10)
miles_entry.grid(column=2, row=1)

input_label = Label(text="Miles", font=("Arial", 12))
input_label.grid(column=3, row=1)
input_label.config(padx=10, pady=10)


# -------------------- Result display --------------------
text_label = Label(text="is equal to")
text_label.grid(column=1, row=3)

text_result = Label(text=0)
text_result.grid(column=2, row=3)

km_label = Label(text="Km")
km_label.grid(column=3, row=3)


# -------------------- Calculate button --------------------
calculate_button = Button(text="Calculate", command=milesToKm)
calculate_button.grid(column=2, row=4)


# Keep the window running
window.mainloop()