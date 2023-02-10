import requests
from bs4 import BeautifulSoup

# Hacemos una petición a la página web
url = 'http://espndeportes.espn.com/basquetbol/nba/jugadores'
response = requests.get(url)

# Verificamos que la petición haya sido exitosa
if response.status_code == 200:
    # Parseamos el contenido de la página web
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscamos todos los elementos que contengan información sobre los equipos
    #teams = soup.find_all('td', {'class': 'team'})

    # Obtener todas las etiquetas a
    links = soup.find_all('a')

    # # Filtrar los enlaces por el valor de su atributo href
    teams = [link for link in links if '/basquetbol/nba/equipo/_/nombre/' in link['href']]

    # Imprimimos cada equipo
    for team in teams:
        print(team.attrs['href'])



    a=0;
else:
    # En caso de que la petición no haya sido exitosa, mostramos un mensaje de error
    print('Error al hacer la petición a la página web')