from urllib.request import urlopen
from bs4 import BeautifulSoup
import TwilioKeys
from twilio.rest import Client
from re import sub
from decimal import Decimal


client = Client(TwilioKeys.accountSID, TwilioKeys.authToken)
TwilioNumber = '+15012858815'
myCellphone = '+15015901774'


webpage = 'https://coinmarketcap.com/'

response = urlopen(webpage)		
page = response.read().decode(encoding="iso-8859-1")	
soup = BeautifulSoup(page, 'html.parser')

title = soup.title


tablecells = soup.findAll("td")

#for cell in tablecells[1:6]:
    #print(cell.text)

counter = 1
for x in range(5):
    rank = tablecells[counter].text
    name = tablecells[counter+1].text
    price = tablecells[counter+2].text
    change = tablecells[counter+4].text


    print(f"Rank: {rank}")
    print(f"Name: {name}")
    print(f"Current Price: {price}")
    print(f"% Change 24 Hours: {change}")
    print()
    print()

    if name == "Bitcoin1BTC":
        value = Decimal(sub(r'[^\d.]', '', price))
        if value < 40000:
            textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body='Bitcoin is below $40,000')

    if name == "Ethereum2ETH":
        value = Decimal(sub(r'[^\d.]', '', price))
        if value < 3000:
            textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body='Ethereum is below $3,000')

    input()
    counter += 12










