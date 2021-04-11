from bs4 import BeautifulSoup
import urllib.request

cont = 'regular/qualifiers/?sortcol=td&sortdir=descending'
url = 'https://www.cbssports.com/nfl/stats/player/rushing/nfl/{}'.format(cont)
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'lxml')


if __name__ == "__main__":
    for tr in soup.find_all('tr', class_='TableBase-bodyTr', limit=20):
        name = tr.find('span', class_='CellPlayerName--long').a.text
        position = tr.find('span', class_='CellPlayerName-position').text
        team = tr.find('span', class_='CellPlayerName-team').text
        tds = tr.find_all('td')
        tdwn = tds[6].get_text()
        print('{}\t{}\t{}\t{}'.format(name.strip(), position.strip(),
                                      team.strip(), tdwn.strip()))
