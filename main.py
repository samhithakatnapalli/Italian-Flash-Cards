import random
import pandas
from tkinter import *

window  = Tk()
window.minsize(600,500)
window.title("Flashy Flash")
window.config(bg= "#90b2d1")

FRONT_CARD = PhotoImage(file= "flash-card.png")
BACK_CARD = PhotoImage(file="english-side-card.png")
SCORE = 0

data = pandas.read_csv("italian_words - Sheet1.csv", header = 0)
to_learn = data.to_dict(orient="records")
current_card = {}

def italian_side():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(title, text="Italian")
    canvas.itemconfig(word, text=f"{current_card["French"]}")
    canvas.itemconfig(flash_card, image=FRONT_CARD)

    timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(flash_card, image = BACK_CARD)
    canvas.itemconfig(title,text="English",fill="black")
    canvas.itemconfig(word, text=f"{current_card["English"]}", fill="black")

def right_ans():
    global SCORE
    SCORE += 1
    update_score()
    italian_side()

timer = window.after(5000, func=flip_card)

score_text = Label(text = f"Score: {SCORE}", font = ("Verdana",16,"bold"), bg= "#90b2d1", fg="#2b5174")
score_text.place(x = 250, y = 20)
def update_score():
    score_text.config(text = f"Score: {SCORE}")

canvas = Canvas(window, width = 420, height = 270, bg= "#90b2d1", highlightthickness = 0)
flash_card = canvas.create_image(215, 138, image = FRONT_CARD)
title = canvas.create_text(215,55,text= "", font= ("Verdana",16,"italic"))
word = canvas.create_text(215,130,text= "Word", font= ("Verdana",25,"bold"))
canvas.place(x = 90, y = 60)

right_image = PhotoImage(file="right.png")
right_button = Button(window, image=right_image, bg= "#90b2d1", command= right_ans,highlightthickness=0, borderwidth=0)
right_button.place(x = 200, y = 380)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(window, image=wrong_image, bg= "#90b2d1",command= italian_side, highlightthickness=0, borderwidth=0)
wrong_button.place(x = 340, y = 380)

italian_side()

window.mainloop()