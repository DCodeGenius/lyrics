from bs4 import BeautifulSoup
import requests
from get_url import url_name

url = url_name()
#url = "https://genius.com/Doja-cat-kiss-me-more-lyrics"
html_text = requests.get(url)
html_text = html_text.text
soup = BeautifulSoup(html_text, 'lxml')
body = soup.find("routable-page")
lyrics = body.find("div", class_="lyrics").text
print(lyrics)
