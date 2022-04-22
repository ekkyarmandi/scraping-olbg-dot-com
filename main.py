# import function script
from pandas import DataFrame
import scraper


# iterate the table row
links = []
html = scraper.render('https://www.olbg.com/betting-tips/Horse_Racing/2')
table = html.find('table',id='tipsListingContainer-Match')
table = table.find('tbody',id='tips-table-tbody-match')
for tr in table.find_all('tr'):
    if 'class' in tr.attrs and 'tip-row' in tr.attrs['class']:
        link = 'https://www.olbg.com' + tr.find('a')['href']
        links.append(link)

# reparser the bottom list
bottom_table = scraper.render('https://www.olbg.com/storage/framework/block_cache/betting-tips/Horse_Racing/2-bottom.php')
for tr in bottom_table.find_all('tr'):
    if 'class' in tr.attrs and 'tip-row' in tr.attrs['class']:
        link = 'https://www.olbg.com' + tr.find('a')['href']
        links.append(link)

# parse all gathered links
results = []
links = list(dict.fromkeys(links))
for link in links:
    result = scraper.parser(link)
    if result != None:
        results.extend(result)
        print(result)

# export results as CSV
data = DataFrame(results)
data.to_csv('results.csv',index=False)