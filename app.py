from lxml import html
from tabulate import tabulate
import requests

page = requests.get('https://coinmarketcap.com/')

# convert html.fromstring object need page.content rather than page.text

tree = html.fromstring(page.content)

curr_name = tree.xpath('//a[@class="currency-name-container link-secondary"]/text()')
curr_price = tree.xpath('//a[@class="price"]/text()')

# making a dictionary on gatherd data
paired_dict = list(zip(curr_name,curr_price))

tabulate_table = tabulate(paired_dict,headers=["Currency", "Price"])
print(tabulate_table)

