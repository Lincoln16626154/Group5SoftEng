from tkinter import *
from newsRequest import makeRequest, getNewsSources

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Application Title")

        self.keywordLabel = Label(master, text="Enter Keywords seperated by spaces")       
        self.keywordLabel.pack()

        self.keywordInput = Entry(master)
        self.keywordInput.pack()

        self.sourceSelection = [IntVar(),IntVar(),IntVar(),IntVar()]

        self.sourcesLabel = Label(master, text="Select news sources")
        self.sourcesLabel.pack()

        self.check0 = Checkbutton(master, text="Source A", variable=self.sourceSelection[0])
        self.check0.pack()

        self.check1 = Checkbutton(master, text="Source B", variable=self.sourceSelection[1])
        self.check1.pack()

        self.check2 = Checkbutton(master, text="Source C", variable=self.sourceSelection[2])
        self.check2.pack()

        self.check3 = Checkbutton(master, text="Source D", variable=self.sourceSelection[3])
        self.check3.pack()

        self.generateHeadlines = Button(master, text="Generate", command=self.generateHeadlines)
        self.generateHeadlines.pack()

        self.headlineLabel = Label(master, text="Headlines:")
        self.headlineLabel.pack()

        self.headlines = Label(master, text="")
        self.headlines.pack()
        
        self.getSources()

    def getSources(self):
        newsSources = getNewsSources()
        self.check0['text'] = newsSources[1][0]
        self.check1['text'] = newsSources[1][2]
        self.check2['text'] = newsSources[1][4]
        self.check3['text'] = newsSources[1][5]

    def generateHeadlines(self): 
        keyword = self.keywordInput.get()     
        headlines = makeRequest(keyword)
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
