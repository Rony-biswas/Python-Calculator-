from customtkinter import *
import math

root = CTk()
root.title("Calculator")
root.geometry("420x590")
root.configure(fg_color="#17161b")

FONT = ("Arial", 20, "bold")
screen = ""

def show(value):
    global screen
    screen += value
    result.configure(text=screen)

def sinx():
    global screen
    try:
        if screen:
            f = float(screen)
            num = math.radians(f)
            sin_x = math.sin(num)
            s = round(sin_x, 6)
            screen = str(s)
            result.configure(text=screen)
    except:
        result.configure(text="Error")
        screen = ""

def cosx():
    global screen
    try:
        if screen:
            f = float(screen)
            num = math.radians(f)
            cos_x = math.cos(num)
            s = round(cos_x, 6)
            screen = str(s)
            result.configure(text=screen)
    except:
        result.configure(text="Error")
        screen = ""

def dollar(v):
    global screen
    try:
        if screen:
            bdt_amount = float(screen)
            usd_amount = round(bdt_amount / 120, 2)
            result.configure(text=f"{usd_amount} USD")
    except:
        result.configure(text="Error")
        screen = ""

def calculate():
    global screen
    try:
        reslt = eval(screen)
        screen = str(reslt)
    except:
        reslt = "Error"
        screen = ""
    result.configure(text=reslt)

def delet():
    global screen
    screen = screen[:-1]
    result.configure(text=screen)

def clear():
    global screen
    screen = ""
    result.configure(text="")


result = CTkLabel(
    root,
    text="",
    font=("Arial", 24),
    fg_color="#3b3b3b",
    text_color="white",
    height=60,
    anchor="e"
)
result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")


buttons = [
    ("C",   1, 0, "#ff6600", clear),
    ("del", 1, 1, "#ff6400", delet),
    ("sin", 1, 2, "#ff6400", sinx),
    ("cos", 1, 3, "#ff6400", cosx),

    ("7", 2, 0, "#3b3b3b", lambda: show("7")),
    ("8", 2, 1, "#3b3b3b", lambda: show("8")),
    ("9", 2, 2, "#3b3b3b", lambda: show("9")),
    ("/", 2, 3, "#3b3b3b", lambda: show("/")),

    ("4", 3, 0, "#3b3b3b", lambda: show("4")),
    ("5", 3, 1, "#3b3b3b", lambda: show("5")),
    ("6", 3, 2, "#3b3b3b", lambda: show("6")),
    ("x", 3, 3, "#3b3b3b", lambda: show("*")),

    ("1", 4, 0, "#3b3b3b", lambda: show("1")),
    ("2", 4, 1, "#3b3b3b", lambda: show("2")),
    ("3", 4, 2, "#3b3b3b", lambda: show("3")),
    ("-", 4, 3, "#3b3b3b", lambda: show("-")),

    ("0", 5, 0, "#3b3b3b", lambda: show("0")),
    (".", 5, 1, "#3b3b3b", lambda: show(".")),
    ("+", 5, 2, "#3b3b3b", lambda: show("+")),
    ("=", 5, 3, "#0042ff", calculate),
]

for text, row, col, color, command in buttons:
    CTkButton(
        root,
        text=text,
        font=FONT,
        fg_color=color,
        text_color="white",
        width=80,
        height=50,
        command=command
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
