import requests
import re
import html2text
import time
from bs4 import BeautifulSoup

years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
         '2013', '2014', '2015']

# with open('./data/%s/links/mens_links.txt') as f:
#     mens_links = f.readlines()
for year in years:
    mens_links = [line.rstrip('\n')
                  for line in open('./data/%s/mens_links2.txt' % year)]
    mens_ints = ''
    t1 = time.time()
    for link in mens_links:
        r = requests.get(link)
        temp = (html2text.html2text(r.text))
        temp = temp.replace('*', '')
        # temp = temp.replace('\n', '')
        mens_ints = mens_ints + temp
        # print(soup)
    t2 = time.time()
    dt = t2 - t1
    with open('./data/%s/mens_ints2.txt' % year, 'w') as f:
        f.write(mens_ints)
    print(dt)

    womens_links = [line.rstrip('\n')
                    for line in open('./data/%s/womens_links2.txt' % year)]
    womens_ints = ''
    t1 = time.time()
    for link in womens_links:
        r = requests.get(link)
        temp = (html2text.html2text(r.text))
        temp = temp.replace('*', '')
        # temp = temp.replace('\n', '')
        womens_ints = womens_ints + temp
        # print(soup)
    t2 = time.time()
    dt = t2 - t1
    with open('./data/%s/womens_ints2.txt' % year, 'w') as f:
        f.write(womens_ints)
    # print(mens_ints)
    print(dt)
