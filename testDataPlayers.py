import checkByCountry,pandas as pd,checkContinent
#testeo de lectura de datos por jugador

# Cargar el archivo CSV en un DataFrame de pandas

df = pd.read_csv("uscities.csv")
#playerUrl=[{'aj-green':'https://espndeportes.espn.com/basquetbol/nba/jugador/bio/_/id/4397475/aj-green'}, {'wesley-matthews': 'https://espndeportes.espn.com/basquetbol/nba/jugador/bio/_/id/4032/wesley-matthews'},{'marjon-beauchamp':'https://espndeportes.espn.com/basquetbol/nba/jugador/bio/_/id/4432179/marjon-beauchamp'}]
playerUrl=[{'Jason Tatum':'https://espndeportes.espn.com/basquetbol/nba/jugador/bio/_/id/4065648/jayson-tatum'},{'luke-kornet':'https://espndeportes.espn.com/basquetbol/nba/jugador/bio/_/id/3064560/luke-kornet'}]
lista_final=checkByCountry.filterByCountry(playerUrl,df)
print(lista_final)