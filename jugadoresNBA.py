import requests, re, urllib.parse
from bs4 import BeautifulSoup
import re
def checkTeams(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parseamos el contenido de la página web
        soup = BeautifulSoup(response.content, 'html.parser')
        # Obtener todas las etiquetas a
        links = soup.find_all('a')
        return links
    else:
        # En caso de que la petición no haya sido exitosa, mostramos un mensaje de error
        print('Error al hacer la petición a la página web')

def getPlayersUrl(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parseamos el contenido de la página web
        soup = BeautifulSoup(response.content, 'html.parser')
        # Obtener todas las etiquetas a
        players = []

        for div in soup.find_all("a", class_="AnchorLink", tabindex="0", href=lambda x: x and x.startswith("http://espndeportes.espn.com/basquetbol/nba/jugador/_/id/")):
            link=div.attrs['href']
            #convertir url de https://espndeportes.espn.com/basquetbol/nba/jugador/_/id/2566769/malcolm-brogdon
            #a https://espndeportes.espn.com/basquetbol/nba/jugador/bio/_/id/2566769/malcolm-brogdon

            # Separa la URL en partes
            parts = urllib.parse.urlsplit(link)

            # Dividimos el string original en una lista
            split_string = parts[2].split("/")
            # Modificamos la lista agregando el nuevo componente
            split_string[4:4] = ["bio"]

            # Unimos la lista de nuevo en un string
            modified_string = "/".join(split_string)

            new_url='https://'+parts[1]+modified_string




            players.append(new_url)

        players=eliminarDuplicados(players)
        return players

def filterByCountry(players):

    try:
        players=players
    except keyError:
        return None
def get_continent(country):
        try:
            country_info = pycountry.countries.get(name=country)
            continent_code = country_info.region.split(" ")[0]
            return pycountry.continents.get(code=continent_code).name
        except KeyError:
            return None
def eliminarDuplicados(lista):
    return list(set(lista))

# Hacemos una petición a la página web
url = 'http://espndeportes.espn.com/basquetbol/nba/jugadores'
links=checkTeams(url)

# # Filtrar los enlaces por el valor de su atributo href
teams = [link for link in links if '/basquetbol/nba/equipo/_/nombre/' in link['href']]

# Para cada equipo, obtengo sus jugadores

for team in teams:
    print(team.attrs['href'])
    #Compruebo que URL de equipo funciona

    url2 = 'http://espndeportes.espn.com'+team.attrs['href'];
    #La url hay que modificarla por que no redirige a la pagina de jugadores, si no a la portada del equipo. creamos nueva url que acceda directamente al plantel
    result = re.search('nombre/(.*)', url2)

    if result:
        team = result.group(1)
        new_url = 'https://espndeportes.espn.com/basquetbol/nba/equipo/plantel/_/nombre/' + team

    playersUrl=getPlayersUrl(new_url)

    filterByCountry(playersUrl)

