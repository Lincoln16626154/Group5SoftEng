from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Radiobutton
from newsRequest import makeRequest

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Application Title")

        self.generateHeadlines = Button(master, text="Generate", command=self.generateHeadlines)
        self.generateHeadlines.pack()

        self.headlineLabel = Label(master, text="Headlines:")
        self.headlineLabel.pack()

        self.headlines = Label(master, text="")
        self.headlines.pack()
        

    def generateHeadlines(self): 
        headlines = makeRequest()
        self.headlines['text'] = ""
        for item in headlines:
            self.headlines['text'] += item + "\n"

        

def checkKeywords():
    # txt = self.exampleTextInput.get()
    # print(txt)
    with open('data_file2.json'):
        for line in file.readlines:
            getTitles()
        if x == re.search(txt):
            print("yes")
        else:
            print("no")




root = Tk()
my_gui = GUI(root)
root.mainloop()
