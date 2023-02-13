import urllib
import pycountry
import translators as ts
import pycountry_convert as pc
import translate,us,getEEUUStates

def get_continent_from_string(data,df):
#def get_continent_from_string(data):     """definicion para test"""
    try:
        #si data contiene datos, ejecutate
        if data:
            # Hay casos que solo viene el pais (evan fournier por ejemolo) asi que city no tiene valor y state si
            if not ", " in data:
                    data= ", ".join(["",data])
            # Separa la URL en partes
            city, state = data.split(", ")
            if len(state) > 2:
                data_translated = translate.translateText(data)
                state_or_country = data_translated.split()

            try:
                country = pycountry.countries.get(name=state_or_country[-1])
                country_continent_name = pc.country_alpha2_to_continent_code(country.alpha_2)
                return country_continent_name
            except:
                try:
                    #Si no se reconoce, mirar si el valor de pais / estado tiene solo dos letras, lo que indica que es Estados unidos
                    country_continent_name = getEEUUStates.checkCityAndState(city,state,df)
                    return country_continent_name

                except:
                    raise LookupError(f"No se encontró una subdivisión o país con nombre o código {state_or_country[-1]}")
    except:
        country_continent_name = 'NULL'
        return country_continent_name

#Datos para test

"""example1 = "Francia"
print(get_continent_from_string(example1))

example2 = "Sant'Angelo Lodigiano, Italia"
print(get_continent_from_string(example2))

example3 = "Atlanta, GA"
print(get_continent_from_string(example3))"""