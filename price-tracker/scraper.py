import requests
import smtplib
import time
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Wacom-CTL-472-6-inch-3-5-inch-Graphic/dp/B078HRR1XV/ref=sr_1_3?crid=1OE3A25XGBHYV&keywords=wacom+tablet&qid=1562926548&s=gateway&sprefix=wacom%2Caps%2C461&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[2:].replace(',',''))

    if(converted_price > 3700.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('prig261@gmail.com', '<insert password')

    subject = 'Price fell!'
    body = 'Check this product link: \n' + URL

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'prig261@gmail.com',
        'kickstart7962@gmail.com',
        msg
    )

    print('[Output] Mail Sent')

while(True):
     check_price()
     time.sleep(60*60*6)