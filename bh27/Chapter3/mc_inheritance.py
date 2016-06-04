class class1():
    def __init__(self, parm):
        self.parm = parm

    def func1(self):
        print(self.parm)
        pass


class class2(class1):
    def func2(self):
        pass


c = class1("parm")

d = class2("parm")


if __name__ == "__main__":
    assert isinstance(d, class2)

    d.func1()


