from tkinter import *

window = Tk()
window.title("Input")
window.minsize(width=500, height=300)

my_label = Label(text="Nothing", font=("Arial", 24))
my_label.pack()


def output():
    txt = input.get()
    print(txt)
    my_label.config(text=txt)


# TODO: Input
input = Entry(width=15)
input.pack()


button = Button(text="Click Me", command=output)
button.pack()


window.mainloop()
