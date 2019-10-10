# -*- coding: utf-8 -*-


from time import sleep
from bs4 import BeautifulSoup as soup #BeautifulSoup

from urllib.request import urlopen as u_req #urllib.request
my_url = "https://thehackernews.com"
u_client = u_req(my_url)
page_html = u_client.read()
u_client.close()
page_soup = soup(page_html, "html.parser")
container = page_soup.findAll("div", {"class":"clear home-right"})
for getter in container:
    print(getter.h2.text)
    print()
sleep(5)
