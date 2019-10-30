from tkinter import Tk, Label, Button

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Application Title")

        self.label = Label(master, text="This is a label")
        self.label.pack()

        self.example_button = Button(master, text="This is button", command=self.buttonFunction)
        self.example_button.pack()

    def buttonFunction(self):
        print("button function called")

root = Tk()
my_gui = GUI(root)
root.mainloop()
