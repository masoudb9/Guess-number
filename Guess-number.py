from tkinter import *
from tkinter import messagebox
import random
import os
import sys
num = random.randint(1, 100)
score = 50


def click():
    global score
    var = str(e1.get())
    if int(var) > num:
        score = score - 5
        messagebox.showinfo("Info", "Your Guess is Too High")
        l1.config(text=f"Score{score}", background='red', foreground='black')
    elif int(var) < num:
        score = score - 5
        messagebox.showinfo("Info", "Your Guess is Too Low")
        l1.config(text=f"Score{score}", background='red', foreground='black')
    elif var == str(num):
        score = score + 5
        messagebox.showinfo("Congratulation", "You Won The Game")
        l1.config(text=f"Score {score}", background='lightgreen', foreground='black')
    if score == 0:
        messagebox.showwarning("Error", "you do not have enough score to play the game".title())
        window.destroy()


def click2():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def click3():
    window.destroy()


window = Tk()
window.config(background="gold")
window.title("|^_^| Guess Number")
window.minsize(280, 250)
window.maxsize(280, 250)
window.resizable(False, False)
Label(window, text="Enter A Number", border=5, background='gold', foreground='black').pack(pady=5)
e1 = Entry(window, background="white", foreground="black", width=35, border=2)
e1.pack(pady=5)
l1 = Label(window, text=f"Score{score}", background="yellow")
l1.pack(pady=5)
b1 = Button(window, text="Guess", font=("", 13, "bold"), background="lightgrey", foreground='black', border=1,
            width=15, command=click)
b2 = Button(window, text="New Game", background='lightgrey', foreground='black', border=1, font=("", 13, "bold"),
            width=15, command=click2)
b3 = Button(window, text="Exit", font=("", 13, "bold"), background='lightgrey', border=1, width=15, foreground='black',
            command=click3)
b1.pack(pady=5)
b2.pack(pady=5)
b3.pack(pady=5)


window.mainloop()
