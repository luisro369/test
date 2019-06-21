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



    #---------For con el que llenas los arreglos del titulo
    title = []
    title_href = []
    for question in question_summary:
        title.append(question.h3.a["title"])
        title_href.append(question.h3.a["href"])
    print (title[4])
    print (title_href[4])#<---eligo pregunta 5


    #------------segunda conexion con la respuesta
    try:
        res2 = requests.get("https://stackoverflow.com"+title_href[4])
        soup = BeautifulSoup(res2.text, "html.parser")
        answer_summary = soup.findAll("div",{"class": "post-text"})
    except Exception as e:
        print("Ups... something whent wrong, exception code: \n" +str(e))

    #============OJO pasar a texto la variable answer_summary
    print(answer_summary)
        
        
if __name__=="__main__":
    main(input('ingrese pregunta: '))


   
