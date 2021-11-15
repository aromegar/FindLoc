import pandas as pd

def limpiame(lista,tipo):
    """
    limpia un json y me devuelve una lista donde cada respuesta es un diccionario
    Args:
        lista : la lista respuesta de la API de Google
        tipo : el tipo de petición que le he hecho a Google
    """
    limpia=[]
    for elemento in lista:
        dicc={}
        dicc["tipo"]=tipo
        dicc["nombre"]=elemento["name"]
        dicc["latitud"]=elemento["geometry"]["location"]["lat"]
        dicc["longitud"]=elemento["geometry"]["location"]["lng"]
        dicc["location"]={'type': 'Point', 'coordinates': [elemento["geometry"]["location"]["lng"],elemento["geometry"]["location"]["lat"]]}
        limpia.append(dicc)
    return limpia