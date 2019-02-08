import requests
import os

import bs4

def mr_downpg(ch_url, filepath):
    """Download the chapter pages"""
    mr_url = 'https://www.mangareader.net'
    req_churl = requests.get(ch_url)
    ch_html = bs4.BeautifulSoup(req_churl.text, "html.parser")
    
    pages = ch_html.select('#selectpage option')
    pages = [mr_url + page.get('value') for page in pages]
    
    page_number = 1
    
    for page in pages:
        
        page_number = '0'*(3-len(str(page_number))) + str(page_number)
        
        page_req = requests.get(page).content
        page_img = bs4.BeautifulSoup(page_req)
        
        filename = os.path.join(filepath, page_number)
        with open(filename + '.png', 'wb') as f_obj:
            f_obj.write(page_req)
        
        page_number = int(page_number) + 1