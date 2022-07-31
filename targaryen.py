from bs4 import BeautifulSoup
import requests
 
url = 'https://www.imdb.com/title/tt11198330/fullcredits'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.character a')
names=[]
for i in range(len(movies)):
    if i%2 ==0:
        if((movies[i].text.count("Targaryen")>0)):
           names.append(movies[i].text)
print(names)