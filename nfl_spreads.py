from bs4 import BeautifulSoup
import urllib.request

url = 'https://en.wikipedia.org/wiki/Shark_attack'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'lxml')

table = soup.find('table', class_="wikitable sortable")


if __name__ == "__main__":
    print("table for shark attacks not NFL spreads")

    title = table.caption.text
    print(title)

    for tbody in table.find_all('tbody'):
        rows = tbody.find_all('tr')[1:]
        for row in rows:
            region = row.find('td').text
            total = row.find_all('td')[1].get_text()
            fatal = row.find_all('td')[2].get_text()
            last = row.find_all('td')[3].get_text()
            print('{}\t{}\t{}\t{}'.format(region, total, fatal, last))
