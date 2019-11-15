from tkinter import *
from newsRequest import makeRequest, getNewsSources

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Application Title")

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

    newsSources = []
    
    def getSources(self):
        self.newsSources = getNewsSources()
        self.check0['text'] = self.newsSources[1][0]
        self.check1['text'] = self.newsSources[1][1]
        self.check2['text'] = self.newsSources[1][2]
        self.check3['text'] = self.newsSources[1][3]

    def checksources(self):
        IDs = []
        for i in range (4):
            if self.sourceSelection[i].get() == 1:
                IDs.append(self.newsSources[0][i])
        return IDs

    def generateHeadlines(self):
        keyword = self.keywordInput.get()     
        headlines = makeRequest(keyword, self.checksources())
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
