# import tkinter

# window = tkinter.Tk()

# window.title("My first GUI program")
# window.minsize(width=500, height=300)



# my_label = tkinter.Label(text="I am a label")
# my_label.pack()

# window.mainloop()


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum



print(add(1,2,3))