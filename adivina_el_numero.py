# Este es el juego de adivinar el número de dias que Paola y Juan llevan de novios

#Los import son ...
import random
import datetime

# Ponemos las fechas de referencia. 
# La variable "today" se formara gracias a los datos de datetime.
# Empezamos a andar el 4 de septiembre de 2018, estara en la variable "star"
# La fecha de hoy - la fecha de inicio, nos dara los dias que han pasado entre estas dos fechas

today = datetime.date.today()
start = datetime.date(2018, 9, 4)
dating_days = today - start
dating_days = dating_days.days

# Usaremos un contador de intentos. Habra 6. 

intentosRealizados = 0

print("¡Hola! ¿Cómo te llamas?")
miNombre = input()

print("Ah, ¡Hola!, " + miNombre + ", ¿Sabes cuantos dias de novios llevan Paola y Juan?")

while intentosRealizados < 6:
    print("Intenta adivinar. Llevan andando desde el 4 de septiembre de 2018") # Hay cuatro espacios delante de print.
    estimación = input()
    estimación = int(estimación)
    intentosRealizados = intentosRealizados + 1
    if estimación < dating_days:
        print("¡Oye, no tienes ni idea! Tu estimación es muy baja.") # Hay ocho espacios delante de print.
    if estimación > dating_days:
        print("¡Oye, no tienes ni idea! Tu estimación es muy alta.")
    if estimación == dating_days:
        break

if estimación == dating_days:
    intentosRealizados = str(intentosRealizados)
    print("¡Buen trabajo, " + miNombre + "! ¡Has adivinado el número de dias en " + intentosRealizados + " intentos!" + " ¡Bien hecho! Juan y Paola han estado amandose por todos estos dias ❤ ")
if estimación != dating_days:
    dating_days = str(dating_days)
    print("Pues no. El número de dias era " + dating_days)