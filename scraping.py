import requests
import re
from bs4 import BeautifulSoup
import time

# Getting all links from a certain year
# These links will be to events
# ex) Women's ACC Tournament
# These will have press conferences nested within them
years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
         '2013', '2014', '2015']
# years = ['2016', '2017', '2018', '2019', '2020']
for year in years:
    t1 = time.time()
    url = 'http://www.asapsports.com/show_year.php?category=11&year=' + year
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features='lxml')
    links_temp = soup.find_all('a', attrs={'href': re.compile("^http://")})
    # Contains links to all event pages from this year
    links = []
    for link in links_temp:
        if 'event' in link['href']:
            links.append(link['href'])
    # for link in links:
    #     print(link)

    # For each event:
    # 1)
    mens_page_links = []
    womens_page_links = []
    womens_interview_links = []
    mens_interview_links = []
    for link in links:
        r = requests.get(link)
        data = r.text
        soup = BeautifulSoup(data, features='lxml')
        links_temp = soup.find_all('a', attrs={'href': re.compile("^http://")})
        # Contains links to all event pages from this year
        for link in links_temp:
            if 'NCAA' in link['href'] and 'event' in link['href'] and not ('nba' in link['href'].casefold() or 'all-star' in link['href'].casefold()):
                # print(link)
                if "women" in link['href'].casefold():
                    womens_page_links.append(link['href'])
                elif "men" in link['href'].casefold():
                    mens_page_links.append(link['href'])
        # Remove potential duplicates
        mens_page_links = list(dict.fromkeys(mens_page_links))
        womens_page_links = list(dict.fromkeys(womens_page_links))
        for link in womens_page_links:
            r = requests.get(link)
            data = r.text
            soup = BeautifulSoup(data, features='lxml')
            links_temp = soup.find_all(
                'a', attrs={'href': re.compile("^http://")})
            # Contains links to all interviews
            for link in links_temp:
                if 'interview' in link['href']:
                    womens_interview_links.append(link['href'])
        for link in mens_page_links:
            if len(mens_interview_links) < len(womens_interview_links):
                r = requests.get(link)
                data = r.text
                soup = BeautifulSoup(data, features='lxml')
                links_temp = soup.find_all(
                    'a', attrs={'href': re.compile("^http://")})
                # Contains links to all interviews
                for link in links_temp:
                    if 'interview' in link['href']:
                        mens_interview_links.append(link['href'])

    mens_interview_links = list(dict.fromkeys(mens_interview_links))
    womens_interview_links = list(dict.fromkeys(womens_interview_links))

    with open('./data/%s/mens_links2.txt' % year, 'w') as f:
        for item in mens_interview_links:
            f.write("%s\n" % item)
    print(len(mens_interview_links))
    with open('./data/%s/womens_links2.txt' % year, 'w') as f:
        for item in womens_interview_links:
            f.write("%s\n" % item)
    print(len(womens_interview_links))
    t2 = time.time()
    dt = t2 - t1
    print(dt)
