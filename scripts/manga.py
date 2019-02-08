import re
import os

from manga_reader.mr_getch import mr_getch
from manga_reader.mr_downpg import mr_downpg

class Manga():
    """Manga class that holds chapter, title and download
    server information"""
    
    def __init__(self, title, server):
        """Initiates manga class."""
        self.title = title.lower()
        self.server = server
    
    def get_chapters(self):
        """Get manga chapter info from the choosen website."""
        if self.server=='manga reader':
            self.title = self.title.replace(' ', '-')
            self.chapters = mr_getch(self.title)
            
    def choose_chapters(self):
        """Choose what chapters you want to download"""
        self.chapters = self.chapters[5]
            
    def download_chapters(self):
        """Downlaods pages from the choosen chapter."""
        print('Choose the download folder')
        if self.server=='manga reader':
            for chapter in self.chapters:
                print(chapter)
                reg_chnum = re.compile(r'\d+')
                chnum = reg_chnum.search(chapter).group()
                chnum = '0'*(3-len(chnum)) + chnum
                
                filepath = os.path.join(self.title, chnum)
                os.makedirs(filepath, exist_ok=True)
                
                print('Baixando: ' + chnum)
                
                mr_downpg(chapter, filepath)