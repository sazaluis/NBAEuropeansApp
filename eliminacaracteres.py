from bs4 import BeautifulSoup

html = '<a class="AnchorLink" href="http://espndeportes.espn.com/basquetbol/nba/jugador/_/id/2566769/malcolm-brogdon" tabindex="0"><div class="headshot inline-block relative TableHeadshot roster-headshot headshot'

soup = BeautifulSoup(html, 'html.parser')

link = soup.find('a')

result = link['href'].split('/')[-1]

print(result)
result=''