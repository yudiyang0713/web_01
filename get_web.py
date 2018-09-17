__author__ = 'Yudi'

import requests
from bs4 import BeautifulSoup


request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/black/p2083183")
#<div class="prices-container">  <p class="price price--large">£129.00 </p> </div>

content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class":"price price--large"})
string_price = element.text.strip()
price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if(price<200):
    print("You should but this Chair, the price is {}".format(string_price))
else:
    print("Too expensive, you shouldnt but this Chair.")