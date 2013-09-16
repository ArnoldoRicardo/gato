#!/usr/bin/env python
# -*- coding: utf-8 -*-

mapa = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
matriz = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "]
]

def cleanMap():
	del mapa[:]

	for i in range(3):
		mapa.append([fila[i] for fila in matriz])

def si(preg):
    from string import lower
    resp = lower(raw_input(preg))
    return (resp[0] == 's')

def tirar(player,pos):
	ind = pos.split(",")
	n = int(ind[0]) - 1
	m = int(ind[1]) - 1

	if player == 1:
		mapa[n][m] = "x"
	else:
		mapa[n][m] = "o"

def check(np):
	if np == 1:
		ficha = "x"
	else:
		ficha = "o"

	fin = False

	if mapa[0][0] == ficha and mapa[1][1] == ficha and mapa[2][2] == ficha:
		fin = True
	elif mapa[2][0] == ficha and mapa[1][1] == ficha and mapa[0][2] == ficha:
		fin = True
	else:
		for z in range(3):
			if mapa[0][z] == ficha and mapa[1][z] == ficha and mapa[2][z] == ficha:
				fin = True

		for w in range(3):
			if mapa[w][0] == ficha and mapa[w][1] == ficha and mapa[w][2] == ficha:
				fin = True

	print "ganaste jugador " + str(np)
	return fin

def printcrux():
	print mapa[0][0]+" | "+mapa[0][1]+" | "+mapa[0][2]+" "
	print "----------"
	print mapa[1][0]+" | "+mapa[1][1]+" | "+mapa[1][2]+" "
	print "----------"
	print mapa[2][0]+" | "+mapa[2][1]+" | "+mapa[2][2]+" "

def main():
	i=0
	while True:
		np = (i % 2) + 1
		pos = str(raw_input("jugador "+str(np)+" (ejemplo 2,3): "))
		tirar(np,pos)
		if check(np):
			cleanMap()
			break
		printcrux()

		i= i + 1

if __name__ == '__main__':
	while True:
		if si("Quieres iniciar la partida? "):
			main()
		else:
			break