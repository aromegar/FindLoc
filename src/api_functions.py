import json
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

def get_coord_from_zip(zip):
    """
    Argumentos: un string con 5 dígitos
    Devuelve un json con información del zipcode (ciudad, long, lat, etc)
    """
    load_dotenv()
    zipkey = os.getenv("zipapi")
    mail = os.getenv("mail")
    password = os.getenv("password")
    try:
        resp = requests.get(f"https://service.zipapi.us/zipcode/{zip}?X-API-KEY={zipkey}&fields=geolocation",
            auth=HTTPBasicAuth(f"{mail}", f"{password}"))
        return resp.json()["data"]
    except: 
        return "error"

def google(busco,radio,location):
    """
    Argumentos(3):  busco: un string (palabra clave para buscar, ej "vegan")
                    radio: un entero (radio, en METROS, para hacer la búsqueda)
                    location: un string del tipo '37.76785,-122.392861' con el centro de la búsqueda.
    Devuelve:   un json: lista de places en ese radio, con (demasiada) información de cada uno
    """
    load_dotenv()
    mykey = os.getenv("google")
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radio}&keyword={busco}&key={mykey}"
    payload={}
    headers={}
    try:
        resp = requests.get(url, headers=headers, data=payload)
        return resp.json()
    except:
        return "error"

