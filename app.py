from lxml import html
from tabulate import tabulate
import requests

page = requests.get('https://coinmarketcap.com/')

# convert html.fromstring object need page.content rather than page.text

tree = html.fromstring(page.content)

curr_name = tree.xpath('//a[@class="currency-name-container link-secondary"]/text()')
curr_price = tree.xpath('//a[@class="price"]/text()')
curr_volume = tree.xpath('//a[@class="volume"]/text()')
# curr_change = tree.xpath('//td[@class="no-wrap percent-change text-right negative_change"]/text()')


# making a dictionary on gatherd data
paired_list = list(zip(curr_name,curr_price,curr_volume))
# print(paired_list)

tabulate_table = tabulate(paired_list,headers=["Currency", "Price","Volume"])
print(tabulate_table)

