import requests, re, urllib.parse,pandas as pd,checkContinent
from bs4 import BeautifulSoup

def getTeams(url):
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
            #creo un diccionario con nombre de jugador y url
            players.append({split_string[8]: new_url})

        players=eliminarDuplicados(players)
        return players
    else:
        # En caso de que la petición no haya sido exitosa, mostramos un mensaje de error
        print('Error al buscar jugadores')
#def getPlayerBio(url):


def filterByCountry(players,df):
    players_by_country={}
    for playerUrl in players:
        for key, value in playerUrl.items():
            #print(f"Clave: {key}, Valor: {value}")
            #elimino simbolo '
            response = requests.get(value)
            if response.status_code == 200:
                # Parseamos el contenido de la página web
                soup = BeautifulSoup(response.content, 'html.parser')

                card_bio = soup.find("section", {"class": "Card Bio"})
                #hay jugadores que no tienen en su bio info de nacio en, asi que asignamos no data
                try:
                    born_in = card_bio.find("span", string="Nacido en").find_next("span").text
                except:
                    born_in = "No data"
            else:
                #En caso de que la petición no haya sido exitosa, mostramos un mensaje de error
                key, value = next(iter(playerUrl.items()))
                print('Error al buscar Bio del jugador'+value)
        continent = checkContinent.get_continent_from_string(born_in, df)
        players_by_country[key]=(born_in,continent)
    return players_by_country

def eliminarDuplicados(players):
    lista_de_tuplas = [tuple(d.items()) for d in players]
    lista_sin_duplicados = [dict(t) for t in set(lista_de_tuplas)]
    return lista_sin_duplicados

def guardar_lista_en_archivo(diccionario, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        for clave, valor in diccionario.items():
            try:
                valor = list(valor)
                archivo.write(f"{clave}: {{'{valor[0]}', '{valor[1]}'}}\n")

            except:
                raise LookupError(f"Error para{clave}: {{'{valor[0]}', '{valor[1]}'}}")




# Logica de codigo abajo, funciones arriba

#cargo listado de ciudades / estados de US
# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv("uscities.csv")

# Hacemos una petición a la página web
url = 'http://espndeportes.espn.com/basquetbol/nba/jugadores'
links=getTeams(url)

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

    lista_final=filterByCountry(playersUrl,df)

    ##print(lista_final)
    eq, equipo =team.split("/")
    nombre_archivo = "Equipos/"+f"{equipo}.txt"
    guardar_lista_en_archivo(lista_final, nombre_archivo)

