import requests

class ClaseAPI:

    def __init__(self, url_base = 'http://localhost:5000'):
        self.url_base = url_base

    def consultar(self, limite):
        endpoint = self.url_base
        try:
            respuesta = requests.get(endpoint)
            respuesta.raise_for_status()
            datos = respuesta.json()
        except requests.exceptions.RequestException as e:
            print(f'Error en la consulta: {e}')
            return None

clasesita = ClaseAPI.consultar(5)
