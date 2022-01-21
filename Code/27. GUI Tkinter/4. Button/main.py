from tkinter import *

window = Tk()
window.title("Button")
window.minsize(width=500, height=300)

my_label = Label(text="Button", font=("Arial", 24))
my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text="New Button")


def button_clicked():
    # print("I got clicked.")
    my_label.config(text="Button Got Clicked.")


button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
