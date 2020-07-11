#!/usr/bin/python
# -*- encoding: utf-8 -*-
from random import seed, randint #para generar n�meros
#para poder esperar, y crear la semilla del proceso aleatorio:
from time import sleep, time
from datetime import datetime
#texto predefinido
cadenaiching = "I Ching"

introduccion = '''Dijo el Maestro �no es el libro de las mutaciones lo Supremo?.
El Libro de las Mutaciones es la obra mediante la cual los sabios
santos elevaron su modo de ser y ampliaron su campo de accion.'''

pregunta = '''Haz una pregunta en voz alta al or�culo.
Tienes 13 segundos.
Si no haces ninguna pregunta, el or�culo te guiar� igualmente.'''

sign_lineas = '''Las l�neas se cuentan desde abajo hacia arriba. El trazo
del comienzo es, pues, el de m�s abajo. Si el consultante obtiene
un siete, se trata por cierto de un trazo fuerte que se toma
en consideraci�n en cuanto a la estructura del signo en su
totalidad, pero este trazo no se mueve y no tiene, por tanto,
significaci�n individual. Si en cambio, el consultante obtiene 
un nueve, el trazo se mueve, destac�ndose con ello su significaci�n
peculiar y debiendo ten�rselo en cuenta y meditarse sobre �l, en
calidad de trazo individual, si el trazo es seis tambi�n se mueve. 
Lo mismo vale en cuanto a las dem�s l�neas fuertes en todo el libro. 
En cada uno de los hexagramas las dos l�neas de abajo significan la
tierra, las del medio la regi�n del mundo humano, las de arriba
el cielo.'''


#palabras para diferenciar las iteraciones de selecci�n de lineas
ordinales = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta", "Sexta"]
assert len(ordinales) == 6

#diccionarios para convertir un n�mero en la linea correspondiente
lineas_principales = {9:"9 _______",
                      7:"7 _______",
                      6:"6 ___ ___",
                      8:"8 ___ ___",}
lineas_mutadas  = {9:"9 ___ ___",
                   7:"7 _______",
                   6:"6 _______",
                   8:"8 ___ ___",}


#mostrar t�tulo
print cadenaiching.center(70, "=")

print introduccion
print
sleep(8)
#mostrar invitaci�n a preguntar algo
print pregunta
print
sleep(13)
print

#crear semilla del m�dulo random
ts = time()
st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
momentarySeed = unicode(ts)
seed(momentarySeed)

#formacion del hexagrama (que son seis lineas una sobre otra)

#guardar las lineas en una lista
lineas = []
for ordinal in ordinales:
    #generar n�mero
    lineas.append(randint(6,9))
    #usa cada prefijo ordinal
    print ordinal + " " + "tirada..."
    print
    sleep(1)
#se espera seis lineas en total
assert len(lineas) == 6

#mostrar hexagramas
print "Tu hexagrama principal es :"
print
for este_numero_aleatorio in reversed(lineas):
    #mostrar el patr�n de lineas en orden
    try:
        print lineas_principales[este_numero_aleatorio]
    except KeyError:
        print "Valor erroneo"
print

sleep(1)
#describir como leer el i-ching
print sign_lineas
print
sleep(1)

print "Tu hexagrama mutado es :"
print
for este_numero_aleatorio in reversed(lineas):
    #mostrar el patr�n de lineas en orden
    try:
        print lineas_mutadas[este_numero_aleatorio]
    except KeyError:
        print "Valor erroneo"
print