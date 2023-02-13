import requests,checkContinent
from bs4 import BeautifulSoup

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
                    born_in = ""
            else:
                #En caso de que la petición no haya sido exitosa, mostramos un mensaje de error
                key, value = next(iter(playerUrl.items()))
                print('Error al buscar Bio del jugador'+value)
        continent = checkContinent.get_continent_from_string(born_in, df)
        players_by_country[key]=(born_in,continent)
    return players_by_country