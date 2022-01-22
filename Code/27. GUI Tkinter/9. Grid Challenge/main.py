from tkinter import *

window = Tk()
window.title("GRID Challenge")
window.minsize(width=500, height=400)
window.config(padx=50, pady=120)

# TODO: Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# TODO: Button
button1 = Button(text="New Button")
button1.grid(row=0, column=2)

button2 = Button(text="Button")
button2.grid(row=1, column=1)

# TODO: Input
input = Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()
