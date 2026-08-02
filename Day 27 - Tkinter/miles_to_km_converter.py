from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=100, pady=200)





miles_entry = Entry(width=10)

miles_entry.grid(column=2, row=1)
input_label = Label(text="Miles", font=("Arial", 12))
input_label.grid(column=3, row=1)
input_label.config(padx=10, pady=10)

def milesToKem():
    result = int(miles_entry.get()) * 1.609
    text_result.config(text=result)
    print(result)
    



text_label = Label(text="is equal to ")
text_label.grid(column=1, row=3)


text_result = Label(text=0)
text_result.grid(column=2, row=3)

km_label = Label(text="Km")
km_label.grid(column=3, row=3)


calculate_button = Button(text="Calculate", command=milesToKem)
calculate_button.grid(column=2, row=4)

# print(result)

window.mainloop()