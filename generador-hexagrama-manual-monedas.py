#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""for random(100)
	if random > 50
		yang
	else
		ying
return 0 or 1"""
from time import sleep
#formacion del hexagrama(que son seis lineas una sobre otra)
cadenaiching = "I Ching"
print cadenaiching.center(70, "=")
print " Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?."
print " El Libro de las Mutaciones es la obra mediante la cual los sabios"
print " santos elevaron su modo de ser y ampliaron su campo de accion."
print ""
sleep(8)
print "Primera tirada de seis, linea inferior del hexagrama "
print "Coje tres monedas iguales y a un lado le asignas valor 2 y al otro 3"
print "Tira las monedas y suma los valores, solo pueden ser 6,7,8 y 9"
sleep(8)
linea1 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Segunda tirada..."
linea2 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Tercera tirada..."
linea3 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Cuarta tirada..."
linea4 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Quinta tirada..."
linea5 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Sexta tirada..."
linea6 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
#linea1 = self.assert_(True, 'message')
"""listaching = [6,7,8,9]
trigramainf = [linea1,linea2,linea3]
trigramasup = [linea4,linea5,linea6]"""
#Tipos de tirada fuerte o debil
yangf = "_______" #9
yingf = "___ ___" #6
yangd = "_______" #7
yingd = "___ ___" #8
basicyang = 7
basicying = 6
trigramainf = []
trigramasup = []
#trigramas inferiores
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Chien"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 9 or linea1 == 7:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior Chen"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior K'an"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Ken"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior K'un"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Sun"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 9 or linea1 == 7:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Li"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior Tui"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
#
if linea4 == 9 or linea4 == 7:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Ch'ien"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
#
if linea4 == 9 or linea4 == 7:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior Chen"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior K'an"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Ken"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior K'un"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Sun"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 9 or linea4 == 7:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Li"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 9 or linea4 == 7:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior Tui"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
#
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

#Hexagrama mutado
print "Tu hexagrama mutado es : \n"
sleep(2)
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
