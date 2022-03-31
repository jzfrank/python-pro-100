import tkinter as tk

window = tk.Tk()
# window.minsize(width=400, height=200)
window.config(padx=20, pady=10)
window.title("Mile to Km Converter")

user_input = tk.Entry(width=10)
user_input.grid(column=1, row=0)
user_input.config(align="right")

# blank = tk.Label(text=" ")
# blank.grid(column=0, row=0)
tk.Label(text="Miles").grid(column=2, row=0)
tk.Label(text="is equal to").grid(column=0, row=1)

kilo = tk.Label(text="0")
kilo.grid(column=1, row=1)

tk.Label(text="Km").grid(column=2, row=1)

def on_click():
    miles = float(user_input.get())
    km = miles * 1.689
    kilo.config(text=km)

calc_btn = tk.Button(text="Calculate",
                     command=on_click)
calc_btn.grid(column=1, row=2)


window.mainloop()