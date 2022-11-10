
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)


tablecells = soup.findAll("tr")

for cell in tablecells[1:6]:
    print(cell.text)

'''counter = 0

for x in tablecells[1:6]:
    rank = tablecells[counter].text
    name = tablecells[counter+1].text

    print(f"Rank {rank}")
    print(f"Name {name}")

    counter += 1'''

    

##
##
##
##

