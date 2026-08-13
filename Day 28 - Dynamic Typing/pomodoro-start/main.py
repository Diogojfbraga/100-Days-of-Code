from tkinter import *
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    reps = 0

    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # Odd repetitions are work sessions
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)

    else:
        completed_work_sessions = reps // 2

        # Long break after every 5 completed work sessions
        if completed_work_sessions % 5 == 0:
            timer_label.config(text="Long Break", fg=RED)
            count_down(long_break_seconds)

        else:
            timer_label.config(text="Break", fg=PINK)
            count_down(short_break_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(
        timer_text,
        text=f"{minutes:02d}:{seconds:02d}"
    )

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        timer = None

        # Add a check mark when a work session finishes
        if reps % 2 != 0:
            completed_work_sessions = (reps + 1) // 2
            check_marks.config(text="✓" * completed_work_sessions)

        # Automatically start the next work session or break
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer heading
timer_label = Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 50)
)
timer_label.grid(column=1, row=0)

# Tomato canvas
canvas = Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightthickness=0
)

image_path = Path(__file__).parent / "tomato.png"
tomato_png = PhotoImage(file=image_path)

canvas.create_image(100, 112, image=tomato_png)

timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)

canvas.grid(column=1, row=1)

# Start button
start_button = Button(
    text="Start",
    highlightthickness=0,
    command=start_timer
)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer
)
reset_button.grid(column=2, row=2)

# Completed work sessions
check_marks = Label(
    text="",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 18, "bold")
)
check_marks.grid(column=1, row=3)

window.mainloop()