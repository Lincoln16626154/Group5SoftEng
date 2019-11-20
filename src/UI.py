from tkinter import *
from newsRequest import makeRequest, getNewsSources
from musicGeneration import genSpotify
import subprocess
subprocess.call([r'..\setup.bat'])

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
        
        self.generateTracks = Button(master, text="Generate", command=self.generateTracks)
        self.generateTracks.pack()

        self.trackLabel = Label(master, text="Tracks:")
        self.trackLabel.pack()

        self.tracks = Label(master, text="")
        self.tracks.pack()
        
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

    def generateTracks(self): 
        headlines = makeRequest(self.checksources())
        strHeadline = ''
        for item in headlines:
            strHeadline += item + ' '
        tracks = genSpotify(strHeadline)
        self.tracks['text'] = ""
        for item in tracks:
            self.tracks['text'] += item + "\n"

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
