import requests
from bs4 import BeautifulSoup as bs


res = requests.get("https://www.youtube.com/results?search_query=jupyter")
content = res.content
soup = bs(content,"html.parser")
for item in soup.find_all('a',{"rel":"spf-prefetch"}):
    video_title = item.get('title')
    print(video_title)