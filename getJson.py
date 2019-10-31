import requests
import json
from findTitles import getTitlesFromData

# key = 'cb8a243e53e042ceb003054dabdda67c'
URL = "https://newsapi.org/v2/everything?q=bitcoin&from=2019-09-30&sortBy=publishedAt&apiKey=cb8a243e53e042ceb003054dabdda67c"
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 

print(getTitlesFromData(data))

with open('data_file2.json', 'w') as outfile:
    json.dump(data, outfile)

# print(data)