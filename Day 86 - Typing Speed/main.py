# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("450x200")
window.title("Typing Speed Test")


# defining the function for the test
def game():

    # remove the start screen
    for widget in window.winfo_children():
        widget.destroy()

    words = ['programming', 'coding', 'algorithm',
             'systems', 'python', 'software']

    # select a random word
    word = random.randint(0, len(words) - 1)

    # start timer
    start = timer()

    # defining function for results of test
    def check_result():
        if entry.get().strip().lower() == words[word]:
            end = timer()

            # calculate the time taken
            result = round(end - start, 2)

            x4.config(text=f"Correct! Time: {result} seconds")

        else:
            x4.config(text="Wrong Input")

    # detect when Enter is pressed
    def enter_pressed(event):
        check_result()

    # display the selected word
    x2 = Label(window, text=words[word], font="times 20")
    x2.place(x=150, y=10)

    x3 = Label(window, text="Start Typing", font="times 20")
    x3.place(x=10, y=50)

    # text entry
    entry = Entry(window)
    entry.place(x=280, y=55)
    entry.focus_set()

    # bind Enter to check the result
    entry.bind("<Return>", enter_pressed)

    # button to submit and check results
    b2 = Button(window, text="Done",
                command=check_result, width=12, bg='grey')
    b2.place(x=150, y=100)

    # button to restart the game
    b3 = Button(window, text="Try Again",
                command=game, width=12, bg='grey')
    b3.place(x=250, y=100)

    # display the result
    x4 = Label(window, text="", font="times 12")
    x4.place(x=150, y=150)


# start screen
x1 = Label(window, text="Lets start playing..", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=12, bg='grey')
b1.place(x=150, y=100)

# calling window
window.mainloop()