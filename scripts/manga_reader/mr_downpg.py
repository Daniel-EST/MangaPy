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
        
        page_req = requests.get(page).text
        page_html = bs4.BeautifulSoup(page_req, "html.parser")
        
        img_scr = page_html.select('#imgholder #img')[0].get('src')     
        img_req = requests.get(img_scr).content   
        
        filename = os.path.join(filepath, page_number)      
        with open(filename + '.jpg', 'wb') as f_obj:
            f_obj.write(img_req)
        
        page_number = int(page_number) + 1