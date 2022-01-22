from tkinter import *

window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=300)

# TODO: Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

# TODO: Button
button = Button(text="Click Me")
button.grid(row=1, column=1)

# TODO: Entry
input = Entry(width=10)
input.grid(row=2, column=2)

window.mainloop()
