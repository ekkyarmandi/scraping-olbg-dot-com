import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


def render(url):
    '''
    Make a request to the url and return it as soup object
    :param url: str
    :return s: BeautifulSoup object
    '''
    h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    r = requests.get(url, headers=h)
    s = BeautifulSoup(r.text,'html.parser')
    return s

def parser(url):
    '''
    Parser the url and gather the race event data
    :param url: str
    :return results: list of dictionaries -> race event horse data
    '''

    # render the url
    html = render(url)

    # find race title
    title = html.find('div',id='tips-title').text.strip()

    # find race timestamp
    date_row = html.find('span',class_='event-start-time')
    timestamp = int(date_row['data-timestamp'])
    date = datetime.fromtimestamp(timestamp)

    # find table
    results = []
    table = html.find('table',id='tipsListingContainer')
    for tr in table.find_all('tr'):
        if 'class' in tr.attrs and 'tip-row' in tr.attrs['class']:

            # find horse name
            horse_name = tr.find('h4',class_='selection-name').text
            horse_name = " ".join(re.findall('[a-zA-Z]+',horse_name))
            horse_name = re.sub('\s+',' ',horse_name).strip()

            # find WIN tips, EW tips, and find NAPs
            tips = tr.find_all('p',class_='tips')

            # find Odds fractional
            odds = tr.find('div',class_=['odds','formatted-odds'])
            
            result = {
                'Race': title,
                'Date': date.strftime('%H:%M:%S %d/%m/%Y'),
                'Horse': horse_name,
                'Win Tips': tips[0].text.strip(),
                'EW Tips': tips[1].text.strip(),
                'NAPs': tips[2].text.strip(),
                'Odds': odds['oddfractional']
            }

            results.append(result)
    return results