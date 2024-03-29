#===Class for stackoverflow.com Consumption
import requests
from bs4 import BeautifulSoup

class Stack():
    #-------Atributes
    def __init__(self):
        self.URL_BASE = "https://stackoverflow.com"
        self.Title_link = []
    #======================Method 1 ASKING IN STACKOVERFLOW================================
    def ask(self,question):
        try:
            res = requests.get(self.URL_BASE + "/search?q=" + question)
            soup = BeautifulSoup(res.text,"html.parser")
            question_summary = soup.findAll("div",{"class": "question-summary search-result"})
            title = []
            for question in question_summary:
                title.append(question.h3.a["title"])
                self.Title_link.append(question.h3.a["href"])
            return title
        except Exception as e:
            return e
    #======================Method 2 GETTING THE ANSWER=====================================
    def getAnswer(self,response):   
        try:
            res = requests.get(self.URL_BASE + self.Title_link[response])
            soup = BeautifulSoup(res.text,"html.parser")
            answer_summary = soup.findAll("div",{"class": "post-text"})#<---es würde nur "find", wenn du nur die erste frage willst
            #=================BURGO'S CODE HERE===========================
            algo = []
            for answer in answer_summary:
                algo.append(answer.text)
            return algo
        except Exception as e:
            return e
    #============================Method 3 OBJECT DESTRUCTOR==============
    def __del__(self):
        print ("object deleted")
