#!/usr/bin/env python
# -*- coding: utf-8 -*-

def si(preg):
    from string import lower
    resp = lower(raw_input(preg))
    return (resp[0] == 's')

def main():
	while True:
		if not si(Quieres iniciar la partida?):
			break

		print "x | x | x "
		print "__________"
		print "x | x | x "
		print "__________"
		print "x | x | x "
		break

if __name__ == '__main__':
	main()