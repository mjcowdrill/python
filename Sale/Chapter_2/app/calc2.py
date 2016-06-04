class Calculate2(object):

    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

if __name__ == '__main__': #pragma: no cover
    calc = Calculate2()
    result = calc.add(2, 2)
    # Uncomment this line to try adding two strings. Comment out the line above.
    # result = calc.add("Hello", "World")
    print result
