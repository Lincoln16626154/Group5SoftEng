import requests
from bs4 import BeautifulSoup
URLS = ["https://newsapi.org/v2/everything?q=bitcoin&from=2019-09-30&sortBy=publishedAt&apiKey=cb8a243e53e042ceb003054dabdda67c","https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=cb8a243e53e042ceb003054dabdda67c",
"https://newsapi.org/v2/everything?q=apple&from=2019-10-29&to=2019-10-29&sortBy=popularity&apiKey=cb8a243e53e042ceb003054dabdda67c",
"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=cb8a243e53e042ceb003054dabdda67c",
"https://newsapi.org/v2/everything?domains=wsj.com&apiKey=cb8a243e53e042ceb003054dabdda67c"]
titles = []
result = requests.get[URLS]
    result.text[:1000]
    soup = BeautifulSoup(result.text, 'html.parser')
def getandparseURL(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    return(soup)

for i in (URLS):
    Title = soup.find("title",class_ = "articles")
    titles [Title] = titles[Title] + 1

print(titles)


    










