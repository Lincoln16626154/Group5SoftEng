import requests
import json


def makeRequest(keywords = ""):
    key = "cb8a243e53e042ceb003054dabdda67c"
    URL = "https://newsapi.org/v2/everything?apiKey=" + key + "&q=" + keywords + "&language=en"  
    response = requests.get(url = URL)    
    responseData = response.json() 
    if errorHandling(responseData):
        return "ERROR: Keyword Required"
    else:
        return getTitles(responseData)


def errorHandling(response):
    if response['status'] == "error":
        print("\n\n\n" + "ERROR:   " + response['message'] + "\n\n\n")
        return True
    else:
        return False


def getTitles(data):
    text_ocurrences=[] 
    for item in data['articles']:
            text_ocurrences.append(item['title'])
    return text_ocurrences

def parseSources(data):
    ids=[] 
    names=[]
    for item in data['sources']:
            ids.append(item['id'])
            names.append(item['name'])
    return ids, names

def getNewsSources():
    key = "cb8a243e53e042ceb003054dabdda67c"
    URL = "https://newsapi.org/v2/sources?apiKey=" + key + "&country=gb"  + "&language=en"  
    response = requests.get(url = URL)    
    responseData = response.json() 
    if errorHandling(responseData):
        return "ERROR: Keyword Required"
    else:
        return parseSources(responseData)