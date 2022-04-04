from tkinter import *
from french_dict import french2english
import random 
import time 
import pandas as pd 

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_LIST = list(french2english.keys())
english_word = ""
french_word = ""
last_event = None



def next_card_right():
	global french_word, FRENCH_LIST
	print(f"french_word: {french_word}")
	del french2english[french_word]
	pd.DataFrame.from_dict({
		"French": list(french2english.keys()),
		"English": list(french2english.values())}
		).to_csv("data/words_to_learn.csv", index=False)
	FRENCH_LIST = list(french2english.keys())
	next_card()


def next_card():
	global last_event, english_word, french_word
	if last_event is not None:
		root.after_cancel(last_event)
	canvas.itemconfig(canvas_image, image=FRONT_IMAGE)
	french_word = random.choice(FRENCH_LIST)
	english_word = french2english[french_word]
	canvas.itemconfig(canvas_title, text="French", fill="black")
	canvas.itemconfig(canvas_word, text=french_word, fill="black")
	last_event = root.after(3000, flip_card)


def flip_card():
	global last_event, english_word, french_word
	canvas.itemconfig(canvas_image, image=BACK_IMAGE)
	canvas.itemconfig(canvas_title, text="English", fill="white")
	canvas.itemconfig(canvas_word, text=english_word, fill="white")


if __name__ == "__main__":
	root = Tk()
	root.title("Flashy")
	root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

	FRONT_IMAGE = PhotoImage(file="images/card_front.png")
	BACK_IMAGE = PhotoImage(file="images/card_back.png")
	

	# widgets 
	canvas = Canvas(width=800, height=526, bd=0, 
		highlightthickness=0, relief="ridge", bg=BACKGROUND_COLOR)
	canvas_image = canvas.create_image(400, 260, image=FRONT_IMAGE, 
		anchor=CENTER)
	canvas_title = canvas.create_text(400, 150, text="French", font=("ariel", 40, "italic"))
	canvas_word = canvas.create_text(400, 260, text="word", font=("ariel", 50, "bold"))
	next_card()

	wrong_image = PhotoImage(file="./images/wrong.png")
	wrong_button = Button(
		image=wrong_image, 
		bd=0,
		highlightthickness=0, command=next_card)
	right_image = PhotoImage(file="./images/right.png")
	right_button = Button(
		image=right_image,
		bd=0,
		highlightthickness=0, command=next_card_right)


	# layout 
	canvas.grid(column=0, row=0, columnspan=2)
	wrong_button.grid(column=0, row=1)
	right_button.grid(column=1, row=1)


	root.mainloop()