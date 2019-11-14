import requests
import json

def makeRequest():
    key = "cb8a243e53e042ceb003054dabdda67c"
    URL = "https://newsapi.org/v2/top-headlines?apiKey=" + key + "&language=en"  
    response = requests.get(url = URL)    
    responseData = response.json() 
    if errorHandling(responseData):
        return {"See Console for Details", "ERROR: Failed to retrieve headlines"}
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
