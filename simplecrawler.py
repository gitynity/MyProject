import requests
from bs4 import BeautifulSoup


def simplecrawler(url):
    url_to_crawl = [url]	#set of urls to crawl
    crawled = []			#set of urls successfully crawled
    
    while url_to_crawl:
        page = url_to_crawl.pop()
        print('Crawled' + page)
        
        source = requests.get(url)
        plain_text = source.text
        soup = BeautifulSoup(plain_text,'lxml')	#beautifulsoup object
        
        links = soup.findAll('a', href=True)	#find a where href exists ..... a is for anchor tag
        
        if page not in crawled:
            for l in links:
                url_to_crawl.append(l['href'])
                crawled.append(page)
    return crawled


simplecrawler('http://www.manit.ac.in/')
