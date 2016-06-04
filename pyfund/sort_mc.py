#!/usr/bin/env python3


from pprint import pprint as pp

def a():
	d = { "MC": 53, "JH": 57, "RB":49, "ME":37, "JS":35 }
	pp(sorted(d.items(), key=lambda x: x[1]))


def b():
	d = { "MC": 53, "JH": 57, "RB":49, "ME":37, "JS":35 }
	pp(x for x in d.items())
	#pp(sorted(d.items()))
	#pp(sorted(d, key=lambda x: x[1]))

if __name__ == "__main__":
	b()
