#!/usr/bin/env python3

def lucas():
	yield 2
	a = 2
	b = 1
	while True:
		yield b
		a,b = b,a+b


if __name__ == "__main__":
	i = 0
	for x in lucas():
		if i > 10:
			break
		print(x)
		i = i + 1
