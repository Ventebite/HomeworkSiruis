stringa = input()
scraping = stringa.replace('(', '').replace(')', '').replace('-', '')
#end = scraping.join('.')
print(scraping.replace(' ', ''))