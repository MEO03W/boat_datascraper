import requests
from bs4 import BeautifulSoup
import re

print("***Scraperstart***")

# url ='https://www.boat24.com/en/sailingboats/?sort=datdesc'
url = 'https://www.boat24.com/en/sailingboats/?src=Beneteau+Oceanis+393&cat=1&cem=&whr=EUR&prs_min=&prs_max=&lge_min=&lge_max=&bre_min=&bre_max=&tie_min=&tie_max=&gew_min=&gew_max=&jhr_min=&jhr_max=&lei_min=&lei_max=&mai_min=&mai_max=&per_min=&per_max=&cab_min=&cab_max=&ber_min=&ber_max=&hdr_min=&hdr_max=&sort=datdesc'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)
print("####################################################\n\n\n")
########################################################


scraped_data = []

angebote = soup.find_all("div", class_="blurb")

for angebot in angebote:
    # main
    # main = angebot.find("div", class_="blurb__main")
    title_blurb = angebot.find("h3", class_="blurb__title")
    title = title_blurb.find("a")
    title_text = title.text
    href = title['href']
    match = re.search(r'/detail/(\d+)/', href)  # searching for the id
    if match:
        angebot_id = match.group(1)
    else:
        angebot_id = ''
    # side
    price_blurb = angebot.find("p", class_="blurb__price")
    price_text = price_blurb.text
    match = re.search(r'([A-Z]+) (\d+\.\d+)', price_text)
    print(match)
    if match:
        currency = match.group(1)
        amount_str = match.group(2)
        amount = int(amount_str.replace('.', ''))
        print(currency)
        print(amount_str)
    else:
        amount_str = ''
        currency = ''
        print("no match found")

    angebot_data = {
        'id': angebot_id,
        'title': title_text,
        'href': href,
        'price': amount,
        'currency': currency
    }
    scraped_data.append(angebot_data)
# Print scraped data object
print(scraped_data)
