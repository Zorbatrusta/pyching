#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""for random(100)
    if random >? 50%
        yang
    else
        ying
return 0 or 1"""
import time
from random import seed
from random import randint
from time import sleep
#formacion del hexagrama(que son seis lineas una sobre otra)
cadenaiching = "I Ching"
print cadenaiching.center(70, "=")
print " Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?."
print " El Libro de las Mutaciones es la obra mediante la cual los sabios"
print " santos elevaron su modo de ser y ampliaron su campo de acción."
print ""
#sleep(10)
print " Haz una pregunta en voz alta al oráculo\n"
print " Tienes 13 segundos\n"
print " Si no haces ninguna pregunta el oráculo te guiará igualmente"
#sleep(13)
print ""
print " Primera tirada...\n"
ts = time.time()
seed(ts)
linea1 = randint(6, 9)
print (linea1)
sleep(1)
print ""
print " Segunda tirada...\n"
linea2 = randint(6, 9)
print (linea2)
sleep(1)
print ""
print " Tercera tirada...\n"
linea3 = randint(6, 9)
print (linea3)
sleep(1)
print ""
print " Cuarta tirada...\n"
linea4 = randint(6, 9)
print (linea4)
sleep(1)
print ""
print " Quinta tirada...\n"
linea5 = randint(6, 9)
print (linea5)
sleep(1)
print ""
print " Sexta tirada...\n"
linea6 = randint(6, 9)
print (linea6)
sleep(1)
print ""
#degugger
#linea1 = 8
#linea2 = 9
#linea3 = 8
#linea4 = 9
#linea5 = 9
#linea6 = 9
#linea1 = self.assert_(True, 'message')
"""listaching = [6,7,8,9]
trigramainf = [linea1,linea2,linea3]
trigramasup = [linea4,linea5,linea6]"""
#Tipos de tirada fuerte o debil
yangf = "_______"  # 9
yingf = "___ ___"  # 6
yangd = "_______"  # 7
yingd = "___ ___"  # 8
basicyang = 7
basicying = 8
trigramainf = []
trigramasup = []
#trigramas inferiores
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            print "Trigrama inferior Ch'ien, Lo Creativo, el Cielo"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            print "Trigrama inferior Chen, Lo Suscitativo, el trueno"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            print "Trigrama inferior K'an, Lo Abismal, el agua"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 9 or linea3 == 7:
            print "Trigrama inferior Ken, El aquietamiento, la montaña"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            print "Trigrama inferior K'un, Lo Receptivo, la tierra"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            print "Trigrama inferior Sun, Lo Suave, el viento"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 9 or linea3 == 7:
            print "Trigrama inferior Li, Lo Adherente, la llama"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            print "Trigrama inferior Tui, Lo Suscitativo, el lago"
            trigramainf = [linea1, linea2, linea3]
            print trigramainf
            print ""
#
if linea4 == 9 or linea4 == 7:
    if linea5 == 9 or linea5 == 7:
        if linea6 == 9 or linea6 == 7:
            print "Trigrama superior Ch'ien, Lo Creativo, el Cielo"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
#
if linea4 == 9 or linea4 == 7:
    if linea5 == 8 or linea5 == 6:
        if linea6 == 8 or linea6 == 6:
            print "Trigrama superior Chen, Lo Suscitativo, el trueno"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
if linea4 == 8 or linea4 == 6:
    if linea5 == 9 or linea5 == 7:
        if linea6 == 8 or linea6 == 6:
            print "Trigrama superior K'an, Lo Abismal, el agua"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
if linea4 == 8 or linea4 == 6:
    if linea5 == 8 or linea5 == 6:
        if linea6 == 9 or linea6 == 7:
            print "Trigrama superior Ken, El aquietamiento, la montaña"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
if linea4 == 8 or linea4 == 6:
    if linea5 == 8 or linea5 == 6:
        if linea6 == 8 or linea6 == 6:
            print "Trigrama superior K'un, Lo Receptivo, la tierra"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
if linea4 == 8 or linea4 == 6:
    if linea5 == 9 or linea5 == 7:
        if linea6 == 9 or linea6 == 7:
            print "Trigrama superior Sun, Lo Suave, el viento"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
if linea4 == 9 or linea4 == 7:
    if linea5 == 8 or linea5 == 6:
        if linea6 == 9 or linea6 == 7:
            print "Trigrama superior Li, Lo Adherente, la llama"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
if linea4 == 9 or linea4 == 7:
    if linea5 == 9 or linea5 == 7:
        if linea6 == 8 or linea6 == 6:
            print "Trigrama superior Tui, Lo Suscitativo, el lago"
            trigramasup = [linea4, linea5, linea6]
            print trigramasup
            print ""
#
print "Tu hexagrama principal es : \n"
if linea6 == 9:
    print "9 _______"
elif linea6 == 7:
    print "7 _______"
elif linea6 == 6:
    print "6 ___ ___"
elif linea6 == 8:
    print "8 ___ ___"
else:
    print "Valor erroneo"
#
if linea5 == 9:
    print "9 _______"
elif linea5 == 7:
    print "7 _______"
elif linea5 == 6:
    print "6 ___ ___"
elif linea5 == 8:
    print "8 ___ ___"
else:
    print "Valor erroneo"
#
if linea4 == 9:
    print "9 _______"
elif linea4 == 7:
    print "7 _______"
elif linea4 == 6:
    print "6 ___ ___"
elif linea4 == 8:
    print "8 ___ ___"
else:
    print "Valor erroneo"
#
if linea3 == 9:
    print "9 _______"
elif linea3 == 7:
    print "7 _______"
elif linea3 == 6:
    print "6 ___ ___"
elif linea3 == 8:
    print "8 ___ ___"
else:
    print "Valor erroneo"
#
if linea2 == 9:
    print "9 _______"
elif linea2 == 7:
    print "7 _______"
elif linea2 == 6:
    print "6 ___ ___"
elif linea2 == 8:
    print "8 ___ ___"
else:
    print "Valor erroneo"
#
if linea1 == 9:
    print "9 _______"
elif linea1 == 7:
    print "7 _______"
elif linea1 == 6:
    print "6 ___ ___"
elif linea1 == 8:
    print "8 ___ ___"
else:
    print "Valor erroneo"
sleep(4)
print ""
#hexagrama principal
sign_lineas = '''Las líneas se cuentan desde abajo hacia arriba. El trazo
del comienzo es, pues, el de más abajo. Si el consultante obtiene
un siete, se trata por cierto de un trazo fuerte que se toma
en consideración en cuanto a la estructura del signo en su
totalidad, pero este trazo no se mueve y no tiene, por tanto,
significación individual. Si en cambio, el consultante obtiene
un nueve, el trazo se mueve, destacándose con ello su significación
peculiar y debiendo tenérselo en cuenta y meditarse sobre él, en
calidad de trazo individual.
En cada uno de los hexagramas las dos líneas de abajo significan
la tierra, las del medio la región del mundo humano, las de arriba el cielo.'''
print (sign_lineas)
print "\n"
#sleep(25)
#1 Ch'ien -Lo Creativo
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        print "Hexagrama 1.䷀ Ch'ien, Lo Creativo\n"
                        file1 = open("./db/1.txt", 'r')
                        contenido = file1.read()
                        print (contenido)
                        file1.close()

if linea1 == 9:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file1_1 = open("./db/1_1.txt", 'r')
                        conlin1 = file1_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file1_1.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file1_2 = open("./db/1_2.txt", 'r')
                        conlin2 = file1_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file1_2.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file1_3 = open("./db/1_3.txt", 'r')
                        conlin3 = file1_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file1_3.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file1_4 = open("./db/1_4.txt", 'r')
                        conlin4 = file1_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file1_4.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9:
                    if linea6 == 9 or linea6 == 7:
                        file1_5 = open("./db/1_5.txt", 'r')
                        conlin5 = file1_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file1_5.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9:
                        file1_6 = open("./db/1_6.txt", 'r')
                        conlin6 = file1_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file1_6.close()
if linea1 == 9 and linea2 == 9 and linea3 == 9 and linea4 == 9 and linea5 == 9 and linea6 == 9:
    file1_7 = open("./db/1_7.txt", 'r')
    conlin7 = file1_7.read()
    print "Significado si todas las líneas son 9 : \n"
    print (conlin7)
    file1_7.close()

#2 K'un -Lo Receptivo
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        print "Hexagrama 2.䷁ K'un, Lo Receptivo"
                        file2 = open("./db/2.txt", 'r')
                        contenido = file2.read()
                        print (contenido)
                        file2.close()

if linea1 == 6:
    if linea2 == 6 or linea2 == 8:
        if linea3 == 6 or linea3 == 8:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file2_1 = open("./db/2_1.txt", 'r')
                        conlin1 = file2_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file2_1.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6:
        if linea3 == 6 or linea3 == 8:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file2_2 = open("./db/2_2.txt", 'r')
                        conlin2 = file2_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file2_2.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file2_3 = open("./db/2_3.txt", 'r')
                        conlin3 = file2_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file2_3.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file2_4 = open("./db/2_4.txt", 'r')
                        conlin4 = file2_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file2_4.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6 or linea5 == 8:
                if linea5 == 6:
                    if linea6 == 6 or linea6 == 8:
                        file2_5 = open("./db/2_5.txt", 'r')
                        conlin5 = file2_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file2_5.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6 or linea5 == 8:
                if linea5 == 6 or linea6 == 8:
                    if linea6 == 6:
                        file2_6 = open("./db/2_6.txt", 'r')
                        conlin6 = file2_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file2_6.close()
if linea1 == 6 and linea2 == 6 and linea3 == 6 and linea4 == 6 and linea5 == 6 and linea6 == 6:
    file2_7 = open("./db/2_7.txt", 'r')
    conlin7 = file2_7.read()
    print "Significado si todas las líneas son 6 : \n"
    print (conlin7)
    file2_7.close()
#3 Chun -La dificultad inicial
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        print "Hexagrama 3.䷂ Chun, La Dificultad Inicial"
                        file3 = open("./db/3.txt", 'r')
                        contenido = file3.read()
                        print (contenido)
                        file3.close()

if linea1 == 9:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file3_1 = open("./db/3_1.txt", 'r')
                        conlin1 = file3_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file3_1.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file3_2 = open("./db/3_2.txt", 'r')
                        conlin2 = file3_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file3_2.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file3_3 = open("./db/3_3.txt", 'r')
                        conlin3 = file3_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file3_3.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file3_4 = open("./db/3_4.txt", 'r')
                        conlin4 = file3_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file3_4.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9:
                    if linea6 == 8 or linea6 == 6:
                        file3_5 = open("./db/3_5.txt", 'r')
                        conlin5 = file3_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file3_5.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 6:
                        file3_6 = open("./db/3_6.txt", 'r')
                        conlin6 = file3_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file3_6.close()
#4 Meng - La Necedad Juvenil
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 9 or linea6 == 7:
                        print "Hexagrama 4.䷃ Meng, La Necedad Juvenil"
                        file4 = open("./db/4.txt", 'r')
                        contenido = file4.read()
                        print (contenido)
                        file4.close()

if linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 9 or linea6 == 7:
                        file4_1 = open("./db/4_1.txt", 'r')
                        conlin1 = file4_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file4_1.close()
if linea1 == 6 or linea1 == 8:
    if linea2 == 9:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 9 or linea6 == 7:
                        file4_2 = open("./db/4_2.txt", 'r')
                        conlin1 = file4_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin1)
                        file4_2.close()
if linea1 == 6 or linea1 == 8:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 9 or linea6 == 7:
                        file4_3 = open("./db/4_3.txt", 'r')
                        conlin1 = file4_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin1)
                        file4_3.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 9 or linea6 == 7:
                        file4_4 = open("./db/4_4.txt", 'r')
                        conlin1 = file4_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin1)
                        file4_4.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 6:
                    if linea6 == 9 or linea6 == 7:
                        file4_5 = open("./db/4_5.txt", 'r')
                        conlin1 = file4_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin1)
                        file4_5.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 9:
                        file4_6 = open("./db/4_6.txt", 'r')
                        conlin1 = file4_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin1)
                        file4_6.close()
#5 Hsü -La Espera
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        print "Hexagrama 5.䷄ Hsü -La Espera\n"
                        file5 = open("./db/5.txt", 'r')
                        contenido = file5.read()
                        print (contenido)
                        file5.close()

if linea1 == 9:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file5_1 = open("./db/5_1.txt", 'r')
                        conlin1 = file5_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file5_1.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file5_2 = open("./db/5_2.txt", 'r')
                        conlin2 = file5_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file5_2.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file5_3 = open("./db/5_3.txt", 'r')
                        conlin3 = file5_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file5_3.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        file5_4 = open("./db/5_4.txt", 'r')
                        conlin4 = file5_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file5_4.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9:
                    if linea6 == 8 or linea6 == 6:
                        file5_5 = open("./db/5_5.txt", 'r')
                        conlin5 = file5_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file5_5.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 6:
                        file5_6 = open("./db/5_6.txt", 'r')
                        conlin6 = file5_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file5_6.close()
#6 Sung -El Conflicto (El Pleito)
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        print "Hexagrama 6.䷅ Sung -El Conflicto\n"
                        file6 = open("./db/6.txt", 'r')
                        contenido = file6.read()
                        print (contenido)
                        file6.close()

if linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file6_1 = open("./db/6_1.txt", 'r')
                        conlin1 = file6_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file6_1.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file6_2 = open("./db/6_2.txt", 'r')
                        conlin2 = file6_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file6_2.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file6_3 = open("./db/6_3.txt", 'r')
                        conlin3 = file6_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file6_3.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file6_4 = open("./db/6_4.txt", 'r')
                        conlin4 = file6_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file6_4.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9:
                    if linea6 == 9 or linea6 == 7:
                        file6_5 = open("./db/6_5.txt", 'r')
                        conlin5 = file6_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file6_5.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9:
                        file6_6 = open("./db/6_6.txt", 'r')
                        conlin6 = file6_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file6_6.close()
#7 Shih - El Ejército
if linea1 == 8 or linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        print "Hexagrama 7.䷆ Shih - El Ejército"
                        file7 = open("./db/7.txt", 'r')
                        contenido = file7.read()
                        print (contenido)
                        file7.close()

if linea1 == 6:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 6 or linea3 == 8:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file7_1 = open("./db/7_1.txt", 'r')
                        conlin1 = file7_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file7_1.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 9:
        if linea3 == 6 or linea3 == 8:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file7_2 = open("./db/7_2.txt", 'r')
                        conlin2 = file7_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file7_2.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 7 or linea3 == 9:
        if linea3 == 6:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file7_3 = open("./db/7_3.txt", 'r')
                        conlin3 = file7_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file7_3.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 7 or linea3 == 9:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6:
                if linea5 == 6 or linea5 == 8:
                    if linea6 == 6 or linea6 == 8:
                        file7_4 = open("./db/7_4.txt", 'r')
                        conlin4 = file7_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file7_4.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 7 or linea3 == 9:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6 or linea5 == 8:
                if linea5 == 6:
                    if linea6 == 6 or linea6 == 8:
                        file7_5 = open("./db/7_5.txt", 'r')
                        conlin5 = file7_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file7_5.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 7 or linea3 == 9:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6 or linea5 == 8:
                if linea5 == 6 or linea6 == 8:
                    if linea6 == 6:
                        file7_6 = open("./db/7_6.txt", 'r')
                        conlin6 = file7_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file7_6.close()
#8 Pi -La Solidaridad (El mantenerse unido)
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 8 or linea6 == 6:
                        print "Hexagrama 8.䷇ Pi, La Solidaridad (El mantenerse unido)"
                        file8 = open("./db/8.txt", 'r')
                        contenido = file8.read()
                        print (contenido)
                        file8.close()

if linea1 == 6:
    if linea2 == 6 or linea2 == 8:
        if linea3 == 6 or linea3 == 8:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 7 or linea5 == 9:
                    if linea6 == 6 or linea6 == 8:
                        file8_1 = open("./db/8_1.txt", 'r')
                        conlin1 = file8_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file8_1.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6:
        if linea3 == 6 or linea3 == 8:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 7 or linea5 == 9:
                    if linea6 == 6 or linea6 == 8:
                        file8_2 = open("./db/8_2.txt", 'r')
                        conlin2 = file8_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file8_2.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6:
            if linea4 == 6 or linea4 == 8:
                if linea5 == 7 or linea5 == 9:
                    if linea6 == 6 or linea6 == 8:
                        file8_3 = open("./db/8_3.txt", 'r')
                        conlin3 = file8_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file8_3.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6:
                if linea5 == 7 or linea5 == 9:
                    if linea6 == 6 or linea6 == 8:
                        file8_4 = open("./db/8_4.txt", 'r')
                        conlin4 = file8_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file8_4.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6 or linea5 == 8:
                if linea5 == 9:
                    if linea6 == 6 or linea6 == 8:
                        file8_5 = open("./db/8_5.txt", 'r')
                        conlin5 = file8_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file8_5.close()
if linea1 == 6 or linea2 == 8:
    if linea2 == 6 or linea3 == 8:
        if linea3 == 6 or linea4 == 8:
            if linea4 == 6 or linea5 == 8:
                if linea5 == 7 or linea6 == 9:
                    if linea6 == 6:
                        file8_6 = open("./db/8_6.txt", 'r')
                        conlin6 = file8_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file8_6.close()
#9 Hsiao Ch'u -La Fuerza Domesticadora de lo Pequeño
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        print "Hexagrama 9.䷈ Hsiao Ch'u. La Fuerza Domesticadora de lo Pequeño\n"
                        file9 = open("./db/9.txt", 'r')
                        contenido = file9.read()
                        print (contenido)
                        file9.close()

if linea1 == 9:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file9_1 = open("./db/9_1.txt", 'r')
                        conlin1 = file9_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file9_1.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file9_2 = open("./db/9_2.txt", 'r')
                        conlin2 = file9_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file9_2.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file9_3 = open("./db/9_3.txt", 'r')
                        conlin3 = file9_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file9_3.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file9_4 = open("./db/9_4.txt", 'r')
                        conlin4 = file9_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file9_4.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9:
                    if linea6 == 9 or linea6 == 7:
                        file9_5 = open("./db/9_5.txt", 'r')
                        conlin5 = file9_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file9_5.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9:
                        file9_6 = open("./db/9_6.txt", 'r')
                        conlin6 = file9_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file9_6.close()
#10 Lü -El Porte (La Pisada)
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        print "Hexagrama 10.䷉ Lü ,El Porte (La Pisada)\n"
                        file10 = open("./db/10.txt", 'r')
                        contenido = file10.read()
                        print (contenido)
                        file10.close()

if linea1 == 9:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file10_1 = open("./db/10_1.txt", 'r')
                        conlin1 = file10_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file10_1.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file10_2 = open("./db/10_2.txt", 'r')
                        conlin2 = file10_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file10_2.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file10_3 = open("./db/10_3.txt", 'r')
                        conlin3 = file10_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file10_3.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file10_4 = open("./db/10_4.txt", 'r')
                        conlin4 = file10_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file10_4.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9:
                    if linea6 == 9 or linea6 == 7:
                        file10_5 = open("./db/10_5.txt", 'r')
                        conlin5 = file10_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file10_5.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9:
                        file10_6 = open("./db/10_6.txt", 'r')
                        conlin6 = file10_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file10_6.close()
#11 T'ai' -La Paz
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        print "Hexagrama 11.䷊ T'ai, La Paz\n"
                        file11 = open("./db/11.txt", 'r')
                        contenido = file11.read()
                        print (contenido)
                        file11.close()

if linea1 == 9:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        file11_1 = open("./db/11_1.txt", 'r')
                        conlin1 = file11_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file11_1.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        file11_2 = open("./db/11_2.txt", 'r')
                        conlin2 = file11_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file11_2.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        file11_3 = open("./db/11_3.txt", 'r')
                        conlin3 = file11_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file11_3.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        file11_4 = open("./db/11_4.txt", 'r')
                        conlin4 = file11_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file11_4.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 6:
                    if linea6 == 8 or linea6 == 6:
                        file11_5 = open("./db/11_5.txt", 'r')
                        conlin5 = file11_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file11_5.close()
if linea1 == 9 or linea1 == 7:
    if linea2 == 9 or linea2 == 7:
        if linea3 == 9 or linea3 == 7:
            if linea4 == 8 or linea4 == 6:
                if linea5 == 8 or linea5 == 6:
                    if linea6 == 6:
                        file11_6 = open("./db/11_6.txt", 'r')
                        conlin6 = file11_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file11_6.close()
#12 P'i -El Estancamiento
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        print "Hexagrama 12.䷋ P'i, El Estancamiento\n"
                        file12 = open("./db/12.txt", 'r')
                        contenido = file12.read()
                        print (contenido)
                        file12.close()

if linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file12_1 = open("./db/12_1.txt", 'r')
                        conlin1 = file12_1.read()
                        print "Significado de la primera línea: \n"
                        print (conlin1)
                        file12_1.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file12_2 = open("./db/12_2.txt", 'r')
                        conlin2 = file12_2.read()
                        print "Significado de la segunda línea: \n"
                        print (conlin2)
                        file12_2.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file12_3 = open("./db/12_3.txt", 'r')
                        conlin3 = file12_3.read()
                        print "Significado de la tercera línea: \n"
                        print (conlin3)
                        file12_3.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9 or linea6 == 7:
                        file12_4 = open("./db/12_4.txt", 'r')
                        conlin4 = file12_4.read()
                        print "Significado de la cuarta línea: \n"
                        print (conlin4)
                        file12_4.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9:
                    if linea6 == 9 or linea6 == 7:
                        file12_5 = open("./db/12_5.txt", 'r')
                        conlin5 = file12_5.read()
                        print "Significado de la quinta línea: \n"
                        print (conlin5)
                        file12_5.close()
if linea1 == 8 or linea1 == 6:
    if linea2 == 8 or linea2 == 6:
        if linea3 == 8 or linea3 == 6:
            if linea4 == 9 or linea4 == 7:
                if linea5 == 9 or linea5 == 7:
                    if linea6 == 9:
                        file12_6 = open("./db/12_6.txt", 'r')
                        conlin6 = file12_6.read()
                        print "Significado de la sexta línea: \n"
                        print (conlin6)
                        file12_6.close()
#Hexagrama mutado
print ""
print "Tu hexagrama mutado que significa futuro o devenir es : \n"
if linea6 == 9:
    print " ___ ___"
elif linea6 == 7:
    print " _______"
elif linea6 == 6:
    print " _______"
elif linea6 == 8:
    print " ___ ___"
else:
    print "Valor erroneo"
#
if linea5 == 9:
    print " ___ ___"
elif linea5 == 7:
    print " _______"
elif linea5 == 6:
    print " _______"
elif linea5 == 8:
    print " ___ ___"
else:
    print "Valor erroneo"
#
if linea4 == 9:
    print " ___ ___"
elif linea4 == 7:
    print " _______"
elif linea4 == 6:
    print " _______"
elif linea4 == 8:
    print " ___ ___"
else:
    print "Valor erroneo"
#
if linea3 == 9:
    print " ___ ___"
elif linea3 == 7:
    print " _______"
elif linea3 == 6:
    print " _______"
elif linea3 == 8:
    print " ___ ___"
else:
    print "Valor erroneo"
#
if linea2 == 9:
    print " ___ ___"
elif linea2 == 7:
    print " _______"
elif linea2 == 6:
    print " _______"
elif linea2 == 8:
    print " ___ ___"
else:
    print "Valor erroneo"
#
if linea1 == 9:
    print " ___ ___"
elif linea1 == 7:
    print " _______"
elif linea1 == 6:
    print " _______"
elif linea1 == 8:
    print " ___ ___"
else:
    print "Valor erroneo"
print ""
