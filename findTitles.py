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
    
print(getTitles('data_file2.json'))