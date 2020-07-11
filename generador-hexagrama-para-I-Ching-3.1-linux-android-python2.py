#!/usr/bin/python
# -*- encoding: utf-8 -*-
##---------------------------------------------------------------------------##
##
## pyching -- a Python program to cast and interpret I Ching hexagrams
##
## Copyright (C) 2020 Zorbatrusta
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be of some
## interest to somebody, but WITHOUT ANY WARRANTY; without even the
## implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING or COPYING.txt. If not,
##  write to the Free Software Foundation, Inc.,
## 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
## The license can also be found at the GNU/FSF website: http://www.gnu.org
##
import time
from random import seed
from random import randint
from time import sleep
#formacion del hexagrama(que son seis lineas una sobre otra)
cadenaiching = "I Ching"
cadenawilhem = "Richard H. Wilhem"
print cadenaiching.center(70, "=")
print " Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?."
print " El Libro de las Mutaciones es la obra mediante la cual los sabios"
print " santos elevaron su modo de ser y ampliaron su campo de acción."
print cadenawilhem.center(70, "=")
print ""
sleep(9)
yoda = '''                   
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_DLC;-";.__
          .-j/'.;  ;""""  / .'!"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   |.
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /  
                 "-.t-._:'
'''
print (yoda)
sleep(3)
print " Haz una pregunta en voz alta al oráculo, también puedes pensarla.\n"
print " Tienes 13 segundos."
print " Si no haces ninguna pregunta, el oráculo te guiará igualmente."
sleep(13)
print ""
print "Primera tirada..."
ts = time.time()
seed(ts)
linea1 = randint(6, 9)
print ""
print (linea1)
sleep(1)
print "Segunda tirada..."
linea2 = randint(6, 9)
print ""
print (linea2)
sleep(1)
print "Tercera tirada..."
linea3 = randint(6, 9)
print ""
print (linea3)
sleep(1)
print "Cuarta tirada..."
linea4 = randint(6, 9)
print ""
print (linea4)
sleep(1)
print "Quinta tirada..."
linea5 = randint(6, 9)
print ""
print (linea5)
sleep(1)
print "Sexta tirada..."
linea6 = randint(6, 9)
print ""
print (linea6)
sleep(1)
print "Tu hexagrama principal es; busca en el I Ching y lee el hexagrama y las líneas que sean 6 o 9: \n"
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
print ""
sleep(1)
#hexagramas
sign_lineas = '''Las líneas se cuentan desde abajo hacia arriba. El trazo
del comienzo es, pues, el de más abajo. Si el consultante obtiene
un siete, se trata por cierto de un trazo fuerte que se toma
en consideración en cuanto a la estructura del signo en su
totalidad, pero este trazo no se mueve y no tiene, por tanto,
significación individual.
 
Si en cambio, el consultante obtiene un nueve, el trazo se mueve,
destacándose con ello su significación peculiar y debiendo tenérselo 
en cuenta y meditarse sobre él, en calidad de trazo individual, 
si el trazo es seis también se mueve.

Lo mismo vale en cuanto a las demás líneas fuertes en todo el libro.
En cada uno de los hexagramas las dos líneas de abajo significan la
tierra, las del medio la región del mundo humano, las de arriba el cielo.'''
#
sleep(1)
print (sign_lineas)
print ""
sleep(6)
print "Tu hexagrama mutado que significa futuro o devenir es; lee el hexagrama pero no sus líneas : \n"
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
print "Enlace del I Ching escaneado: www.libroesoterico.com/biblioteca/I-Ching/I-Ching-Libro_de_las_Mutaciones-r-h-wilhem.pdf "
print "Enlace del Tao te king escaneado: www.libroesoterico.com/biblioteca/I-Ching/TaoTeKing-LaoTse-RH-Wilhem.pdf "
print ""
print "Consejo: lee la parte del libro con tu propia interpretación, estado emocional, vivencias..."
print "         aunque no entiendas algo sigue leyendo y te aconsejará en algún momento o reflejará tu realidad"
print ""
