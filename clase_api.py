import requests

class ClaseAPI:

    def __init__(self, url_base = 'https://www.datos.gov.co/resource/2pnw-mmge.json'):
        self.url_base = url_base

    def consultar(self, limite):
        endpoint = self.url_base
        try:
            respuesta = requests.get(endpoint)
            respuesta.raise_for_status()
            datos = respuesta.json()
            return datos[:limite]
        except requests.exceptions.RequestException as e:
            print(f'Error en la consulta: {e}')
            return None
