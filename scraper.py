#!/bin/python3

import requests
from bs4 import BeautifulSoup

url = u'https://twitter.com/amermathsoc'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text 
    for p in soup.findAll('p', class_='tweet-text')]

print(tweets)
