import requests
import json


# def get(pelicula, payload={}, headers={}) -> dict:
#     response = requests.request("GET", "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + pelicula,
#                                 headers=headers,
#                                 data=payload)
#     print(response.status_code)
#     paginas = response.json().get("total_pages")
#     for i in range(1, paginas + 1):
#         print(paginas)
#         parametros = {
#             "Title": pelicula,
#             "pages": i
#         }
#         response = requests.request("GET", "https://jsonmock.hackerrank.com/api/movies/search/", headers=headers,
#                                     data=payload, params=parametros)
#         pelicualAux = response.json().get("Year")
#         print(pelicualAux)
#         i + 1
#
#     return response.json()


def get(pelicula, payload={}, headers={}):
    years = []
    respuesta = []
    dicPerYear={}
    response = requests.request("GET", "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + pelicula,
                                headers=headers,
                                data=payload)

    response.json()['total_pages']
    for i in range(response.json()['total_pages']):
        req = requests.request("GET",
                               "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + pelicula + "&page=" + (
                                   f'{i + 1}'))

        for j in req.json()['data']:
            respuesta.append(j)
            years.append(j["Year"])

    years = list(set(years))
    for year in years:
        listYear=[]
        for resp in respuesta:
            yearToCompare= resp.get("Year")
            if year == yearToCompare:
                listYear.append(resp)
                dicPerYear[year]=listYear

    # print(dicPerYear)
    # print(len(titles))
    # print(len(years))
    return dicPerYear


if __name__ == '__main__':
    respuesta = get(str(input("Ingrese la pelicula a buscar: ")))
    print((respuesta))
