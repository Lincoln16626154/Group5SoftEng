from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Radiobutton



class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Application Title")

        self.exampleLabel = Label(master, text="This is a label")       

        self.exampleTextInput = Entry(master)
        
        self.exampleButton = Button(master, text="This is button", command=self.buttonFunction)
        
        self.exampleRadioBtn = Radiobutton(master, text="This is a radio button", value = 1)
        self.exampleRadioBtn2 = Radiobutton(master, text="This is another radio button", value = 2)

# LAYOUT

        self.exampleLabel.grid(row=0, column=0, sticky=W)

        self.exampleTextInput.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.exampleButton.grid(row=2, column=0)

        self.exampleRadioBtn.grid(row=3, column = 0)
        self.exampleRadioBtn2.grid(row=4, column = 0)

    def buttonFunction(self):
        print("button function called")






root = Tk()
my_gui = GUI(root)
root.mainloop()
