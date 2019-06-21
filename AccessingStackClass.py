##===============Model of how to access Stack class in the folder StackApi
## ACA TIENEN QUE ESTAR TODAS LAS VALIDACIONES DE TIPO DE ELEMENTOS A ENVIAR
import StackApi.Stack as Conexion
#----------object "stack" creation
stack = Conexion.Stack()
#-----------------Making question to "API-REST"
pregunta = input('bienvenido al asistente de preguntas por consola de Stackoverflow, porfavor ingrese su pregunta: \n')
print("la respuesta obtenida por stack overflow es la siguinte: \n" + str(stack.ask(pregunta)))
#-----------------Choosing the best question and getting answer
respuesta = int(input('A cual de las preguntas anteriores desea acceder? : '))
print(stack.getAnswer(respuesta))
