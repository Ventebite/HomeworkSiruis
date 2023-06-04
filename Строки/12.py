stringa = input()
scraping = int(stringa.replace('<span>', '').replace('&nbsp', '').replace(';', '').replace('P</span>', ''))
print(scraping + 1)