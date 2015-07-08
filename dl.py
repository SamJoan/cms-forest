
from bs4 import BeautifulSoup

txt = open("/tmp/url")
contents = txt.read()

soup = BeautifulSoup(contents)

elems = soup.select("#node-91 > div > div > div > div > ul > li > a")

for elem in elems:
    url = elem["href"]
    if url.endswith('.tar.gz'):
        print(url)
