# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from generate_pswd import generate_pswd
import pyperclip
import os 

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pswd():
    website = website_input.get()
    email = email_input.get()
    pswd = pswd_input.get()
    if any(len(i) == 0 for i in [website, email, pswd]):
        print("Please don't leave any fields empty!!")
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                   f"\nPassword: {pswd} \n Is it ok to save?")
    if not is_ok:
        return
    else:
        with open(".pswd.txt", "a") as file:
            file.write(
                f"{website} | {email} | {pswd} \n"
            )
        for entry in [website_input, pswd_input]:
            entry.delete(0, END)


def generate_pswd_on_click():
    password = generate_pswd()
    pswd_input.delete(0, END)
    pswd_input.insert(0, password)
    root.clipboard_clear()
    root.clipboard_append(password)

# ---------------------------- UI SETUP ------------------------------- #


if __name__ == "__main__":
    TEST_EMAIL = os.environ["TEST_EMAIL"]
    print("END:", END)
    print(type(END))
    root = Tk()
    root.config(padx=50, pady=50)
    canvas = Canvas(root, width=200, height=200)
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    canvas.create_image(100, 100, anchor=CENTER, image=img)
    canvas.grid(column=1, row=0)

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    website_input = Entry(width=35)
    website_input.grid(column=1, row=1, columnspan=2)
    website_input.focus()

    email_label = Label(text="Email/Username:")
    email_label.grid(column=0, row=2)

    email_input = Entry(width=35)
    email_input.grid(column=1, row=2, columnspan=2)
    email_input.insert(0, TEST_EMAIL)

    pswd_label = Label(text="Password:")
    pswd_label.grid(column=0, row=3)

    pswd_input = Entry(width=21)
    pswd_input.grid(column=1, row=3)

    generate_pswd_button = Button(text="Generate Password", command=generate_pswd_on_click)
    generate_pswd_button.grid(column=2, row=3)

    add_button = Button(text="Add", width=36, command=save_pswd)
    add_button.grid(column=1, row=4, columnspan=2)
    root.mainloop()
