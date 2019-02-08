import requests
import re
import os

import bs4

def mr_getch(title):
    """Get chapter information in manga reader website"""
    mr_url = 'https://www.mangareader.net'
    manga_url = mr_url + '/' + title
    
    req_manga = requests.get(manga_url)
    req_manga = req_manga.text
    manga_html = bs4.BeautifulSoup(req_manga, "html.parser")
    
    links = manga_html.select('td a')
    links = [link.get('href') for link in links]
    links = [mr_url + link for link in links]
    
    chapter_links = []
    
    chapter_reg = re.compile(title)
    
    for link in links:
        if chapter_reg.search(link):
            chapter_links.append(link)
    
    if chapter_links:          
        message = 'There are %i chapters of %s available at Manga Reader'
        print(message % (len(chapter_links), title.title().replace('-', ' ')))
        return chapter_links
    else:
        print('The manga you are looking for isn\'t available at manga reader')
        