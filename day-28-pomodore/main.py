from tkinter import *

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

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkbox_label.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        if reps % 4 == 0:
            timer_label.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN * 60)
        else:
            timer_label.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    print("count: ", count)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        if reps % 2 == 1:
            checkbox_label.config(
                text=checkbox_label.cget("text") + "√"
            )
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
if __name__ == "__main__":
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    canvas = Canvas(width=200, heigh=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
    canvas.grid(column=1, row=1)

    timer_label = Label(text="Timer" , bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
    timer_label.grid(column=1, row=0)

    start_button = Button(text="start", highlightbackground=YELLOW, command=start_timer)
    start_button.grid(column=0, row=2)

    reset_button = Button(text="reset", highlightbackground=YELLOW, command=reset_timer)
    reset_button.grid(column=2, row=2)

    checkbox_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    checkbox_label.grid(column=1, row=3)

    window.mainloop()