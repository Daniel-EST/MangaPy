from manga import Manga

available_servers = ['manga reader', 'manga rock', 'kiss manga']

while True:
    server = input('In what server you want to download: ')
    server = server.lower()
    if server not in available_servers:
        print('Please choose a available server')
        continue
    
    title = input('Manga title: ')
    
    manga = Manga(title, server)
    manga.get_chapters()
    if manga.chapters:
        manga.choose_chapters()
        manga.download_chapters()
        break
    else:
        print('Not available')