import requests

API_COUNTRIES="https://countriesnow.space/api/v0.1/countries"


class UbicacionService:
    @staticmethod
    def obtener_paises():
        response=requests.get(API_COUNTRIES)
        data=response.json()
        return [pais['country'] for pais in data["data"]]
    @staticmethod
    def obtener_ciudades_por_pais(nombre_pais):
        response=requests.get(API_COUNTRIES)
        data=response.json()
        for pais in data["data"]:
            if pais["country"]== nombre_pais:
                return pais["cities"]
        return[]
