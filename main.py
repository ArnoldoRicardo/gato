#!/usr/bin/env python
# -*- coding: utf-8 -*-

map = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def si(preg):
    from string import lower
    resp = lower(raw_input(preg))
    return (resp[0] == 's')

def tirar(player,pos):
	ind = pos.split(",")
	n = int(ind[0]) - 1
	m = int(ind[1]) - 1

	if player == 1:
		map[m][n] = "x"
	else:
		map[m][n] = "o"

def check():
	print "hola"

def printcrux():
	print map[0][0]+" | "+map[0][1]+" | "+map[0][2]+" "
	print "----------"
	print map[1][0]+" | "+map[1][1]+" | "+map[1][2]+" "
	print "----------"
	print map[2][0]+" | "+map[2][1]+" | "+map[2][2]+" "

def main():
	i=0
	while True:
		pass
		np = i % 2 + 1
		pos = str(raw_input("jugador "+str(np)+" (ejemplo 2,3): "))
		tirar(np,pos)
		check()
		printcrux()

		i= i + 1

if __name__ == '__main__':
	while True:
		if si("Quieres iniciar la partida? "):
			main()
		else:
			break