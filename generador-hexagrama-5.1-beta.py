#!/usr/bin/python
# -*- encoding: utf-8 -*-
from random import seed, randint #para generar números
#para poder esperar, y crear la semilla del proceso aleatorio:
from time import sleep, time
from datetime import datetime
#texto predefinido
cadenaiching = "I Ching"

introduccion = '''Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?.
El Libro de las Mutaciones es la obra mediante la cual los sabios
santos elevaron su modo de ser y ampliaron su campo de accion.'''

pregunta = '''Haz una pregunta en voz alta al oráculo.
Tienes 13 segundos.
Si no haces ninguna pregunta, el oráculo te guiará igualmente.'''

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
tierra, las del medio la región del mundo humano, las de arriba
el cielo.'''
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

#palabras para diferenciar las iteraciones de selección de lineas
ordinales = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta", "Sexta"]
assert len(ordinales) == 6

#diccionarios para convertir un número en la linea correspondiente
lineas_principales = {9:"9 _______",
                      7:"7 _______",
                      6:"6 ___ ___",
                      8:"8 ___ ___",}
lineas_mutadas  = {9:"9 ___ ___",
                   7:"7 _______",
                   6:"6 _______",
                   8:"8 ___ ___",}


#mostrar título
print cadenaiching.center(70, "=")

print introduccion
print
sleep(8)
#maestro yoda
print yoda
#mostrar invitación a preguntar algo
print pregunta
print
sleep(13)
print

#crear semilla del módulo random
ts = time()
st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
momentarySeed = unicode(ts)
seed(momentarySeed)

#formacion del hexagrama (que son seis lineas una sobre otra)

#guardar las lineas en una lista
lineas = []
for ordinal in ordinales:
    #generar número
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
    #mostrar el patrón de lineas en orden
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
    #mostrar el patrón de lineas en orden
    try:
        print lineas_mutadas[este_numero_aleatorio]
    except KeyError:
        print "Valor erroneo"
print
print ""
print "Enlace del I Ching escaneado: www.libroesoterico.com/biblioteca/I-Ching/I-Ching-Libro_de_las_Mutaciones-r-h-wilhem.pdf "
print "Enlace del Tao te king escaneado: www.libroesoterico.com/biblioteca/I-Ching/TaoTeKing-LaoTse-RH-Wilhem.pdf "
print ""
print "Consejo: lee la parte del libro con tu propia interpretación, estado emocional, vivencias..."
print "         aunque no entiendas algo sigue leyendo y te aconsejará en algún momento o reflejará tu realidad"
print ""
#---------------------------------------------------------------------------
#
# pyching -- a Python program to cast and interpret I Ching hexagrams
#
# Copyright (C) 2020 Zorbatrusta
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be of some
# interest to somebody, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING or COPYING.txt. If not,
#  write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# The license can also be found at the GNU/FSF website: http://www.gnu.org
#

