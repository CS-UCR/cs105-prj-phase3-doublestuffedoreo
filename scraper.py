import requests
import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

#website
url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Riverside%2C+CA"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

#use "a" with findall to get sites, re.compile("/biz/") since all business links contain this
restaurantList = soup.find_all("a", href=re.compile("/biz/"))

for link in restaurantList:
	link.get("href")

def unique_links(tags,url):
	cleaned_links = set()

	for link in restaurantList:
		link = link.get("href")

		if link is None:
			continue
		if link.endswith('/') or link.endswith('#'):
			link = link [-1]

		actual_url = urllib.parse.urljoin(url,link)
		cleaned_links.add(actual_url)
	return cleaned_links

cleaned_links = unique_links(restaurantList,url)

filename = "restaurantLinks.csv"
f = open(filename,"w")
header = "Restaurant Links\n"
f.write(header)

for link in cleaned_links:
	f.write(str(link) + '\n')