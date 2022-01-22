from tkinter import *

window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=300)

# TODO: Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.place(x=20, y=20)

# TODO: Button
button = Button(text="Click Me")
button.place(x=40, y=70)

# TODO: Entry
input = Entry(width=10)
input.place(x=70, y=100)

window.mainloop()
