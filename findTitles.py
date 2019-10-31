import json
import re

def getTitles(filename):
    regex_chain = re.compile(r'(title)": "(.*)"')
    text_ocurrences=[]
    with open(filename, encoding="utf16") as file:
        for line in file:
            match = regex_chain.search(line)
            if match:
                text_ocurrences.append(match.group(2))
    return text_ocurrences
    
def getTitlesFromData(data):
    print(data)
    regex_chain = re.compile(r'(title)": "(.*)"')
    text_ocurrences=[] 
    for line in data:
        match = regex_chain.search(line)
        if match:
            text_ocurrences.append(match.group(2))
    return text_ocurrences