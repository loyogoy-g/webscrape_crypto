="""Web Scraping is fun , You can take all data you need or you want on a certain website
especially if the website api's doesn't support the data that you needed or the website
doesn't have any api, but be careful about the terms and conditions of the website"""

from bs4 import BeautifulSoup #import all necessary modules
import requests

class CRYPTO:
    def __init__(self, coinname): #example of coin name : bitcoin, ethereum, stellar
        self.url = "https://coinmarketcap.com/currencies/{}".format(coinname)
        self.resp = requests.get(self.url)
        self.soup = BeautifulSoup(self.resp.text, 'html.parser')

    #return the price of coin
    def price(self):
        price = self.soup.find("span", {"class": "h2 text-semi-bold details-panel-item--price__value"}).text
        return "{} US dollar".format(price)

    #return the rank of the coin
    def rank(self):
        rank = self.soup.find("span", {"class": "label label-success"}).text
        return rank


while True:
    coinname = input("Coin Name :") #take input from the user
    try:
        cryp = CRYPTO(coinname)
        print(cryp.rank())  #coin rank and price
        print(cryp.price())
    except: #Catch all the error hahahaha, You can edit and specify all the exception
        print("Error Occurred Check your internet connection or your coin name")