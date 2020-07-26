import requests
import re
from bs4 import BeautifulSoup

# Getting all links from a certain year
# These links will be to events
# ex) Women's ACC Tournament
# These will have press conferences nested within them
year = '2019'

# url = 'http://www.asapsports.com/show_year.php?category=11&year=' + year
# r = requests.get(url)
# data = r.text
# soup = BeautifulSoup(data, features='lxml')
# links_temp = soup.find_all('a', attrs={'href': re.compile("^http://")})
# # Contains links to all event pages from this year
# links = []
# for link in links_temp:
#     if 'event' in link['href']:
#         links.append(link['href'])
# # for link in links:
# #     print(link)

# # For each event:
# # 1)
# mens_page_links = []
# womens_page_links = []
# womens_interview_links = []
# mens_interview_links = []
# for link in links:
#     r = requests.get(link)
#     data = r.text
#     soup = BeautifulSoup(data, features='lxml')
#     links_temp = soup.find_all('a', attrs={'href': re.compile("^http://")})
#     # Contains links to all event pages from this year
#     for link in links_temp:
#         if 'event' in link['href'] and not ('nba' in link['href'].casefold() or 'all-star' in link['href'].casefold()):
#             if 'women' in link['href'].casefold():
#                 womens_page_links.append(link['href'])
#             else:
#                 mens_page_links.append(link['href'])
#     # Remove potential duplicates
#     mens_page_links = list(dict.fromkeys(mens_page_links))
#     womens_page_links = list(dict.fromkeys(womens_page_links))
#     for link in womens_page_links:
#         r = requests.get(link)
#         data = r.text
#         soup = BeautifulSoup(data, features='lxml')
#         links_temp = soup.find_all('a', attrs={'href': re.compile("^http://")})
#         # Contains links to all interviews
#         for link in links_temp:
#             if 'interview' in link['href']:
#                 womens_interview_links.append(link['href'])
#     for link in mens_page_links:
#         if len(mens_interview_links) < len(womens_interview_links):
#             r = requests.get(link)
#             data = r.text
#             soup = BeautifulSoup(data, features='lxml')
#             links_temp = soup.find_all(
#                 'a', attrs={'href': re.compile("^http://")})
#             # Contains links to all interviews
#             for link in links_temp:
#                 if 'interview' in link['href']:
#                     mens_interview_links.append(link['href'])

# mens_interview_links = list(dict.fromkeys(mens_interview_links))
# womens_interview_links = list(dict.fromkeys(womens_interview_links))

# with open('./data/%s/links/mens_links.txt' % year, 'w') as f:
#     for item in mens_interview_links:
#         f.write("%s\n" % item)
# print(len(mens_interview_links))
# with open('./data/%s/links/womens_links.txt' % year, 'w') as f:
#     for item in womens_interview_links:
#         f.write("%s\n" % item)
# print(len(womens_interview_links))
