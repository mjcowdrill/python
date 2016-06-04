class Calculate(object):

    def add(self, x, y):

        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

if __name__ == '__main__': #pragma: no cover
    calc = Calculate()
    result = calc.add(2, 2)
    print result

# Replace the result line with this line to try
# adding two strings:
# result = calc.add("Hello", "World")