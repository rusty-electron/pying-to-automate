import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Microprocessor-Architecture-Programming-Applications-8085/dp/8187972882/ref=sr_1_2?crid=1HEM7HT2F9JY&keywords=goankar&qid=1562793926&s=gateway&sprefix=goankar%2Caps%2C339&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
print(title.strip())