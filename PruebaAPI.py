# importando librerias de stack exchange (pip install py_stackExchange si no la tienen)
import stackexchange,sys
# Encerrando la coneccion en un try except
try:
    StackConexion = stackexchange.Site(stackexchange.StackOverflow, impose_throttling=True)
    StackConexion.be_inclusive()

    sys.stdout.write('Loading... \n')
    sys.stdout.flush()

       
except:
    print('Sorry!! there was trouble with your connexion please verify the followin: \n- You are conected to internet')

####Investigar de como usar el questions.related_to
#questions = StackConexion.recent_questions(pagesize=10, filter='_b')
questions = StackConexion.questions.related_to('pregunta en stackoverflow',pagesize=10, filter='_b')
print('\r #  vote ans view')


cur = 1
for question in questions[:10]:
    print('%2d %3d  %3d  %3d \t%s' % (cur, question.score, len(question.answers), question.view_count, question.title))
    cur += 1

    num = int(input('Question no.: '))
    qu  = questions[num - 1]
    print('--- %s' % qu.title)
    print('%d votes, %d answers, %d views.' % (qu.score, len(qu.answers), qu.view_count))
    print('Tagged: ' + ', '.join(qu.tags))
    print()
    print(qu.body[:250] + ('...' if len(qu.body) > 250 else ''))
    

































    #===========pruebas fallidas de apis
    
'''import http.client
import json
import zlib

c = http.client.HTTPConnection('api.stackoverflow.com')
c.request('GET', '/1.1/questions?answers=true&page=1&pagesize=5&tagged=sql')
r = c.getresponse()

compressedData = r.read()
uncompressedData= zlib.decompress(compressedData, 15+32)

data = str(uncompressedData, 'utf-8')
print(data)
'''

'''import requests

response = requests.get("https://stackoverflow.com/questions")

print(response.text)
'''

'''
#impotando libreria de stackAPI
import json
from stackapi import StackAPI
from datetime import datetime
try:
    SITE = StackAPI('stackoverflow')
    SITE.max_pages=10
except StackAPIError as e:
    print(e.message)
questions = SITE.fetch('questions', fromdate=datetime(2011,11,11), todate=datetime(2018,12,31), min=10, sort='votes', tagged='zelda')

print ('La cantidad de preguntas con este tag son: ' + str(len(questions['items'])))

#print(questions)
'''




'''import requests, json

url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
headers = {'content-type':'application/json'}

r = requests.post(url, data = json.dumps(payload), headers=headers)
'''
