#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
from random import seed
from random import randint
from time import sleep
#formacion del hexagrama(que son seis lineas una sobre otra)
cadenaiching = "I Ching"
print cadenaiching.center(70, "=")
print " Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?."
print " El Libro de las Mutaciones es la obra mediante la cual los sabios"
print " santos elevaron su modo de ser y ampliaron su campo de accion."
print ""
sleep(8)
print " Haz una pregunta en voz alta al oráculo.\n"
print " Tienes 13 segundos."
print " Si no haces ninguna pregunta, el oráculo te guiará igualmente."
sleep(13)
print ""
print "Primera tirada..."
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
momentarySeed = unicode(ts)
random.seed(momentarySeed)
seed(momentarySeed)
linea1 = randint(6,9)
print ""
sleep(1)
print "Segunda tirada..."
linea2 = randint(6,9)
print ""
sleep(1)
print "Tercera tirada..."
linea3 = randint(6,9)
print ""
sleep(1)
print "Cuarta tirada..."
linea4 = randint(6,9)
print ""
sleep(1)
print "Quinta tirada..."
linea5 = randint(6,9)
print ""
sleep(1)
print "Sexta tirada..."
linea6 = randint(6,9)
print ""
sleep(1)
print "Tu hexagrama principal es : \n"
if linea6 == 9 :
	print "9 _______"
elif linea6 == 7 :
	print "7 _______"
elif linea6 == 6 :
	print "6 ___ ___"
elif linea6 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea5 == 9 :
	print "9 _______"
elif linea5 == 7 :
	print "7 _______"
elif linea5 == 6 :
	print "6 ___ ___"
elif linea5 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea4 == 9 :
	print "9 _______"
elif linea4 == 7 :
	print "7 _______"
elif linea4 == 6 :
	print "6 ___ ___"
elif linea4 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea3 == 9 :
	print "9 _______"
elif linea3 == 7 :
	print "7 _______"
elif linea3 == 6 :
	print "6 ___ ___"
elif linea3 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea2 == 9 :
	print "9 _______"
elif linea2 == 7 :
	print "7 _______"
elif linea2 == 6 :
	print "6 ___ ___"
elif linea2 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea1 == 9 :
	print "9 _______"
elif linea1 == 7 :
	print "7 _______"
elif linea1 == 6 :
	print "6 ___ ___"
elif linea1 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
print ""
sleep(1)
#hexagramas
sign_lineas = '''Las líneas se cuentan desde abajo hacia arriba. El trazo
del comienzo es, pues, el de más abajo. Si el consultante obtiene
un siete, se trata por cierto de un trazo fuerte que se toma
en consideración en cuanto a la estructura del signo en su
totalidad, pero este trazo no se mueve y no tiene, por tanto,
significación individual. Si en cambio, el consultante obtiene 
un nueve, el trazo se mueve, destacándose con ello su significación
peculiar y debiendo tenérselo en cuenta y meditarse sobre él, en
calidad de trazo individual, si el trazo es seis también se mueve. 
Lo mismo vale en cuanto a las demás líneas fuertes en todo el libro. 
En cada uno de los hexagramas las dos líneas de abajo significan la
tierra, las del medio la región del mundo humano, las de arriba el cielo.'''
#
sleep(1)
print (sign_lineas)
print ""
sleep(1)
print "Tu hexagrama mutado es : \n"
if linea6 == 9 :
	print " ___ ___"
elif linea6 == 7 :
	print " _______"
elif linea6 == 6 :
	print " _______"
elif linea6 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea5 == 9 :
	print " ___ ___"
elif linea5 == 7 :
	print " _______"
elif linea5 == 6 :
	print " _______"
elif linea5 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea4 == 9 :
	print " ___ ___"
elif linea4 == 7 :
	print " _______"
elif linea4 == 6 :
	print " _______"
elif linea4 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea3 == 9 :
	print " ___ ___"
elif linea3 == 7 :
	print " _______"
elif linea3 == 6 :
	print " _______"
elif linea3 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea2 == 9 :
	print " ___ ___"
elif linea2 == 7 :
	print " _______"
elif linea2 == 6 :
	print " _______"
elif linea2 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea1 == 9 :
	print " ___ ___"
elif linea1 == 7 :
	print " _______"
elif linea1 == 6 :
	print " _______"
elif linea1 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
print ""
print ""
