import pandas as pd

def checkCityAndState(city,state,df):

    # Crear un filtro para seleccionar solo las filas que cumplen con los valores especificados
    filter = (df["city"] == city) & (df["state_id"] == state)

    # Aplicar el filtro al DataFrame y obtener solo las filas que cumplen con los valores especificados
    result = df[filter]

    # Imprimir los resultados
    ##print(result)
    if not result.empty:
        continent = "US"
    else:
        content = "None"
    return continent