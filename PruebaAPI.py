#LIBRERIAS QUE SE VAN A OCUPAR, INSTALALAS CON PIP, SI NO TE SIRVE BS4 PIP INSTALL --UPDATE BS4 <---ALGO ASI REVISALO
import requests
from bs4 import BeautifulSoup
import json
    
def main(params):
    #=====CONEXION CON STACKOVERFLOW ESPECIFICAMENTE EL BUSCADOR, Y BUSCAMOS LO QUE QUEREMOS
    res = requests.get("https://stackoverflow.com/search?q="+params)
    #-----------PARCEAMOS EL RESULTADO DE LA BUSQUEDA A HTML
    soup = BeautifulSoup(res.text, "html.parser")
    #-----------SCRAPEAMOS EN EL HTML DE LA PAGINA LAS CLASES DE INTERES 
    question_summary = soup.findAll("div",{"class": "question-summary search-result"})
    #-----------ACCEDEMOS AL TITULO DE CADA PREGUNTA
    #print (question_summary)
    print (question_summary[0].h3.a["title"])#<--------PODES BUSCAR ALGO EN STACKOVERFLOW Y COMPARARLO CON ESTO TENES QUE CAMBIAR LOS NUMEROS PARA VER LAS DEMAS

    #------------PROPUESTA PARA LLENAR UNA VARIABLE QUESTION_TITLE (NO FUNCIONA) MEJORAR ACA
    '''
    question_title = []
    counter = 0
    for question in question_summary:
        question_title[counter] = question_summary[counter].h3.a["title"]
        counter += 1
    print (question_title)
    '''


    
if __name__=="__main__":
    main(input('ingrese parametro: '))


   
