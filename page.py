import tkinter as tk
from constante import *


fen = tk.Tk()
fen.title("SUM Blocks")

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=fen,
            relief=tk.RAISED,
            borderwidth=1,
            background="#D6ABAB",
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

# crÃ©ation du canevas


fen.mainloop()
