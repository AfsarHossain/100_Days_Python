import tkinter

window = tkinter.Tk()

window.title("My First GUI Program.")
window.minsize(width=500, height=300)

# TODO: Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 25, "italic"))
my_label.pack(expand=True)  # left, right, bottom, Center-> expand=True

window.mainloop()
