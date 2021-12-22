# ChallengeSofka2021

El programa funciona en python a traves de una clase donde se desarrolla toda la partida.
Para poder ejecutarse el programa requiere de dos archivos que estan en el mismo directorio.
Ambos Archivos son CSV y contienen información requerida, uno de ellos contiene los datos de las preguntas y el otro los historicos.

El csv que contiene las preguntas tiene un header donde se indica a que corresponde cada columna y aparte de esa tiene otras 25 filas, 
5 filas por cada categoría. Dentro del programa dependiendo de la ronda que este jugando el jugador se establece un punto para acceder a las preguntas que corresponden a cada ronda.

El otro csv contiene los datos como el nombre, el puntaje, la categoria o ronda y la fehca de la partida.
Este archivo se modifica al acabar la partida, añadiendo los datos de la partida actual y ordenandolos de mayor a menor con base en el puntaje.
