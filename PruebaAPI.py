#LIBRERIAS QUE SE VAN A OCUPAR, INSTALALAS CON PIP, SI NO TE SIRVE BS4 PIP INSTALL --UPDATE BS4 <---ALGO ASI REVISALO
import requests
from bs4 import BeautifulSoup
import json
    
def main(params):
    #=====CONEXION CON STACKOVERFLOW ESPECIFICAMENTE EL BUSCADOR, Y BUSCAMOS LO QUE QUEREMOS
    try:
        res = requests.get("https://stackoverflow.com/search?q="+params)
        #-----------PARCEAMOS EL RESULTADO DE LA BUSQUEDA A HTML
        soup = BeautifulSoup(res.text, "html.parser")
        #-----------SCRAPEAMOS EN EL HTML DE LA PAGINA LAS CLASES DE INTERES 
        question_summary = soup.findAll("div",{"class": "question-summary search-result"})
        #-----------ACCEDEMOS AL TITULO DE CADA PREGUNTA
        #print (question_summary)
    except Exception as e:
        print("Ups... something whent wrong, exception code: \n" +str(e))

    #======si no hay internet:
    question_summary = None
    
    if question_summary is not None:
        for question in question_summary:
            title = question.h3.a["title"]
            print (title)
    else:
        print("estas sin inter perro")



        
if __name__=="__main__":
    main(input('ingrese pregunta: '))


   
